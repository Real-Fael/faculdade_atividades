O objetivo da atividade, era implementar uma estrutura de Árvore B+, capaz de inserir, buscar e remover elementos que possuem uma quantidade variável de campos, composto por uma chave e N atributos, é importante ressaltar que cada página da árvore possui um valor fixo em Bytes, então a quantidade de atributos, seus tipos, e valores atribuídos a cada campo impactam na quantidade de elementos que pode ser inserido em cada uma das páginas criadas.
Neste arquivo temos os arquivos de exemplo que utilizei para os testes no formato .csv onde o próprio nome do arquivo diz quantos campos ele possui e quantas inserções.

* O gerador de entradas e saídas automáticas desenvolvidas pelo meu Professor [Marcos Roberto](https://github.com/ribeiromarcos) pode ser encontrado em: [SIOgen](https://ribeiromarcos.github.io/siogen/)

Diminui a quantidade de prints ao máximo evitando mostrar os valores das páginas pois gasta muito tempo, e as implementações perdem desempenho. Na árvore mostro apenas a criação de novas raízes (desconsiderando a raiz inicial) durante a criação.

A execução pode ser feita diretamente pelo terminal utilizando os seguintes parâmetros: 


Para BMais.py podemos fazer.

'''

    usage: BMais [-h] [-tp TAMPAGINA] [-f FILENAME]

    optional arguments:

    -h, --help            show this help message and exit
    -tp TAMPAGINA, --tamPagina TAMPAGINA
                        Maximum page size (default: 2048)
     -f FILENAME, --filename FILENAME
                        Input filename (default: D_a2_i20000.csv)

'''
