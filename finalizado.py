import tkinter as tk
from tkinter import simpledialog
from tkinter import simpledialog

class InterfaceGrafica:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("SGB")
        self.livros = [] 
        self.livros_comuns = []  # Lista para armazenar os livros comuns
        self.livros_raros = []  # Lista para armazenar os livros raros

        # Lista para armazenar as informações dos funcionários cadastrados
        self.funcionarios_cadastrados = []

        # Lista para armazenar as informações dos clientes cadastrados
        self.clientes_cadastrados = []

        # Criação dos botões
        self.botao_funcionario = tk.Button(janela, text="Funcionário", command=self.abrir_tela_funcionario)
        self.botao_funcionario.pack(pady=10)

        self.botao_cliente = tk.Button(janela, text="Cliente", command=self.abrir_tela_cliente)
        self.botao_cliente.pack(pady=10)

    def abrir_tela_funcionario(self):
        # Código para abrir a tela de funcionário
        tela_funcionario = tk.Toplevel(self.janela)
        tela_funcionario.title("Tela do Funcionário")
        tela_funcionario.geometry("300x300")

        # Centralizar os botões na tela do funcionário
        tela_funcionario.pack_propagate(0)
        tela_funcionario.grid_rowconfigure(0, weight=1)
        tela_funcionario.grid_columnconfigure(0, weight=1)

        # Criação dos botões na tela do funcionário
        botao_cadastro = tk.Button(tela_funcionario, text="Cadastro", command=self.abrir_tela_cadastro)
        botao_cadastro.pack(pady=10)

        botao_login = tk.Button(tela_funcionario, text="Login", command=self.abrir_tela_login)
        botao_login.pack(pady=10)

    def abrir_tela_cadastro(self):
        # Código para abrir a tela de cadastro
        tela_cadastro = tk.Toplevel(self.janela)
        tela_cadastro.title("Cadastro de Funcionário")
        tela_cadastro.geometry("300x200")

        # Centralizar os campos de email e senha
        tela_cadastro.pack_propagate(0)
        tela_cadastro.grid_rowconfigure(0, weight=1)
        tela_cadastro.grid_columnconfigure(0, weight=1)

        # Campos de email e senha
        label_email = tk.Label(tela_cadastro, text="Email:")
        label_email.pack(pady=5)
        entry_email = tk.Entry(tela_cadastro)
        entry_email.pack(pady=5)

        label_senha = tk.Label(tela_cadastro, text="Senha:")
        label_senha.pack(pady=5)
        entry_senha = tk.Entry(tela_cadastro, show="*")
        entry_senha.pack(pady=5)

        botao_confirmar = tk.Button(tela_cadastro, text="Confirmar", command=lambda: self.cadastrar_funcionario(entry_email.get(), entry_senha.get()))
        botao_confirmar.pack(pady=10)

    def abrir_tela_login(self):
        # Código para abrir a tela de login
        tela_login = tk.Toplevel(self.janela)
        tela_login.title("Login de Funcionário")
        tela_login.geometry("300x200")

        # Centralizar os campos de email e senha
        tela_login.pack_propagate(0)
        tela_login.grid_rowconfigure(0, weight=1)
        tela_login.grid_columnconfigure(0, weight=1)

        # Campos de email e senha
        label_email = tk.Label(tela_login, text="Email:")
        label_email.pack(pady=5)
        entry_email = tk.Entry(tela_login)
        entry_email.pack(pady=5)

        label_senha = tk.Label(tela_login, text="Senha:")
        label_senha.pack(pady=5)
        entry_senha = tk.Entry(tela_login, show="*")
        entry_senha.pack(pady=5)

        botao_confirmar = tk.Button(tela_login, text="Login", command=lambda: self.validar_login(entry_email.get(), entry_senha.get()))
        botao_confirmar.pack(pady=10)

    def abrir_tela_cliente(self):
        # Código para abrir a tela de cliente
        tela_cliente = tk.Toplevel(self.janela)
        tela_cliente.title("Tela do Cliente")
        tela_cliente.geometry("300x200")

        # Centralizar os botões na tela do cliente
        tela_cliente.pack_propagate(0)
        tela_cliente.grid_rowconfigure(0, weight=1)
        tela_cliente.grid_columnconfigure(0, weight=1)

        # Criação dos botões na tela do cliente
        botao_cadastro_cliente = tk.Button(tela_cliente, text="Cadastro", command=self.abrir_tela_cadastro_cliente)
        botao_cadastro_cliente.pack(pady=10)

        botao_login_cliente = tk.Button(tela_cliente, text="Login", command=self.abrir_tela_login_cliente)
        botao_login_cliente.pack(pady=10)

    def abrir_tela_cadastro_cliente(self):
        # Código para abrir a tela de cadastro do cliente
        tela_cadastro_cliente = tk.Toplevel(self.janela)
        tela_cadastro_cliente.title("Cadastro de Cliente")
        tela_cadastro_cliente.geometry("300x200")

        # Centralizar os campos de email e senha do cliente
        tela_cadastro_cliente.pack_propagate(0)
        tela_cadastro_cliente.grid_rowconfigure(0, weight=1)
        tela_cadastro_cliente.grid_columnconfigure(0, weight=1)

        # Campos de email e senha do cliente
        label_email_cliente = tk.Label(tela_cadastro_cliente, text="Email:")
        label_email_cliente.pack(pady=5)
        entry_email_cliente = tk.Entry(tela_cadastro_cliente)
        entry_email_cliente.pack(pady=5)

        label_senha_cliente = tk.Label(tela_cadastro_cliente, text="Senha:")
        label_senha_cliente.pack(pady=5)
        entry_senha_cliente = tk.Entry(tela_cadastro_cliente, show="*")
        entry_senha_cliente.pack(pady=5)

        botao_confirmar_cliente = tk.Button(tela_cadastro_cliente, text="Confirmar", command=lambda: self.cadastrar_cliente(entry_email_cliente.get(), entry_senha_cliente.get()))
        botao_confirmar_cliente.pack(pady=10)

    def abrir_tela_login_cliente(self):
        # Código para abrir a tela de login do cliente
        tela_login_cliente = tk.Toplevel(self.janela)
        tela_login_cliente.title("Login de Cliente")
        tela_login_cliente.geometry("300x200")

        # Centralizar os campos de email e senha do cliente
        tela_login_cliente.pack_propagate(0)
        tela_login_cliente.grid_rowconfigure(0, weight=1)
        tela_login_cliente.grid_columnconfigure(0, weight=1)

        # Campos de email e senha do cliente
        label_email_cliente = tk.Label(tela_login_cliente, text="Email:")
        label_email_cliente.pack(pady=5)
        entry_email_cliente = tk.Entry(tela_login_cliente)
        entry_email_cliente.pack(pady=5)

        label_senha_cliente = tk.Label(tela_login_cliente, text="Senha:")
        label_senha_cliente.pack(pady=5)
        entry_senha_cliente = tk.Entry(tela_login_cliente, show="*")
        entry_senha_cliente.pack(pady=5)

        botao_confirmar_cliente = tk.Button(tela_login_cliente, text="Login", command=lambda: self.validar_login_cliente(entry_email_cliente.get(), entry_senha_cliente.get()))
        botao_confirmar_cliente.pack(pady=10)

    def cadastrar_funcionario(self, email, senha):
        # Verifica se o e-mail termina com "@funcionario"
        if email.endswith("@funcionario"):
            # Adiciona as informações do funcionário à lista de funcionários cadastrados
            self.funcionarios_cadastrados.append((email, senha))
            print("Cadastro de funcionário realizado com sucesso!")
            print("Email:", email)
            print("Senha:", senha)
        else:
            print("E-mail inválido! O e-mail deve terminar com '@funcionario'")

    def validar_login(self, email, senha):
        # Verifica se as informações de login correspondem a um funcionário cadastrado
        for funcionario in self.funcionarios_cadastrados:
            if email == funcionario[0] and senha == funcionario[1]:
                print("Login de funcionário realizado com sucesso!")
                print("Email:", email)
                print("Senha:", senha)
                self.abrir_tela_menu_funcionario()  # Abre a tela do menu do funcionário
                return
                
        print("Login inválido! Verifique suas informações.")

###############inicio menu funcionario#################
#################################3###############
    def abrir_tela_menu_funcionario(self):
        tela_menu_funcionario = tk.Toplevel(self.janela)
        tela_menu_funcionario.title("Menu do Funcionário")
        tela_menu_funcionario.geometry("300x400")
################################################botooes menu funcionario ###############
########################################################
        botao_adicionar_comum = tk.Button(tela_menu_funcionario, text="Adicionar um livro comum à biblioteca", command=self.adicionar_livro_comum)
        botao_adicionar_comum.pack(pady=10)

        botao_adicionar_raro = tk.Button(tela_menu_funcionario, text="Adicionar um livro raro à biblioteca", command=self.adicionar_livro_raro)
        botao_adicionar_raro.pack(pady=10)

        botao_remover = tk.Button(tela_menu_funcionario, text="Remover um livro da biblioteca", command=self.obter_isbn_remover_livro)
        botao_remover.pack(pady=10)
        
        botao_emprestimo = tk.Button(tela_menu_funcionario, text="Registrar um empréstimo de um livro", command=self.registrar_emprestimo)
        botao_emprestimo.pack(pady=10)

        botao_devolucao = tk.Button(tela_menu_funcionario, text="Registrar a devolução de um livro", command=self.registrar_devolucao)
        botao_devolucao.pack(pady=10)

        botao_listar_emprestados = tk.Button(tela_menu_funcionario, text="Listar todos os livros emprestados", command=self.listar_livros_emprestados)
        botao_listar_emprestados.pack(pady=10)

        botao_listar_cadastrados = tk.Button(tela_menu_funcionario, text="Listar todos os livros cadastrados", command=self.listar_livros_cadastrados)
        botao_listar_cadastrados.pack(pady=10)


        botao_sair = tk.Button(tela_menu_funcionario, text="Sair do programa", command=self.janela.quit)
        botao_sair.pack(pady=10)
#################################################funçao add livro comun########
###############################################
    def adicionar_livro_comum(self):
        titulo = tk.simpledialog.askstring("Adicionar livro comum", "Digite o título do livro:")
        autor = tk.simpledialog.askstring("Adicionar livro comum", "Digite o autor do livro:")
        isbn = tk.simpledialog.askstring("Adicionar livro comum", "Digite o ISBN do livro:")
        ano_publicacao = tk.simpledialog.askstring("Adicionar livro comum", "Digite o Ano da publicação do livro:")
        categoria = tk.simpledialog.askstring("Adicionar livro comum", "Digite a categoria do livro:")
        numero_de_copias = tk.simpledialog.askinteger("Adicionar livro comum", "Digite o número de cópias do livro:")

        livro = {
            "titulo": titulo,
            "autor": autor,
            "isbn": isbn,
            "ano_publicacao": ano_publicacao,
            "categoria": categoria,
            "numero_de_copias": numero_de_copias
        }

        self.livros_comuns.append(livro)  # Adiciona o livro à lista de livros comuns
#########################add livro raro#################
##################################################################3

    def adicionar_livro_raro(self):
        titulo = tk.simpledialog.askstring("Adicionar livro raro", "Digite o título do livro:")
        autor = tk.simpledialog.askstring("Adicionar livro raro", "Digite o autor do livro:")
        isbn = tk.simpledialog.askstring("Adicionar livro raro", "Digite o ISBN do livro:")
        ano_publicacao = tk.simpledialog.askstring("Adicionar livro raro", "Digite o Ano da publicação do livro:")
        categoria = tk.simpledialog.askstring("Adicionar livro raro", "Digite a categoria do livro:")
        edicao = tk.simpledialog.askstring("Adicionar livro raro", "Digite a edição do livro:")
        estado = tk.simpledialog.askstring("Adicionar livro raro", "Digite o estado do livro:")
        numero_de_copias = tk.simpledialog.askinteger("Adicionar livro raro", "Digite o número de cópias do livro:")

        livro = {
            "titulo": titulo,
            "autor": autor,
            "isbn": isbn,
            "ano_publicacao": ano_publicacao,
            "categoria": categoria,
            "edicao": edicao,
            "estado": estado,
            "numero_de_copias": numero_de_copias
        }

        self.livros_raros.append(livro)  # Adiciona o livro à lista de livros raros


    def remover_livro(self, isbn):
        livro_removido = False

        for livro in self.livros_comuns:
            if livro['isbn'] == isbn:
                print("Livro comum encontrado:")
                print(livro)
                self.livros_comuns.remove(livro)
                print("Livro comum removido com sucesso!")
                livro_removido = True
                break

        if not livro_removido:
            for livro in self.livros_raros:
                if livro['isbn'] == isbn:
                    print("Livro raro encontrado:")
                    print(livro)
                    self.livros_raros.remove(livro)
                    print("Livro raro removido com sucesso!")
                    livro_removido = True
                    break

        if not livro_removido:
            print("Livro não encontrado.")

    def obter_isbn_remover_livro(self):
        isbn = tk.simpledialog.askstring("Remover livro", "Digite o ISBN do livro que deseja remover:")
        self.remover_livro(isbn)


    def registrar_emprestimo(self):
        isbn = tk.simpledialog.askstring("Registrar empréstimo", "Digite o ISBN do livro que deseja emprestar:")
        nome_usuario = tk.simpledialog.askstring("Registrar empréstimo", "Digite o nome do usuário que está emprestando o livro:")
        email_usuario = tk.simpledialog.askstring("Registrar empréstimo", "Digite o email do usuário:")
        
        livro_encontrado = False

        for livro in self.livros_comuns:
            if livro['isbn'] == isbn:
                livro['emprestado'] = True
                livro['nome_usuario'] = nome_usuario
                livro['email_usuario'] = email_usuario
                print("Empréstimo registrado com sucesso para o livro comum!")
                livro_encontrado = True
                break

        if not livro_encontrado:
            for livro in self.livros_raros:
                if livro['isbn'] == isbn:
                    livro['emprestado'] = True
                    livro['nome_usuario'] = nome_usuario
                    livro['email_usuario'] = email_usuario
                    print("Empréstimo registrado com sucesso para o livro raro!")
                    livro_encontrado = True
                    break

        if not livro_encontrado:
            print("Livro não encontrado.")



    def registrar_devolucao(self):
        isbn = tk.simpledialog.askstring("Registrar devolução", "Digite o ISBN do livro que está sendo devolvido:")
        nome_usuario = tk.simpledialog.askstring("Registrar devolução", "Digite o nome do usuário que está devolvendo o livro:")
        email_usuario = tk.simpledialog.askstring("Registrar devolução", "Digite o e-mail do usuário que está devolvendo o livro:")
        
        livro_encontrado = False

        for livro in self.livros_comuns:
            if livro['isbn'] == isbn:
                if livro.get('emprestado', False):
                    if livro.get('nome_usuario') == nome_usuario and livro.get('email_usuario') == email_usuario:
                        del livro['emprestado']
                        del livro['nome_usuario']
                        del livro['email_usuario']
                        print("Devolução registrada com sucesso para o livro comum!")
                    else:
                        print("As informações do usuário não correspondem ao empréstimo registrado.")
                else:
                    print("O livro comum não está emprestado.")
                livro_encontrado = True
                break

        if not livro_encontrado:
            for livro in self.livros_raros:
                if livro['isbn'] == isbn:
                    if livro.get('emprestado', False):
                        if livro.get('nome_usuario') == nome_usuario and livro.get('email_usuario') == email_usuario:
                            del livro['emprestado']
                            del livro['nome_usuario']
                            del livro['email_usuario']
                            print("Devolução registrada com sucesso para o livro raro!")
                        else:
                            print("As informações do usuário não correspondem ao empréstimo registrado.")
                    else:
                        print("O livro raro não está emprestado.")
                    livro_encontrado = True
                    break

        if not livro_encontrado:
            print("Livro não encontrado.")

    def listar_livros_emprestados(self):
        print("Livros emprestados:")

        for livro in self.livros_comuns + self.livros_raros:
            if livro.get('emprestado', False):
                print("Título:", livro['titulo'])
                print("Autor:", livro['autor'])
                print("ISBN:", livro['isbn'])
                print("Nome do usuário:", livro['nome_usuario'])
                print("Email do usuário:", livro['email_usuario'])
                print("--------------------")

    
    def listar_livros_cadastrados(self):
        tela_listagem = tk.Toplevel(self.janela)
        tela_listagem.title("Lista de Livros Cadastrados")

        # Crie um widget de texto para exibir as informações dos livros
        texto_listagem = tk.Text(tela_listagem)
        texto_listagem.pack()

        # Adicione as informações dos livros ao widget de texto
        texto_listagem.insert(tk.END, "Lista de livros cadastrados:\n\n")

        for livro in self.livros_comuns + self.livros_raros:
            texto_listagem.insert(tk.END, f"Título: {livro['titulo']}\n")
            texto_listagem.insert(tk.END, f"Autor: {livro['autor']}\n")
            texto_listagem.insert(tk.END, f"ISBN: {livro['isbn']}\n")
            texto_listagem.insert(tk.END, f"Ano de Publicação: {livro['ano_publicacao']}\n")
            texto_listagem.insert(tk.END, f"Categoria: {livro['categoria']}\n")
            texto_listagem.insert(tk.END, f"Número de Cópias: {livro['numero_de_copias']}\n")
            texto_listagem.insert(tk.END, "--------------------\n")

    # Desabilitar a edição do widget de texto
        texto_listagem.configure(state="disabled")

    def adicionar_livro_comum_backend(self, titulo, autor, isbn, ano_publicacao, categoria, numero_de_copias):
        print("Adicionar um livro comum à biblioteca...")
        # Substitua esta parte do código com a lógica do seu programa para adicionar um livro comum

    def adicionar_livro_raro_backend(self, titulo, autor, isbn, ano_publicacao, categoria, edicao, estado, numero_de_copias):
        print("Adicionar um livro raro à biblioteca...")
        # Substitua esta parte do código com a lógica do seu programa para adicionar um livro raro

    def remover_livro_backend(self, isbn):
        print("Remover um livro da biblioteca...")
        # Substitua esta parte do código com a lógica do seu programa para remover um livro

    def registrar_emprestimo_backend(self, isbn, nome_usuario, email_usuario):
        print("Registrar um empréstimo de um livro...")
        # Substitua esta parte do código com a lógica do seu programa para registrar um empréstimo

    def registrar_devolucao_backend(self, isbn, nome_usuario, email_usuario):
        print("Registrar a devolução de um livro...")
        # Substitua esta parte do código com a lógica do seu programa para registrar uma devolução

    def listar_livros_emprestados_backend(self):
        print("Listar todos os livros emprestados...")
        # Substitua esta parte do código com a lógica do seu programa para listar os livros emprestados



    ########################################################################################
    #######################ao sair volta tela de funcionario e cliente#########
    #def iniciar(self):
        #self.janela.mainloop()
#######################################33###############################

    def cadastrar_cliente(self, email, senha):
        # Verifica se o e-mail termina com "@cliente"
        if email.endswith("@cliente"):
            # Adiciona as informações do cliente à lista de clientes cadastrados
            self.clientes_cadastrados.append((email, senha))
            print("Cadastro de cliente realizado com sucesso!")
            print("Email:", email)
            print("Senha:", senha)
        else:
            print("E-mail inválido! O e-mail deve terminar com '@cliente'")

    def validar_login_cliente(self, email, senha):
        # Verifica se as informações de login correspondem a um cliente cadastrado
        for cliente in self.clientes_cadastrados:
            if email == cliente[0] and senha == cliente[1]:
                print("Login de cliente realizado com sucesso!")
                print("Email:", email)
                print("Senha:", senha)
                self.abrir_tela_menu_cliente()  # Abre a tela do menu do cliente
                return
                return
        print("Login inválido! Verifique suas informações.")

    def abrir_tela_menu_cliente(self):
        # Código para abrir a tela do menu do cliente
        tela_menu_cliente = tk.Toplevel(self.janela)
        tela_menu_cliente.title("Menu do Cliente")
        tela_menu_cliente.geometry("300x300")

        # Centralizar os botões na tela do menu do cliente
        tela_menu_cliente.pack_propagate(0)
        tela_menu_cliente.grid_rowconfigure(0, weight=1)
        tela_menu_cliente.grid_columnconfigure(0, weight=1)

        # Criação dos botões na tela do menu do cliente
        botao_buscar = tk.Button(tela_menu_cliente, text="Buscar um livro na biblioteca", command=self.buscar_livro)
        botao_buscar.pack(pady=10)

        botao_listar = tk.Button(tela_menu_cliente, text="Listar todos os livros da biblioteca", command=self.listar_livros)
        botao_listar.pack(pady=10)

        

        botao_sair = tk.Button(tela_menu_cliente, text="Sair do programa", command=self.janela.quit)
        botao_sair.pack(pady=10)

    def buscar_livro(self):
        # Código para buscar um livro na biblioteca
        tela_buscar_livro = tk.Toplevel(self.janela)
        tela_buscar_livro.title("Buscar Livro")
        tela_buscar_livro.geometry("300x200")

        # Centralizar os campos de busca
        tela_buscar_livro.pack_propagate(0)
        tela_buscar_livro.grid_rowconfigure(0, weight=1)
        tela_buscar_livro.grid_columnconfigure(0, weight=1)

        # Campo de busca
        label_busca = tk.Label(tela_buscar_livro, text="Digite o título do livro:")
        label_busca.pack(pady=5)
        entry_busca = tk.Entry(tela_buscar_livro)
        entry_busca.pack(pady=5)

        # Botão de busca
        botao_buscar = tk.Button(tela_buscar_livro, text="Buscar", command=lambda: self.exibir_livro(entry_busca.get()))
        botao_buscar.pack(pady=10)

    def exibir_livro(self, titulo):
        # Procurar o livro na biblioteca pelo título
        livro_encontrado = None

        for livro in self.livros_comuns + self.livros_raros:
            if livro['titulo'].lower() == titulo.lower():
                livro_encontrado = livro
                break

        # Criar uma nova janela para exibir as informações do livro
        tela_exibir_livro = tk.Toplevel(self.janela)
        tela_exibir_livro.title("Livro Encontrado")
        tela_exibir_livro.geometry("400x300")

        # Centralizar os campos de exibição
        tela_exibir_livro.pack_propagate(0)
        tela_exibir_livro.grid_rowconfigure(0, weight=1)
        tela_exibir_livro.grid_columnconfigure(0, weight=1)

        # Exibir as informações do livro
        if livro_encontrado:
            label_titulo = tk.Label(tela_exibir_livro, text="Título: " + livro_encontrado['titulo'])
            label_titulo.pack(pady=5)
            label_autor = tk.Label(tela_exibir_livro, text="Autor: " + livro_encontrado['autor'])
            label_autor.pack(pady=5)
            # Adicionar mais informações do livro, se necessário
        else:
            label_mensagem = tk.Label(tela_exibir_livro, text="Livro não encontrado.")
            label_mensagem.pack(pady=5)

        def realizar_busca(self, titulo):
            # Código para realizar a busca do livro
            print("Realizando busca do livro com título:", titulo)





    def listar_livros(self):
        # Criação da nova janela para listar os livros
        tela_listar_livros = tk.Toplevel(self.janela)
        tela_listar_livros.title("Lista de Livros")
        tela_listar_livros.geometry("400x300")

        # Centralizar os campos de exibição
        tela_listar_livros.pack_propagate(0)
        tela_listar_livros.grid_rowconfigure(0, weight=1)
        tela_listar_livros.grid_columnconfigure(0, weight=1)

        # Criação de um frame para exibir a lista de livros com scrollbar
        frame_livros = tk.Frame(tela_listar_livros)
        frame_livros.pack(pady=10, fill=tk.BOTH, expand=True)

        # Criação da scrollbar vertical
        scrollbar_vertical = tk.Scrollbar(frame_livros)
        scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

        # Criação da listbox para exibir os livros
        listbox_livros = tk.Listbox(frame_livros, yscrollcommand=scrollbar_vertical.set)
        listbox_livros.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configuração da scrollbar para funcionar com a listbox
        scrollbar_vertical.config(command=listbox_livros.yview)

        # Adicionar os livros cadastrados à listbox
        for livro in self.livros_comuns + self.livros_raros:
            titulo = livro['titulo']
            autor = livro['autor']
            listbox_livros.insert(tk.END, f"Título: {titulo} - Autor: {autor}")

        # Função para fechar a janela
        def fechar_janela():
            tela_listar_livros.destroy()

        # Botão de fechar janela
        botao_fechar = tk.Button(tela_listar_livros, text="Fechar", command=fechar_janela)
        botao_fechar.pack(pady=10)


# Criar a janela principal
janela_principal = tk.Tk()

# Definir o tamanho da janela
janela_principal.geometry("300x300")

# Centralizar os botões na janela
janela_principal.pack_propagate(0)
janela_principal.grid_rowconfigure(0, weight=1)
janela_principal.grid_columnconfigure(0, weight=1)

# Criar a instância da interface gráfica
interface = InterfaceGrafica(janela_principal)

# Iniciar o loop principal da aplicação
janela_principal.mainloop()




# Criação da janela principal
janela = tk.Tk()

# Criação da instância da classe InterfaceGrafica
minha_instancia = InterfaceGrafica(janela)

# Início do loop principal da interface gráfica
janela.mainloop()