#include <iostream>

using namespace std;

void bubble (int *V,int n){ //algoritmo bublleSort é passado a posição inicial do vetor e o tamnho dele
int aux;// variavel para aramazenar o valor para realizar a troca
   for(int i=n-1;i>0;i--){ //contador que começa do fnal e decrementa pois no final do vetor temos a garantia que tera o maior valor
      for(int j=0;j<i;j++){ //contador que vai do valor inicial 0 ATE I-1 pois ele sempre troca com o da frente evitando assim acessar posições inexistentes
           if(V[j]>V[j+1]){//verifica se o valor e maior que o da frente caso seja ele troca os valores empurrando o maior para frente
                aux=V[j]; //troca os valores
                V[j]=V[j+1];
                V[j+1]=aux;
            }
      }
    }
}
void mostrar (int *V,int n){ //utilizado para exibir o vetor na tela
    cout<<"["; //escreve na tela
    for(int i=0;i<n;i++){ // contador ate o final do vetor
        if (i==n-1){ //se for o ultimo elemento a ser exibido ele finaliza com "]"
            cout<< V[i]<<"]";
        }else{  //se não for o ultimo elemento separa com ","
            cout<< V[i]<<",";
        }
    }
    cout<<endl;
}

int main()
{
    int v[]={1,6,7,2,3,0,4,5,9,1}; // aqui se começa o vetor com valores pre definidos não é em tempo de execução
    int tam=10; //o tamanho do vetor é colocado aqui lembrando que para efeito de calculo do tamanho a primeira posição é 1 e nao 0
    cout<<"vetor original"<<endl; //exibe na tela
    mostrar(v,tam);// mostra o vetor original sem passar pelo algoritmo
    bubble(v,tam);// executa o bubble passando o vetor e o tamanho
    cout<<endl<<"vetor ordenado"<<endl;
    mostrar(v,tam); //exibe o resultado obtido apos execuçao do bubble


    return 0;
}
