#importações de bibliotecas
import openai
import telebot

from funcoes.code import code
from funcoes.community import community
from funcoes.example import example
from funcoes.language import language
from funcoes.networkmask import networkmask
from funcoes.project import project
from funcoes.syntax import syntax
from funcoes.operationalsystem import operationalsystem
from funcoes.solutions import solutions
from funcoes.presentation import presentation

#variáveis
openai.api_key = "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"
chave_api_telegram = "6106311624:AAGH_MRyPVA6y2yNcRLu3-mn4pXyjCXF-HY"
bot = telebot.TeleBot(chave_api_telegram)

#chamada das funções

@bot.message_handler(commands=["codigo"])
def chamada(message):
	code(bot, message)

@bot.message_handler(commands=["linguagem"])
def chamada(message):
	language(bot, message)

@bot.message_handler(commands=["comunidade"])
def chamada(message):
	community(bot, message)

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

@bot.message_handler(commands=["sistemasOperacionais"])
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