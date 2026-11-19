
from war_game import *
def main():
    print("""1.game
    2.exite""")

    choose = input("press 1 to begin game , or 2 to exiet")
    if choose =="1":
        name =input("put your name")
        player = Player(name)
        computer = Player("computer")

        g =Game(player,computer)
        g.crete_paket()
        g.mix_paket()
        g.dealing_cards()
        g.play_round()
    if choose == "2":
        print("good bye")
        return    


main()