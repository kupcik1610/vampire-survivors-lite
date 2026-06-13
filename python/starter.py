# =============================================================================
#  MINI SURVIVORS — STARTER (Python / pygame)
#  You start with ONE blue dot (Stage 1 is done). Build the rest top to bottom.
#  Curriculum-Python.pdf gives you the exact code for each Stage.
#
#  HOW TO FILL IN:
#   • Each "# >>> Stage N" is where that stage's new code goes.
#   • The draw() function and the game LOOP at the bottom grow as you go.
#     Most stages you just UNCOMMENT one line in them (look for "# Stage N").
#   • That bottom area is the ONLY place you scroll back to. Everything else
#     is written once, top to bottom.
#
#  STAGE MAP — what each stage adds:
#   Stage 2  move_player()                            (+ uncomment 1 line in loop)
#   Stage 3  enemies/frame + spawn_enemy()            (+ uncomment in draw & loop)
#   Stage 4  distance() + move_enemies()              (+ uncomment 1 line in loop)
#   Stage 5  bullets + auto_shoot() + fireRate↑Stage1 (+ uncomment in draw & loop)
#   Stage 6  score/game_over + move_bullets()         (+ uncomment 1 line in loop)
#   Stage 7  HUD + game-over screen + restart         (+ wrap the loop)
#
#  Run it (from this folder):  venv/bin/python starter.py
# =============================================================================

import pygame
# >>> Stage 3: import random   (for random spawn spots)
# >>> Stage 4: import math     (for the distance() function)


# ===== Stage 1 — SETUP (done for you) =====
pygame.init()
W, H = 700, 500
FPS = 120          # frames per second (match your screen; 120 on most Macs)
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mini Survivors")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 16)        # (used by the HUD in Stage 7)
big_font = pygame.font.SysFont("monospace", 30)    # (used by the game-over screen)

BG     = (30, 30, 46)
BLUE   = (85, 170, 255)   # player
RED    = (229, 85, 85)    # enemies
YELLOW = (255, 255, 85)   # bullets
WHITE  = (255, 255, 255)  # text


# ===== Stage 1 — the player (done for you) =====
player = {"x": W / 2, "y": H / 2, "size": 12, "speed": 3}
# >>> Stage 5: add  "fireRate": 30  inside the player (so it can shoot on a timer)
# (Python doesn't need a circle() helper — pygame.draw.circle is built in.)


# ===== Stage 2 — move_player() =====
# >>> Stage 2: def move_player():  read pygame.key.get_pressed(), change
#     player["x"]/["y"] by player["speed"], then clamp inside the screen.


# ===== Stage 3 — enemies list + frame, and spawn_enemy() =====
# >>> Stage 3:  enemies = []   and   frame = 0
#     then def spawn_enemy(): append an enemy at a random edge now and then.


# ===== Stage 4 — distance() + move_enemies() =====
# >>> Stage 4: def distance(ax, ay, bx, by): return math.hypot(...)
#     then def move_enemies(): step each enemy toward the player.


# ===== Stage 5 — bullets list + auto_shoot() =====
# >>> Stage 5:  bullets = []   then def auto_shoot(): fire at the nearest enemy
#     every player["fireRate"] frames.
#     (Also do the "Stage 5" note up in the Stage 1 player block.)


# ===== Stage 6 — score + game_over, and move_bullets() =====
# >>> Stage 6:  score = 0   and   game_over = False
#     def move_bullets() (move, drop off-screen ones, kill enemies on hit),
#     and add the "game over on touch" line inside move_enemies() above.


# ===== Stage 7 — game-over screen + restart =====
# >>> Stage 7: def draw_game_over(), def reset_game(), and the "R to restart"
#     handling in the loop's event section below.


# ===== DRAW — uncomment one line per stage =====
def draw():
    screen.fill(BG)                                                  # wipe screen
    # for e in enemies:                                              # Stage 3
    #     pygame.draw.circle(screen, RED, (int(e["x"]), int(e["y"])), e["size"])
    # for b in bullets:                                              # Stage 5
    #     pygame.draw.circle(screen, YELLOW, (int(b["x"]), int(b["y"])), b["size"])
    pygame.draw.circle(screen, BLUE,                                 # Stage 1: player
                       (int(player["x"]), int(player["y"])), player["size"])
    # Stage 7: draw the HUD here (screen.blit of font.render for Time and Score)


# ===== THE GAME LOOP — uncomment one line per stage =====
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # >>> Stage 7: add "R to restart" here (KEYDOWN K_r when game_over)

    # --- update the world (uncomment one line per stage) ---
    # move_player()    # Stage 2
    # frame += 1       # Stage 3
    # spawn_enemy()    # Stage 3
    # move_enemies()   # Stage 4
    # auto_shoot()     # Stage 5
    # move_bullets()   # Stage 6

    draw()

    pygame.display.flip()   # show this frame
    clock.tick(FPS)         # wait so we run at FPS frames per second

    # >>> Stage 7: wrap the update lines + draw() in
    #       if game_over: draw_game_over()
    #       else: ...updates...; draw()

pygame.quit()
