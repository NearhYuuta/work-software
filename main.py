#importações de bibliotecas
import openai
import telebot

from funcoes.code import code
from funcoes.community import community
from funcoes.exemple import exemple
from funcoes.language import language
from funcoes.networkmask import networkmask
from funcoes.project import project
from funcoes.syntax import syntax
from funcoes.operationalsystem import operationalsystem
from funcoes.solutions import solutions

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
	exemple(bot, message)

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
def answer(message):

  text  = """
	Olá, eu sou o TechAssist
 
	/codigo - Fornece informações sobre a estrutura e sintaxe do código em diferentes linguagens de programação.
 
    /comunidade - Fornece informações sobre comunidades de desenvolvedores, fóruns e outras plataformas de discussão relacionadas à tecnologia da informação.
    
    /exemplo - Fornece exemplo de um código a partir de uma sintaxe informada.
    
    /linguagem - Fornece informações sobre linguagens de programação.
    
    /mascaraDeRede - Fornece o calculo de mascara de rede.
    
    /projeto - Fornece informações sobre boas práticas de desenvolvimento de projetos de software, metodologias e ferramentas utilizadas.
    
    /sintaxe - Fornece informações detalhadas sobre a sintaxe e estrutura de diferentes linguagens de programação.
    
    /sistemasOperacionais - Fornece informações sobre sistemas operacionais, suas funcionalidades e diferenças entre as versões.
    
    /solucoes - Fornece soluções para problemas comuns encontrados na programação e no uso de tecnologias da informação.
  """
      
  bot.reply_to(message,text)
  

	
bot.polling()