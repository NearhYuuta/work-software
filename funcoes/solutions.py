import PySimpleGUI as sg

def solutions(bot, message):
	solucoes = ['Verifique se todos os cabos estão conectados corretamente.', 
                'Reinicie o computador.', 
                'Atualize os drivers do dispositivo.', 
                'Realize uma limpeza nos componentes internos do computador.', 
                'Verifique se há algum malware no sistema.', 
                'Realize um diagnóstico de hardware para identificar o problema.']
	
	layout = [
		[sg.Text("Soluções de problema de hardware:")],
		[sg.Listbox(values=solucoes, size=(50, 6))],
		[sg.Button("Fechar")]
	]

	janela = sg.Window("oluções para problemas de hardware").Layout(layout)

	while True:
		evento, valores = janela.Read()
		if evento in (None, "Fechar"):
			break

	janela.Close()