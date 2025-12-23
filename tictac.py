import random

class TicGame():
    def __init__(self):
        self.data = [[" ", " ", " "], [" ", " ", " "], [" ", " " , " "]]  
        self.spots_left = [(0,0), (0, 1), (0,2),
                      (1, 0),(1, 1),(1, 2),
                      (2, 0), (2, 1), (2, 2)]
        self.taken = []
        self.winig_spots = [[(0,0), (0, 1), (0,2)], [(1, 0),(1, 1),(1, 2)], [(2, 0), (2, 1), (2, 2)],
                            [(0,0), (1, 0)]]
        self.desplay()

    def desplay(self):
        for i in range(3):
            print(f"  {self.data[i][0]}  |  {self.data[i][1]}  |  {self.data[i][2]}  ")
            if i != 2:
                print("-----------------")
    
    # moving computer moves
    def computer_move(self):
        if len(self.spots_left) != 0:
            com_move = random.choice(seq=self.spots_left)
            self.taken.append(com_move)
            self.data[com_move[0]][com_move[1]] = "O"
            for spot in self.spots_left:
                if spot == com_move:
                    self.spots_left.remove(spot)
            return True
        else:
            print("it is a draw")
            return False
    #moving user_respose 
    def user_move(self, user_index):
        if not user_index in self.taken:
            self.taken.append(user_index)
            self.data[user_index[0]][user_index[1]] = "X"
            for spot in self.spots_left:
                if spot == user_index:
                    self.spots_left.remove(spot)
            return True
        else:
            return False
        
    def check_winner(self):
        players =('X', 'O')
        for player in players:
            # checking for a row 
            if self.data[0][0] == player and self.data[0][1] == player and self.data[0][2] == player and self.data[0][0] != " ":
                return player
            if self.data[1][0] == player and self.data[1][1] == player and self.data[1][2] == player and self.data[1][0] != " ":
                return player
            if self.data[2][0] == player and self.data[2][1] == player and self.data[2][2] == player and self.data[2][0] != " ":
                return player
            
            # checking for a column
            if self.data[0][0] == player and self.data[1][0] == player and self.data[2][0] == player and self.data[0][0] != " ":
                return player
            if self.data[0][1] == player and self.data[1][1] == player and self.data[2][1] == player and self.data[0][1] != " ":
                return player
            if self.data[0][2] == player and self.data[1][2] == player and self.data[2][2] == player and self.data[0][2] != " ":
                return player
            
            #checking for a diagonal
            if self.data[0][0] == player and self.data[1][1] == player and self.data[2][2] == player and self.data[2][2] != " ":
                return player
            if self.data[0][2] == player and self.data[1][1] == player and self.data[2][0] == player and self.data[2][0] != " ":
                return player