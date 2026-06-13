# =============================================================================
#  MINI SURVIVORS  —  a tiny Vampire Survivors clone (Python / pygame version)
#
#  The code is laid out in the SAME order you build it: Stage 1 at the top,
#  Stage 7 at the bottom. The functions that grow as you go — draw() and the
#  game loop — live near the bottom, and you add one line to them each stage.
#
#  This is the same game as javascript/index.html, just written in Python.
#
#  To run it (from this folder):  venv/bin/python game.py
# =============================================================================

import pygame      # the game library (drawing, input, the window)
import random      # for picking random spawn spots
import math        # for the distance() math


# ===== Stage 1 — SETUP =====
# Start pygame, make a window, and a clock that keeps a steady frame rate.
pygame.init()
W, H = 700, 500
FPS = 120          # frames per second. Higher = the whole game runs faster.
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mini Survivors")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 16)        # (used by the HUD in Stage 7)
big_font = pygame.font.SysFont("monospace", 30)    # (used by the game-over screen)

# A few colors, written as (Red, Green, Blue) from 0 to 255.
BG     = (30, 30, 46)
BLUE   = (85, 170, 255)   # player
RED    = (229, 85, 85)    # enemies
YELLOW = (255, 255, 85)   # bullets
WHITE  = (255, 255, 255)


# ===== Stage 1 — the player =====
# A dictionary is just a bag of related values. This bag describes our hero.
player = {
    "x": W / 2,      # position, starts in the middle
    "y": H / 2,
    "size": 12,      # radius of the circle
    "speed": 3,      # how many pixels it moves per frame
    "fireRate": 30,  # (added in Stage 5) shoot every 30 frames. Lower = faster.
}
# (Python doesn't need a circle() helper — pygame.draw.circle is built in.)


# ===== Stage 2 — move the player =====
def move_player():
    keys = pygame.key.get_pressed()   # which keys are held down right now
    if keys[pygame.K_w] or keys[pygame.K_UP]:    player["y"] -= player["speed"]
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:  player["y"] += player["speed"]
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:  player["x"] -= player["speed"]
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: player["x"] += player["speed"]

    # Keep the player inside the screen.
    player["x"] = max(player["size"], min(W - player["size"], player["x"]))
    player["y"] = max(player["size"], min(H - player["size"], player["y"]))


# ===== Stage 3 — enemies (a list) and a frame counter =====
enemies = []
frame = 0          # counts how many frames have passed (our clock)

# ===== Stage 3 — spawn an enemy at a random edge, every so often =====
def spawn_enemy():
    # The longer you survive, the more often enemies appear.
    spawn_every = max(6, 45 - frame / 120)
    if frame % int(spawn_every) != 0:
        return

    # Pick a random spot somewhere on the border.
    if random.random() < 0.5:                 # left or right edge
        x = 0 if random.random() < 0.5 else W
        y = random.random() * H
    else:                                     # top or bottom edge
        x = random.random() * W
        y = 0 if random.random() < 0.5 else H

    enemies.append({"x": x, "y": y, "size": 10, "speed": 1.6})


# ===== Stage 4 — distance between two points (a helper) =====
def distance(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)

# ===== Stage 4 — move every enemy toward the player =====
def move_enemies():
    global game_over
    for e in enemies:
        d = distance(e["x"], e["y"], player["x"], player["y"])
        if d == 0:
            continue                          # never divide by zero
        e["x"] += ((player["x"] - e["x"]) / d) * e["speed"]
        e["y"] += ((player["y"] - e["y"]) / d) * e["speed"]

        # (Stage 6) Touching the player = instant death.
        if d < e["size"] + player["size"]:
            game_over = True


# ===== Stage 5 — bullets (a list) =====
bullets = []

# ===== Stage 5 — fire a bullet at the nearest enemy, on a timer =====
def auto_shoot():
    if frame % player["fireRate"] != 0:   # not time to shoot yet
        return
    if len(enemies) == 0:                 # nothing to shoot at
        return

    # Find the nearest enemy.
    target = enemies[0]
    best = float("inf")
    for e in enemies:
        d = distance(player["x"], player["y"], e["x"], e["y"])
        if d < best:
            best = d
            target = e

    # Aim a bullet from the player toward that enemy.
    d = distance(player["x"], player["y"], target["x"], target["y"])
    bullets.append({
        "x": player["x"],
        "y": player["y"],
        "dx": ((target["x"] - player["x"]) / d) * 6,   # 6 = bullet speed
        "dy": ((target["y"] - player["y"]) / d) * 6,
        "size": 4,
    })


# ===== Stage 6 — score and the game-over flag =====
score = 0
game_over = False

# ===== Stage 6 — move bullets; remove off-screen ones; kill enemies on hit ====
def move_bullets():
    global score
    # Loop over a copy so we can safely remove items while looping.
    for b in bullets[:]:
        b["x"] += b["dx"]
        b["y"] += b["dy"]

        # Off the screen? Remove it.
        if b["x"] < 0 or b["x"] > W or b["y"] < 0 or b["y"] > H:
            bullets.remove(b)
            continue

        # Did this bullet hit any enemy?
        for e in enemies[:]:
            if distance(b["x"], b["y"], e["x"], e["y"]) < b["size"] + e["size"]:
                score += 10                # you get points for the kill
                bullets.remove(b)          # bullet is used up
                enemies.remove(e)          # enemy dies
                break


# ===== Stage 7 — drawing the world (the HUD lives here too) =====
def draw():
    screen.fill(BG)                         # wipe the previous frame

    for e in enemies:                                              # Stage 3
        pygame.draw.circle(screen, RED, (int(e["x"]), int(e["y"])), e["size"])
    for b in bullets:                                              # Stage 5
        pygame.draw.circle(screen, YELLOW, (int(b["x"]), int(b["y"])), b["size"])
    pygame.draw.circle(screen, BLUE,                              # Stage 1: player
                       (int(player["x"]), int(player["y"])), player["size"])

    # Stage 7: the HUD (text in the corner).
    screen.blit(font.render("Time: " + str(frame // FPS) + "s", True, WHITE), (10, 10))
    screen.blit(font.render("Score: " + str(score), True, WHITE), (10, 30))


# ===== Stage 7 — the game-over screen =====
def draw_game_over():
    t1 = big_font.render("GAME OVER", True, WHITE)
    t2 = font.render("You survived " + str(frame // FPS) + " seconds", True, WHITE)
    t3 = font.render("Final score: " + str(score), True, WHITE)
    t4 = font.render("Press R to play again", True, WHITE)
    screen.blit(t1, (W / 2 - t1.get_width() / 2, H / 2 - 40))
    screen.blit(t2, (W / 2 - t2.get_width() / 2, H / 2 + 5))
    screen.blit(t3, (W / 2 - t3.get_width() / 2, H / 2 + 30))
    screen.blit(t4, (W / 2 - t4.get_width() / 2, H / 2 + 60))


# ===== Stage 7 — reset everything for a new run =====
def reset_game():
    global enemies, bullets, frame, score, game_over
    enemies = []
    bullets = []
    frame = 0
    score = 0
    game_over = False
    player["x"] = W / 2
    player["y"] = H / 2


# ===== THE GAME LOOP =====
# This runs ~FPS times per second until you close the window. It IS the game.
running = True
while running:
    # Handle window events (like clicking the X to close, or pressing R).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and game_over:
            reset_game()

    if game_over:
        draw_game_over()
    else:
        move_player()    # Stage 2
        frame += 1       # Stage 3
        spawn_enemy()    # Stage 3
        move_enemies()   # Stage 4
        auto_shoot()     # Stage 5
        move_bullets()   # Stage 6
        draw()

    pygame.display.flip()   # show this frame on screen
    clock.tick(FPS)         # wait so we run at FPS frames per second

pygame.quit()
