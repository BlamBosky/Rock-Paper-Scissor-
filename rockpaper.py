import random

moves = {}
player = 0
comp = 0
for i in range (10):
  present = []
  user_choice = str(input("Enter your choice: "))
  present.append(user_choice)
  choice = user_choice.lower()
  comp_outcome = ["Rock", "Paper", "Scissor"]
  comp_rand = random.choice(comp_outcome)
  comp_choice = comp_rand.lower()
  present.append(comp_choice)
  pw = "Player won"
  cw = "Computer won"
  tie = "Tie"

  if choice == comp_choice:
    print(f"{tie} \n")
    present.append(tie)
  elif choice == "rock":
    if comp_choice == "scissor":
      print("You win! \n")
      player = player + 1
      present.append(pw)
    else:
      print("Computer won \n")
      comp = comp + 1
      present.append(cw)
  elif choice == "paper":
    if comp_choice == "rock":
      print("You win! \n")
      player = player + 1
      present.append(pw)
    else:
      print("Computer won \n")
      comp = comp + 1
      present.append(cw)
  elif choice == "scissor":
    if comp_choice == "paper":
      print("You win! \n")
      player = player + 1
      present.append(pw)
    else:
      print("Computer won \n")
      comp = comp + 1
      present.append(cw)
  moves[i+1] = present

if(player>comp):
  print("Player won the match \n")
elif (player==comp):
  print("Tie \n")
else:
  print("Computer won the match \n")

x = "y"
while x == "y":
  round_val = int(input("Enter the round for which you need the instruction : "))
  if round_val>10:
    print("Invalid input")
  else:
    print(f" \n Player's move:{moves[round_val][0]} \n\n Computer's move:{moves[round_val][1]} \n")
    if(moves[round_val][2]=="Tie"):
      print(" Its a Tie \n")
    else:
      print(f" {moves[round_val][2]} Round {round_val} \n")

  x = input("Do you want to again check 'y or n':")
