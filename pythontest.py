import random



def my_RPS():
     ans1=""
     name=input("Enter Name: ")
     userwin=0
     cpuwin=0
     while ans1.upper()!="EXIT":  
        ans1=input("Please Choose either Rock, Paper, Sissors to play or Exit to Quit the game: ").upper()
        ans2= random.choice(["rock","paper","sissors"]).upper()
        if ans1=="ROCK" or ans1=="SISSORS" or ans1=="PAPER" or ans1=="EXIT":
            if ans1=="EXIT":
                break          
            if  ans1=="PAPER" and ans2=="ROCK":
                print(f"{name}:{ans1}")
                userwin+=1
            elif ans1=="ROCK" and ans2=="SISSORS":
                print(f"{name}:{ans1}")
                userwin+=1
            elif ans1=="SISSORS" and ans2=="PAPER":
                print(f"{name}:{ans1}")
                userwin+=1    
            elif ans1==ans2:
                print("DRAW")
                continue  
            else: 
                print(f"CPU:{ans2}") 
                cpuwin+=1
        else: print(f"{ans1} is not one of the options")
     if userwin>cpuwin:
        print(f"Winner {name}:{userwin} CPU:{cpuwin}")
     elif cpuwin>userwin:
        print(f"Winner CPU:{cpuwin} {name}:{userwin}")
     else: print(f"Draw {name}:{userwin} CPU:{cpuwin}")
my_RPS()