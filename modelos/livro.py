class Livro:
    def __init__(self, id, titulo, autor, disponibilidade=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade
    
    def __str__(self):
        status = "Disponível" if self.disponibilidade else "Indisponível"
        return f'{self.id} | {self.titulo} | {self.autor} | {status}'
    
  
