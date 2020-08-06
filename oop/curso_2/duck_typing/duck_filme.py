class FilmeDuck:
    def __init__(self, titulo, lancamento, diretor) -> None:
        self.titulo = titulo
        self.lancamento = lancamento
        self.diretor = diretor

    def exibir(self) -> str:
        return f'Lançamento: {self.titulo.title()}, {self.lancamento}, {self.diretor.title()}'
