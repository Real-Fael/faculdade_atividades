%caso tenha pelo menos 2 elementos verifica se o componente X é maior que Y caso seja ele realiza a troca e coloca na lista do 2º parametro
troca([ X, Y | Resto ], [ Y, X | Resto ] ) :- X > Y, ! . %! é para que não faça o mesmo com a sub arvore  

%caso tenha pelo menos 1 elemento ele mantem o primeiro elemento em ambas as listas
troca([ Z | Resto ], [ Z | Resto1 ] ) :-
    troca(Resto, Resto1 ).% ele chama troca novamente para atualizar a sub lista Resto1
%ou seja ele troca os 2 primeiros elementos da lista caso o primeiro seja maior que o segundo em seguida mantem o menor e procura no resto da lista
%aqui é onde chamamos o algoritmo passamos a Lista desordenada no 1º parametro e o segundo onde sera ordenada

bubblesort( Desordenada, ListaOrd) :-
    troca( Desordenada, Lista1 ),%passamos a lista desordenada por parametro e crimaos outra variavel para armazenar a lista apos empurrar o maior pro final
    ! ,%impedimos que execute as subarvores
    bubblesort( Lista1, ListaOrd).% passamos a lista que o elemento foi empurrado pro final por parametro assim fazendo recursão e repetindo o processo

bubblesort( Ordenada, Ordenada). %apos terminar a recursão passamos o valor do primeiro parametro que esta ordenado para o segundo
