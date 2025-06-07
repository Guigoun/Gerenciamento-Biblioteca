class Usuario:
    def __init__(self, id, nome, matricula, livros_emprestados_usuario=[]):
        self.id = id
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados_usuario = livros_emprestados_usuario
        
    def __str__(self):
            return f'{self.id.ljust(20)} | {self.nomeljust(20)} | {self.matriculaljust(20)}'
    