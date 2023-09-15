import os, time, sys, random, socket

run = True
menu = True
key = False
play = False
twoatks = "0"
threeatks = "0"
fouratks = "0"
skta = False
prices_better = "0"
hp2x = "0"
at2x = "0"
st2x = "0"
symbol_lost = "▯"
symbol_remaining = "▮"
symbol_lost_xp = "▯"
symbol_remaining_xp = "▮"
#▮▯

name = "NIL"
HP = 25
ATK = 5
pot = 3
gold = 0
x = 0
y = 0
elix = 0
spot = 1
HPMAX = 25
kills = 0
difficulty = "Null"
level = 0
exp = 0
totalexp = 0
STAM = 50
MAXSTAM = 50
SKPTS = 0
placeholderbool = False
placeholderint = 0
stamcap = 100
hpcap = 150
atcap = 25
expreq = 100
max_exp = expreq
bars = 25
current_hp = HP
symbol = "█"

color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_blue2 = "\33[36m"
color_blue3 = "\33[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\33[33m"
color_yellow = "\33[93m"
color_grey = "\33[37m"
color_default = "\033[0m"
health_color = color_green2
health_color1 = color_green1

def print_variable_name(variable: object) -> None:
    for name, value in globals().items():
        if id(value) == id(variable):
            return name

def hpbar():
    global health_color
    remaining_HP_bars = round(HP / HPMAX * bars)
    lost_HP_bars = bars - remaining_HP_bars

    print(f" HP: {HP} / {HPMAX}")
    print(f"|{health_color}{remaining_HP_bars * symbol_remaining}"
          f"{lost_HP_bars * symbol_lost}{color_default}|")

    if HP > 0.50 * HPMAX:
        health_color = color_green1
    elif HP > 0.2511 * HPMAX:
        health_color = color_yellow
    else:
        health_color = color_red

def expbar():
    remaining_exp_bars = round(exp / max_exp * bars)
    lost_exp_bars = bars - remaining_exp_bars

    print(f"EXP: {exp} / {expreq}")
    #print(f"EXP: |{remaining_exp_bars*symbol_remaining_xp}{lost_exp_bars*symbol_lost_xp}|")
    print(f"|{color_blue1}{remaining_exp_bars * symbol_remaining}"
          f"{lost_exp_bars * symbol_lost}{color_default}|")
    

def stambar():
    global health_color
    remaining_stam_bars = round(STAM / MAXSTAM * bars)
    lost_stam_bars = bars - remaining_stam_bars

    print(f"STAMINA: {STAM} / {MAXSTAM}")
    print(f"|{color_green2}{remaining_stam_bars * symbol_remaining}"
          f"{lost_stam_bars * symbol_lost}{color_default}|")

def heal(amount):
    global HP, STAM
    if HP + amount < HPMAX:
        HP += amount
    else:
        HP = HPMAX
    if STAM + amount < MAXSTAM:
        STAM += amount
    else:
        STAM = MAXSTAM
    print(name + "'s HP refilled to " + str(HP) + "!")
    print(name + "'s STAMINA refilled to " + str(STAM) + "!")
    input("> ")

mobs = {
    "Gladiator": {
        "hp": 25,
        "at": 3,
        "go": 12,
        "xp": 20
    },
    "Wolf": {
        "hp": 15,
        "at": 6,
        "go": 12,
        "xp": 20
    },
    "Tiger": {
        "hp": 30,
        "at": 5,
        "go": 13,
        "xp": 30
    },
    "Lion": {
        "hp": 60,
        "at": 8,
        "go": 12,
        "xp": 10
    },
    "Snake": {
        "hp": 20,
        "at": 4,
        "go": 12,
        "xp": 15
    },
    "Gladiator Cavalry": {
        "hp": 20,
        "at": 4,
        "go": 12,
        "xp": 20
}
}

mobs_shard = {
    "gladiator": {
        "hp": 30,
        "at": 6,
        "go": 8,
        "xp": 50
    },
    "wolf": {
        "hp": 30,
        "at": 6,
        "go": 11,
        "xp": 75
    },
    "tiger": {
        "hp": 45,
        "at": 3,
        "go": 13,
        "xp": 100
    },
    "lion": {
        "hp": 45,
        "at": 5,
        "go": 15,
        "xp": 50
    },
    "snake": {
        "hp": 40,
        "at": 3,
        "go": 18,
        "xp": 35
    },
    "Gladiator cavalry": {
        "hp": 30,
        "at": 4,
        "go": 20,
        "xp": 55
}
}

attackl = {
    "Rip and Tear": {
        "atk": 50,
        "stam": 50
    },
    "Ember": {
        "atk": 15,
        "stam": 40
    },
    "Kick": {
        "atk": 10,
        "stam": 30
    },
    "Flame": {
        "atk": 15,
        "stam": 40
    },
    "Spark": {
        "atk": 30,
        "stam": 40
    },
    "Scratch": {
        "atk": 10,
        "stam": 35
    },
    "Fire Breath": {
        "atk": 25,
        "stam": 35
    },
    "Ice Breath": {
        "atk": 25,
        "stam": 40
    },

}

def clear():
    os.system("cls")

def draw():
    print("xX--------------------xX")

attacks = ["Ember", "Kick", "Flame", "Scratch", "Ember", "Kick", "Flame", "Spark", "Scratch", "Fire Breath", "Ice Breath", "Ember", "Kick", "Flame", "Spark", "Scratch", "Fire Breath", "Ice Breath", "Ember", "Kick", "Flame", "Spark", "Scratch", "Fire Breath", "Ice Breath", "Ember", "Kick", "Flame", "Spark", "Scratch", "Fire Breath", "Ice Breath", "Rip & Tear",  "Kick",  "Kick",  "Kick", "Scratch", "Scratch", "Scratch", "Rip and Tear"]

e_list_easy = ["Gladiator Cavalry", "Snake", "Lion", "Tiger", "Wolf", "Gladiator", "Gladiator"]
e_list_shard = ["Gladiator cavalry", "snake", "lion", "tiger", "wolf", "gladiator", "gladiator"]

def gladarena():
    global fight, play, run, HP, pot, elix, gold, boss, kills, spot, enemy, difficulty, level, exp, totalexp, STAM, health_color1

    fight = True

    attacks_got1 = random.choice(attacks)
    if twoatks == "1":
        attacks_got2 = random.choice(attacks)
    if threeatks == "1":
        attacks_got3 = random.choice(attacks)
    if fouratks == "1":
        attacks_got4 = random.choice(attacks)

    if difficulty == "SHard":
        enemy = random.choice(e_list_shard)
    if difficulty == "Easy":
        enemy = random.choice(e_list_easy)
    if difficulty == "SHard":
        hp = mobs_shard[enemy]["hp"]
        hpmax = hp
        atk = mobs_shard[enemy]["at"]
        g = mobs_shard[enemy]["go"]
        xp = mobs_shard[enemy]["xp"]
    elif difficulty == "Easy":
        hp = mobs[enemy]["hp"]
        hpmax = hp
        atk = mobs[enemy]["at"]
        g = mobs[enemy]["go"]
        xp = mobs[enemy]["xp"]
        
        if level >= 1:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 2:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 3:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 4:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 5:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 6:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 7:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 8:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 9:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 10:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 11:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 12:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 13:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 14:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 15:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 16:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 17:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 18:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 19:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 20:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 21:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 22:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 23:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 24:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 25:
            hp += 15
            hpmax += 15
            atk += 15
        if level >= 26:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 27:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 28:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 29:
            hp += 5
            hpmax += 5
            atk += 10
        if level >= 30:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 31:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 32:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 33:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 34:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 35:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 36:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 37:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 38:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 39:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 40:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 41:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 42:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 43:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 44:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 45:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 46:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 47:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 48:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 49:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 50:
            hp += 100
            hpmax += 100
            atk += 100
        if level >= 51:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 52:
            hp += 5
            hpmax += 5
            atk += 5
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 53:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 54:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 55:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 56:
            hp += 5
            hpmax += 5
            atk += 5
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 57:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 58:
            hp += 5
            hpmax += 5
            atk += 5
        if level >= 59:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 60:
            hp += 10
            hpmax += 10
            atk += 10
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 61:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 62:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 63:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 64:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 65:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 66:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 67:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 68:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 69:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 70:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 71:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 72:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 73:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 74:
            hp += 10
            hpmax += 10
            atk += 10
        if level >= 75:
            hp += 100
            hpmax += 100
            atk += 100
        if level > 76:
            hp += 100
            hpmax += 100
            atk += 100

    while fight:
        clear()
        draw()
        print("Defeat the " + enemy + "!")
        draw()
        remaining_hp_bars = round(hp / hpmax * bars)
        lost_hp_bars = bars - remaining_hp_bars

        print(f"ENEMY HP: {hp} / {hpmax}")
        print(f"|{health_color1}{remaining_hp_bars * symbol_remaining}"
            f"{lost_hp_bars * symbol_lost}{color_default}|")

        if hp > 0.66 * hpmax:
            health_color1 = color_green1
        elif hp > 0.33 * hpmax:
            health_color1 = color_yellow
        else:
            health_color1 = color_red
        hpbar()
        stambar()
        print("POTIONS: " + str(pot))
        print("SUPER POTIONS: " + str(spot))
        print("ELIXIR: " + str(elix))
        draw()
        print("1 - ATTACK (Based On Attack)")
        print("2 - ATTACK (" + attacks_got1 + ")")
        if twoatks == True:
            print("3 - ATTACK (" + attacks_got2 + ")")
        else:
            print("3 - LOCKED")
        if threeatks == True:
            print("4 - ATTACK (" + attacks_got3 + ")")
        else:
            print("4 - LOCKED")
        if fouratks == True:
            print("5 - ATTACK (" + attacks_got4 + ")")
        else:
            print("5 - LOCKED")
        if pot > 0:
            print("6 - USE POTION (30HP - 30STAM)")
        if elix > 0:
            print("7 - USE ELIXIR (100HP - 100STAM)")
        if spot > 0:
            print("8 - USE SUPER POTION (50 HP - 50STAM)")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy + ".")
            if hp > 0:
                HP -= atk
                print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            input("> ")
        if choice == "2":
            if attacks_got1 == "Rip and Tear":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Rip and Tear"
                hp -= attackl[spell]["atk"]
                STAM -= attackl[spell]["stam"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Scratch":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Scratch"
                hp -= attackl[spell]["atk"]
                STAM -= attackl[spell]["stam"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Flame":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Flame"
                hp -= attackl[spell]["atk"]
                STAM -= attackl[spell]["stam"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Fire Breath":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Fire Breath"
                hp -= attackl[spell]["atk"]
                STAM -= attackl[spell]["stam"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Ice Breath":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Ice Breath"
                hp -= attackl[spell]["atk"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Kick":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Kick"
                hp -= attackl[spell]["atk"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Ember":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Ember"
                hp -= attackl[spell]["atk"]
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".")
            if attacks_got1 == "Spark":
                if STAM <= 0:
                    print("You collapse from exhaustion")
                    input("> ")
                    break
                spell = "Spark"
                hp -= attackl[spell]["atk"] 
                if hp > 0:
                    HP -= atk
                    print(enemy + " dealt " + str(atk) + " damage to " + name + ".") 
        if twoatks == True:       
            if choice == "3":
                if attacks_got1 == "Rip and Tear":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Rip & Tear"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Scratch":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Scratch"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Flame":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Flame"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Fire Breath":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Fire Breath"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Ice Breath":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        break
                    spell = "Ice Breath"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Kick":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Kick"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Ember":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Ember"
                    hp -= attackl[spell]["atk"]
                    STAM -= attackl[spell]["stam"]
                if attacks_got1 == "Spark":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Spark"
                    hp -= attackl[spell]["atk"]
        if threeatks == True:
            if choice == "4":
                if attacks_got1 == "Rip and Tear":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Rip & Tear"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Scratch":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Scratch"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Flame":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Flame"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Fire Breath":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Fire Breath"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Ice Breath":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Ice Breath"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Kick":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        input("# ")
                        break
                    spell = "Kick"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Ember":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Ember"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Spark":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Spark"
                    hp -= attackl[spell]["atk"]
        if fouratks == True:
            if choice == "5":
                if attacks_got1 == "Rip and Tear":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Rip & Tear"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Scratch":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Scratch"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Flame":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Flame"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Fire Breath":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Fire Breath"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Ice Breath":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Ice Breath"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Kick":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        input("# ")
                        break
                    spell = "Kick"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Ember":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Ember"
                    hp -= attackl[spell]["atk"]
                if attacks_got1 == "Spark":
                    if STAM <= 0:
                        print("You collapse from exhaustion")
                        input("> ")
                        break
                    spell = "Spark"
                    hp -= attackl[spell]["atk"]
        if choice == "6":
            if pot >= 1:
                heal(30)
            else:
                print("No Potions")
        if choice == "7":
            if spot >= 1:
                heal(50)
            else:
                print("No Super Potions")
        if choice == "8":
            if elix >= 1:
                heal(100)
            else:
                print("No Elixers")      
        if STAM <= 0:
            print("you collapse from exhaustion")
            input("> ")
            STAM = 0
            break
        if HP <= 0:
            print(enemy + " defeated " + name + "...")
            draw()
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
        if hp <= 0:
            print(name + " defeated the " + enemy + "!")
            draw()
            fight = False
            gold += g
            print("You've found " + str(g) + " gold!")
            kills += 1
            print("You now have " + str(kills) + " kills!")
            exp += xp
            totalexp += xp
            print("You have recieved " + str(xp) + " exp!")
            print("You now have " + str(totalexp) + " total exp!")
            if random.randint(1, 2) == 2:
                pot += 1
                print("You've found a potion!")
            if random.randint(-100, 200) < -50:
                pot += 5
                print("You've found 5 potions, Rare")
            if random.randint(-100, 99) < -50:
                elix += 1
                print("You've found 1 elixer, nice")
            if random.randint(0, 1000000) == 69420:
                elix += 100
                pot += 100
                spot += 100
                print("This is a one in 1000000 chance to happen, for example you have a 3153 percent higher chance to get struck by lightning.")
                print("You found 100 elixers, 100 potions and 100 super potions")
            input("> ")
            clear()

def skt():
    save()
    global skta, SKPTS, ATK, HPMAX, HP
    while skta == True:
        draw()
        print("SKILL POINTS: " + str(SKPTS))
        print("LEVEL: " + str(level))
        if level >= 1:
            print("1 - 2x Attack")
        else:
            print("Reach level 1 to be able to get this upgrade")
        if level >= 2:
            print("2 - 2x Defense when buying")
        else:
            print("Reach level 2 to be able to get this upgrade")
        if level >= 3:
            print("3 - 2x Stamina when buying")
        else:
            print("Reach level 3 to be able to get this upgrade")
        if level >= 5:
            print("4 - Get Second Attack Option")
        else:
            print("Reach level 5 to be able to get this upgrade")
        if level >= 10:
            print("5 - Get Third Attack Option")
        else:
            print("Reach level 10 to be able to get this upgrade")
        if level >= 15:
            print("6 - Get Fourth Attack Option")
        else:
            print("Reach level 15 to be able to get this upgrade")
        print("7 - Leave")
        choice = input("# ")
        if level >= 1:
            if choice == "1":
                if SKPTS >= 1:
                    SKPTS -= 1
                    at2x = "1"
                    save()
                    print("You now get 2x Attack from buying")
                else:
                    print("You do not have the skill points, or the level.")
        if choice == "7":
            skta = False
        if level >= 2:
            if choice == "2":
                if SKPTS >= 1:
                    SKPTS -= 1
                    hp2x = "1"
                    print("You now get 2x HP from buying")
                else:
                    print("You do not have the skill points, or the level.")
        if level >= 3:
            if choice == "3":
                if SKPTS >= 1:
                    SKPTS -= 1
                    st2x = "1"
                    print("You now Have 2x Stamina when purchasing Stamina")
                else:
                    print("You do not have the skill points, or the level.")
        if level >= 5:
            if choice == "4":
                if SKPTS >= 1:
                    SKPTS -= 1
                    twoatks = "1"
                    print("You now have access to a third attack")
                else:
                    print("You do not have the skill points, or the level.")
        if level >= 10:
            if choice == "9484049850":
                if SKPTS >= 1:
                    SKPTS -= 1
                    prices_better = "1"
                    print("You now get better prices")
                else:
                    print("You do not have the skill points, or the level")
        if level >= 10:
            if choice == "5":
                if SKPTS >= 1:
                    SKPTS -= 1
                    threeatks = "1"
                    print("You now have access to a fourth attack")
                else:
                    print("You do not have the skill points, or the level.")
        if level >= 15:
            if choice == "6":
                if SKPTS >= 1:
                    SKPTS -= 1
                    fouratks = "1"
                    print("You now have access to a fifth attack")
                else:
                    print("You do not have the skill points, or the level.")
        input("> ")
        clear()

def shop():
    global buy, gold, pot, elix, ATK, HPMAX, spot, STAM, MAXSTAM, prices_better

    while buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        hpbar()
        stambar()
        expbar()
        print("GOLD: " + str(gold))
        print("POTIONS: " + str(pot))
        print("ELIXIRS: " + str(elix))
        print("SUPER POTIONS: " + str(spot))
        print("ATK: " + str(ATK))
        draw()
        print("1 - BUY POTION (30 HP) - 8 GOLD")
        print("2 - BUY SUPER POTION (50 HP) - 12 GOLD")
        print("3 - BUY ELIXIR (100 HP) - 14 GOLD")
        print("4 - UPGRADE WEAPON (+1 ATK) - 10 GOLD")
        print("5 - UPGRADE HEALTH (+5 HP) - 15 GOLD")
        print("6 - UPGRADE STAMINA (+5 STAMINA) - 10 GOLD")
        print("7 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if gold >= 8:
                pot += 1
                gold -= 5
                print("You've bought a potion!")
            input("> ")
        elif choice == "2":
            if gold >= 12:
                spot += 1
                gold -= 12
                print("You've bought a Super Potion!")
            input("> ")
        elif choice == "3":
            if gold >= 14:
                elix += 1
                gold -= 14
                print("You've bought an elixer!")
            input("> ")
        elif choice == "4":
            if ATK >= atcap:
                print("Max attack reached")
                input("> ")
                break
            if gold >= 10:
                if at2x == "1":
                    ATK += 2
                    gold -= 10
                    print("You have upgraded your weapon")
                else:
                    ATK += 1
                    gold -= 10
                    print("You have upgraded your weapon")
            input("> ")
        elif choice == "5":
            if gold >= 15:
                if HPMAX >= hpcap:
                    print("MAX HP REACHED")
                    input("# ")
                    break
                if hp2x == "1":
                    HPMAX += 10
                    gold -= 15
                if hp2x == "0":
                    HPMAX += 5
                    gold -= 15
                print("You've upgraded your HP!")
            input("> ")
        elif choice == "6":
            if gold >= 10:
                if STAM >= stamcap:
                    print("MAX STAMINA REACHED")
                    input("# ")
                else:
                    STAM += 5
                    MAXSTAM += 5
                    gold -= 10
                    print("You've Upgraded your stamina!")
            else:
                print("You Do Not Have Enough Gold")
            input("> ")
        elif choice == "7":
            buy = False

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(level),
        str(HPMAX),
        str(kills),
        str(spot),
        str(difficulty),
        str(exp),
        str(level),
        str(totalexp),
        str(STAM),
        str(MAXSTAM),
        str(SKPTS),
        str(twoatks),
        str(prices_better),
        str(hp2x),
        str(at2x),
        str(st2x),
        str(threeatks),
        str(fouratks),
        str(hpcap),
        str(stamcap),
        str(atcap),
        str(expreq)
    ]
    file = open("loadgld.txt", "w")

    for item in list:
        file.write(item + "\n")
    file.close()

while run:
    while menu:
        clear()
        print('''
 @@@@@@@@  @@@        @@@@@@   @@@@@@@   @@@   @@@@@@   @@@@@@@   @@@@@@   @@@@@@@   
@@@@@@@@@  @@@       @@@@@@@@  @@@@@@@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  
!@@        @@!       @@!  @@@  @@!  @@@  @@!  @@!  @@@    @@!    @@!  @@@  @@!  @@@  
!@!        !@!       !@!  @!@  !@!  @!@  !@!  !@!  @!@    !@!    !@!  @!@  !@!  @!@  
!@! @!@!@  @!!       @!@!@!@!  @!@  !@!  !!@  @!@!@!@!    @!!    @!@  !@!  @!@!!@!   
!!! !!@!!  !!!       !!!@!!!!  !@!  !!!  !!!  !!!@!!!!    !!!    !@!  !!!  !!@!@!    
:!!   !!:  !!:       !!:  !!!  !!:  !!!  !!:  !!:  !!!    !!:    !!:  !!!  !!: :!!   
:!:   !::   :!:      :!:  !:!  :!:  !:!  :!:  :!:  !:!    :!:    :!:  !:!  :!:  !:!  
 ::: ::::   :: ::::  ::   :::   :::: ::   ::  ::   :::     ::    ::::: ::  ::   :::  
 :: :: :   : :: : :   :   : :  :: :  :   :     :   : :     :      : :  :    :   : :                                         
''')
        print("1 - New Game")
        print("2 - Load Game")
        print("3 - Quit Game")
        choice = input("# ")
        if choice == "1":
            print("What is your name, Gladiator?")
            name = input("# ")
            if name == "Jonathan":
                print("You are probably bad at this game.")
            if name == "jonathan":
                print("You are trash")
            if name == "Eno":
                print("My name is tyler")
            if name == "Jeff":
                print("My name jeff")
            print("CHOOSE YOUR DIFFICULTY")
            draw()
            print("1. Normal")
            print("2. Impossible")
            draw()
            difficultych = input("# ")
            if difficultych == "1":
                print("Ok, noob")
                difficulty = "Easy"
            if difficultych == "2":
                print("Your funeral.")
                difficulty = "SHard"
            input("> ")
            clear()
            menu = False
            play = True
        elif choice == "2":
            try:
                placeholderbool = False
                f = open("loadgld.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 28:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    level = int(load_list[6][:-1])
                    HPMAX = int(load_list[7][:-1])
                    kills = int(load_list[8][:-1])
                    spot = int(load_list[9][:-1])
                    difficulty = load_list[10][:-1]
                    exp = int(load_list[11][:-1])
                    level = int(load_list[12][:-1])
                    totalexp = int(load_list[13][:-1])
                    STAM = int(load_list[14][:-1])
                    MAXSTAM = int(load_list[15][:-1])
                    SKPTS = int(load_list[16][:-1])
                    twoatks = str(load_list[17][:-1])                           
                    prices_better = str(load_list[18][:-1])                            
                    hp2x = str(load_list[19][:-1])                            
                    at2x = str(load_list[20][:-1])                            
                    st2x = str(load_list[21][:-1]) 
                    threeatks = str(load_list[22][:-1])
                    fouratks = str(load_list[23][:-1]) 
                    hpcap = int(load_list[24][:-1])
                    stamcap = int(load_list[25][:-1])
                    atcap = int(load_list[26][:-1])
                    expreq = float(load_list[27][:-1])

                    print("Welcome back, " + name + "!")
                    menu = False
                    play = True

                    input("> ")
                    clear()
                else:
                    print("Corrupt save file!")
                    input("> ")
            except OSError:
                print("No loadable save file!")
                input("> ")
        elif choice == "3":
            quit()
    while play:
        #check for level
        if exp >= expreq:
            level += 1
            exp = 0
            print("You Have Gained A Level!")
            print("level is now... " + str(level))
            print("You have recieved 5 Hp!")
            print("You have recieved 2 Atk!")
            print("You have recieved 5 Stamina")
            print("You have recieved 1 Skill Point")
            print("You have recieved 25 Gold!")
            ATK += 2
            SKPTS += 1
            gold += 25
            expinc = expreq / 10
            if level >= 1:
                atcap += 3
                hpcap += 5
                stamcap += 10
                expreq += expinc
                round(expreq)
            if level >= 10:
                atcap += 4
                hpcap += 5
                stamcap += 15
                expreq += expinc
                round(expreq)
            if level >= 15:
                atcap += 5
                hpcap += 10
                stamcap += 15
                expreq += expinc
                round(expreq)
            if level >= 25:
                atcap += 6
                hpcap += 15
                stamcap += 20
                expreq += expinc
                round(expreq)
            if level >= 35:
                atcap += 7
                hpcap += 20
                stamcap += 25
                expreq += expinc
                round(expreq)
            if level >= 50:
                atcap += 8
                hpcap += 30
                stamcap += 30
                expreq += expinc
                round(expreq)
            if level >= 65:
                atcap += 9
                hpcap += 50
                stamcap += 50
                expreq += expinc
                round(expreq)
            print("Max HP has increased to " + str(hpcap))
            print("Max Attack has increased to " + str(atcap))
            print("Max Stamina has increased to " + str(stamcap))
            input("> ")
        save() #autosave
        clear()
        if play:
            print("NAME: " + name)
            hpbar()
            expbar()
            stambar()
            print("ATK: " + str(ATK))
            print("LEVEL: " + str(level))
            print("GOLD: " + str(gold))
            print("POTIONS: " + str(pot))
            print("SUPER POTIONS: " + str(pot))
            print("ELIXERS: " + str(pot))
            draw()
            print("0 - Save & Quit")
            print("1 - Go To Arena")
            print("2 - Go To Shop")
            print("3 - Go To Medic")
            print("4 - Go to Skill Tree")
            print("5 - Stats")
            if name == "EnoBoyA":
                print("404 - Cheats")
            draw()
            choice1 = input("# ")
            if choice1 == "0":
                save()
                play = False
                menu = True
            if choice1 == "1":
                fight = True
                gladarena()
            if choice1 == "2":
                buy = True
                shop()
            if choice1 == "3":
                heal(69420)
            if choice1 == "4":
                skta = True
                skt()
            if choice1 == "5":
                print(f"Fights won: {kills}")
                print(f"Playtime: ")
                input("> ")
                
            if name == "W01":
                if choice1 == "404":
                    exp = 249
                    ATK += 500
                    HP += 500
                    HPMAX += 500
                    spot += 100
                    pot += 200
                    elix += 300
                    gold += 5000
                    MAXSTAM += 500
                    print("WOW, How did you find it, by chance? From someone else, I guess only you know, and you arent telling")
                    input("> ")
            
