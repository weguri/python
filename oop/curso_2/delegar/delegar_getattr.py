class A:
    def fazer_algo(self):
        pass

    def outro_metodo(self):
        pass

    def algum_metodo(self, nome):
        print("Nome:", nome)


class B:
    def __init__(self):
        self.a = A()

    def fazer_algo(self):
        return self.a.fazer_algo()

    def outro_metodo(self):
        return self.a.outro_metodo()

    def __getattr__(self, item):
        """
        Quando o metodo chamado não existe dentro da class B então
        é delegado para class A e se o metodo existe lá
        """
        return getattr(self.a, item)


'''
Teste de USO
'''
b = B()
b.fazer_algo()  # Isso chama B.fazer_algo() (existe em B)
b.algum_metodo('python')  # Isso chama B.__getattr__('algum_metodo') e delega para A.algum_metodo()
