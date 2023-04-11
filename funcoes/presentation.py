def presentation(bot, message):
  text  = """
	Olá! Eu sou o TechAssist, um assistente virtual pronto para ajudá-lo com todas as suas dúvidas relacionadas a tecnologia e programação. Com meus recursos avançados, posso oferecer diversos comandos úteis que podem auxiliá-lo no seu dia a dia. Confira abaixo:

/buscar - Posso buscar códigos em minha base de dados de acordo com a linguagem que você especificar.

/codigo - Você pode me enviar um código e informar a qual linguagem ele pertence e o que ele faz. Assim, poderei armazená-lo em minha base de dados para que outras pessoas possam buscar.

/exemplo - Posso mostrar exemplos de códigos com base na linguagem que você pedir.

/linguagem - Fornecerei informações detalhadas sobre a linguagem de programação que você especificar.

/mascaraDeRede - Posso calcular uma máscara de rede para você com base nas informações que me fornecer.

/organizacao - Posso mostrar organizações aleatórias de programação do GitHub para você explorar.

/projeto - Vou fornecer ideias de projetos de programação, seja para sites ou softwares.

/sistemaOperacional - Posso informar qual o seu sistema operacional e mostrar informações relevantes sobre ele.

/solucoes - Posso fornecer soluções para problemas comuns encontrados em dispositivos de hardware, como computadores, celulares e outros equipamentos eletrônicos.

Para utilizar qualquer um desses comandos, basta digitar "/comando" e enviar a mensagem para mim. Fico feliz em ajudá-lo a se tornar um programador ainda melhor e a solucionar seus problemas de TI.
  """
      
  bot.reply_to(message, text)
