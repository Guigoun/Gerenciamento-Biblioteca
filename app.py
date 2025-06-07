from modelos.biblioteca import Biblioteca

def exibir_opcoes():
    print("Escolha uma das opções abaixo:\n[1] - Adicionar livro\n[2] - Cadastrar usuário\n[3] - Pegar livro emprestado\n[4] - Exibir livros disponíveis\n[5] - Exibir livros emprestados\n[6] - Exibir livros emprestados por usuário\n[7] - Sair")
         
def escolher_opcao():
    
    biblioteca = Biblioteca()
    
    while True:
        
        try:
            opcao = int(input(": "))
             
            if opcao == 1:
                biblioteca.adicionar_livro()
            elif opcao == 2:
                biblioteca.adicionar_usuario()
            elif opcao == 3:
                biblioteca.pegar_livro_emprestado()
            elif opcao == 4:
                biblioteca.exibir_livros_disponiveis()
            elif opcao == 5:
                biblioteca.exibir_livros_emprestados()
            elif opcao == 6:
                biblioteca.exibir_livros_emprestados_usuarios()
            elif opcao == 7:
                print("Saindo...")
                break
        except ValueError:
            print("entrada inválida!")
        
        exibir_opcoes()
            

def main():
    exibir_opcoes()
    escolher_opcao()
    
    
if __name__ == '__main__':
    main()	