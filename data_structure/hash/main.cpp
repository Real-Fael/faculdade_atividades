#include <iostream>
#include <string.h>
#include <fstream>
#define n 47
using namespace std;

struct celula{
    celula *prox;
    char *chave;
};

struct lista{
    celula *cabeca;
    celula *cauda;
};



void inicia_lista(lista *m[]){
    for(int i=0;i<n;i++){
       m[i]= new lista;
       m[i]->cabeca=NULL;
       m[i]->cauda=NULL;
    }
}


int retorna_hash(char *str){
    int total=0;
    int i;
    for (i=0;i<strlen(str);i++){
        total+=str[i];
    }
    cout<<total<<" num";
    return (total%n);
}

void inserir(char *str,lista *m[]){
    int h=retorna_hash(str);
    cout<<"Hash: "<<h<<endl;
    celula *c= new celula;
    c->prox= NULL;
    c->chave= new char;
    strcpy(c->chave,str);
    if (m[h]->cabeca==NULL){
        m[h]->cabeca=m[h]->cauda=c;
        cout<<"inserindo primeira vez"<<endl;
    }else{
        m[h]->cauda->prox=c;
        m[h]->cauda=c;
        cout<<"inserindo no final"<<endl;
    }
}

celula *retorna_celula(char *str, lista *m[]){
    int h=retorna_hash(str);
    bool verifica=false;
    string b,a=str;
    celula *encontra;
    encontra= m[h]->cabeca;

    cout<<"procurando por "<<str<<endl;
    while (encontra!=NULL && !verifica){
        b=encontra->chave;
        if (b==a){
            verifica=true;
            cout<<"encontrado"<<endl;
            return encontra;
        }else{
            encontra=encontra->prox;
            cout<<"procurando"<<endl;
        }
    }
    return NULL;
}


void mostrar_hash(lista *m[]){
    celula *aux;
    for(int i=0;i<n;i++){
        aux=m[i]->cabeca;
        cout<<"hash "<<i<<":";
        while(aux!=NULL){
            cout<<" "<<aux->chave<<",";
            aux=aux->prox;
        }
        cout<<" NULL"<<endl;
    }

}/*
celula *removerHash(char *str,lista *m[]){
    celula *aux,*removido;
    aux=retorna_anterior(str,m);
    int h=retorna_hash(str);
    if (aux!=NULL){
        if (aux==m[h]->cabeca){
            removido=aux;
            m[h]->cabeca=m[h]->cabeca->prox;
        }else{
            removido=aux->prox;
            aux->prox=aux->prox->prox;
        }
        return removido;
    }else{
    cout<<" dado nao encontrado"<<endl;
    return NULL;
    }
}
*/
celula *removerHash(char *str,lista *m[]){
    int h=retorna_hash(str);
    bool verifica=false;
    string b,a=str;
    celula *encontra,*anterior;
    encontra= m[h]->cabeca;
    anterior=encontra;
    cout<<"procurando por "<<str<<endl;
    while (encontra!=NULL && !verifica){
        b=encontra->chave;
        if (b==a){
            if(anterior==encontra){
                m[h]->cabeca=m[h]->cabeca->prox;
            }else{
                anterior->prox=anterior->prox->prox;
            }
            verifica=true;
            cout<<"encontrado"<<endl;
            return encontra;
        }else{
            anterior=encontra;
            encontra=encontra->prox;
            cout<<"procurando"<<endl;
        }
    }
    return NULL;

}

void lerarq(lista *m[]){
    ifstream entrada("nomes.txt",fstream::in);
    char nome[50];
    while(entrada.good()){
    entrada>>nome;

    cout<<nome<<", ";
    inserir(nome, m);

    }
    entrada.close();
cout<<"fim"<<endl;
}
void escreverarq(lista *m[]){
    ofstream saida;
    celula *aux;
    saida.open("nomes.txt");
    saida.app;
    if(saida.is_open()){
        for(int i=0;i<n;i++){
            aux=m[i]->cabeca;
            while(aux!=NULL){
                saida<<aux->chave;
                saida<<" ";
                aux=aux->prox;
            }
        }
        cout<<"arquivo salvo"<<endl;
    }else{
        cout<<"erro ao abrir arquivo"<<endl;
    }
    saida.close();

}

int main()
{
    char nome[20],test;
    celula *anterior,*removido;
    lista *m[n];
    inicia_lista(m);
    lerarq(m);
    do{
    cout<<"*******  digite um nome  *******"<<endl;
    cin>>nome;
    cout<<"o nome digitado foi: "<<nome<<endl;
    inserir(nome,m);
    cout<<"digite 0 para sair e qualquer coisa para inserir novamente"<<endl;
    cin>>test;
    }while(test!='0');
    mostrar_hash(m);
    cout<<"digite um nome para procurar"<<endl;
    cin>>nome;
    anterior=retorna_celula(nome,m);
    if(anterior!=NULL){
        cout<<"o valor e "<<anterior->chave<<endl;
        if(anterior->prox!=NULL){
            cout<< " *** O proximo é "<<anterior->prox->chave<<endl;
        }else{
            cout<<"o proximo nao existe"<<endl;
        }
    }else{
        cout<<"nao encontrado"<<endl;
    }
    cout<<"digite um nome para remover"<<endl;
    cin>>nome;
    removido= removerHash(nome,m);

    mostrar_hash(m);
    escreverarq(m);


    return 0;
}
