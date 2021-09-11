import random
def test(a,b):
    r=""
    if(a==b):
       r="Tie" 
       return r
    elif(a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
        r="LOST"
        return r
    elif(a==1 and b==3) or (a==2 and b==1) or (a==3 and b==2):
        r="WON"
        return r
moves = {}
print("ENTER YOUR CHOICE\n1) ROCK\n2) PAPER\n3) SCISSOR")
for i in range (10):
  present = []
  user_choice = int(input("Enter your choice for round {}: ".format(i+1)))
  comp_outcome = [1, 2, 3]
  comp_choice = random.choice(comp_outcome)
  c=test(user_choice,comp_choice)  
  present[:3]=[user_choice,comp_choice,c]
  moves[i+1] = present  
round_val = int(input("Enter the round for which you need the instruction : "))
if round_val>10:
    print("Invalid input")
else:
    print(f" \n Player's move:{moves[round_val][0]} \nComputer's move:{moves[round_val][1]}")
    if(moves[round_val][2]=="Tie"):
      print("Its a Tie \n")
    else:
      print(f"{moves[round_val][2]} Round {round_val} \n")
