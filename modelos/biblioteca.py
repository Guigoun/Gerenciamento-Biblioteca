from modelos.livro import Livro
from modelos.usuario import Usuario

class Biblioteca:
    
    def __init__(self):
            
        self.livros = {}
        self.usuarios = {}

    def adicionar_livro(self):
            
        nome_livro = str(input("Digite o nome do livro que deseja adicionar: "))
            
        if any(livro.titulo  == nome_livro for livro in self.livros.values()):
            print("\nEsse livro já está cadastrado\n")
            return
            
        id_livro = len(self.livros) + 1
        nome_autor = str(input("Digite o nome do autor: "))
                
        novo_livro = Livro(id_livro, nome_livro, nome_autor, disponibilidade=True)
        self.livros[id_livro] = novo_livro
            
        print(f"\nLivro {nome_livro} cadastrado com sucesso\n")
        
    def adicionar_usuario(self):
            
        nome_usuario = str(input("Digite seu nome: "))
            
        if any(usuario.nome == nome_usuario for usuario in self.usuarios.values()):
            print("\nEsse usuário já está cadastrado\n")
            return
            
        id_usuario = len(self.usuarios) + 1
        matricula_usuario = len(self.usuarios) + 100
                
        novo_usuario = Usuario(id_usuario, nome_usuario, matricula_usuario, livros_emprestados_usuario=[])
        self.usuarios[id_usuario] = novo_usuario
                
        print(f"\nO Usuário {nome_usuario} foi cadastrado!\n")
                         
    def exibir_livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.livros.values() if livro.disponibilidade]
        
        if not livros_disponiveis:
            print("\nNão há livros disponíveis\n")
        else:
            for livro in livros_disponiveis:
                print(livro)
        
    def pegar_livro_emprestado(self):
            
        nome_usuario = input("Digite seu nome: ")
        usuario = None
        livro = None
        
        for u in self.usuarios.values():
            if u.nome == nome_usuario:
                usuario = u
                break
    
        if not usuario:
            print("\nUsuário não está cadastrado\n")
            return

        nome_livro = input("Digite o nome do livro que deseja pegar emprestado: ")

        for l in self.livros.values():
            if l.titulo == nome_livro:
                livro = l
                break

        if not livro:
            print("\nO livro que deseja não está cadastrado\n")
            return

        if not livro.disponibilidade:
            print("\nO livro já está emprestado\n")
            return

        usuario.livros_emprestados_usuario.append(nome_livro)
        livro.disponibilidade = False
        print(f"\nEmpréstimo do livro {nome_livro} bem-sucedido para o usuário {nome_usuario}\n")
    
    def exibir_livros_emprestados(self):
        livro_emprestado = [livro for livro in self.livros.values() if livro.disponibilidade == False]
        
        if not livro_emprestado:
            print("\nNenhum livro da biblioteca foi emprestado\n")
            return
        
        print("\nLista de Livros emprestados\n")
        for livro in livro_emprestado:
            print(f"{livro}\n")
            
    def exibir_livros_emprestados_usuarios(self):
        livros_usuarios = [usuario for usuario in self.usuarios.values() if usuario.livros_emprestados_usuario]
        
        if not livros_usuarios:
            print("\nNenhum livro da biblioteca foi emprestado\n")
            return
        
        for livro in livros_usuarios:
            print(f"\n{livro.nome} - {livro.livros_emprestados_usuario}\n")
        