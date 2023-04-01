def presentation(bot, message):
  text  = """
	Olá, eu sou o TechAssist e estou aqui para ajudá-lo com suas dúvidas relacionadas à tecnologia e programação. 

/buscar - buscarei códigos na minha base de dados de acordo com a lingaugem que você informar

/codigo - Me envie um codigo e diga a qual linguagem ele pertence e o que ele faz, assim poderei armazená-lo para outras pessoas poderem buscar na minha base de dados

/organizacoes - Vou mostrar para você alguma organização aleatoria de programação do github.

/exemplo - Vou mostrar um exemplo de código com base na linguagem que você pedir.

/linguagem - Vou fornecer informações sobre a linguagem de programação que você especificar.

/mascaraDeRede - Posso calcular uma máscara de rede para você com base nas informações que me fornecer.

/projeto - Vou fornecer ideias para projetos de programação.

/sintaxe - Vou fornecer informações detalhadas sobre a sintaxe e estrutura de diferentes linguagens de programação.

/sistemasOperacionais - Vou fornecer informações sobre sistemas operacionais, suas funcionalidades e diferenças entre as versões.

/solucoes - Vou fornecer soluções para problemas comuns encontrados na programação e no uso de tecnologias da informação.

Para usar qualquer um desses comandos, basta digitar "/comando" e enviar a mensagem para mim. Estou aqui para ajudá-lo a se tornar um melhor programador e resolver seus problemas de TI!
  """
      
  bot.reply_to(message,text)