from tkinter import * # importa a biblioteca tkinter
janela = Tk()

janela.geometry("600x600") #largura x altura da janela


instrucao = Label(janela, text="\nVAI SE FOUDER MANO", font=("Arial", 20))# texto da janela e tamanho da fonte
instrucao.pack()
instrucao = Label(janela, text="\nVai se fouder o perua", font=("Arial", 20)) # texto da janela e tamanho da fonte
instrucao.pack() # coloca o texto na janela
janela.title("Interface Gráfica") # titulo da janela
janela.mainloop() # abre a janela