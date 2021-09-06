class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar()) #se tiver mais um argumento dentro do parenteses da erro pq o p ja foi passado no começo
    print(p.nome)
    p.nome = 'Emanuel'
    print(p.nome)
    print(p.idade)