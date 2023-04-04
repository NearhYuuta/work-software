import openai

def project(bot, message):
    openai.api_key = "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"
    prompt = "Me diga uma ideia de projeto para um software ou site"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    text_response = f"Aqui está uma ideia de projeto: \n{response.choices[0].text}"
    
    bot.reply_to(message, text_response)
