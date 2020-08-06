def somar(n1, n2):
    return n1 + n2


somar_lambda = lambda n1, n2: n1 + n2

print(
    somar(1, 2),
    somar_lambda(1, 2),
    sep="\n"
)
