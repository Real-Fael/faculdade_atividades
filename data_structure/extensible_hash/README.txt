Neste arquivo temos os arquivos que utilizamamos para os testes no formato .csv
Diminui a quantidade de prints ao maximo evitando mostrar os valores das paginas e buckets pois gasta muito tempo e as implementações perdem desempenho.
Na arvore mostro apenas a criação de novas raizes (desconsiderando a raiz inicial) durante a criação.
Na hash mostro apenas a profundidade global durante a criação.
A execussão pode ser feita diretamente pelo terminal utilizando os parametros. 
 

Para BMais.py podemos fazer.

usage: BMais [-h] [-tp TAMPAGINA] [-f FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -tp TAMPAGINA, --tamPagina TAMPAGINA
                        Maximum page size (default: 2048)
  -f FILENAME, --filename FILENAME
                        Input filename (default: D_a2_i20000.csv)


Para Hash_extensivel.py podemos fazer.

usage: HashEX [-h] [-tp TAMPAGINA] [-f FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  -tp TAMPAGINA, --tamPagina TAMPAGINA
                        Maximum page size (default: 3000)
  -f FILENAME, --filename FILENAME
                        Input filename (default: D_a2_i20000.csv)


