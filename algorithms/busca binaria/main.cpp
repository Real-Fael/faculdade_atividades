#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream entrada("vetor.txt",fstream::in);
    int tam,inicio,fim,aux;
    entrada >>tam;

    double valor,vet[tam];
    bool verifica=false,encontrado;
    for (int i=0; i<tam; i++){
        entrada >> vet[i];
    }
    for(int i=0; i<tam;i++){
        cout<< "posição "<<i<<" numero "<< vet[i]<<endl;
    }
    while (verifica==false){
        cout<<"digite o valor para pesquisa"<<endl;
        cin>>valor;
        inicio=0;
        fim=tam-1;
        aux=0;
        encontrado=false;
        while (!encontrado){

        cout<<"********** o o vetor foi dividido **********"<<endl;
        cout<<"inicio: "<<inicio<<endl<<"Fim: "<<fim<<endl;
         for(int i=inicio;i<=fim;i++){
            cout<<"posicao: "<<i<<" numero: "<<vet[i]<<endl;;

         }
        if (vet[inicio]==valor){
            cout<<"valor encontrado posição: "<<inicio<<endl;
            encontrado=true;
        }else{
            if (vet[fim]==valor){
                cout<<"valor encontrado posição: "<<fim<<endl;
                encontrado=true;
            }else{
                aux=(inicio+fim)/2;
                if ( valor<=vet[aux]){
                    if(fim==aux){
                        encontrado=true;
                        cout<<"numero nao existe"<<endl;
                    }
                    fim=aux;
                }else{
                    if(valor>vet[aux]){
                       if(inicio==aux){
                        encontrado=true;
                        cout<<"numero nao existe"<<endl;
                       }
                        inicio=aux;
                    }
                }
            }
        }

     }
    }
    return 0;

}
