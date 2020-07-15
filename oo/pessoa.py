class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro')
    rafael = Pessoa(pedro, nome='Rafael')
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome)
    print(rafael.idade)
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Fernandez'
    print(rafael.sobrenome)
