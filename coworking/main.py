import tkinter as tk


def fechar_janela(janela_atual):
    janela_atual.destroy()

def abrir_janela_clientes():
    # Função para abrir a janela de cadastro
    janela_clientes = tk.Toplevel()
    janela_clientes.title("Clientes")

    # Para a tela abrir uma sobre a outra
    # Obtendo a geometria da janela principal
    geometria_janela_principal = janela_principal.geometry()
    # Definindo a geometria da janela de cadastro para ser igual à geometria da janela principal
    janela_clientes.geometry(geometria_janela_principal)

    def cadastrar_cliente():
        print()


    def abrir_janela_registrar_clientes():
        janela_cadastro_clientes = tk.Toplevel()
        janela_cadastro_clientes.title("Registrar novo cliente")

        geometria_janela_principal = janela_principal.geometry()
        janela_cadastro_clientes.geometry(geometria_janela_principal)

        # Labels e campos de entrada
        tk.Label(janela_cadastro_clientes, text="Nome:").grid(row=0, column=0, padx=10, pady=5)
        entry_nome = tk.Entry(janela_cadastro_clientes)
        entry_nome.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(janela_cadastro_clientes, text="Data de nascimento:").grid(row=1, column=0, padx=10, pady=5)
        entry_nome = tk.Entry(janela_cadastro_clientes)
        entry_nome.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(janela_cadastro_clientes, text="CPF:").grid(row=2, column=0, padx=10, pady=5)
        entry_nome = tk.Entry(janela_cadastro_clientes)
        entry_nome.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(janela_cadastro_clientes, text="CPF:").grid(row=2, column=0, padx=10, pady=5)
        entry_nome = tk.Entry(janela_cadastro_clientes)
        entry_nome.grid(row=2, column=1, padx=10, pady=5)

        btn_salvar = tk.Button(janela_cadastro_clientes, text="Cadastrar", command=cadastrar_cliente)
        btn_salvar.grid(row=6, column=0, pady=10)

        btn_fechar = tk.Button(janela_cadastro_clientes, text="Fechar Janela", command=lambda: fechar_janela(janela_cadastro_clientes))
        btn_fechar.grid(row=6, column=1, pady=10)

    def abrir_janela_clientes_cadastrados():
        print("precisa ter um código aqui?")


    btn_registrar_cliente = tk.Button(janela_clientes, text="Registrar cliente", command=abrir_janela_registrar_clientes)
    btn_registrar_cliente.pack(padx=5, pady=5)

    btn_clientes_registrados = tk.Button(janela_clientes, text="Clientes cadastrados", command=abrir_janela_clientes_cadastrados)
    btn_clientes_registrados.pack(padx=5, pady=5)

# Criando a janela principal
janela_principal = tk.Tk()
janela_principal.title("Exemplo de Cadastro")
janela_principal.geometry("400x300")

# Botão para abrir a janela de cadastro
botao_cadastro = tk.Button(janela_principal, text="Clientes/Parceiros", command=abrir_janela_clientes)
botao_cadastro.pack(padx=5, pady=5)

# Executando o loop principal da aplicação
janela_principal.mainloop()

