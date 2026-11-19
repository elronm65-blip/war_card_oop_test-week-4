import random

class Player:
    def __init__(self ,name):
        self.name = name
        self.cards = []

    def mix_cards(self):
        new = self.cards.copy()
        new_cards =[]
        while new:
            index = random.randint(0 , len(new)-1)
            new_cards.append(new.pop(index))
        self.cards = new_cards    
    
    def __str__(self):
        return  f'{self.name}:  {self.cards[0]}' 


    def count_cards(self):
        return len(self.cards)


class Card:
    def __init__( self , val , visual):
        self.val =val
        self.visual =visual

    def __str__(self):
        return f'{self.val} :  {self.visual}'






class Game:
    def __init__(self , player:Player ,computer:Player):
        self.player =player
        self.computer =computer
        self.paket = []

    def show_paket(self):
        for c in self.paket:
            print(c)


    def  show_player(self):
        print(self.player)


    def  show_computer(self):
            print(self.computer)    

    
    def crete_paket(self):
        list = [2,3,4,5,6,7,8,9,10,11,12,13,14]
        shapes = ["H" ,"D" ,"C","S"]
        count = 4
        s = 0
        while count > 0:
            for num in list:
                i = Card(num ,shapes[s] )
                self.paket.append(i)
            count -= 1  
            s += 1
            
    def mix_paket(self):
        
        new = self.paket.copy()
        new_paket = []

        while new:
            random_index = random.randint(0 , len(new)-1)
            new_paket.append(new.pop(random_index))
        
        self.packet = new_paket  
        
        
            

    def dealing_cards(self):
        self.player.cards = self.paket[1:27]
        self.computer.cards = self.paket[26:53]

    def play_round(self):
        game_over = False
        while not game_over:
            round = input("press on something for play round")
            if round:
                print("========TURN=======")
                self.show_computer()
                self.show_player()
                if self.player.cards[0].val > self.computer.cards[0].val:
                    self.player.cards.append(self.computer.cards[0])
                    self.computer.cards.pop(0)
                    print(f'wineer : {self.player.name}')
                    print(f'computer cards :{self.computer.count_cards()}   , player cards : {self.player.count_cards()}')
                elif self.player.cards[0].val < self.computer.cards[0].val:
                    self.computer.cards.append(self.player.cards[0])
                    self.player.cards.pop(0)
                    print(f'wineer : {self.computer.name}')
                    print(f'computer cards :{self.computer.count_cards()}   , player cards : {self.player.count_cards()}')

                elif self.player.cards[0].val == self.computer.cards[0].val:
                    self.player.mix_cards()
                    self.computer.mix_cards()
                    print("its draww!!")
                    print(f'computer cards :{self.computer.count_cards()}   , player cards : {self.player.count_cards()}')
                    

                if self.player.count_cards == 52 or self.computer.count_cards ==52:
                    game_over =True


                

                
                
                
                
        
            








