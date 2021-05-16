#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#define maxnivel 4
using namespace std;


struct Tcelula{
   Tcelula *dir[maxnivel],*esq[maxnivel];
   int val;

};
struct TskipList{
   Tcelula *inicio,*fim;
   int quantidade;

};

void inicia_skip(TskipList &l){
    l.inicio = NULL;
    l.fim=NULL;
    l.quantidade=0;

}
int retorna_Nivel(){
    int nivel=-1;
    srand( (unsigned)time(NULL) );
    int ran = rand()%100;
    cout<<"sorteado: "<<ran;
    for (int i=0;i<maxnivel;i++){
        if (ran<=100/(pow(2,i)) ){
            nivel++;
        }
    }
    cout<<"   Nivel: "<<nivel<<endl;
    return nivel;
}
Tcelula retorna_celula(int x){
    Tcelula cel;
    for (int i=0;i<maxnivel;i++){
       cel.dir[i]=NULL;
       cel.esq[i]=NULL;
    }
    cel.val=x;
    return cel;
}

void inserir_skip(TskipList &skip,int h,int x){
    Tcelula *aux,*novacel;
    aux=skip.inicio;
    novacel= new Tcelula;
    for (int i=0;i<maxnivel;i++){
       novacel->dir[i]=NULL;
       novacel->esq[i]=NULL;
    }
    novacel->val=x;


    if(skip.inicio==NULL){
        skip.fim=skip.inicio=novacel;
        cout<<"o numero foi inserido no inicio da skip"<<endl;
    }else{
        if(novacel->val<=skip.inicio->val){
            for(int i=maxnivel-1;i>=0;i--){
                novacel->dir[i]=skip.inicio;
                skip.inicio->esq[i]=novacel;

            }
            skip.inicio=novacel;
        }else{

        for (int i=maxnivel-1;i>=0;i--){
           while(aux->dir[i]!=NULL && aux->dir[i]->val<novacel->val){
                aux=aux->dir[i];
           }
           if(i<=h){
                if(aux->dir[i]==NULL){
                    aux->dir[i]=novacel;
                    novacel->esq[i]=aux;
                    if(i==0){
                        skip.fim=aux->dir[i];
                    }
                }else{
                    if(aux->dir[i]->val>=novacel->val){
                        novacel->dir[i]=aux->dir[i];
                        novacel->esq[i]=aux;
                        aux->dir[i]->esq[i]=novacel;
                        aux->dir[i]=novacel;
                    }
                }
           }
        }
    }
    }
}

void cadastrar_skip(TskipList &lista){
    Tcelula celula, *aux;
    int x,nivel;
    cout<<"digite um valor para inserir"<<endl;
    cin>>x;
    nivel= retorna_Nivel();
    inserir_skip(lista,nivel,x);

}
void mostraSkip(TskipList &l){
    Tcelula *aux;
    for(int i=maxnivel-1;i>=0;i--){
        aux=l.inicio;
        cout<<"**** mostrando Nivel: "<< i<<" *******"<<endl;
        while (aux!=NULL){
            cout<<"   "<<aux->val;
            aux=aux->dir[i];
    }
    cout<<endl;
}
}
Tcelula *procura_cel(TskipList &l,int x){
    Tcelula *aux;
    aux=l.inicio;
    for (int i=maxnivel-1;i>=0;i--){

        while(aux->dir[i]!=NULL && aux->dir[i]->val<=x){
            aux=aux->dir[i];
        }
        if(aux->val==x){
            cout<<"existe num "<<aux->val;
            if(aux->esq[i]!= NULL)
               cout<<" a direita de "<<aux->esq[i]->val;
            cout<<endl;
            return aux;
        }
    }
    cout<<"nao encontrado"<<endl;
    return NULL;
}
void deleta_cel(TskipList &l){
    int x;
    Tcelula *aux;
    cout<< "digite um numero pra procura"<<endl;
    cin>>x;
    aux=procura_cel(l,x);
    if(aux!=NULL){
        if(aux==l.inicio){
            cout<<"esta no inicio"<<endl;
            if(aux->dir[0]!=NULL){
                aux=aux->dir[0];
                for(int i=maxnivel-1;i>=0;i--){
                    if(l.inicio->dir[i]!=aux){
                        aux->dir[i]=l.inicio->dir[i];
                        aux->esq[i]=l.inicio->esq[i];
                        if(aux->dir[i]!=NULL){
                            aux->dir[i]->esq[i]=aux;
                        }
                    }else{
                        aux->esq[i]=l.inicio->esq[i];

                    }
                }
                delete l.inicio;
                l.inicio=aux;
            }else{
                l.inicio=l.fim=NULL;
            }
        }else{
            if(aux==l.fim){
                aux=l.fim->esq[0];
                for (int i=maxnivel-1;i>=0;i--){
                        if(l.fim->esq[i]!=NULL){
                            l.fim->esq[i]->dir[i]=NULL;
                        }
                }
                delete l.fim;
                l.fim=aux;
            }else{
                for (int i=maxnivel-1;i>=0;i--){
                    if(aux->dir[i]==NULL && aux->esq[i]!=NULL){
                        aux->esq[i]->dir[i]=NULL;
                    }else{
                        if(aux->dir[i]!=NULL && aux->esq[i]!=NULL){
                            aux->dir[i]->esq[i]=aux->esq[i];
                            aux->esq[i]->dir[i]=aux->dir[i];
                        }
                    }
                }
                delete aux;
            }
        }
    }else{
        cout<<"pra deletar é preciso existir"<<endl;
    }
}
int main()
{
    TskipList skip;
    inicia_skip(skip);
    bool loop=false;
    char test;
    while(!loop){
        cout<<"======digite uma opção======="<<endl;
        cout<<"digite 1 para cadastrar"<<endl
        <<"gigite 2 para exibir lista" <<endl
        <<"digite 3 para buscar na lista"<<endl;
        cin>>test;
        switch (test){
            case '1':
                cadastrar_skip(skip);

            break;

            case '2':
                mostraSkip(skip);

            break;

            case '3':

                deleta_cel(skip);


            break;
        }
    }


    cout << "Hello world!" << endl;
    return 0;
}
