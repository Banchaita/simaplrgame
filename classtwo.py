birds="Nyctibiu Bluebirds Penguins Columbidae Budgeriga"
birds_guess = input("Guess a birds name:")
if(birds_guess.capitalize() in birds) == False: 
 print("No, not thaning of", birds_guess)
 print()
else:
  print("You guess it correct")