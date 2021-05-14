# Hash Extensível

O objetivo da atividade, era implementar uma estrutura de Hash Extensível, capaz de inserir, buscar e remover elementos que possuem uma quantidade variável de campos, composto por uma chave e N atributos, é importante ressaltar que cada Bucket da Hash possui um valor fixo em Bytes, então a quantidade de atributos, seus tipos, e valores atribuídos a cada campo impactam na quantidade de elementos que pode ser inserido em cada um dos Buckets criados.
Neste arquivo temos os arquivos de exemplo que utilizei para os testes no formato .csv onde o próprio nome do arquivo diz quantos campos ele possui e quantas inserções.

* O gerador de entradas e saídas automáticas desenvolvidas pelo meu Professor [Marcos Roberto](https://github.com/ribeiromarcos) pode ser encontrado em: [SIOgen](https://ribeiromarcos.github.io/siogen/)

A execução pode ser feita diretamente pelo terminal utilizando os seguintes parâmetros: 


Para Hash_extensivel.py podemos fazer.

'''

    usage: HashEX [-h] [-tp TAMPAGINA] [-f FILENAME]

    optional arguments:
      -h, --help            show this help message and exit
      -tp TAMPAGINA, --tamPagina TAMPAGINA
                            Maximum page size (default: 3000)
      -f FILENAME, --filename FILENAME
                            Input filename (default: D_a2_i20000.csv)
'''

