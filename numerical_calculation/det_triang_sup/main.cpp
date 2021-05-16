#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{

    ifstream entrada("matriz.txt", ifstream::in) ;
    int tam;
    double aux1, err=0;
    entrada >> tam;
    double matriz[tam][tam];

    cout<<"matriz: "<<tam<<"X"<<tam <<endl;
    for (int i=0; i<tam; i++)
    {
        for (int j=0; j<tam; j++)
        {
           entrada >> matriz[i][j];
        }

    }

    cout <<"apos inserção"<<endl;
    for (int i=0; i<tam; i++)
    {
        for (int j=0; j<tam; j++)
        {
            cout << setw(5) << setprecision(5) << matriz[i][j]<<"   " ;
        }
        cout<<endl;
    }
    cout<<endl<<endl<<endl;

for (int i=tam-1; i>=0; i--) // triangular para cima
    {
        for (int j=i-1; j>=0; j--)
        {
            for (int l=0; l<tam; l++)
            {
                for (int c=0; c<tam; c++)
                {
                    cout << setw(5) << setprecision(5) <<  matriz[l][c]<<" " ;
                }

                 if (l==j+1){
                    cout << "   ERRO:"<<err<< endl;
                 }else{
                    cout << "   ERRO:"<<0.0<< endl;
                 }
                cout<<endl;
            }
            cout<<endl<<endl<<endl;

            if (matriz[i][i] !=0)
            {
                aux1= matriz[j][i]/matriz[i][i];
                err=0;
             for (int k=tam-1; k>=0; k--)
             {


                matriz[j][k]=matriz[j][k]-matriz[i][k]*aux1;
                if(k==i){
                err=matriz[j][k];
                }
                if (matriz[j][k]!=0){
                matriz[j][k]= matriz[j][k]-err;
                }

             }


            }
        }
    }

    aux1=1;
    for (int i=0; i<tam; i++)
    {
        for (int j=0; j<tam; j++)
        {
            cout << setw(5) << setprecision(5) << matriz[i][j]<<"   " ;
        }

        cout<<endl;

        aux1*=matriz[i][i];
    }
    cout<<endl<<endl<<endl;
    cout<< " O Determinante da Matriz é: "<<aux1<<endl;





       return 0;
}
