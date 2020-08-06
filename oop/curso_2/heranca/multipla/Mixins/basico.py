"""
Python suporta um tipo simples de herança múltipla que permite a criação de Mixins.
Mixins são um tipo de classe usada para "misturar" propriedades e métodos extras em uma classe.
Isso permite criar classes em um estilo de composição.
"""


class Livro:
    def __init__(self, nome, conteudo):
        self.nome = nome
        self.conteudo = conteudo


class LivroHTMLMixin:
    def renderizar(self):
        return ('\n<html>\n<title>%s</title>\n<body>%s</body>\n</html>') % (self.nome, self.conteudo)


class LivroHTML(Livro, LivroHTMLMixin):
    pass


livro_html = LivroHTML('Algum Livro', 'Conteudo do livro')
print(livro_html.renderizar())
