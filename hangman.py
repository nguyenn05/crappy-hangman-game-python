import random
from clear_screen import clear
guess = ""
board = []
manp = ["O","/","|","\\","|","/","\\"]
man = ["","","","","","",""]
dd = 0 
z = 0
he = ""

def draw_word():
  if check_input() == True:
    list_duplicates_of(guessli,user)
  for y in locs:
    board[y] = guessli[y]

def vocab():
  global guess, guessli
  # Open the file in read mode
  with open("test.txt", "r") as file:
      allText = file.read()
      words = list(map(str, allText.split()))
  guess = random.choices(words)[0]
  guessli = list(guess)

def draw_saved():
  print("     thanks")
  print(" \\  O  / ")
  print("   \\|/  ")
  print("    |   ")
  print("   / \\")

def check_win():
  if board == guessli or str(user) == guess:
    return True

def draw_man():
  global he
  global z
  if z < 7:
    clear()
    print(z)
    man[z] = manp[z]
    z += 1
  if z == 4:
    he = "help!:((("
  if z == 6:
    print("Last chance")
  elif z > 6 :
    death()
    exit()

  
def death():
  clear()
  print("He dead!!!")
  print(f"The word is '{guess.upper()}'.")


  

def list_duplicates_of(seq,item):
    global locs
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


def check_input():
  if str(user) in guess:
    return True
  else:
    return False




def draw_vocab():
  if check_input() == True:
    list_duplicates_of(guess,int(user))
    for p in locs:
      board[p] = int(user)

    

 
def user_input():
  global user
  user = input("\nplease guess or type 'quit' to escape: ")
  if str(user) == "quit":
    clear()
    exit()
  elif str(user) == "ad":
    clear()
    print(guess)
    print(guessli)
  elif str(user) == "draw":
    draw_man()
  else: 
    if check_input() == True:
      clear()
      draw_word()
      if check_win():
        clear()
        print("You save him\n")
        draw_saved()
        print(f"The word is '{guess.upper()}'")
      
    else:
      draw_man()
  
      



def draw_guess():
  for ji in range(0,legu):
    print(board[ji],end="")

  


def create_board():
  global legu
  legu = len(guess)
  ii = 0
  while ii < legu:
    board.append(" _ ")
    ii += 1
  return board

def draw_cot():
  print("--------|")
  print(f"|       {man[0]}    {he}")
  print(f"|      {man[1]}{man[2]}{man[3]}")
  print(f"|       {man[4]}")
  print(f"|      {man[5]} {man[6]}")
  print("|______") 

def play_game():
  print("Save him from not being executed")
  draw_cot()
  print("Guess the word")
  draw_guess()
  user_input()

# Main game loop
def main():
  
  run = True
  vocab()
  create_board()


  while run:
    play_game()
    if check_win():
      run = False
    
  cons = input("Want to put him in danger again? (y/n): ")
  if cons == "y":
    print("HaHa you cannot do that:)))))")
  else:
    clear()
    exit()
if __name__ == '__main__':
  main()