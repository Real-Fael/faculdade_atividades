import sys
import csv
import numpy as np
import time

TAMPAG_DEFAULT = 2048  # funciona bem
FILE_DEFAULT = "D_a2_i20000.csv"  # lê um arquivo padrao qualquer


class Registro(object):  # registro com todos os campos
    def __init__(self, campos=None):  # inicializa o registro com os campos vazios
        if campos is None:
            campos = [[], []]
        self.key = int(
            campos[0])  # recebe primeiro valor do vetor se nao for passado nenhum parametro chave recebe um vetor vazio
        self.campos = campos[1:]  # recebe os outros campos ou uma lista vazia

    def __sizeof__(self):  # retorna o tamanho do registro como o somatorio dos campos do mesmo
        # retorna o tamanho da chave + a soma de cada um dos campos
        return sys.getsizeof(self.key) + sum(sys.getsizeof(x) for x in
                                             self.campos)

    def __str__(self):  # uma forma de mostrar o registro
        return "{k}:{c}".format(k=self.key, c=self.campos)

    def getKey(self):  # retorna a chave do registro
        return self.key

    def getRegistro(self):  # retorna o proprio registro
        return self


class Pagina(object):
    def __init__(self, folha=False, tamPagina=4096):  # por padrao uma pagina não é uma folha
        self.folha = folha  # armazena se a chave é uma folha
        self.tamPagina = tamPagina  # armazena tamanho da pagina
        self.registros = []
        self.chaves = []  # atribui listas vazias em todos os campos
        self.filhos = []
        self.pagIrmaDir = None  # pagina irma a direita
        self.pagIrmaEsq = None  # pagina irma a esquerda

    def isFolha(self):  # verifica se é uma folha
        return self.folha

    def __str__(self):
        if self.isFolha():  # caso seja uma folha deve retornar uma string com formato da folha ou seja sem filhos
            aux = "| "  # | determina inicio e fim de uma pagina nao folha
            for x in self.registros:
                aux = aux + "(" + x.__str__() + ")" + " , "
            return aux + "| "
        else:  # se for um nó da arvore mostra as chaves
            aux = "$ Chaves:"  # $ delimita o inicio e o fim de uma pagina não folha
            for x in self.chaves:  # percorre as chaves da pagina
                aux = aux + "(" + x.__str__() + ") , "
            aux = aux + "\n Filhos:\n"
            cont = 0
            for x in self.filhos:  # percorre os filhos para mostrar cada um deles com seus respectivos filhos se for o caso
                cont += 1
                aux = aux + "Filho({})".format(cont) + x.__str__() + "\n"
            return aux + " $"

    def __sizeof__(self):  # o tamanho da pagina depende se é uma folha ou um nó
        if self.isFolha():  # se for uma folha somente elementos com relação a folha é contabilizado
            aux = sum(sys.getsizeof(x) for x in
                      self.registros)
            return aux  # nao consideramos o tamanho das irmãs
        else:
            # pegamos o tamanho gasto pelos ponteiros dos filhos + o tamanho de cada uma das chaves
            aux = (sys.getsizeof(self.filhos)) + sum(sys.getsizeof(x) for x in self.chaves)
            return aux

    def estaVazia(self):  # verifica se a pagina esta vazia
        if self.isFolha():
            if not self.registros:  # verifica se é uma folha vazia
                return True
            else:
                return False
        else:
            if not self.chaves:  # verifica se é um nó vazio
                return True
            else:
                return False

    def estaCheia(self):
        if self.estaVazia():  # se não esta vazia entao podemos inserir elementos
            return False
        else:  # se tem algum elemento devemos verificar se há espaço para mais um
            if self.isFolha():  # verifica se há espaço na folha
                if (self.tamPagina - self.__sizeof__()) >= self.registros[0].__sizeof__():
                    # se o espaço disponivel é maior que uma amostra do registro entao tem espaço para outro igual
                    return False
                else:
                    return True
            else:  # se não é uma folha olha se tem espaço para uma chave e um ponteiro
                if (self.tamPagina - self.__sizeof__()) > (
                        sys.getsizeof(self.chaves) / len(self.chaves) + sys.getsizeof(self.filhos) / len(self.filhos)):
                    return False  # caso o espaçõ livre seja maior que a quantidade de byte usado por uma chave e um filho entao ha espaço
                else:
                    return True

    def procuraFilho(self, chave):
        if not self.isFolha():  # caso não seja folha tem filhos
            pos = -1
            for x in self.chaves:  # percorre todos as chaves da pagina
                pos += 1
                if chave < x:  # verifica se a chave é menor que a chave de cada registro
                    return self.filhos[pos]  # caso seja retorna o filho a esquerda da chave
            return self.filhos[pos + 1]  # caso ele seja maior que todos os registros retorna o ultimo filho
        else:
            return None  # caso seja uma folha retorna um objeto NULL

    def inserirNaPagina(self, elemento):
        if self.isFolha():  # verifica se é uma pagina folha para poder inserir
            if not self.estaCheia():  # verifica se o tamanho disponivel suporta mais um registro
                self.registros.append(elemento)  # caso tenha espaço adiciona elemento na pagina folha
                self.registros.sort(key=lambda x: x.getKey())  # ordena elementos da pagina apartir da chave de registro

            # self.registros.

    def ocupacaoMinima(self):

        if (
                self.__sizeof__() / self.tamPagina) >= 0.50:  # se o tamanho  ocupado é maior que 50% entao tem uma ocupaçao minima
            return True
        else:
            return False

    def podeEmprestar(self):

        if self.isFolha():
            if ((self.__sizeof__() - sys.getsizeof(self.registros[
                                                       0])) / self.tamPagina) >= 0.50:  # se o tamanho  ocupado é maior que 50% entao tem uma ocupaçao minima
                return True
            else:
                return False
        else:
            if ((self.__sizeof__() - sys.getsizeof(
                    self.chaves)) / self.tamPagina) >= 0.50:  # se o tamanho  ocupado é maior que 50% entao tem uma ocupaçao minima
                return True
            else:
                return False


class Arvore(object):
    def __init__(self, tamPaginas=4096):
        self.raiz = Pagina(True, tamPaginas)  # ao criar uma arvore a primeira pagina criada é uma folha
        self.tamPagina = tamPaginas

    def pesquisaIntervalo(self, k1, k2):  # pesquisa por intervalo sendo k1 o menor valor e k2 o maior

        pag = self.pesquisaNo(self.raiz, k1)  # pesquisa o nó folha correspondente a menor chave

        forainterval = False
        vetInterval = []
        while not forainterval:  # executa ate que a flag seja acionada

            for x in pag.registros:  # percorre todos os registros de cada uma das paginas
                if x.getKey() >= k1:
                    if x.getKey() <= k2:
                        vetInterval.append(x)  # se esta no intervalo adiciona no vetor
                    else:
                        forainterval = True  # troca a flag se o valor passou o tamanho de k2
                        break  # interrompe o for atual
            if not forainterval:
                pag = pag.pagIrmaDir  # atualiza a pagina para a proxima pagina
            if pag is None:  # se a pagina atual for None chegamos ao final dos elementos inseridos assim interrompe o while
                break
        return vetInterval

    def pesquisaRegistro(self, k):  # pesquisa por um registro especifico

        pag = self.pesquisaNo(self.raiz, k)  # pesquisa a pagina folha corresponente a chave
        reg = None
        for x in pag.registros:
            if x.getKey() == k:  # percorre todos os elementos em busca daquele que corresponde com a chave
                reg = x

        return reg, pag  # retorna a pagina e o registro solicitado

    def pesquisaNo(self, pag, k):  # função que retorna a pagina folha
        if pag.isFolha():
            return pag  # se a pagina passada para função é folha retorna ela mesma

        return self.pesquisaNo(pag.procuraFilho(k), k)  # se não é folha mandamos chamamos a função recursivamente
        # usando o filho correspondente a k

    def insereFolha(self, N, elemento):  # inserir na folha
        if not N.estaCheia():  # caso caiba elemento na folha insere na folha
            N.inserirNaPagina(elemento)
            # print("inserindo elemento na folha")
            return None, None
        # caso nao caiba vamos criar uma nova pagina e dividir os elementos
        M = Pagina(folha=True, tamPagina=self.tamPagina)
        # como sempre ao inserir ele ordena ja é garantido que a lista estará ordenada
        M.registros = N.registros[(len(N.registros) // 2):]  # divide os elementos entre as paginas
        N.registros = N.registros[:(len(N.registros) // 2)]
        M.pagIrmaDir = N.pagIrmaDir  # pega o antigo ponteiro da direita de N e passa para M

        N.pagIrmaDir = M  # liga as paginas como irmãs
        M.pagIrmaEsq = N
        KM = M.registros[0].getKey()  # paga a menor chave da pagina a direita como uma nova chave
        # print("*******************\nfolha cheia dividindo entre: \nM{M}\nN{N}\n*******************".format(M=M, N=N))
        if elemento.getKey() < KM:  # verifica em qual pagina o elemento deve ser inserido
            N.inserirNaPagina(elemento)  # insere na pagina e ordena
        else:
            M.inserirNaPagina(elemento)
        return KM, M  # retorna a chave de M e o a nova pagina criada

    def insere(self, pag, elemento):
        if pag.isFolha():  # caso seja uma folha chamamos o insere folha para se encarregar da inserção
            chave, filhoDir = self.insereFolha(N=pag, elemento=elemento)
            return chave, filhoDir  # caso haja estouro na folha retorna a nova irma e a nova chave
        else:  # caso nao seja folha
            F = pag.procuraFilho(elemento.getKey())  # procura o filho que corresponde a chave
            chave, filhoDir = self.insere(F, elemento)  # e se chama recursivamente com esse filho
        if not (chave is None) and not (filhoDir is None):  # entra se caso nao for folha e é diferente de vazio
            if not (pag.estaCheia()):  # se a pagina não esta cheia entao cabe uma chave e um elemento
                aux = -1
                for x in pag.chaves:
                    aux += 1
                    if chave < x:  # verifica se a nova chave é menor que algum elemento
                        pag.chaves.insert(aux, chave)  # insere a chave antes do elemento que é menor
                        pag.filhos.insert(aux + 1, filhoDir)  # adiciona o filho na posição+1 pois defini que quando
                        # for posição igual quer dizer que esta a esquerda entao o da direita é o proximo
                        # print("====== nova chave adicionada======\n", pag)
                        return None, None  # como ja foi inserido o elemento acaba funçao e retorna vazio

                pag.chaves.insert(aux + 1, chave)  # insere a chave no final pois nao foi menor que nenhuma outra
                pag.filhos.insert(aux + 2, filhoDir)  # insere o filho na ultima pois a ultima é a pagina
                # print("====== nova chave adicionada======\n", pag)
                return None, None  # cujos elementos sao maiores que todas as chaves
            else:
                if len(pag.chaves) % 2 == 0:
                    # caso tenha uma quantidade par de chaves devemos ter metade+1 elementos no nó da esquerda
                    # metade=(len(pag.chaves)//2)+1
                    metade = (len(pag.filhos) // 2) + 1
                else:
                    metade = (len(pag.filhos) // 2)  # caso tenha quanbtidade impar basta fazer uma divisao inteira
                M = Pagina(False, self.tamPagina)
                M.chaves = pag.chaves[(len(pag.chaves) // 2):]  # pega a segunda metade das chaves e guarda em M
                KM = M.chaves.pop(0)  # remove da lista o primeiro elemento e guarda em KM
                M.filhos = pag.filhos[metade:]  # metade varia dependendo se quantidade de chaves é par ou impar
                pag.chaves = pag.chaves[:(len(pag.chaves) // 2)]  # pega a primeira metade dos elementos chaves
                pag.filhos = pag.filhos[
                             :metade]  # pega primeira metade caso a quantidade de chaves chega par pega 1 filho a mais
                # print("/////nó dividido/////")
                return KM, M
        return None, None

    def insereRaiz(self, elemento):
        cha, pag = self.insere(pag=self.raiz, elemento=elemento)
        if not (cha is None) and not (pag is None):  # caso retorne algo diferente de None nesse ponto
            newraiz = Pagina(False, self.tamPagina)  # significa que a raiz enncheu e o metodo insere a dividiu
            newraiz.chaves = [cha]  # entre self.raiz e pag  sendo assim criamos uma nova raiz com uma chave
            newraiz.filhos = [self.raiz, pag]  # e apontamos para os 2 filhos que era a antiga raiz
            self.raiz = newraiz  # agora atualizamos a nova raiz da arvore
            print("======Nova raiz Criada======\n")
            # print("======Nova raiz Criada======\n", self.raiz)

    """def removeFolha(self,P,N,k):
        cont=-1
        for x in N.registros:
            cont+=1
            if x.getKey()==k:
                N.registros.pop(cont)#remove o elemento da pagina
        if N.ocupacaoMinima():
            return None, None
        else:
            if not(N.pagIrmaDir is None):
                if N.podeEmprestar():
    """


def get_arguments(print_help=False):  # pega os argumentos
    '''
    Get arguments
    '''
    import argparse
    parser = argparse.ArgumentParser('BMais')
    # -tp agora é para setar o tamanho da pagina
    parser.add_argument('-tp', '--tamPagina', action='store', type=int,
                        default=TAMPAG_DEFAULT,
                        help='Maximum page size (default: ' +
                             str(TAMPAG_DEFAULT) + ')')
    # -f é o nome do arquivo de entrada
    parser.add_argument('-f', '--filename', action='store', type=str,
                        default=FILE_DEFAULT,
                        help='Input filename (default: ' +
                             FILE_DEFAULT + ')')
    args = parser.parse_args()
    if print_help:
        parser.print_help()
    return args


if __name__ == '__main__':
    inicio = time.time()
    args = get_arguments()  # lê os argumentos
    # leitura de arquivo
    arquivo = open(args.filename)  # abre o arquivo passado por parametro
    dados = csv.DictReader(arquivo)
    Bmais = Arvore(tamPaginas=args.tamPagina)

    # print("criando arvore tamanho da raiz:", Bmais.raiz.__sizeof__())

    quantidade = 0
    for data in dados:

        operacao = list(data.values())  # transforma cada linha do dicionario em um vetor
        if operacao[0] == "+":
            quantidade += 1
            aux = [int(a) for a in operacao[1:]]  # converte a entrada para vetor de inteiros
            aux = Registro(aux)  # gera um objeto Registro com o vetor de inteiros
          #  print("\ninserindo o registro:{n}".format(n=quantidade), " de tamanho", aux.__sizeof__())
            Bmais.insereRaiz(aux)
            # print("iteracao {}".format(quantidade)," Raiz Folha? ",Bmais.raiz.isFolha(),"tamanho da raiz:", Bmais.raiz.__sizeof__())
        if quantidade == 1072:
            print(quantidade)
        #    break

    fim = time.time()
    print("\nA criação desta arvore demorou:{:4.4f} segundos".format(
        fim - inicio))  # mostra o tempo gasto ate a construção da arvore
    while (1):  # repete ate que o usuario queia sair
        entrada = int(input(
            "\n\n******Escolha uma opção******\n-1) Buscar Elemento\n-2) Buscar intervalo\n-3) Mostrar Arvore\n-4) Sair\n"))
        if entrada == 1:
            entrada2 = int(input("digite a chave para buscar: "))
            inicio = time.time()
            reg, pag = Bmais.pesquisaRegistro(entrada2)
            if reg == None:
                print("registro NÃO encontrado deveria estar na pagina:{}".format(pag))
            else:
                print("Registro: {} encontrado na pagina:{}".format(reg, pag))
            fim = time.time()
            print("\nEsta operação demorou:{:4.4f} segundos".format(fim - inicio))

        elif entrada == 2:
            entrada2 = int(input("o valor inicial: "))
            entrada3 = int(input("o valor final: "))
            inicio = time.time()
            print("os elementos neste intervalo são:", *Bmais.pesquisaIntervalo(entrada2, entrada3))
            fim = time.time()
            print("\nEsta operação demorou:{:4.4f} segundos".format(fim - inicio))
        # hashPrincipal.removerHash(entrada2)
        elif entrada == 3:
            print("\n************* B+ ************\n\n", Bmais.raiz)

        elif entrada == 4:
            break
        else:
            print("Opção invalida tente novamente!")
