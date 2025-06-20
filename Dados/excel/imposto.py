import pandas as pd
import tkinter as tk
from tkinter import messagebox
import os  # import padrão pra manipular arquivos

def calcular_ir(rendimento_anual, dependentes=0, gastos_saude=0, gastos_educacao=0, inss=0):
    deducao_dependente = 189.59 * 12  # por dependente ao ano
    deducao_total = (dependentes * deducao_dependente +
                     gastos_saude + gastos_educacao + inss)

    base_calculo = rendimento_anual - deducao_total

    if base_calculo <= 22560.00:
        aliquota = 0.0
        deducao = 0.0
    elif base_calculo <= 33792.00:
        aliquota = 0.075
        deducao = 1692.00
    elif base_calculo <= 45000.00:
        aliquota = 0.15
        deducao = 3816.00
    elif base_calculo <= 55944.00:
        aliquota = 0.225
        deducao = 6924.00
    else:
        aliquota = 0.275
        deducao = 9504.00

    imposto = (base_calculo * aliquota) - deducao
    return max(imposto, 0.0)

def gerar_relatorio():
    try:
        rendimento_mensal = float(entry_rendimento.get())
        dependentes = int(entry_dependentes.get())
        gastos_saude = float(entry_saude.get())
        gastos_educacao = float(entry_educacao.get())
        inss = float(entry_inss.get())

        rendimento_anual = rendimento_mensal * 12
        imposto = calcular_ir(rendimento_anual, dependentes, gastos_saude, gastos_educacao, inss)

        dados = {
            "Rendimento Mensal (R$)": [rendimento_mensal],
            "Rendimento Anual (R$)": [rendimento_anual],
            "Dependentes": [dependentes],
            "Gastos com Saúde (R$)": [gastos_saude],
            "Gastos com Educação (R$)": [gastos_educacao],
            "INSS (R$)": [inss],
            "IR Devido (R$)": [round(imposto, 2)]
        }

        df_novo = pd.DataFrame(dados)

        if os.path.exists("relatorio_irpf.xlsx"):
            df_existente = pd.read_excel("relatorio_irpf.xlsx")
            df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_atualizado = df_novo

        df_atualizado.to_excel("relatorio_irpf.xlsx", index=False)

        messagebox.showinfo("Resultado", f"IR Devido: R$ {round(imposto, 2)}")
        messagebox.showinfo("Arquivo Excel", "Arquivo 'relatorio_irpf.xlsx' atualizado com sucesso.")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

# Interface com Tkinter
janela = tk.Tk()
janela.title("Calculadora de IRPF")
janela.geometry("400x430")
janela.resizable(False, False)

largura_entry = 30

tk.Label(janela, text="Rendimento Mensal (R$):").pack(pady=5)
entry_rendimento = tk.Entry(janela, width=largura_entry)
entry_rendimento.pack()

tk.Label(janela, text="Número de Dependentes:").pack(pady=5)
entry_dependentes = tk.Entry(janela, width=largura_entry)
entry_dependentes.pack()

tk.Label(janela, text="Gastos com Saúde (anual R$):").pack(pady=5)
entry_saude = tk.Entry(janela, width=largura_entry)
entry_saude.pack()

tk.Label(janela, text="Gastos com Educação (anual R$):").pack(pady=5)
entry_educacao = tk.Entry(janela, width=largura_entry)
entry_educacao.pack()

tk.Label(janela, text="Total pago de INSS (anual R$):").pack(pady=5)
entry_inss = tk.Entry(janela, width=largura_entry)
entry_inss.pack()

tk.Button(janela, text="Calcular IR", command=gerar_relatorio, bg="green", fg="white").pack(pady=20)

janela.mainloop()