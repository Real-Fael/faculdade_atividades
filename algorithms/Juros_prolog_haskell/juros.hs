
juros v_i taxa tempo = if tempo==1-- o tempo é subtraido para simular um laço for e executar a quantidade de vezes solicitado na variavel tempo
                       then v_i*(1+taxa/100) -- se o tempo é igual a 1 então ele calcula o primeiro juros que serve de base para calcular os outros na recursão
                       else (1+taxa/100)*(juros v_i taxa (tempo-1)) -- calcula os juros de acordo com o resultado da recursão 
