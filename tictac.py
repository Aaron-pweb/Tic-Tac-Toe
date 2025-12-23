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
        com_move = random.choice(seq=self.spots_left)
        self.taken.append(com_move)
        self.data[com_move[0]][com_move[1]] = "O"
        for spot in self.spots_left:
            if spot == com_move:
                self.spots_left.remove(spot)

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

    # check if there is a winner
    def check_winner(self):
        pass