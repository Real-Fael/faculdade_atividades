%Caso base quando Tempo é zero quer dizer que não e necessario calcular taxa então é so atualizado o valor de total para o valor inicial
juros(Vinicial,_,0,Total):- Total is Vinicial.
%juros(Vinicial,Taxa,Tempo,Total) a taxa é dado em % por exemplo 5%,3%,10% o Tempo é a quantidade de vezes que a Taxa é contabilizada e Total é onde sera armazenado o resultado
juros(Vinicial,Taxa,Tempo,Total) :- 
    Tempo>0,%delimitamos a execução dessa recursao para quando Tempo é maior que 0
    Tp is (Tempo-1),%é subtraido de Tempo e guardado numa variavel auxiliar Tp 
    juros(Vinicial,Taxa,Tp,To),!,%passamos o valor inicial e Taxa sem alterar, Tp é o tempo -1 quando chega a 0 cai no caso base,To é utilizado para não alterar o parametro Total assim evitando erros
    Total is To*(1+(Taxa/100)). %Total é alterado apartir do valor To calculado recursivamente pela instrução anterior  
  