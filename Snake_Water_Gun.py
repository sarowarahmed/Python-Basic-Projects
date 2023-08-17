import random
randomno=random.randint(1,3)
print("computer turn: snake(s) water(w) or gun(g)")
if randomno==1:
    comp="s"
elif randomno==2:
    comp="w"  
elif randomno==3:
    comp="g"  

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True  
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True 
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True                   

you=input("Your turn: snake(s) water(w) or (g): ")  
f=gamewin(comp,you)     
print(f"computer chooose: {comp}") 
print(f"you chooose: {you}") 
if f==None:
    print("The Game is a draw")
elif f: #means if "f" == True
    print("You win this the Game") 
else:
    print("You lose this the Game")   
