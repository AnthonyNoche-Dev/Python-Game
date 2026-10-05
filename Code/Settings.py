import os

# This is for file (images specifically) importing (This line changes the directory to where the project is saved)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
	"player": -26,
	"object": -40,
	"grass": -10,
	"invisible": 0
	}

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "../Graphics/Font/Joystix.ttf"
UI_FONT_SIZE = 18

# General Colors
WATER_COLOR = "#71ddee"
UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

# UI Colors
HEALTH_COLOR = "Red"
ENERGY_COLOR = "Blue"
UI_BORDER_COLOR_ACTIVE = "Gold"

# Upgrade Menu
TEXT_COLOR_SELECTED = "#111111"
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED = "#111111"
UPGRADE_BG_COLOR_SELECTED = "#EEEEEE"

#Keybinds
MOVE_UP = "Up ARROW"
MOVE_DOWN = "Down ARROW"
MOVE_LEFT = "Left ARROW"
MOVE_RIGHT = "Right ARROW"
ATTACK_KEY = "Space"
MAGIC_KEY = "Ctrl"
SWITCH_WEAPON_KEY = "Q"
SWITCH_MAGIC_KEY = "E"
UPGRADE_KEY = "M"

#Blocks Path
FENCE_INDEX_SNOW = 28
FENCE_INDEX_SAND = 29

# Weapons
weapon_data = {
	"sword": {"cooldown": 90, "damage": 25, "graphic": "../Graphics/Weapons/Sword/Full.png"},
	"lance": {"cooldown": 220, "damage": 45, "graphic": "../Graphics/Weapons/Lance/Full.png"},
	"axe": {"cooldown": 280, "damage": 55, "graphic": "../Graphics/Weapons/Axe/Full.png"},
	"rapier": {"cooldown": 110, "damage": 35, "graphic": "../Graphics/Weapons/Rapier/Full.png"},
	"sai": {"cooldown": 40, "damage": 20, "graphic": "../Graphics/Weapons/Sai/Full.png"}
    }

# Magic
magic_data = {
	"flame": {"strength": 35, "cost": 25, "graphic": "../Graphics/Particles/Flame/Fire.png"},
	"heal": {"strength": 25, "cost": 15, "graphic": "../Graphics/Particles/Heal/Heal.png"}
	}

# Enemies
monster_data = {
	"squid": {"health": 120, "exp": 220, "damage": 7, "attack_type": "slash", "attack_sound": "../Audio/Attack/Slash.wav", "speed": 3, "resistance": 2.25, "attack_radius": 80, "notice_radius": 280,},
	"raccoon": {"health": 1250, "exp": 1050, "damage": 65, "attack_type": "claw", "attack_sound": "../Audio/Attack/Claw.wav", "speed": 2, "resistance": 2.8, "attack_radius": 120, "notice_radius": 380},
	"spirit": {"health": 85, "exp": 190, "damage": 10, "attack_type": "thunder", "attack_sound": "../Audio/Attack/Fireball.wav", "speed": 4, "resistance": 1.5, "attack_radius": 60, "notice_radius": 260},
	"bamboo": {"health": 35, "exp": 140, "damage": 3, "attack_type": "leaf_attack", "attack_sound": "../Audio/Attack/Slash.wav", "speed": 3, "resistance": 1, "attack_radius": 50, "notice_radius": 240}
	}

# Enemy Score Values
score_values = {
	"squid": 140,
	"bamboo": 900,
	"spirit": 120,
	"raccoon": 1100
}