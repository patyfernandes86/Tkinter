import tkinter as tk

def converter():
  
    cm = float(entrada_cm.get())
   
    metros = cm / 100
    
    resultado_label.config(text=f'{cm} centímetros equivalem a {metros} metros.')

janela = tk.Tk()
janela.title('Conversor de Centímetros para Metros')

tk.Label(janela, text='Insira o valor em centímetros:').pack()
entrada_cm = tk.Entry(janela)
entrada_cm.pack()
btn_converter = tk.Button(janela, text='Converter', command=converter)
btn_converter.pack()
resultado_label = tk.Label(janela, text='')
resultado_label.pack()


janela.mainloop()