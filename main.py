import random
import time
import sys

import os

rows, cols = 10, 10
player_pos = [1, 1]  # Start position of the player

maze = [
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') #screen clear

def display_maze():
    clear_screen()
    for r in range(rows):
        row_str = ""
        for c in range(cols): #iterates over the maze and prints the player position. So it clears console everytime player moves
            if [r, c] == player_pos: 
                row_str += '*'  
            else:
                row_str += maze[r][c]
        print(row_str)
    print("Use WASD and q to quit")

def move_player(direction):
    global player_pos
    dr, dc = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}.get(direction, (0, 0)) #movement function
    new_r, new_c = player_pos[0] + dr, player_pos[1] + dc

    if 0 <= new_r < rows and 0 <= new_c < cols and maze[new_r][new_c] != '#':
        player_pos = [new_r, new_c] #makes sure player doesnt go out of bounds. 

def play_game(): 
    while True:
        display_maze()

        move = input("Enter move: ").lower()

        if move == 'q':
            print("Thanks for playing!")
            

        if move in ['w', 'a', 's', 'd']:
            move_player(move)

            if player_pos == [8, 8]:  # The exit position (row 8, column 8)
                display_maze()
                print("good job")                
                boss()
                

def startmaze():
    print("Find your way to the exit to go to boss ifhgt.")
    play_game()


#game menu
def menu(): 
  print("Welcome to Ashen Catacombs!")
  print("Type 'i' for info")
  print("Type 's' to start")
  print("Type 'q' to quit")
  response = input("Type here: ")
  if (response == 'i'):
    print("This is game info")
  elif (response == 'q'):
    print("Game quit")
    sys.exit()
  elif (response == 's'):
    game()
  else:
    print("invalid input")

def gameover():
  print("GAME OVER. YOU DIED!")
  keepPlaying = True
  while(keepPlaying):
    response = input("Return to Menu? 'y'/'n' ")
    if(response == 'y'):
      menu()
    elif(response == 'n'):
      print("Thank you for playing Ashen Catacombs!")
      print("Game quit")
      sys.exit()
    else:
      print("invalid input")

class Player:
  def __init__(self, health, inventory):
    self.health = health
    self.inventory = inventory
  def changeHp(self, amt):
    self.health += amt;
    if (amt > 0):
      time.sleep(1)
      print("You gained " + str(amt) + " hp.")
    else:
      amt = -amt
      time.sleep(1)
      print("You lost " + str(amt) + " hp.")
    if(self.health > 10):
      self.health = 10
    elif (self.health <= 0):
      gameover()
      self.health = 0
    time.sleep(1)
    print("You now have " + str(self.health) + " hp.")
  #add or delete item from inventory list
  def addInventory(self, isAdd, item): #item is an array [string, int]
    if(isAdd):
      self.inventory.append(item)
      time.sleep(1)
      print(item[0] + " was added to your inventory.")
    if(isAdd == False):
      self.inventory.remove(item)
      time.sleep(1)
      print(item[0] + " was removed from your inventory.")
    keepLoop = True;
    while(keepLoop == True):
      i = input("Show inventory? 'y'/ 'n'")
      if (i == 'y'):
        self.displayInventory()
        keepLoop = False
      elif (i == 'n'):
        time.sleep(1)
        print("Moving on.")
        keepLoop = False
      else:
        time.sleep(1)
        print("I didn't catch that. Try another response.")
  def displayInventory(self):
    time.sleep(1)
    print("Your current inventory:")
    for i in range(len(self.inventory)):
      print(str(i) + ": " + self.inventory[i][0])

user = Player(10, [["stick", 2], ["apple", 0], ["key", 1]])

def randomItem():
  items = [
    ["rock", 2],
    ["large rock", 4],
    ["bag of pebbles", 1],
    ["wooden spear", 4],
    ["iron spear", 5],
    ["grappling hook", 2],
    ["arrow", 1],
    ["special arrow", 3],
    ["dagger", 3],
    ["flower petal", 0],
    ["rapier", 4],
    ["shoelace", 0],
    ["alchemist's fire", 6],
    ["grenade", 5],
    ["ninja star", 2],
    ["morning star", 6],
    ["axe", 5],
    ["potion of damaging", 7],
    ["dirt", 0],
    ["the excalibur", 100],
    ["glass shard", 1]
  ]
  randomNumber = random.randint(0, len(items) - 1)
  randomItem = items[randomNumber]
  time.sleep(1)
  print("You found " + randomItem[0] + "!")
  user.addInventory(True, randomItem)

class Monster:
  def __init__(self, name, hp, dmg, description, img):
    self.name = name
    self.hp = hp
    self.dmg = dmg
    self.description = description
    self.img = img
  def changeHp(self, amt):
    self.hp = self.hp + amt

monsters = [
  Monster("Goblin", 5, 1, "You encounter a Goblin! It attacks with a spiked club.", """
    .-"-.   
   /|6 6|\\ 
  {/(_0_)\\}
   _/ ^ \\_ 
  (/ /^\\ \\)-'
   ""' '""  
"""),
  Monster("Mimic", 5, 2, "You encounter a Mimic! It takes the form of banal items and catches you off guard.", """
  _____
 /     \\
|       |
|_______|
"""),
  Monster("Purple Worm", 3, 1, "You encounter a Purple Worm! It attacks by entering and infecting your veins, corrupting you from the inside out.", """

   o~~~~~~ 
"""),
  Monster("Car car", 10, 3, "You encounter a Car car! It transforms into a car and rolls around very smoothly.", r"""
       ______
      /|_||_\`.__
     (   _    _ _\
     =`-(_)--(_)-'
"""),
  Monster("Sapphire Dragon", 20, 4, "You encounter the Sapphire Dragon! It deals damage through shooting its scales, which are shards of crystal.", r"""
               ___====-_  _-====___
             _--^^^#####//      \\\\#####^^^--_
          _-^##########// (    ) \\\\##########^-_
         -############//  |\\^^/|  \\\\############-
       _/############//   (@::@)   \\\\############\\_
      /#############((     \\\\//     ))#############\\
     -###############\\\\    (oo)    //###############-
    -#################\\\\  / "" \\  //#################-
   -###################\\\\/  ()  \\//###################-
  _#/|##########/\\######(   ()   )######/\\##########|\\#_
 |/ |#/\\#/\\#/\\/  \\#/\\##\\  ()  //##/\\#/  \\/\\#/\\#/\\#| \\|
 `  |/  V  V  `   V  \\#\\| () |/#/  V   '  V  V  \\|  '
    `   `  `      `   / | () | \\   '      '  '   '
                     (  | () |  )
                    __\\ | () | /__
                   (vvv(-----)vvv)
"""),
  Monster("Vampire", 8, 3, "You encounter a Vampire! It sucks your blood.", r"""
          .-"".
       /       \
   __ /   .-.  .\
  /  `\  /   \/  \
  |  _ \/   .==.==.
  | (   \  /____\__\
   \ \      (_()(_()
    \ \            '---._
     \                   \_
  /\ |`       (__)________/
 /  \|     /\___/
|    \     \||VV
|     \     \|"",
|      \     ______)
\       \  /`
"""),
  Monster("Bull King", 15, 4, "You encounter the Bull King! It's giant axe is fatal upon strike.", r"""
          ,     .
        /(     )\               A
   .--.( `.___.' ).--.         /_\
   `._ `%_&%#%$_ ' _.'     /| <___> |\
      `|(@\*%%/@)|'       / (  |L|  ) \
       |  |%%#|  |       J d8bo|=|od8b L
        \ \$#%/ /        | 8888|=|8888 |
        |\|%%#|/|        J Y8P"|=|"Y8P F
        | (.".)%|         \ (  |L|  ) /
    ___.'  `-'  `.___      \|  |L|  |/
  .'#*#`-       -'$#*`.       / )|
 /#%^#%*_ *%^%_  #  %$%\    .J (__)
 #&  . %%%#% ###%*.   *%\.-'&# (__)
 %*  J %.%#_|_#$.\J* \ %'#%*^  (__)
 *#% J %$%%#|#$#$ J\%   *   .--|(_)
 |%  J\ `%%#|#%%' / `.   _.'   |L|
 |#$%||` %%%$### '|   `-'      |L|
 (#%%||` #$#$%%% '|            |L|
 | ##||  $%%.%$%  |            |L|
 |$%^||   $%#$%   |            |L|
 |&^ ||  #%#$%#%  |            |L|
 |#$*|| #$%$$#%%$ |\           |L|
 ||||||  %%(@)$#  |\\          |L|
 `|||||  #$$|%#%  | L|         |L|
      |  #$%|$%%  | ||l        |L|
      |  ##$H$%%  | |\\        |L|
      |  #%%H%##  | |\\|       |L|
      |  ##% $%#  | Y|||       |L|
      J $$#* *%#% L  |E/
      (__ $F J$ __)  F/
      J#%$ | |%%#%L
      |$$%#& & %%#|
      J##$ J % %%$F
       %$# * * %#&
       %#$ | |%#$%
       *#$%| | #$*
      /$#' ) ( `%%\
     /#$# /   \ %$%\
    ooooO'     `Ooooo)
    """),
  Monster("Unicorn", 6, 2, "You encounter a Unicorn! It's horn holds magical spells.", r"""
      \
       \   /-/--\
      (@~@)   )/\
  ___/--      \  |
 (oo)__ _      )_/
  ^^___/       \
        \       |/-\
         (      )   |
         |       \_/ 
"""),
  Monster("Fire Dragon", 8, 3, "You encounter the Fire Dragon! It has wings of fire and burning claws.", r"""
               \                  /
    _________))                ((__________
   /.-------./\\    \    /    //\.--------.\
  //#######//##\\   ))  ((   //##\\########\\
 //#######//###((  ((    ))  ))###\\########\\
((#######((#####\\  \\  //  //#####))########))
 \##' `###\######\\  \)(/  //######/####' `##/
  )'    ``#)'  `##\`->oo<-'/##'  `(#''     `(
          (       ``\`..'/''       )
                     \""(
                      `- )
                      / /
                     ( /\
                     /\| \
                    (  \
                        )
                       /
                      (
                      `   
  """),
    Monster("Iguana", 5, 1, "You encounter an Iguana! Its camouflaging abilities make it difficult to attack.", r"""
              _,\,\,\|\|\|\|\|\|\|\/-\___.._
     __,-'                           () .\
    /  __/---\___                __   ---/
   |  /          \ \___________/\\  \___/
   | |            \ \            \\
   | |            / |             \\__/_
   | |            | \/_              /\
    ||             \--\
     ||
      \\_______
       \-------\\____
       """),
    Monster("Sabertooth", 6, 2, "You encounter a Sabertooth! Beware of its piercing fangs!", r"""
                 /\
            ( ;`~v/~~~ ;._
         ,/'"/^) ' < o\  '".~'\\\--,
       ,/",/W  u '`. ~  >,._..,   )'
      ,/'  w  ,U^v  ;//^)/')/^\;~)'
   ,/"'/   W` ^v  W |;         )/'
 ;''  |  v' v`" W }  \\
"    .'\    v  `v/^W,) '\)\.)\/)
         `\   ,/,)'   ''')/^"-;'
              \
            ".
           \  
    """),
    Monster("Dark Knight", 7, 3, "You encounter the Dark Knight! Be mindful of his silver sword and armour!", r"""
      ,/         \.
 ((           ))
  \`.       ,'/
   )')     (`(
 ,'`/       \,`.
(`-(         )-')
 \-'\,-'"`-./`-/
  \-')     (`-/
  /`'       `'\
 (  _       _  )
 | ( \     / ) |
 |  `.\   /,'  |
 |    `\ /'    |
 (             )
  \           /
   \         /
    `.     ,'
      `-.-'
"""),
    Monster("Centaur", 9, 2, "You encounter a Centaur! Beware of its spear!", r"""
      <=======]}======
    --.   /|
   _\"/_.'/
 .'._._,.'
 :/ \{}/
(L  /--',----._
    |          \\
   : /-\ .'-'\ / |
    \\, ||    \|
     \/ ||    ||
    """),
    Monster("Minatour", 8, 2, "You encounter a Minatour! Beware of its dagger!", r"""
     .      .
     |\____/|
    (\|----|/)
     \ 0  0 /
      |    |
   ___/\../\____
  /     --       \
 /  \         /   \
|    \___/___/(   |
\   /|  }{   | \  )
 \  ||__}{__|  |  |
  \  |;;;;;;;\  \ / \_______
   \ /;;;;;;;;| [,,[|======'
     |;;;;;;/ |     /
     ||;;|\   |
     ||;;/|   /
     \_|:||__|
      \ ;||  /
      |= || =|
      |= /\ =|
      /_/  \_\
    """),
    Monster("Twin Ghosts", 5, 3, "You encounter Twin Ghosts! Double the trouble!", r"""
        ___
      _/ @@\
     ( \  O/__
      \    \__)
      /     \
     /      _\
    `""``""``""
        ___
      _/  "\
     ( \  ~/__
      \    \__)
      /     \
jgs  /      _\
    `""``""``""
    """),
    Monster("Devil", 7, 3, "You encounter the Devil! Although it seems he lost his pitchfork...", r"""
  *                       *
    *                 *
   )       (\___/)     (
* /(       \ (. .)     )\ *
  # )      c\   >'    ( #
   '         )-_/      '
 \\|,    ____| |__    ,|//
   \ )  (  `  ~   )  ( /
    #\ / /| . ' .) \ /#
    | \ / )   , / \ / |
     \,/ ;;,,;,;   \,/
      _,#;,;;,;,
     /,i;;;,,;#,;
    //  %;;,;,;;,;
   ((    ;#;,;%;;,,
  _//     ;,;; ,#;,
 /_)      #,;    ))
         //      \|_
         \|_      |#\
          |#\      -"
 """),
    Monster("Flower Fairies", 5, 2, "You encounter the Flower Fairies! They peacefully tend to their flowers...", r"""
                       _()/^)
   (^\()_               _)\<
    >/(_     _.-.-.       \\)_
   (/\\     (_\_|_/_)      \  `
     /|    (__>(@)<__)     `
     ``     (_/^|^\_)
              '-'-'#,  _/\
                   `# / _/
               |\_ ,#|/_/
               \ \|#'
                `-#' /|
               /\_# | /_
               \_.|#,__/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""),
    Monster("Gryphon", 7, 3, "You encounter a Gryphon! It seems to be looking for its child...", r"""
                          ______
             ______,---'__,---'
         _,-'---_---__,---'
  /_    (,  ---____',
 /  ',,   `, ,-'
;/)   ,',,_/,'
| /\   ,.'//\
`-` \ ,,'    `.
     `',   ,-- `.
     '/ / |      `,         _
     //'',.\_    .\\      ,{==>-
  __//   __;_`-  \ `;.__,;'
((,--,) (((,------;  `--' 
```  '   ```
"""),
    Monster("Gryhon Baby", 3, 1, "You encounter a Gryphon Baby! It seems to be looking for its mother...", r"""
   ____       ____
  /    )     (    \
 /    (  ^_^  )    \
|  {   \('v')/   }  |
|   {   /   \   }   |
|_)(   /\   /\   )(_|
|)  (_ | \|/  |_)  (|
'     "--^^^^--"    '
"""),
    Monster("Mr. Skull", 5, 2, "You encounter Mr. Skull! Rattle rattle!", r"""
      .-.
     (o.o)
      |=|
     __|__
   //.=|=.\\
  // .=|=. \\
  \\ .=|=. //
   \\(_=_)//
    (:| |:)
     || ||
     () ()
     || ||
     || ||
    ==' '==
"""),
    Monster("The Ashen Dragon", 30, 4, "This ancient dragon has been awakened after centuries of sleep.", r"""
                             'X)                                            
                              )|                                            
                              )|                                            
                             _)|                                            
                             )||                                  /X`       
                            _)||                                 //(        
                           _) ||                                // (        
                          _)  ||                               // (         
                         _)   ||                              //  (         
                       __)    ||                             //   (         
                     __)      ||                            //    /         
                     )        ||                           //    (          
                   'X\        ||                          //     (          
                    )\\       ||                         //      (          
                    ) \\      ||                        //       /          
                     ) \\     ||                       //       (           
                     )  \\    ||                      //        (           
                      \  \\   ||                     //         (_          
                       )  \\  ||                    //           (_         
                        )  \\ ||                   //             (_        
                        \   \\||                  //                \       
                         )   >. )               _/(__________________X`     
                         \  //||               (  .------------------.>     
                         _)// ||                )/\\             __.-'      
                        _)//  ||               //  \\          _(           
                        )//.. ||              //    \\       _(             
                        X/'  \||             //      \\     (               
           __   _____,_,,_,,,,||            //        \\   (                
         .-` \_/.-._______)   )|           //.--------.\\ (                 
         `  `-- )        /  \'||   .--.__.//'-.________`\X'                 
               '        (   ,)||  <\--<_(//-/> \       `.                   
                         \ /(\||  /   ^.'/_/(\  \        `.                 
                         (   \|`./  ^.' /<   .-  \/\___    \                
                          \ |/) | ^ /  /  \ /    /( \  `-.  \               
                          ( `/  ^  ^   (  \/>   /(   \    \  \              
                           >--) ^  L/     \(   /(     )    )  )             
                        .(\  / ^/)/ \   ( / \ ((     /    /  /              
                      .'  )\/ ^/(/  (    \)  `-\\   /\   /  /               
                     /    > ^   /,   |  //      `\   /  ( .'                
                    /    (=  =)).'  /  //,        ) (    \`.                
                   /  ,  <, ,_>/    > '/',       /   >    \ )               
                   ) '  _/ /\>'    / ~ )'    ___/ _>'     (/                
                  /  .-(^-^)/}-.  / / /     (---. `--.                      
                 /  (  (-^-(/   ) \' /       `   \ \--)                     
                /  /    )   )   ._/ /             `-)'                      
                ) /    (   (   (-^. \-._           '                        
               /  >             `  \)`--)                                   
              (   `--.             '   '                       
              / />----)                                                     
             / /\)   '                                                      
            (-'  `                                                          
             `
  """)
]

class Event:
  def __init__(self, name, hp, description):
    self.name = name
    self.hp = hp
    self.description = description

badEvents = [
  Event("Hail of poisoned darts", -4, "Out of nowhere rains a Hail of poisoned darts! You are pierced and poisoned."),
  Event("Disguised pit", -2, "The ground below your feet is no longer there. You have fallen into a Disguised pit."),
  Event("Gout of white flame", -3, "Out of nowhere shoots a Gout of white flame, burning away layers of your skin.")
]

goodEvents = [
  Event("Fountain of youth", 3, "Behind a rotting brick wall covered in vines, you find a Fountain of Youth. You dip your hands in for a sip of the sacred water."),
  Event("Ancient Druid Circle", 5, "You find that you've stepped in a glowing ring of light. You are in an Ancient Druid Circle left behind from countless centuries before. "),
  Event("Chalice of Moon", 5, "Hidden behind rubble, there is a Chalice of Moon, a goblet filled with shimmering moon essence. You from the goblet."),
  Event("Wellspring Altar", 4, "You find the Wellspring Altar, a sacred pool infused with divine energy, guarded by spirits who only allow the righteous to bathe in its waters. You go for a swim.")
]

def randomEvent(eventArray):
  rand = random.randint(0, len(eventArray) - 1)
  chosenEvent = eventArray[rand]
  print(chosenEvent.description)
  user.changeHp(chosenEvent.hp)

#combat mode
def combat(idx):
  #access the Monster object from the array depending on index
  monster = monsters[idx]
  time.sleep(1)
  print(monster.description)
  time.sleep(1)
  print("YOU ARE FIGHTING " + monster.name + "!")
  print(monster.img)
  while(monsters[idx].hp > 0 and user.health > 0):
    time.sleep(1)
    #player turn
    time.sleep(1)
    print("YOUR TURN:")
    print("Type '1' for kick")
    print("Type '2' to punch")
    print("Type '3' to access inventory")
    choice = input("Type here: ")
    totalDmg = 0;
    if(choice == '1' or choice == '2'):
      totalDmg = random.randint(2,5)
    elif(choice == '3'):
      if(user.inventory == []):
        time.sleep(1)
        print("Your inventory is empty.")
      else:
        user.displayInventory()
        item = input("Type # of item you would like to use (one-use): ")
        item = user.inventory[int(item)]
        totalDmg = item[1]
        user.addInventory(False, item)
        time.sleep(1)
        print("You use " + item[0] + "!")
    #1/5 chance for critical hit-double dmg
    rand = random.randint(1,5)
    if(rand == 2):
      totalDmg *= 2
      time.sleep(1)
      print("CRITICAL HIT! x2 DAMAGE!")
    monsters[idx].changeHp(-totalDmg)
    time.sleep(1)
    print("You deal " + str(abs(totalDmg)) + " dmg!")
    if(monsters[idx].hp <= 0):
      time.sleep(1)
      print("You have defeated " + monster.name + "!")
      break
    time.sleep(1)
    print("MONSTER TURN:")
    time.sleep(1)
    print(monster.name + " deals " + str(monster.dmg) + " dmg! Ouch!")
    user.changeHp(-monster.dmg)
    if(user.health <= 0):
      time.sleep(1)
      print("You been defeated by " + monster.name + ".")
      break

def game():
  escaped = False
  print("Game start!")
  print("Welcome! You are in a dungeon! Try to find the hidden room!")
  while escaped == False:
    choice = input("Which direction would you like to turn? 'Left' or 'Right'? ")
    if (choice == "Left"):
      print("Left...")
      second_choice = input("Which direction would you like to go? 'Forward' or 'Right'? ")
      if second_choice == "Forward":
        print("Forward...")
        third_choice = input("Would you like to 'Turn' or go 'Forward' and open the door? ")
        if third_choice == "Forward":
          print("Forward...")
          print("You have found the hidden room!")
          entrance_puzzleroom()
          escaped = True
        elif third_choice == "Turn":
          print("Turning...")
          print("You have hit a dead end!")
          combat(random.randint(0, len(monsters) - 2))
      elif second_choice == "Right":
        print("Right...")
        print("You have hit a dead end!")
        isGoodEvent = random.randint(0, 1)
        if (isGoodEvent == 0):
          randomEvent(goodEvents)
        else:
          randomEvent(badEvents)
    elif (choice == "Right"):
      print("Right...")
      print("You have hit a dead end!")
      randomItem()

def entrance_puzzleroom():
  Puzzleroom= input("Do you want to enter the hidden puzzle room for bonus items?: 'y'/ 'n'")
  if (Puzzleroom== "y"):
    puzzle_room()##make puzzleroom function
  elif(Puzzleroom== "n"):
    mazefn()
  else:
    print("I didn't catch that. Try another response.")
    entrance_puzzleroom() 

def puzzle_room():
  print("You have entered the puzzle room.")
  score = 0
  puzzle_checker = input ("Are you sure you want to partake in the puzzle room and win prizes? (y/n)")
  puzzle_game = False
  aces = False
  if puzzle_checker == "y":
    puzzle_game = True
    aces = False
  else:
    mazefn()
  while puzzle_game == True:
    Question_1 = True
    Question_2 = False
    Question_3 = False
    Question_4 = False
    print ("Within the puzzle room, you will be asked numerous true or false questions and will receive a prize at the end of your quiz, if you get all of your questions correct. Your first question will be shown shortly.")
    while Question_1 == True:
      Q1 = input("2+2 = 4 (T/F)")
      if Q1 == "T":
        Question_1 = False
        Question_2 = True
        score +=1
      else:
        puzzle_game = False
    while Question_2 == True:
      Q2 = input("Napoleon Bonaparte died at the battle of Waterloo. (T/F)")
      if Q2 == "F":
        score+=1
        Question_2 = False
        Question_3 = True
      else:
          puzzle_game = False
    while Question_3 == True:
      Q3 = input("Octopi have three hearts, nine brains, and blue blood. (T/F)")
      if Q3 == "T":
        Question_3 = False
        Question_4 = True
        score+=1
      else:
        puzzle_game = False
    while Question_4 == True:     
      Q4 = input("Christian Skinner set the world record for longest yell of the word 'goal', at 42.56 seconds. (T/F)")
      if Q4 == "F":
        Question_4 = False
        score+=1
        aces = True
        puzzle_game = False
      else:
        puzzle_game = False
  
  if puzzle_game == False and aces == False:
    print("Nice try buddy, but you failed. Your final score was: "+ str(score))
    print("You're being sent to the maze.")
    mazefn()
  if puzzle_game == False and aces == True:
    print("Holy moly, you're a genius! You got every single question correct! Your prize for beating the puzzle_game is…a rock. Yeah, its a nice, shiny rock.")
    user.addInventory(True, ["shiny rock", 15])
    print("Good luck friend, you're going to be sent to the maze.")
    print("Believe me, you'll need it.")
    mazefn()

def mazefn():
  print("You have entered ze maze.")
  startmaze()
  
def boss():
  print("You have made it to the final battle. Will you survive?")
  time.sleep(1)
  print("Drink this potion; you will need it.")
  user.changeHp(10)
  combat(len(monsters) - 1)
  time.sleep(1)
  print("Wow! That was unexpected...")
  time.sleep(1)
  print("Congratulations on beating Ashen Catacombs. We hope you enjoyed the game!")

menu()