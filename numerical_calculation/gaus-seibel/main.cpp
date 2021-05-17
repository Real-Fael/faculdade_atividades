#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
using namespace std;

void calcularX(double mat[][100],double indepen[],double resultados[], int tam){


    for (int j=0;j<tam;j++){

            for(int k=0; k<tam;k++){
               if (k==0){
                   resultados[j]=indepen[j];
               }
               if (j!=k){
                   resultados[j]+= (((-1)*mat[j][k])*resultados[k]);
               }
               if(k==tam-1){
                   resultados[j]/= mat[j][j];
               }
            }
    }

for (int i=0; i<tam;i++){
    cout<<setprecision(20) <<"X"<<i+1<<": "<<resultados[i]<<endl;
}


}


int main()
{
    double erro=0,erro2=0;

    int n;
    ifstream entrada;
    entrada.open("matriz.txt");

    entrada >> n;
     double a[100][100], x[100],indep[100];

    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++ ){
            entrada >>a[i][j];
            cout << a[i][j]<<" ";
        }
        entrada >> indep[i];
        cout<<"= "<< indep[i]<<" entrada"<<endl;
        x[i]=1;
    }

   cout<<"valores inciais"<<endl;
   for (int i=0;i<n;i++){
      cout<<"X"<<i+1<<"= " <<x[i]<< "     ";
   }

   for(int i=0; i<100;i++){
      erro=0;
      erro2=0;
      cout <<"******iteração nº "<< i<<"  *********** "<<endl;
      for(int j=0;j<n;j++){
         erro+= abs(x[j]);

      }
      calcularX(a,indep,x,n);

      for(int j=0;j<n;j++){
         erro2+= abs(x[j]);
         erro= erro-erro2;
         erro=abs(erro);
      }
      cout<<setprecision(20) <<"ERRO: "<< erro<<endl;

   }
    return 0;
}
