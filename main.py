#importações de bibliotecas
import telebot
import pandas as pd
import random
import requests

from funcoes.example import example
from funcoes.language import language
from funcoes.networkmask import networkmask
from funcoes.project import project
from funcoes.syntax import syntax
from funcoes.operationalsystem import operationalsystem
from funcoes.solutions import solutions
from funcoes.presentation import presentation

#variáveis
chave_api_telegram = "6106311624:AAGH_MRyPVA6y2yNcRLu3-mn4pXyjCXF-HY"
bot = telebot.TeleBot(chave_api_telegram)
data_frame = pd.read_csv('assets/data.csv', sep=";")
#chamada das funções

#FUNÇÃO PARA O COMANDO: /codigo
def salvar(language, code, function_code):

	global data_frame

	new_row = pd.DataFrame({"linguagem": [language], "codigo": [code], "funcao": [function_code]})

	data_frame = pd.concat([data_frame, new_row], ignore_index=True)
	data_frame.to_csv("assets/data.csv", index=False, sep=";")

def list_codes(language):
    data_frame = pd.read_csv('assets/data.csv', sep=";")
    df_language = data_frame.loc[data_frame['linguagem'].str.lower() == language.lower()]
    if df_language.empty:
        return f"Não há códigos para a linguagem {language}."
    else:
        codes = ""
        for index, row in df_language.iterrows():
            codes += f"{row['codigo']}\n{row['funcao']}\n\n"
        return f"Códigos em {language}:\n\n{codes}"

@bot.message_handler(commands=["buscar"])
def list_language_codes(message):
    bot.send_message(message.chat.id, "Qual a linguagem?")
    bot.register_next_step_handler(message, wait_language_search)

def wait_language_search(message):
    language = message.text
    codes_list = list_codes(language)
    bot.send_message(message.chat.id, codes_list)

@bot.message_handler(commands=["codigo"])
def add_language(message):
	bot.send_message(message.chat.id, "Qual a linguagem?")
	bot.register_next_step_handler(message, wait_language)

def wait_language(message):
	language = message.text.lower()
	
	bot.send_message(message.chat.id, "Informe o código: ")
	bot.register_next_step_handler(message, lambda m: wait_code(m, language))

def wait_code(message, language):
	code = message.text
	bot.send_message(message.chat.id, "Diga o que o código faz: ")
	bot.register_next_step_handler(message, lambda m: wait_function(m, language, code))

def wait_function(message, language, code):
	function_code = message.text
	salvar(language, code, function_code)
	bot.send_message(message.chat.id, "Seu código foi adicionado com sucesso!")

@bot.message_handler(commands=["linguagem"])
def chamada(message):
	language(bot, message)

@bot.message_handler(commands=["exemplo"])
def chamada(message):
	example(bot, message)

@bot.message_handler(commands=["projeto"])
def chamada(message):
	project(bot, message)

@bot.message_handler(commands=["sintaxe"])
def chamada(message):
	syntax(bot, message)

@bot.message_handler(commands=["mascaraDeRede"])
def chamada(message):
	networkmask(bot, message)

@bot.message_handler(commands=["organizacao"])
def organizations(message):

	response = requests.get("https://api.github.com/organizations")
	organizations = response.json()
	random_org = random.choice(organizations)

	org_name = random_org["login"]

	response_organization = requests.get(f"https://api.github.com/orgs/{org_name}")
	organization = response_organization.json()

	text = f"""
		Nome: {organization["name"]}
		Blog: {organization["blog"]}
		Localização: {organization["location"]}
		Github: {organization["html_url"]}
	"""

	bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["sistemaOperacional"])
def chamada(message):
	operationalsystem(bot, message)

@bot.message_handler(commands=["solucoes"])
def chamada(message):
	solutions(bot, message)

def verificar(message):
	return True

@bot.message_handler(func=verificar)
def chamada(message):
	presentation(bot, message)

bot.polling()