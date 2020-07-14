class Pessoa:
    def __init__(self, nome = None, idade=31):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Rafael')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    # p.nome = 'Rafael'
    print(p.nome)
    print(p.idade)
