def hangman_2():
  import random
  from google.colab import output
  coding = ["python","coding","script","program","programatically","algorithm","code","developer","frontend","backend","server"]
  solar_system = ["sun","mercury","venus","earth","mars","jupiter","saturn","uranus","neptune","pluto","eris","makemake","haumea","ceres","gonggong","sedna","quaoar","goblin","moon","phobos","deimos","io","europa","ganymede","callisto","mimas","enceladus","tethys","rhea","titan","lapetus","hyperion","oberon","titanus","triton","charon"]
  astronomy = ["space","astronomy","nebula","constellation","star","supernova","galaxy","planet","exoplanet","asteroid","comet","moon","exomoon","matter","universe","cluster","distance","blackhole","neutronstar","whitedwarf","supernovaremanant",*solar_system]
  shapes = ["trangle","square","pentagon","hexagon","heptagon","octagon","nonagon","decagon","circle","oval","cube","pyramid","cuboid","rectangle","sphere","ellipse"]
  earth_sciences = ["geology","geography","biology","biogeography","oceanography","evolution","rocks","adaptation","environment","life","science","climate","temperature","habitat","aerodynamic","atmosphere","pollution"]
  sciences = ["learning","world","experimentation","research","areography","paleontology","entomology","scientist","paleobiogeography","astrobiogeography","astrobiology","zoology","ecology","history","math",*earth_sciences,*astronomy]
  words = ["able","about","account","bend","glasses","optics","lens","evolution","microscope","huge","massive","titanic","giant","think","made","make","drive","tube","till","tip","zipper","bomb","flash","boom","bought","rot","for","can","bear","desktop","mouse","voice","am","lot","coordinate","human","cream","sort","soft","site","food","factor","arm","near","far","side","out","outside","in","inside","crack","acid","real","shine","complicated","fish","project","philosophy","mind","truck","car","magic","laptop","tablet","phone","watch","scale","pencil","pen","glass","table","window","door","ethic","thought","term","vegetable","fruit","object","cell","basic","empire","eye","nose","ear","hand","cloud","belt","leg","blue","glucose","water","lava","ice","magma","smell","brain","photosynthesis","garden","anatomy","physiology","asteroid","comet","bank","green","lime","lemon","violet","across","act","air","all","website","popular","national","destruction","tough","release","community","literature","english","adjective","verb","adverb","noun","cow","grass","plant","true","sloth","deer","tooth","tommorow","truth","town","toe","multiplier","coefficient","black","protien","supernova","sugar","flower","flour","nebula","space","allow","almost","oxygen","hydrogen","helium","sulfur","neptune","saturn","mercury","mars","jupiter","uranus","pluto","ceres","vesta","chemical","compound","century","decade","eon","era","an","alone","along","among","amount","amusement","and","angle","angry","animal","answer","ant","any","apparatus","addition","adjustment","advertisement","after","again","against","agreement","altitude","ark","art","anvil","alphabets","code","mail","hangman","game","colaboration","onomatopoeia","internationalisation","fly","podcast","crepuscular","antidisestablishmentarianism","hippopotomonstrosesquippedaliophobia","pneumonoultramicroscopicsilicovolcanoconiosis","apple","orange","pear","map","rainforest","desert","sea","ocean","python","life","nature","astronomy","bark","master","cat","tiger","dog","planets","star","card","money","cash","legacy","cancer","constellations","effect","programatically","science","biology","hack","rat","tree","climate","young","yesterday","today","day","sun","hot","cold","warm","warning","light","dark","purple","red","yellow","earth","wood","wise","old","worn","new","what","why","the","introvert","work","woman","worm","venus","year","yes","how","juice","ireland","land","would","should","shout","loud","quiet","noise","physics","math","to","together","heart","loom","write","language","zoom","zone"]
  long_words = ["pneumonoultramicroscopicsilicovolcanoconiosis","supercalifragilisticexpialidocious","hippopotomonstrosesquippedaliophobia","antidisestablishmentarianism","floccinaucinihilipilification","honorificabilitudinitatibus","pseudopseudohypoparathyroidism","incomprehensibilities","dichlorodiphenyltrichloroethane","methionylthreonylthreonylglutaminylarginyltyrosylglutaminylarginylisoleucine","internationalisation","myxococcusllanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogochensis","sexmillia­quingent­sexagin­tillion","lopado­temacho­selacho­galeo­kranio­leipsano­drim­hypo­trimmato­silphio­karabo­melito­katakechy­meno­kichl­epi­kossypho­phatto­perister­alektryon­opte­kephallio­kigklo­peleio­lagoio­siraio­baphe­tragano­pterygon"]
  categories = {"coding" : coding,"solar system" : solar_system,"astronomy" : astronomy,"shapes" : shapes,"random words" : words, "earth science" : earth_sciences,"sciences" : sciences,"longest words" : long_words}
  category = ""
  print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
  print('''Options:
1. Coding
2. Solar System
3. Astronomy
4. Shapes
5. Random Words
6. Earth Sciences
7. Sciences
8. Long Words''')

  choice = input("Which one would you like? ").lower()
  if choice == "coding" or choice == "1":
    category = "coding"
    word = random.choice(coding)
  elif choice == "solar system" or choice == "2":
    category = "solar system"
    word = random.choice(solar_system)
  elif choice == "astronomy" or choice == "3":
    category = "astronomy"
    word = random.choice(astronomy)
  elif choice == "shapes" or choice == "4":
    category = "shapes"
    word = random.choice(shapes)
  elif choice == "random words" or choice == "5":
    category = "random words"
    word = random.choice(words)
  elif choice == "earth sciences" or choice == "6":
    category = "earth sciences"
    word = random.choice(earth_sciences)
  elif choice == "sciences" or choice == "7":
    category = "sciences"
    word = random.choice(sciences)
  elif choice == "long words" or choice == "8":
    category = "long words"
    word = random.choice(long_words)
  else:
    print("Error 404: list not found")
    return
  HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
  chances = 6
  found = 0
  guessed = []
  letters_found = []
  print(len(word)*" _")
  while chances > 0:
    guess = input("Guess a letter : ")
    if guess.lower() in word and guess.lower() not in letters_found:
      letters_found.append(guess.lower())
      print("Correct!")
      output.clear()
      print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
      print(category)
      if chances == 6:
        print(HANGMANPICS[0])
      elif chances == 5:
        print(HANGMANPICS[1])
      elif chances == 4:
        print(HANGMANPICS[2])
      elif chances == 3:
        print(HANGMANPICS[3])
      elif chances == 2:
        print(HANGMANPICS[4])
      elif chances == 1:
        print(HANGMANPICS[5])
      elif chances == 0:
        print("You lost!")
        print(HANGMANPICS[6])
        print(f"The word was {word} and in category {category}")
        break
      for n in word:
        if n.lower() in letters_found:
          print(" "+n,end='')
        else:
          print(" _",end='')
      print("")
      found += word.count(guess)
      if found == len(word):
        print("You won!")
        print(f"In category {category}")
        break
    elif guess.lower() in letters_found:
      print("Already guessed!")
    else:
      chances -= 1
      if chances == 6:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print(category)
        print(HANGMANPICS[0])
      elif chances == 5:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print(category)
        print(HANGMANPICS[1])
      elif chances == 4:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print(HANGMANPICS[2])
      elif chances == 3:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print(category)
        print(HANGMANPICS[3])
      elif chances == 2:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print(category)
        print(HANGMANPICS[4])
      elif chances == 1:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || | 
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print(category)
        print(HANGMANPICS[5])
      else:
        output.clear()
        print(''' _                                               _  _
| |                                             | || |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   | || |
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | || |
| | | | (_| | | | | (_| | | | | | | (_| | | | | | || |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |_||_|
                    __/ |
                   |___/ ''')
        print("You lost!")
        print(HANGMANPICS[6])
        print(f"The word was {word} and in category {category}")
        break
      print(f"You have {chances} chances left!")
      for n in word:
        if n.lower() in letters_found:
          print(" "+n,end='')
        else:
          print(" _",end='')
      print("")
hangman_2()
