#Action space
#0: Move left
#1: Move down
#2: Move right
#3: Move up
import math

moves = {
    -1: 0,
    +1: 2,
    -4: 3,
    +4: 1,
    -8: 3,
    +8: 1
}

class AgenteV1:
    def __init__(self, map_size: int):
        self.map_size = map_size

        self.target = (map_size**2)-1
        self.x_target = self.target%map_size
        self.y_target = math.floor(self.target/map_size)

        self.f_positions = [0]*(map_size**2)
        self.g_positions = [5]*(map_size**2)

    def get_action(self, obs) -> int:
        return self.a_star(obs)
    
    def possible_move(self, pos) -> list[int]:
        line_size = self.map_size
        max_pos = (self.map_size**2) - 1 #-1 pós a primeira posição é 0
        valid_move = []

        #verifica se pode se mover para cima, se sim adiciona aos movimento validos
        valid_move.append(pos-line_size) if (pos- line_size>= 0) else valid_move
        #verifica se pode se mover para baixo, se sim adiciona aos movimento validos
        valid_move.append(pos+line_size) if (pos+line_size <= max_pos) and (((pos+line_size)%(self.map_size**2)) > 0) else valid_move
        #verifica se pode se mover para esquerda, se sim adiciona aos movimento validos
        valid_move.append(pos-1) if (pos-1 >= (pos-(pos%self.map_size))) else valid_move
        #verifica se pode se mover para direita, se sim adiciona aos movimento validos
        valid_move.append(pos+1) if (pos+1 <= max_pos) and (((pos+1)%self.map_size) > 0) else valid_move

        return valid_move

    def terminated(self, pos):
        #Agente avalia a situação em que foi terminado o episodio, e avalia se o caminho foi um uscesso ou n, se n, penalisa a posição, possivel buraco
        if (pos != (self.map_size**2)-1):
            self.g_positions[pos] = 1000
        else: 
            self.g_positions[pos] = 0

    def heuristic(self, pos) -> int:
        #Distancia entre dois pontos
        x_pos:int = pos%self.map_size
        y_pos:int = math.floor(pos/self.map_size)

        dist = ((x_pos - self.x_target)**2) + ((y_pos - self.y_target)**2)
        #print("({} - {})^2) + ({} - {})^2 = {}".format(x_pos, self.x_target, y_pos, self.y_target, dist))
        return dist

    def a_star(self, cur_pos):
        best_move: int
        possible_move = self.possible_move(cur_pos)

        #print("====================================")
        #print("CP: {} | MOVES: {}".format(cur_pos, possible_move))
        #print("G: {}".format(self.g_positions))
        #print("F: {}".format(self.f_positions))

        #calcula o F dos movimentos possiveis
        best_move = possible_move[0]
        for move in possible_move:
            g = self.g_positions[move]
            h = self.heuristic(move)
            f = g + h
            if(self.f_positions[move] < f):
                self.f_positions[move] = f
            #Guarda o melhor movimento
            best_move = move if self.f_positions[best_move] > self.f_positions[move] else best_move
        
        #acha a direção a se mover
        move_dir = moves[best_move - cur_pos]

        #print("BM: {} MD: {}".format(best_move, move_dir))
        return move_dir