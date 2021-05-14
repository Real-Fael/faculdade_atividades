import sys
import csv
import numpy as np
import time

TAMPAG_DEFAULT = 3000  # tamanho que funciona bem para todos os casos testados
FILE_DEFAULT = "D_a2_i20000.csv"  # lê um arquivo padrao qualquer


class Registro(object):  # registro com todos os campos
    def __init__(self, campos=None):  # inicializa o registro com os campos vazios
        if campos is None:
            campos = [[], []]
        self.key = int(
            campos[0])  # recebe primeiro valor do vetor se nao for passado nenhum parametro chave recebe um vetor vazio
        self.campos = campos[1:]  # recebe os outros campos ou uma lista vazia

    def __sizeof__(self):  # retorna o tamanho do registro como o somatorio dos campos do mesmo
        # return sys.getsizeof(self.key)+sys.getsizeof(self.campos)
        return sys.getsizeof(self.key) + sum(sys.getsizeof(x) for x in
                           self.campos)  # utilizei uma função lambda para pegar o valor de bytes de cada elemento
        # ao inves do tamanho do ponteiro como estava anteriormente dessa forma cada posição do vetor tem 28Bytes

    def __str__(self):
        return "{k}:{c}".format(k=self.key, c=self.campos)

    def getKey(self):  # retorna a chave do registro
        return self.key

    def getRegistro(self):  # retorna o proprio registro
        return self


class Bucket(object):  # objeto bucket que armazenará um conjunto de registros
    def __init__(self, tamBuket=1024, profundidade=2):
        self.profundidade = profundidade  # armazena a profundidade local do bucket
        self.tamBuket = tamBuket  # armazena o tamanho do bucket
        self.registros = []  # cria um vetor vazio inicialmente

    def __str__(self):  # cria uma representação do bucket em forma de string
        aux = "|Profundidade:{} ".format(self.profundidade)
        for x in self.registros:
            aux = aux + "(" + x.__str__() + ")" + " , "
        return aux + "| "

    def __sizeof__(self):  # calcula o tamanho do bucket pela quantidade e tamanho dos registros
        aux = sum(sys.getsizeof(x) for x in
                  self.registros)
        return aux

    def estaVazia(self):  # verifica se o bucket esta vazia

        if not self.registros:  # verifica se nao há nenhum algum elemento dentro do vetor
            return True
        else:
            return False

    def estaCheia(self):
        if self.estaVazia():  # se não esta vazia entao podemos inserir elementos
            return False
        else:  # se tem algum elemento devemos verificar se há espaço para mais um
            if (self.tamBuket - self.__sizeof__()) >= self.registros[0].__sizeof__():
                # se o espaço disponivel é maior que uma amostra do registro entao tem espaço para outro igual
                return False
            else:
                return True

    def inserirNoBucket(self, elemento, ignore=False):  # ignore serve para ignorar overflow
        if not self.estaCheia():  # verifica se o tamanho disponivel suporta mais um registro
            self.registros.append(elemento)  # caso tenha espaço adiciona elemento na pagina folha
            return None
        else:  # caso nao suporte vamos criar um novo bucket e mudar as profundidades para 1 a mais
            self.registros.append(elemento)
            if not ignore:  # se ignore for True significa que é pra aceitar esse Overflow na pagina
                self.profundidade += 1  # aumenta a profudnidade do Bucket
                novoBucket = Bucket(self.tamBuket, self.profundidade)  # cria um novo bucket com a mesma profundidade
                return novoBucket  # retorna o novo Bucket
            return None


class Hash_extensivel(object):  # classe Hash extensivel
    def __init__(self, tamBucket=1024):
        self.profundidade_global = 2  # cria profundidade global inicial
        self.tamBucket = tamBucket  # seta o tamanho das paginas de bucket
        # cria um vetor de buckets vazio do mesmo tamanho da profundidade global
        self.vetBucket = [Bucket(self.tamBucket) for x in range(2 ** self.profundidade_global)]

    def removerHash(self, chaveElemento):  # função para remover a hash
        pos, auxBucket = self.buscarHash(
            chaveElemento)  # prucura o elemento retorna a posição e o bucket onde o elemento esta
        if pos is not None and auxBucket is not None:
            aux = auxBucket.registros.pop(
                pos)  # removemos o elemento da lista e guardamos em uma variavel para poder processalo
            #print("elemento Removido")
            return aux
            #return True
        else:
          #  print("elemento nao existe não pode ser removido")
            return None
            #return False

    def buscarHash(self, chaveElemento):  # busca o elemento pela chave
        # calculla o hash global para ver em que ponteiro devemos procurar
        chaveHash = chaveElemento % (2 ** self.profundidade_global)
        profundidadeAterior = self.profundidade_global  # pega a profundidade anterior como referencia
        # pega a profundidade do bucket referenciado pela chave hash global
        prufundidadeAtual = self.vetBucket[chaveHash].profundidade
        while profundidadeAterior > prufundidadeAtual:  # devemos refazer a hash  com a profundidade do bucket apontado pela hash anterior
            profundidadeAterior = prufundidadeAtual  # a anterior recebe a atual
            chaveHash = chaveElemento % (
                    2 ** prufundidadeAtual)  # calcula nova chave a partir da profundidade atual do bucket
            prufundidadeAtual = self.vetBucket[chaveHash].profundidade  # entao pegamos a nova profundidade atual

        # chaveBucket = chaveElemento % (2 ** auxBucket.profundidade)
        auxBucket = self.vetBucket[chaveHash]  # entao pegamos o bucket de acordo com a hash correspondente
        encontrou = False
        cont = -1
        pos = -1
        for x in auxBucket.registros:  # percorre todos os registros
            cont += 1
            if x.getKey() == chaveElemento:  # verifica se as chaves correspondem
                encontrou = True
                registro = x
                pos = cont
        if encontrou:  # se tiver encontrado o elemento correspondente a chave
        #    print("elemento {a} encontrado no bucket{b}".format(a=registro, b=auxBucket))
            return pos, auxBucket  # retorna a posição e o bucket que o registro esta
        else:
        #    print("elemento nao encontrado")
            return None, None



    #versao 2 do inserir
    def insereHash(self, elemento):  # função para inserir na hash
        chaveHash = elemento.getKey() % (2 ** self.profundidade_global)  # calcula hash global
        novoBucket = self.vetBucket[chaveHash].inserirNoBucket(elemento)
        # quando para esse elemento nao houver uma profundidade menor entao podemos inserilo no bucket
        if novoBucket is not None:  # se nao é nulo entao criamos um novo bucket
           # print("bucket dividido")
            if novoBucket.profundidade > self.profundidade_global:  # se a profundidade do bucket for maior temos que dobrar a head
                self.profundidade_global += 1  # aumentamos a profundidade do hash
                divisorAnterior = 2 ** (self.profundidade_global - 1)
                divisorAtual = 2 ** self.profundidade_global
                print("aumentando tamanho do HEAD para:", divisorAtual)
                # percorremos as novas posições do head que ira dobrar
                for x in range(divisorAnterior, divisorAtual):
                    # fazemos com que as novas posições apontem para os buckets ja existentes no mod anterior
                    # self.vetBucket[x] = self.vetBucket[x % divisorAnterior]#test
                    self.vetBucket.append(self.vetBucket[x % divisorAnterior])
            # agora colocaremos o novo Bucket para ser apontado pela posição da head correspondente
            profAnt= novoBucket.profundidade-1
            total=int(self.profundidade_global-novoBucket.profundidade)
            primeiro=elemento.getKey() % 2**profAnt + 2**profAnt
            self.vetBucket[primeiro] = novoBucket
            t= 2**(total)

            for cont in range(1,t):
                proximo=primeiro + cont*2**novoBucket.profundidade
                self.vetBucket[proximo]=novoBucket


            # pegamos os elementos do bucket cheio para passar novamente pela hash
            aux = self.vetBucket[chaveHash].registros
            # calcula a posição que sera substituida
            self.vetBucket[chaveHash].registros = []
            # self.vetBucket[chaveHash].registros = []  # zeramos os registros e vamos redistribuilos

            self.insereOverFlow(aux)


    def insereOverFlow(self,vetReg):
        pot= 2 ** self.profundidade_global
        for x in vetReg:
            # self.insereHash(x)
            novaChaveHash = x.getKey() % pot
            self.vetBucket[novaChaveHash].inserirNoBucket(x, ignore=True)



    def __str__(self):  # cria uma string para representar a hash
        cont = -1
        aux = ""
        for x in self.vetBucket:
            cont += 1
            aux = aux + "indice {}-->".format(cont) + x.__str__() + "\n"
        return aux


def get_arguments(print_help=False):  # pega os argumentos do console
    '''
    Get arguments
    '''
    import argparse
    parser = argparse.ArgumentParser('HashEX')
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

    inicio = time.time()  # pega o tempo inicial
    # pegando os argumentos
    args = get_arguments()
    # leitura de arquivo
    arquivo = open(args.filename)
    dados = csv.DictReader(arquivo)
    # Bmais=Arvore(tamPaginas=526)
    hashPrincipal = Hash_extensivel(args.tamPagina)

    quantidade = 0
    for data in dados:

        operacao = list(data.values())  # transforma cada linha do dicionario em um vetor
        if operacao[0] == "+":
            quantidade += 1
            aux = [int(a) for a in operacao[1:]]  # converte a entrada para vetor de inteiros
            aux = Registro(aux)  # gera um objeto Registro com o vetor de inteiros
            #print("\ninserindo o registro:{n}".format(n=quantidade), " de tamanho", aux.__sizeof__(),
           #       "Chave:{}".format(aux.getKey()))
            hashPrincipal.insereHash(aux)
        # print("iteracao {}".format(quantidade), "\n*******HASH*********\n\n", hashPrincipal)
            #if quantidade ==1000:
            #   print("\n*******HASH*********\n\n", hashPrincipal)
            #   break
            #  print(quantidade)
        elif operacao[0] == "-":
            quantidade += 1

            #print("\nRemovendo o registro:{n}".format(n=quantidade), "Chave:{}".format(operacao[1]))
            hashPrincipal.removerHash(int(operacao[1]))

    fim = time.time()
    print("\nA criação desta HASH demorou:{:4.4f} segundos".format(fim - inicio))

    while (1):
        entrada = int(input(
            "******Escolha uma opção******\n-1) Buscar Elemento\n-2) Remover Elemento\n-3) Mostrar Hash\n-4) Sair\n"))
        if entrada == 1:
            entrada2 = int(input("digite a chave para buscar: "))
            inicio = time.time()
            pos,baux=hashPrincipal.buscarHash(entrada2)  # busca e exibe o elemento
            if baux is not None:
                print("encontrado elemento: {} , no Bucket{}".format(baux.registros[pos],baux))
            else:
                print("nao encontrado")
            fim = time.time()
            print("\nA execução desta função demorou:{:4.4f} segundos".format(fim - inicio))
        elif entrada == 2:
            entrada2 = int(input("digite a chave para remoção: "))
            inicio = time.time()
            baux=hashPrincipal.removerHash(entrada2)  # remove e mostra o elemento removido
            if baux is not None:
                print("elemento: {} , Removido".format(baux))
            else:
                print("nao encontrado")

            fim = time.time()
            
            print("\nA execução desta função demorou:{:4.4f} segundos".format(fim - inicio))


        elif entrada == 3:
            print("\n*******HASH*********\n\n", hashPrincipal)  # mostra  a hash

        elif entrada == 4:
            break
        else:
            print("Opção invalida tente novamente!")
