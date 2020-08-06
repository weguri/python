class LivroDuck:
    def __init__(self, titulo, lancamento, autor) -> None:
        self.titulo = titulo
        self.lancamento = lancamento
        self.autor = autor

    def exibir(self) -> str:
        return f'Lançamento: {self.titulo.title()}, {self.lancamento}, {self.autor.title()}'
