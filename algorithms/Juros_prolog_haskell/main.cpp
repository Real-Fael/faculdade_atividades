#include <iostream>

using namespace std;

int main()
{
    double valor_inicial=5000; // esta variavel armazena o valor inicial que sera calculado o juros
    double taxa=3; // a taxa de crescimento anual em % é colocada nesta variável
    int tempo_anos=14; //tempo que sera contabilizado os juros compostos
    for(int i=1;i<=tempo_anos;i++){
        valor_inicial+= (valor_inicial*(taxa/100));// atualiza o valor da variavel para contabilizar o proximo juros
    }
    cout<<valor_inicial<<endl;//exibe o resultado apos a quantidade de tempo solicitada

    return 0;
}
