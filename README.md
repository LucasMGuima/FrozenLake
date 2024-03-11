# Frozen Lake
Consiste em um ambiente onde se deve atravessar um lago congelado até o objetivo, evitando cair em seus buracos.
### Projeto
Esse projeto tem como intuito a implementação de uma algoritmo A* (A-estrela), para se encontrar o melhor caminho até o alvo, sendo o alvo um ponto fixo, o ponto $(n²)-1$, onde $n$ é o tamanho de um dos lados de uma grade quadrada.
Em sua versão completa o ambiente do *Frozen Lake* possui chance de ao se mover ir o lado errado, porém essa caracteristica não foi usada neste momento.
### Agente
O agente criado se utiliza da distancia entre dois pontos para avaliar o melhor caminho até o alvo.
- **Se encontrar**
O ambiente informa a posição do agente como um inteiro, indo de 0 até $(n²)-1$, onde $n$ é o tamanho do tabuleiro, sendo de 4 ou 8. Para se encontrar a posição atual pegamos o resto da divisão do valor informado pelo tamanho do tabuleiro como o valor na codernada X e o quociente da divisão como o valor em Y:
``` Python
    x_pos:int = pos%self.map_size
    y_pos:int = math.floor(pos/self.map_size)
```
- **Heuristica**
Para a solução desse problema foi utilizado a distancia entre dois pontos como heuristica, o valor com a menor distancia até o alvo será priorizado na busca pelo melhor caminho.
Sendo a distancia entre dois pontos dada pela seguinte formula, onde $P_i=(X_i,Y_i)$ e $P_f=(X_f,Y_f)$, são respectivamente o ponto inicial e final.
$$
    D(i,f) = (X_i - X_f) + (Y_i - Y_f)
$$
Em codígo a função para se achar o valor heuristico de dada posição é:
``` Python
    def heuristic(self, pos) -> int:
        x_pos:int = pos%self.map_size
        y_pos:int = math.floor(pos/self.map_size)

        dist = ((x_pos - self.x_target)**2) + ((y_pos - self.y_target)**2)
        return dist
```
- **Avaliando**
  Quando a simulção atual termina, avaliamos se o agente chegou até o alvo ou se caiu em um buraco, para isso vemos se a posição final é a posição alvo, se não for, atibuimos uma penalidade aquela posição, fazendo o agente tender a não escolhe-la novamente.

### Referencias
- [Biblioteca gymnasium](https://gymnasium.farama.org)