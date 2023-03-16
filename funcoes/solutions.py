import openai
openai.api_key = "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"

def solutions(bot, message):

	user_message = message.text.replace("/solucoes", "").strip()
	
	response = openai.Completion.create(
		engine='text-davinci-002',
		promp=user_message,
		max_tokens=1024
	)

	bot.reply_to(message, response.choices[0].text)
