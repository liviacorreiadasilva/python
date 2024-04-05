class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for adjacente in self.adjacentes:
            print(f'{adjacente.vertice.rotulo} -> {adjacente.custo}')


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo


class Grafo:
    def __init__(self):
        self.vertices = []

    def adiciona_vertice(self, vertice):
        self.vertices.append(vertice)

    def mostra_adjacentes(self):
        for vertice in self.vertices:
            vertice.mostra_adjacentes()


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.valores = [None] * capacidade

    def insere(self, vertice):
        if self.numero_elementos == 0:
            self.valores[0] = vertice
            self.numero_elementos = 1
            return

        indice = 0
        for i in range(self.numero_elementos):
            if vertice.distancia_objetivo > self.valores[i].distancia_objetivo:
                indice = i + 1

        for i in range(self.numero_elementos, indice, -1):
            self.valores[i] = self.valores[i - 1]

        self.valores[indice] = vertice
        self.numero_elementos += 1

    def imprime(self):
        for i in range(self.numero_elementos):
            print(f'Vertice: {self.valores[i].rotulo} | Distância Objetivo: {self.valores[i].distancia_objetivo}')


class BuscaAEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print("---------------")
        print(f"Cidade Atual: {atual.rotulo}")

        if atual == self.objetivo:
            self.encontrado = True
            print("Objetivo encontrado! :D")
        else:
            vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if not adjacente.vertice.visitado:
                    adjacente.vertice.visitado = True
                    vetor_ordenado.insere(adjacente.vertice)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] is not None:
                self.buscar(vetor_ordenado.valores[0])


# Definição do grafo
grafo = Grafo()

# Adição dos vértices
porto_uniao = Vertice('Porto_Uniao', 203)
paulo_fortini = Vertice('Paulo_Fortini', 172)
canoinhas = Vertice('Canoinhas', 141)
tres_barras = Vertice('Tres_Barras', 131)
sao_mateus_do_sul = Vertice('Sao_Mateus_do_Sul', 123)
irati = Vertice('Irati', 139)
curitiba = Vertice('Curitiba', 0)
palmeira = Vertice('Palmeira', 59)
mafra = Vertice('Mafra', 94)
campo_largo = Vertice('Campo_Largo', 27)
balsa_nova = Vertice('Balsa_Nova', 41)
lapa = Vertice('Lapa', 74)
tijucas_do_sul = Vertice('Tijucas_do_Sul', 56)
araucaria = Vertice('Araucaria', 23)
sao_jose_dos_pinhais = Vertice('Sao_Jose_dos_Pinhas', 13)
contenda = Vertice('Contenda', 39)

# Adição das adjacências
porto_uniao.adiciona_adjacente(Adjacente(paulo_fortini, 46))
porto_uniao.adiciona_adjacente(Adjacente(sao_mateus_do_sul, 87))
porto_uniao.adiciona_adjacente(Adjacente(canoinhas, 78))

paulo_fortini.adiciona_adjacente(Adjacente(porto_uniao, 46))
paulo_fortini.adiciona_adjacente(Adjacente(irati, 75))

canoinhas.adiciona_adjacente(Adjacente(porto_uniao, 46))
canoinhas.adiciona_adjacente(Adjacente(tres_barras, 12))
canoinhas.adiciona_adjacente(Adjacente(mafra, 66))

tres_barras.adiciona_adjacente(Adjacente(canoinhas, 12))
tres_barras.adiciona_adjacente(Adjacente(sao_mateus_do_sul, 43))

sao_mateus_do_sul.adiciona_adjacente(Adjacente(tres_barras, 43))
sao_mateus_do_sul.adiciona_adjacente(Adjacente(porto_uniao, 87))
sao_mateus_do_sul.adiciona_adjacente(Adjacente(lapa, 60))

irati.adiciona_adjacente(Adjacente(paulo_fortini, 75))
irati.adiciona_adjacente(Adjacente(sao_mateus_do_sul, 57))
irati.adiciona_adjacente(Adjacente(palmeira, 75))

curitiba.adiciona_adjacente(Adjacente(sao_jose_dos_pinhais, 15))
curitiba.adiciona_adjacente(Adjacente(araucaria, 37))
curitiba.adiciona_adjacente(Adjacente(campo_largo, 29))
curitiba.adiciona_adjacente(Adjacente(balsa_nova, 51))

palmeira.adiciona_adjacente(Adjacente(irati, 75))
palmeira.adiciona_adjacente(Adjacente(campo_largo, 55))
palmeira.adiciona_adjacente(Adjacente(sao_mateus_do_sul, 77))

mafra.adiciona_adjacente(Adjacente(lapa, 57))
mafra.adiciona_adjacente(Adjacente(canoinhas, 66))
mafra.adiciona_adjacente(Adjacente(tijucas_do_sul, 99))

campo_largo.adiciona_adjacente(Adjacente(palmeira, 55))
campo_largo.adiciona_adjacente(Adjacente(curitiba, 29))
campo_largo.adiciona_adjacente(Adjacente(balsa_nova, 22))

balsa_nova.adiciona_adjacente(Adjacente(campo_largo, 22))
balsa_nova.adiciona_adjacente(Adjacente(contenda, 19))
balsa_nova.adiciona_adjacente(Adjacente(curitiba, 51))

lapa.adiciona_adjacente(Adjacente(mafra, 57))
lapa.adiciona_adjacente(Adjacente(contenda, 26))
lapa.adiciona_adjacente(Adjacente(sao_mateus_do_sul, 60))

tijucas_do_sul.adiciona_adjacente(Adjacente(mafra, 99))
tijucas_do_sul.adiciona_adjacente(Adjacente(sao_jose_dos_pinhais, 49))

araucaria.adiciona_adjacente(Adjacente(curitiba, 37))
araucaria.adiciona_adjacente(Adjacente(contenda, 18))

sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(curitiba, 15))
sao_jose_dos_pinhais.adiciona_adjacente(Adjacente(tijucas_do_sul, 49))

contenda.adiciona_adjacente(Adjacente(balsa_nova, 19))
contenda.adiciona_adjacente(Adjacente(araucaria, 18))
contenda.adiciona_adjacente(Adjacente(lapa, 26))

# Inicialização da busca A*
busca_aestrela = BuscaAEstrela(curitiba)
busca_aestrela.buscar(porto_uniao)
