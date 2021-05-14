menor x y = if x <= y -- função utilizada para verificar se o primeiro valor é menor que o segundo
           then True
           else False
maior x y = if x >= y -- função utilizada para verificar se o primeiro valor é maior que o segundo
           then True
           else False
mElemento m [] = True -- quando chega nesse ponto é porque não foi encontrado um elemento desordenado
mElemento m (x:xs) = if menor m x --verifica se é menor
                      then  mElemento x xs --é chamado navamente de forma recursiva passando x atual para ser comparado com o outro valor Head do xs
                      else False --se existe um valor que esteja desordenado retorna falso
ordenada (x:xs) =  mElemento x xs --ordenada é uma função usada para passar o primeiro elemento da lista para a função recursiva mElemento

empurra n [] = [n] --caso acabe a lista o valor de n é retornado para a recursão
empurra n (x:xs) = if maior n x-- caso o valor de n seja maior que x é necessario trocar o x e n empurrando sempre o maior valor para o final
                   then [x]++empurra n xs --caso x seja menor é colocado a esquerda e o n é "empurrado" e utilizado na proxima recursão 
                   else [n]++empurra x xs --caso n seja menor que x n permanece na mesma posição e x é usado para comparaçao
bbS (x:xs) =  empurra x xs -- bbS é uma função usada para passar o primeiro parametro pra função recursiva que ira empurrar o maior numero para o final

bubbleSort (x:xs) = if (ordenada (x:xs)) --caso a lista esteja ordenada não executará novamente exibindo o resultado na tela 
                    then ([x]++xs) --exibe a lista
                    else bubbleSort(bbS(x:xs)) --caso a lista nao esteja ordenado é chamado a função bubbleSorte recursivamente passando como parametro o resultado de bbs que é a lista com o maior numero empurrado para o final... essa recursão é feita  ate que a lista fique ordenada
