#include <iostream>
#include <math.h>
using namespace std;
//  *******************      falsa posi��o ****************************

double f(double x){
return sqrt(x)-5* exp(-x);
}
double xk(double a, double b){

return (a*f(b) - b*f(a))/(f(b)-f(a));

}

int main()
{
    double a=1;
    double b=1.448;
    int cont=0;
    double erro;
    double xn,fxn;
    while(cont<=1 || erro>1e-8){

        cout<<"o valor a="<< a<<endl;
        cout<<"o valor b="<< b<<endl;

        cout<<"o valor F(a)="<< f(a)<<endl;
        cout<<"o valor F(b)="<< f(b)<<endl;
        xn=xk(a,b);
        cout<< " o valor de xk="<< xn<<endl;

        cout<< "o F(xk)="<<f(xn)<<endl;
        if (cont >0){
            erro= abs(abs(f(xn))-abs(fxn));
            cout<<"ERRO: "<<erro<<endl;
        }

        fxn=f(xk(a,b));
        if (fxn<=0){
            a=xn;
        }else{
            if (fxn>0){
               b=xn;
            }
        }

        cont++;
        }

    return 0;
}
