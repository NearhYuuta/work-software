#importações de bibliotecas
import openai
import telebot

<<<<<<< HEAD
from funcoes.codigo import codigo
from funcoes.comunidade import comunidade
from funcoes.exemplo import exemplo
from funcoes.linguagem import linguagem
from funcoes.mascaraderede import mascaraderede
from funcoes.projeto import projeto
from funcoes.sintaxe import sintaxe
from funcoes.sistemasoperacionais import sistemasoperacionais
from funcoes.solucoes import solucoes
=======
from funcoes.code import code
from funcoes.community import community
from funcoes.example import example
from funcoes.language import language
from funcoes.networkmask import networkmask
from funcoes.project import project
from funcoes.syntax import syntax
from funcoes.operationalsystem import operationalsystem
from funcoes.solutions import solutions
>>>>>>> 74138ab67b0829c5b31fd7bdfb61f14d3c0e2359

#variáveis
openai.api_key = "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"
chave_api_telegram = "6106311624:AAGH_MRyPVA6y2yNcRLu3-mn4pXyjCXF-HY"
bot = telebot.TeleBot(chave_api_telegram)

#chamada das funções

@bot.message_handler(commands=["codigo"])
def chamada(message):
<<<<<<< HEAD
	codigo(bot, message)

@bot.message_handler(commands=["linguagem"])
def chamada(message):
	linguagem(bot, message)

@bot.message_handler(commands=["comunidade"])
def chamada(message):
	comunidade(bot, message)

@bot.message_handler(commands=["exemplo"])
def chamada(message):
	exemplo(bot, message)

@bot.message_handler(commands=["projeto"])
def chamada(message):
	projeto(bot, message)

@bot.message_handler(commands=["sintaxe"])
def chamada(message):
	sintaxe(bot, message)

@bot.message_handler(commands=["mascaraDeRede"])
def chamada(message):
	mascaraderede(bot, message)

@bot.message_handler(commands=["sistemasOperacionais"])
def chamada(message):
	sistemasoperacionais(bot, message)

@bot.message_handler(commands=["solucoes"])
def chamada(message):
	solucoes(bot, message)
=======
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
>>>>>>> 74138ab67b0829c5b31fd7bdfb61f14d3c0e2359

def verificar(message):
  return True

@bot.message_handler(func=verificar)
<<<<<<< HEAD
def responder(message):
=======
def answer(message):
>>>>>>> 74138ab67b0829c5b31fd7bdfb61f14d3c0e2359

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