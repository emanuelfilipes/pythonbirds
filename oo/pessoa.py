class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    luciano = Pessoa(nome='Luciano')
    emanuel = Pessoa(luciano, nome='Emanuel')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar()) #se tiver mais um argumento dentro do parenteses da erro pq o p ja foi passado no começo
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)