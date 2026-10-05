# Tutorial: https://youtu.be/QU1pPzEGrqw

import pygame
import sys
import os
from Settings import *
from Level import Level
from UI import UI

# Set working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption("Powerspike")
        pygame_icon = pygame.image.load("../Graphics/Test/Player.png")
        pygame.display.set_icon(pygame_icon)
        self.clock = pygame.time.Clock()

        # UI system for menu
        self.ui = UI()

        # Game world
        self.level = Level()

        # Music
        main_sound = pygame.mixer.Sound("../Audio/Main.ogg")
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    # ----------------------------------------------------------
    # MAIN MENU LOOP
    # ----------------------------------------------------------
    def main_menu(self):
        menu_index = 0
        in_menu = True

        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_index = (menu_index - 1) % 3
                    if event.key == pygame.K_DOWN:
                        menu_index = (menu_index + 1) % 3
                    if event.key == pygame.K_RETURN:
                        if menu_index == 0:  # PLAY
                            in_menu = False
                        elif menu_index == 1:  # CONTROLS
                            self.controls_menu()
                        elif menu_index == 2:  # QUIT
                            pygame.quit()
                            sys.exit()

            self.screen.fill((0, 0, 0))
            self.ui.show_main_menu(menu_index)
            pygame.display.update()
            self.clock.tick(FPS)

    # ----------------------------------------------------------
    # CONTROLS MENU (SHARED)
    # ----------------------------------------------------------
    def controls_menu(self):
        in_controls = True

        while in_controls:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        in_controls = False

            # Semi-transparent overlay
            overlay = pygame.Surface((WIDTH, HEIGTH))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            self.ui.show_controls()
            pygame.display.update()
            self.clock.tick(FPS)

    # ----------------------------------------------------------
    # PAUSE MENU
    # ----------------------------------------------------------
    def pause_menu(self):
        menu_index = 0
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_index = (menu_index - 1) % 3
                    if event.key == pygame.K_DOWN:
                        menu_index = (menu_index + 1) % 3
                    if event.key == pygame.K_RETURN:
                        if menu_index == 0:  # RESUME
                            paused = False
                        elif menu_index == 1:  # CONTROLS
                            self.controls_menu()
                        elif menu_index == 2:  # QUIT
                            pygame.quit()
                            sys.exit()

            # Draw pause menu
            self.screen.fill((0, 0, 0))
            self.ui.show_pause_menu(menu_index)
            pygame.display.update()
            self.clock.tick(FPS)

    # ----------------------------------------------------------
    # GAME OVER MENU
    # ----------------------------------------------------------
    def game_over_menu(self):
        menu_index = 0
        in_menu = True

        while in_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu_index = (menu_index - 1) % 2
                    if event.key == pygame.K_DOWN:
                        menu_index = (menu_index + 1) % 2
                    if event.key == pygame.K_RETURN:
                        if menu_index == 0:  # TRY AGAIN
                            in_menu = False
                            self.level = Level()
                            self.run()
                        elif menu_index == 1:  # QUIT
                            pygame.quit()
                            sys.exit()

            self.screen.fill((0, 0, 0))
            self.ui.show_game_over(self.level.score, menu_index)
            pygame.display.update()
            self.clock.tick(FPS)

    # ----------------------------------------------------------
    # GAME RUN LOOP
    # ----------------------------------------------------------
    def run(self):
        self.main_menu()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # ----------------------------
                # TOGGLE UPGRADE MENU (M KEY)
                # ----------------------------
                if event.type == pygame.KEYDOWN:
                    # M — only works during gameplay (not paused menus)
                    if event.key == pygame.K_m:
                        self.level.game_paused = not self.level.game_paused

                    # ESC keeps its old pause menu
                    if event.key == pygame.K_ESCAPE:
                        # Only activate pause menu when not inside upgrade screen
                        if not self.level.game_paused:
                            self.pause_menu()

                # Game over trigger event
                if event.type == pygame.USEREVENT:
                    if event.__dict__.get("action") == "game_over":
                        self.game_over_menu()

            # Draw background
            self.screen.fill(WATER_COLOR)

            # Run level (upgrade or normal)
            self.level.run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
