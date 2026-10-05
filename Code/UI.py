import pygame
from Settings import *
import os

# This is for file (images specifically) importing
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class UI:
    def __init__(self):

        # General
        self.display_surface = pygame.display.get_surface()

        # Fonts
        self.ui_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)  # In-game UI (score, exp)
        self.menu_font = pygame.font.Font(UI_FONT, 45)          # Menu options (PLAY, CONTROLS, QUIT)
        self.title_font = pygame.font.Font(UI_FONT, 120)        # Title "POWER-SPIKE"
        self.controls_font = pygame.font.Font(UI_FONT, 23)      # Keybinds
        # Bar Setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # Convert Weapon Dictionary
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon["graphic"]
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        # Convert Magic Dictionary
        self.magic_graphics = []
        for magic in magic_data.values():
            magic = pygame.image.load(magic["graphic"]).convert_alpha()
            self.magic_graphics.append(magic)

    # -------------------- BARS --------------------
    def show_bar(self, current, max_amount, bg_rect, color):
        # Draw Background
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # Converting Stats to Pixels
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # Drawing the Bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    # -------------------- SCORE --------------------
    def show_score(self, score):
        text_surf = self.ui_font.render(f"Score: {score}", False, TEXT_COLOR)
        text_rect = text_surf.get_rect(topright=(WIDTH - 20, 30))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 10))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 10), 3)

    # -------------------- EXP --------------------
    def show_exp(self, exp):
        text_surf = self.ui_font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    # -------------------- SELECTION BOX --------------------
    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    # -------------------- WEAPON --------------------
    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 630, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(weapon_surf, weapon_rect)

    # -------------------- MAGIC --------------------
    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(100, 630, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center=bg_rect.center)
        self.display_surface.blit(magic_surf, magic_rect)

    # -------------------- FULL DISPLAY --------------------
    def display(self, player, score):
        self.show_bar(player.health, player.stats["health"], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats["energy"], self.energy_bar_rect, ENERGY_COLOR)
        self.show_exp(player.exp)
        self.show_score(score)
        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)

    # -------------------- MAIN MENU --------------------
    def show_main_menu(self, selected_index=0):
        options = ["PLAY", "CONTROLS", "QUIT"]
        menu_x = WIDTH // 2
        menu_y = HEIGTH // 2

        # Title "POWER-SPIKE"
        title_surf = self.title_font.render("POWER-SPIKE", False, TEXT_COLOR)
        title_rect = title_surf.get_rect(center=(menu_x, menu_y - 210))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, title_rect.inflate(60, 30))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, title_rect.inflate(60, 30), 3)
        self.display_surface.blit(title_surf, title_rect)

        # Menu options with custom spacing
        option_positions = [menu_y + 5, menu_y + 110, menu_y + 210]  # individual Y positions for PLAY, CONTROLS, QUIT

        for i, option in enumerate(options):
            text_surf = self.menu_font.render(option, False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(menu_x, option_positions[i]))

            if i == selected_index:
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 25))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, text_rect.inflate(50, 25), 3)
            else:
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 25))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(50, 25), 3)

            self.display_surface.blit(text_surf, text_rect)

    def show_controls(self):
        """
        Display controls screen with key bindings in two columns.
        """
        left_controls = [
            ("Move Up", MOVE_UP),
            ("Move Down", MOVE_DOWN),
            ("Move Left", MOVE_LEFT),
            ("Move Right", MOVE_RIGHT)
        ]

        right_controls = [
            ("Attack", ATTACK_KEY),
            ("Magic", MAGIC_KEY),
            ("Switch Weapon", SWITCH_WEAPON_KEY),
            ("Switch Magic", SWITCH_MAGIC_KEY),
            ("Upgrade Stats", UPGRADE_KEY)
        ]

        start_y = 275
        spacing = 90

        # Column positions
        left_x = WIDTH // 3
        right_x = 2 * WIDTH // 3

        # Optional semi-transparent background
        overlay = pygame.Surface((WIDTH, HEIGTH))
        overlay.set_alpha(200)  # 0 = fully transparent, 255 = opaque
        overlay.fill((0, 0, 0))
        self.display_surface.blit(overlay, (0, 0))

        # Title
        menu_x = WIDTH // 2
        title_surf = self.title_font.render("CONTROLS", False, TEXT_COLOR)
        title_rect = title_surf.get_rect(center=(menu_x, 120))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, title_rect.inflate(60, 30))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, title_rect.inflate(60, 30), 3)
        self.display_surface.blit(title_surf, title_rect)

        # Draw left column
        for i, (action, key) in enumerate(left_controls):
            text = f"{action}: {key}"
            text_surf = self.controls_font.render(text, False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(left_x, start_y + i * spacing))
            pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(40, 20))
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(40, 20), 3)
            self.display_surface.blit(text_surf, text_rect)

        # Draw right column
        for i, (action, key) in enumerate(right_controls):
            text = f"{action}: {key}"
            text_surf = self.controls_font.render(text, False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(right_x, start_y + i * spacing))
            pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(40, 20))
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(40, 20), 3)
            self.display_surface.blit(text_surf, text_rect)

    def show_pause_menu(self, selected_index=0):
        options = ["RESUME", "CONTROLS", "QUIT"]
        menu_x = WIDTH // 2
        menu_y = HEIGTH // 2

        # Title "PAUSED"
        title_surf = self.title_font.render("PAUSED", False, TEXT_COLOR)
        title_rect = title_surf.get_rect(center=(menu_x, menu_y - 210))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, title_rect.inflate(60, 30))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, title_rect.inflate(60, 30), 3)
        self.display_surface.blit(title_surf, title_rect)

        option_positions = [menu_y + 5, menu_y + 110, menu_y + 210]

        for i, option in enumerate(options):
            text_surf = self.menu_font.render(option, False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(menu_x, option_positions[i]))

            if i == selected_index:
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 25))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, text_rect.inflate(50, 25), 3)
            else:
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 25))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(50, 25), 3)

            self.display_surface.blit(text_surf, text_rect)
        
        
    def show_game_over(self, score, selected_index=0):
        options = ["TRY AGAIN", "QUIT"]
        menu_x = WIDTH // 2
        menu_y = HEIGTH // 2

        # Title "GAME OVER"
        title_surf = self.title_font.render("GAME OVER", False, TEXT_COLOR)
        title_rect = title_surf.get_rect(center=(menu_x, menu_y - 200))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, title_rect.inflate(60, 30))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, title_rect.inflate(60, 30), 3)
        self.display_surface.blit(title_surf, title_rect)

        # Total Score
        score_surf = self.menu_font.render(f"Total Score: {score}", False, TEXT_COLOR)
        score_rect = score_surf.get_rect(center=(menu_x, menu_y - 60))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, score_rect.inflate(40, 20))
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, score_rect.inflate(40, 20), 3)
        self.display_surface.blit(score_surf, score_rect)

        # Menu options
        option_positions = [menu_y + 40, menu_y + 140]  # TRY AGAIN, QUIT
        for i, option in enumerate(options):
            text_surf = self.menu_font.render(option, False, TEXT_COLOR)
            text_rect = text_surf.get_rect(center=(menu_x, option_positions[i]))

            if i == selected_index:
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 25))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, text_rect.inflate(50, 25), 3)
            else:
                pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(50, 25))
                pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(50, 25), 3)

            self.display_surface.blit(text_surf, text_rect)
    