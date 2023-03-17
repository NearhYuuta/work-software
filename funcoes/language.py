from googletrans import Translator
import requests

token = "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"
translator = Translator()

headers = {
  "Authorization": f"Bearer {token}"
}

def language(bot, message):

  language = message.text.replace("/linguagem", "").strip()

  if not language:
    bot.send_message(message.chat.id, "Por favor, informe uma linguagem")
    return 

  url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"
  response = requests.get(url)

  if response.status_code == 200:
    print("Conexão bem sucedida!")

    data = response.json()
    language_info = {
      "name": language,
      "description": f"{data['items'][0]['description']}",
      "stars": f"{data['items'][0]['stargazers_count']:,}",
      "url": f"{data['items'][0]['html_url']}"
    }

    traducao = translator.translate(language_info["description"], src="en", dest="pt")

    text = f"""
    Nome: {language_info['name']}
    Descrição: {traducao.text}
    Estrelas: {language_info['stars']}
    Url: {language_info['url']}
    """

    bot.send_message(message.chat.id, text)
  else: 
    print("Conexão não foi feita com sucesso")
  