# =============================================================================
#  PYTHON PRIMER — the building blocks, before we build the game
#
#  This file is a WARM-UP. It shows the handful of Python ideas the game uses,
#  each in its tiniest form. You don't need to memorise anything — just run it
#  and read along, top to bottom.
#
#  Run it (from this folder):   venv/bin/python primer.py
#  (No game window opens — this one just prints text to the terminal.)
#
#  Try this as you go: change a number, save, run it again, see what changed.
#  That "edit → run → look" loop is the whole job. Breaking it is how you learn.
# =============================================================================

print("=== 1. VARIABLES & DATA TYPES ===")

# A variable is just a NAME that holds a VALUE.  name = value
score = 0            # a whole number (int)
speed = 1.6          # a number with a decimal (float)
name = "Mira"        # text, in quotes (str = "string")
alive = True         # a yes/no value (bool = True or False)

# print() shows things in the terminal. Separate items with commas.
print("score is", score)
print("speed is", speed)
print("name is", name)
print("alive is", alive)

# You can change a variable later. "+=" means "add to what's already there".
score = score + 10   # the long way
score += 10          # the short way — same thing
print("score is now", score)        # 20

# Sticking text together for a message (the game does this for its score display):
print("Score: " + str(score))       # str(...) turns the number into text first
print()


print("=== 2. DICTIONARIES — a 'bag of values' ===")

# A dictionary groups related values under one name, each with a label (a "key").
# In the game, the player is exactly this:
player = {"x": 350, "y": 250, "size": 12, "speed": 3}

print("the whole player:", player)
print("player x:", player["x"])     # read one value with ["key"]

player["x"] = 400                   # change one value
print("player x after moving:", player["x"])
print()


print("=== 3. LISTS — many things in one place ===")

# A list holds a bunch of items in order. In the game, all enemies live in a list.
enemies = []                        # start empty
enemies.append("goblin")            # add to the end
enemies.append("bat")
enemies.append("slime")

print("enemies:", enemies)
print("how many:", len(enemies))    # len() = how many items
print("the first one:", enemies[0]) # counting starts at 0!
print()


print("=== 4. IF / ELIF / ELSE — making decisions ===")

# The game constantly asks yes/no questions, like "did a bullet hit an enemy?"
health = 30

if health <= 0:
    print("You died.")
elif health < 50:                   # "elif" = "else, if..." (checked next)
    print("Careful — low health!")
else:
    print("You're fine.")

# Comparisons give True/False:  <  >  <=  >=  ==(equal)  !=(not equal)
print("is health below 50?", health < 50)
print()


print("=== 5. FOR LOOPS — do something to every item ===")

# "for each enemy in the list, do this." The game uses this to move every enemy.
for enemy in enemies:
    print("an enemy:", enemy)

# range(n) counts 0, 1, ... n-1 — handy when you want to repeat n times.
for i in range(3):
    print("shot number", i)
print()


print("=== 6. WHILE LOOPS — keep going until... ===")

# A "while" loop repeats as long as something stays True.
# The game's main loop is basically: while the window is open, keep playing.
countdown = 3
while countdown > 0:
    print("starting in", countdown)
    countdown -= 1                  # subtract 1 each time, or this never ends!
print("GO!")
print()


print("=== 7. FUNCTIONS — name a chunk of work, reuse it ===")

# A function is a named set of steps. You "call" it to run those steps.
# It can take inputs (in the brackets) and give back a result with "return".
def add(a, b):
    return a + b

print("add(2, 3) =", add(2, 3))     # call it with different inputs
print("add(10, 5) =", add(10, 5))

# A real one from the game: how far apart are two points?
import math
def distance(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)

print("distance from (0,0) to (3,4) =", distance(0, 0, 3, 4))   # 5.0
print()


print("=== THAT'S EVERYTHING ===")
print("Variables, dictionaries, lists, if/elif/else, for, while, functions.")
print("The whole game is just these pieces, combined. You're ready for Stage 1.")
