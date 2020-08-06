from oop.curso_2.heranca.humano.PessoaFisica import PessoaFisica

pssFic = PessoaFisica(nome="Silva", idade=66, cpf="100.900.700")

print(
    pssFic.nome, pssFic.idade, pssFic.cpf,
    sep="\n"
)

pssFic.imprimir()
