from pygame import display, image, draw, time, font, init, transform, QUIT, KEYDOWN, K_TAB, MOUSEBUTTONDOWN, BUTTON_LEFT, BUTTON_RIGHT, event, mouse, Rect, KEYDOWN, K_1, K_2, K_SPACE
import random
from math import ceil, floor, log2, log
import copy
from Functions import *

if True: # Pre-processing
    bricksimg = {
        "normal_gray": image.load('Images/brick_gray.png'),
        "normal_yellow": image.load('Images/brick_yellow.png'),
        "normal_red": image.load('Images/brick_red.png'),
        "normal_purple": image.load('Images/brick_purple.png'),
        "normal_white": image.load('Images/brick_white.png'),
        "normal_black": image.load('Images/brick_black.png'),
        "normal_orange": image.load('Images/brick_orange.png'),
        "normal_green": image.load('Images/brick_green.png'),

        "plate_gray": image.load('Images/plate_gray.png'),
        "plate_yellow": image.load('Images/plate_yellow.png'),
        "plate_red": image.load('Images/plate_red.png'),
        "plate_purple": image.load('Images/plate_purple.png'),
        "plate_white": image.load('Images/plate_white.png'),
        "plate_black": image.load('Images/plate_black.png'),
        "plate_orange": image.load('Images/plate_orange.png'),
        "plate_green": image.load('Images/plate_green.png'),
    }
    enemiesimg = {
        0: image.load('Images/brick_darkred.png'),
        1: image.load('Images/enemy_normal.png'),
        2: image.load('Images/enemy_fast.png'),
        3: image.load('Images/enemy_armored.png'),
        4: image.load('Images/enemy_boss_generic.png'),
    }
    altarimg = image.load('Images/altar_generic.png')
    altar2img = image.load('Images/altar_break_generic.png')
    greebleimg = {
        "Bloods": image.load('Images/Greebles/Bloods.png'),
        "Clots": image.load('Images/Greebles/Clots.png'),
        "Pots": image.load('Images/Greebles/Pots.png'),
        "Rocks": image.load('Images/Greebles/Rocks.png'),
        "Shots": image.load('Images/Greebles/Shots.png'),
        "Slops": image.load('Images/Greebles/Slops.png'),

        "Heeds": image.load('Images/Greebles/Heeds.png'),
        "Feeds": image.load('Images/Greebles/Feeds.png'),
        "Beets": image.load('Images/Greebles/Beets.png'),
        "Sheets": image.load('Images/Greebles/Sheets.png'),
        "Leeds": image.load('Images/Greebles/Leeds.png'),
        "Heexs": image.load('Images/brick_orange.png'),

        "Sackans": image.load('Images/Greebles/Sackans.png'),
        "Postans": image.load('Images/Greebles/Postans.png'),
        "Callans": image.load('Images/Greebles/Callans.png'),
        "Verdans": image.load('Images/Greebles/Verdans.png'),
        "Daffans": image.load('Images/Greebles/Daffans.png'),
        "Radeans": image.load('Images/Greebles/Radeans.png'),
        "Xendans": image.load('Images/Greebles/Xendans.png'),

        "Bankors": image.load('Images/Greebles/Bankors.png'),
        "Rangors": image.load('Images/Greebles/Rangors.png'),
        "Fencors": image.load('Images/Greebles/Fencors.png'),
        "Kollors": image.load('Images/Greebles/Kollors.png'),
        "Kollors_off": image.load('Images/Greebles/Kollors_off.png'),
        "Tannors": image.load('Images/Greebles/Tannors.png'),
    }
    raacimg = {
        "Treasure": image.load('Images/Raacs/raac_treasure.png'), # Yellow Room spawn
        "BeetHeal": image.load('Images/Raacs/raac_generic.png'), # Beets decompose into Heeds
        "FencorRegen": image.load('Images/Raacs/raac_FencorRegen.png'), # Fencor regenerate Heeds
        "SaveThrow": image.load('Images/Raacs/raac_SaveThrow.png'), # If you were to die, corrupt Verdans instead to heal X Heeds
        "EnemyLoot": image.load('Images/Raacs/raac_EnemyLoot.png'), # Enemies drop 2 Q0 greebles
        "Altar": image.load('Images/Raacs/raac_Altar.png'), # Adds An Altar for each 5 floors

        "RoomConnectivity": image.load('Images/Raacs/raac_generic.png'), # Increases how many connections rooms have
        "ColoredRoom": image.load('Images/Raacs/raac_generic.png'), # Reveals by chance room's colors, affected by Tannors
        "LuckyCharm": image.load('Images/Raacs/raac_generic.png'), # Chance to transform Q0 into Q1
        "Pottery": image.load('Images/Raacs/raac_generic.png'), # Shots have a chance to turn into Pots
        "ExtraStock": image.load('Images/Raacs/raac_generic.png'), # Shops have more stock
        "SplashDamage": image.load('Images/Raacs/raac_generic.png'), # Gives 50% of your damage to X enemy room's

        "RockCrest": image.load('Images/Raacs/raac_generic.png'), # If you have 2+X rocks, you receive X defense. On damage, Rocks break into Shots
        "SlimeFest": image.load('Images/Raacs/raac_generic.png'), # Each Floor you turn X of each quality 0 Greebles into slime, and add a new gray room to the floor.
        "LeedQuest": image.load('Images/Raacs/raac_generic.png'), # Each Floor, lose 3X Leeds, add X red rooms.
        "TraacBest": image.load('Images/Raacs/raac_generic.png'), # Traac items have X more max charge.
        "AltarRest": image.load('Images/Raacs/raac_generic.png'), # Destroy an unused altar to gain 5X Heeds.
        "BlackTest": image.load('Images/Raacs/raac_generic.png'), # Killing a Boss gives +X charges to your Traacs
    }
    traacimg = {
        "AltarBoost": image.load('Images/Traacs/traac_AltarBoost.png'), # Altars have more charge in exchange for rocks
        "Crystalize": image.load('Images/Traacs/traac_Crystalize.png'), # Convert Heed into Beet
        "Bomb": image.load('Images/Traacs/traac_Bomb.png'), # Deals 10 damage to enemies in room
    }
    brootimg = {
        "DEAD": image.load('Images/brick_darkred.png'),
        "armed": image.load('Images/Broot_armed.png'),
        "defends": image.load('Images/Broot_defends.png'),
        "digests": image.load('Images/Broot_digests.png'),
        "digs": image.load('Images/Broot_digs.png'),
        "deconstructs": image.load('Images/Broot_deconstructs.png'),
    }
    raacNumber = []
    traacNumber = []
    brootNumber = []
    for key in raacimg:
        raacNumber.append(key)
    for key in traacimg:
        traacNumber.append(key)
    for key in brootimg:
        brootNumber.append(key)
    GQ0 = ["Shots", "Bloods", "Pots", "Clots", "Rocks"]
    GQ1 = ["Heeds", "Feeds", "Beets", "Leeds", "Sheets"]
    GQ2 = ["Verdans", "Postans", "Sackans", "Callans", "Daffans", "Radeans", "Xendans"]
    GQ3 = ["Bankors", "Rangors", "Fencors", "Kollors", "Kollors_off", "Tannors"]
    GQ0a = ["Slops"]
    GQ1a = ["Heexs"]
    G = [GQ0, GQ1, GQ2, GQ3]

    raacValue = [
        10,
        7,
        14,
        12,
        18,
        20,

        26,
        22,
        18,
        15,
        9,
        17,

        20,
        8,
        14,
        25,
        27,
        26,
    ]
    traacValue = [
        9,
        7,
        15,
    ]
    brootValue = [
        0,
        4,
        11,
        3,
        7,
        10,
    ]

    colorkey = {
        "red": (255, 0, 0),
        "black": (0, 0, 0),
        "yellow": (255, 255, 0),
        "white": (255, 255, 255),
        "purple": (255, 0, 255),
        "gray": (100, 100, 100),
        "orange": (200, 150, 0),
        "green": (0, 255, 0),
    }
    for key in bricksimg:
        bricksimg[key] = transform.scale(bricksimg[key], (64, 64))
    for key in enemiesimg:
        enemiesimg[key] = transform.scale(enemiesimg[key], (64, 64))
    for key in greebleimg:
        greebleimg[key] = transform.scale(greebleimg[key], (64, 64))
    altarimg = transform.scale(altarimg, (64, 64))
    altar2img = transform.scale(altar2img, (64, 64))
    for key in raacimg:
        raacimg[key] = transform.scale(raacimg[key], (64, 64))
    for key in traacimg:
        traacimg[key] = transform.scale(traacimg[key], (64, 64))
    for key in brootimg:
            brootimg[key] = transform.scale(brootimg[key], (64, 64))


    
# Energy Thermodynamics
# Common Altar charge: 4
# Rare Altar charge: 10
# Unique Altar charge: 25


class Player():
    def __init__(self):
        self.Broots = []
        self.selectedBroot = 0
        self.Raacs = []
        self.Traacs = []
        self.room = 0
        self.initGreebles()
        self.initPlayer(0)
    def initGreebles(self):
        self.Greebles = {}



        # Quality 0b Greebles - Ultra trash
        self.Greebles["Slops"] = 0 # V=1. Slop
        # Quality 0 Greebles - Trash greebles, sometimes used as ammo, usually used in crafting higher grade greebles
        self.Greebles["Shots"] = 0 # V=2. Used for crafting fuel
        self.Greebles["Bloods"] = 0 # V=3. Used for crafting health
        self.Greebles["Clots"] = 0 # V=4. Advanced Shots
        self.Greebles["Pots"] = 0 # V=5. Money, also used for some crafts
        self.Greebles["Rocks"] = 0 # V=6. Advanced Pots

        # Quality 1 Greebles - Resources, are expandable and are in constant use
        self.Greebles["Heeds"] = 0 # V=13 Health
        self.Greebles["Feeds"] = 0 # V=10 Fuel
        self.Greebles["Beets"] = 0 # V=14 Crystalized health
        self.Greebles["Leeds"] = 0 # V=19 Crafting material
        self.Greebles["Sheets"] = 0 # V=23 Speed and crafting
        # Quality 1b Greebles - Useful but rare
        self.Greebles["Heexs"] = 0 # V=20 Traacs usage and "magic"?

        # Quality 2 Greebles - Usually limits the greebles below them, works as storage, or stats
        self.Greebles["Verdans"] = 0 # V=66 Max Health
        self.Greebles["Postans"] = 0 # V=64 Max Fuel
        self.Greebles["Sackans"] = 0 # V=58 Max Q0 inventory*5
        self.Greebles["Callans"] = 0 # V=126 Damage
        self.Greebles["Daffans"] = 0 # V=109 Defense
        self.Greebles["Radeans"] = 0 # V=72 Max Beets, Max Leeds, Max Sheets*4
        self.Greebles["Xendans"] = 0 # V=56 Corrupted Health

        # Quality 3 Greebles - Used as power batteries for Raacs, and as catalysts for operations
        self.Greebles["Bankors"] = 0 # V=393 Max Traacs
        self.Greebles["Rangors"] = 0 # V=300 Max Broots
        self.Greebles["Fencors"] = 0 # V=321 
        self.Greebles["Kollors"] = 0 # V=662 Catalist On
        self.Greebles["Kollors_off"] = 0 # V=460 Catalist Off
        self.Greebles["Tannors"] = 0 # V=??? 




        # Quality 4 Greebles - Used in crafting new Broots and Raacs
        # self.Greebles["???"] = 0
        # self.Greebles["???"] = 0
        # self.Greebles["???"] = 0
        # self.Greebles["???"] = 0
        # self.Greebles["???"] = 0

        # Quality 5 Greebles - Used in super powerful actions
        self.Greebles["black Star"] = 0
        self.Greebles["purple Note"] = 0
        self.Greebles["white Diamond"] = 0
        self.Greebles["Cyan Heart"] = 0
        self.Greebles["red Flower"] = 0







        self.Highlights = {}
        # Quality 0 Greebles - Trash greebles, sometimes used as ammo, usually used in crafting higher grade greebles
        self.Highlights["Shots"] = False # Used for crafting fuel
        self.Highlights["Bloods"] = False # Used for crafting health
        self.Highlights["Pots"] = False # Money, also used for some crafts
        self.Highlights["Clots"] = False # Advanced Shots
        self.Highlights["Rocks"] = False # Advanced Pots
        self.Highlights["Slops"] = False # Slop

        # Quality 1 Greebles - Resources, are expandable and are in constant use
        self.Highlights["Heeds"] = True # V= Health
        self.Highlights["Feeds"] = False # V= Fuel
        self.Highlights["Beets"] = False # V= Crystalized health
        self.Highlights["Leeds"] = False # V= Crafting material
        self.Highlights["Sheets"] = False # V= Speed and crafting

        # Quality 2 Greebles - Usually limits the greebles below them, works as storage, or stats
        self.Highlights["Verdans"] = False # V= Max Health
        self.Highlights["Postans"] = False # V= Max Fuel
        self.Highlights["Sackans"] = False # V= Max Q0 inventory*5
        self.Highlights["Callans"] = False # V= Damage
        self.Highlights["Daffans"] = False # V= Defense
        self.Highlights["Radeans"] = False # V= Max Beets, Max Leeds, Max Sheets*4
        self.Highlights["Xendans"] = False # V= Corrupted Health

        # Quality 3 Greebles - Used as power batteries for Raacs, and as catalysts for operations
        self.Highlights["Bankors"] = False # Max Traacs
        self.Highlights["Rangors"] = False # Max Broots
        self.Highlights["Fencors"] = False
        self.Highlights["Kollors"] = False # Catalist On
        self.Highlights["Kollors_off"] = False # Catalist Off
        self.Highlights["Tannors"] = False

        # Quality 4 Greebles - Used in crafting new Broots and Raacs
        # self.Highlights["???"] = False
        # self.Highlights["???"] = False
        # self.Highlights["???"] = False
        # self.Highlights["???"] = False
        # self.Highlights["???"] = False

        # Quality 5 Greebles - Used in super powerful actions
        self.Highlights["black Star"] = False
        self.Highlights["purple Note"] = False
        self.Highlights["white Diamond"] = False
        self.Highlights["Cyan Heart"] = False
        self.Highlights["red Flower"] = False
    def initPlayer(self, char):
        if char == 0:
            char = random.randrange(5)
        if char == -1:
            for RN in range(len(raacNumber)):
                raac = Raac(RN)
                raac.level = 5
                self.Raacs.append(raac)

            
            self.Greebles["Heeds"] = 12 + random.randrange(-3, 4) # Health
            self.Greebles["Feeds"] = 25 + random.randrange(-5, 6) # Food
            self.Greebles["Beets"] = 2  + random.randrange(-2, 3) # Health2
            self.Greebles["Leeds"] = 4  + random.randrange(-2, 3) # Health3
            self.Greebles["Sheets"] = 20  + random.randrange(-5, 6) # Energy

            self.Greebles["Verdans"] = 12 + random.randrange(4) # Max Health
            self.Greebles["Postans"] = 25 + random.randrange(6) # Max Food
            self.Greebles["Sackans"] = 25 + random.randrange(-5, 6) # Max Q0 inventory*4
            self.Greebles["Callans"] = 3  + random.randrange(-1, 2) # Damage
            self.Greebles["Daffans"] = 0  + random.randrange(4) # Defense
            self.Greebles["Radeans"] = 5  + random.randrange(-2, 3) # Max Health2, Max Health3, Max Energy/2
            self.Greebles["Xendans"] = 0  + random.randrange(6) # Corrupted Health

            self.Greebles["Bankors"] = 2  + random.randrange(-1, 2) # Max Traacs
            self.Greebles["Rangors"] = 3  + random.randrange(-2, 3) # Max Broots
            self.Greebles["Fencors"] = 0 + random.randrange(5)
            self.Greebles["Kollors"] = 0 + random.randrange(5)
            self.Greebles["Tannors"] = 0 + random.randrange(5)
        elif char == 0: # Random
            RNG = random.randrange(100)
            if RNG <= 25:
                traac = random.randrange(len(traacimg))
                self.acquireTraac(Traac(traac))
            else:
                raac = random.randrange(len(raacimg))
                self.acquireRaac(Raac(raac))
            self.Greebles["Heeds"] = 12 + random.randrange(-3, 4)# Health
            self.Greebles["Feeds"] = 25 + random.randrange(-5, 6) # Food
            self.Greebles["Beets"] = 2  + random.randrange(-2, 3) # Health2
            self.Greebles["Leeds"] = 4  + random.randrange(-2, 3)# Health3
            self.Greebles["Sheets"] = 20  + random.randrange(-5, 6) # Energy

            self.Greebles["Verdans"] = 12 + random.randrange(4) # Max Health
            self.Greebles["Postans"] = 25 + random.randrange(6)# Max Food
            self.Greebles["Sackans"] = 25 + random.randrange(-5, 6)# Max Q0 inventory*4
            self.Greebles["Callans"] = 3  + random.randrange(-1, 2)# Damage
            self.Greebles["Daffans"] = 0  + random.randrange(4)# Defense
            self.Greebles["Radeans"] = 5  + random.randrange(-2, 3)# Max Health2, Max Health3, Max Energy/2
            self.Greebles["Xendans"] = 0 # Corrupted Health

            self.Greebles["Bankors"] = 2  + random.randrange(-1, 2) # Max Traacs
            self.Greebles["Rangors"] = 3  + random.randrange(-2, 3)# Max Broots
            self.Greebles["Fencors"] = 0
        elif char == 1: # Classic
            self.acquireRaac(Raac(1))
            self.Greebles["Heeds"] = 8 # Health
            self.Greebles["Feeds"] = 30 # Food
            self.Greebles["Beets"] = 6 # Health2
            self.Greebles["Leeds"] = 3 # Health3
            self.Greebles["Sheets"] = 20 # Energy

            self.Greebles["Verdans"] = 8 # Max Health
            self.Greebles["Postans"] = 30 # Max Food
            self.Greebles["Sackans"] = 20 # Max Q0 inventory*4
            self.Greebles["Callans"] = 3 # Damage
            self.Greebles["Daffans"] = 0 # Defense
            self.Greebles["Radeans"] = 6 # Max Health2, Max Health3, Max Energy/2
            self.Greebles["Xendans"] = 0 # Corrupted Health

            self.Greebles["Bankors"] = 2 # Max Traacs
            self.Greebles["Rangors"] = 4 # Max Broots
            self.Greebles["Fencors"] = 1
        elif char == 2: # Devoted
            self.acquireRaac(Raac(5))
            self.Greebles["Heeds"] = 13 # Health
            self.Greebles["Feeds"] = 20 # Food
            self.Greebles["Beets"] = 2 # Health2
            self.Greebles["Leeds"] = 2 # Health3
            self.Greebles["Sheets"] = 23 # Energy

            self.Greebles["Verdans"] = 13 # Max Health
            self.Greebles["Postans"] = 20 # Max Food
            self.Greebles["Sackans"] = 16 # Max Q0 inventory*4
            self.Greebles["Callans"] = 3 # Damage
            self.Greebles["Daffans"] = 1 # Defense
            self.Greebles["Radeans"] = 5 # Max Health2, Max Health3, Max Energy/2
            self.Greebles["Xendans"] = 0 # Corrupted Health

            self.Greebles["Bankors"] = 1 # Max Traacs
            self.Greebles["Rangors"] = 6 # Max Broots
            self.Greebles["Fencors"] = 0
        elif char == 3: # Corrupted
            self.acquireRaac(Raac(3))
            self.Greebles["Heeds"] = 12 # Health
            self.Greebles["Feeds"] = 25 # Food
            self.Greebles["Beets"] = 4 # Health2
            self.Greebles["Leeds"] = 4 # Health3
            self.Greebles["Sheets"] = 20 # Energy

            self.Greebles["Verdans"] = 12 # Max Health
            self.Greebles["Postans"] = 25 # Max Food
            self.Greebles["Sackans"] = 25 # Max Q0 inventory*4
            self.Greebles["Callans"] = 4 # Damage
            self.Greebles["Daffans"] = 0 # Defense
            self.Greebles["Radeans"] = 5 # Max Health2, Max Health3, Max Energy/2
            self.Greebles["Xendans"] = 4 # Corrupted Health

            self.Greebles["Bankors"] = 1 # Max Traacs
            self.Greebles["Rangors"] = 3 # Max Broots
            self.Greebles["Fencors"] = 0
        elif char == 4: # Bomberman
            self.acquireTraac(Traac(2)) # Bomb
            self.Greebles["Heeds"] = 10 # Health
            self.Greebles["Feeds"] = 35 # Food
            self.Greebles["Beets"] = 5 # Health2
            self.Greebles["Leeds"] = 2 # Health3
            self.Greebles["Sheets"] = 18 # Energy

            self.Greebles["Verdans"] = 10 # Max Health
            self.Greebles["Postans"] = 35 # Max Food
            self.Greebles["Sackans"] = 22 # Max Q0 inventory*4
            self.Greebles["Callans"] = 3 # Damage
            self.Greebles["Daffans"] = 2 # Defense
            self.Greebles["Radeans"] = 5 # Max Health2, Max Health3, Max Energy/2
            self.Greebles["Xendans"] = 0 # Corrupted Health

            self.Greebles["Bankors"] = 3 # Max Traacs
            self.Greebles["Rangors"] = 2 # Max Broots
            self.Greebles["Fencors"] = 1
    def damage(self, qtd):
        qtd -= self.Greebles["Daffans"]//3
        for raac in self.Raacs:
            if raac.name == "RockCrest" and qtd > 0 and self.Greebles["Rocks"] >= 2+raac.level and raac.charged():
                qtd -= raac.level
                self.Greebles["Rocks"] -= 2+raac.level
                self.acquire(["Shots", 2+raac.level])

        if qtd > 0:
            self.Greebles["Heeds"] -= qtd
            if self.Greebles["Heeds"] < 0:
                for raac in self.Raacs:
                    if raac.name == "SaveThrow":
                        break
                else:
                    raac = None
                while raac and raac.used < raac.level and self.Greebles["Verdans"] > 0 and self.Greebles["Heeds"] < 0:
                    self.Greebles["Verdans"] -= 1
                    self.acquire(["Xendans", 1])
                    self.acquire(["Heeds", 3])
                    raac.used += 1
    def acquire(self, greeb):
        name = greeb[0]
        self.Greebles[name] += greeb[1]
        qtd = 0
        if name == "Heeds":
            if self.Greebles["Heeds"] > self.Greebles["Verdans"]:
                qtd = -self.Greebles["Verdans"] + self.Greebles["Heeds"]
                self.Greebles["Heeds"] = self.Greebles["Verdans"]
            else:
                qtd = 0
        elif name == "Feeds":
            if self.Greebles["Feeds"] > self.Greebles["Postans"]:
                qtd = -self.Greebles["Postans"] + self.Greebles["Feeds"]
                self.Greebles["Feeds"] = self.Greebles["Postans"]
            else:
                qtd = 0
        elif name == "Beets":
            if self.Greebles["Beets"] > self.Greebles["Radeans"]:
                qtd = -self.Greebles["Radeans"] + self.Greebles["Beets"]
                self.Greebles["Beets"] = self.Greebles["Radeans"]
            else:
                qtd = 0
        elif name == "Leeds":
            if self.Greebles["Leeds"] > self.Greebles["Radeans"]:
                qtd = -self.Greebles["Radeans"] + self.Greebles["Leeds"]
                self.Greebles["Leeds"] = self.Greebles["Radeans"]
            else:
                qtd = 0
        elif name == "Sheets":
            if self.Greebles["Sheets"] > self.Greebles["Radeans"]*4:
                qtd = self.Greebles["Sheets"] - self.Greebles["Radeans"]*4
                self.Greebles["Sheets"] = self.Greebles["Radeans"]*4
            else:
                qtd = 0
        elif name in ["Shots", "Bloods", "Pots", "Clots", "Rocks"]:
            qtd2 = 0
            for name2 in ["Shots", "Bloods", "Pots", "Clots", "Rocks"]:
                qtd2 += self.Greebles[name2]
            if qtd2 > self.Greebles["Sackans"]*5:
                qtd = qtd2 - self.Greebles["Sackans"]*5
                self.Greebles[name] -= qtd
            else:
                qtd = 0
            
        return qtd
    def walk(self):
        RNG = random.randrange(0, 100)
    def acquireRaac(self, raac):
        for raac2 in self.Raacs:
            if raac2.id == raac.id:
                raac2.upgrade()
                if raac2.name == "TraacBest":
                    for traac in self.Traacs:
                        traac.maxCharge += raac2.level
                return True
        else:
            self.Raacs.append(raac)
            if raac.name == "TraacBest":
                for traac in self.Traacs:
                    traac.maxCharge += raac.level
            return True
    def acquireTraac(self, traac):
        for traac2 in self.Traacs:
            if traac2.id == traac.id:
                traac2.upgrade()
                return None
        else:
            for raac in self.Raacs:
                if raac.name == "TraacBest":
                    for traac in self.Traacs:
                        traac.maxCharge += raac.level
            self.Traacs.append(traac)
        if len(self.Traacs) > self.Greebles["Bankors"]:
            traac = self.Traacs.pop(0)
            for raac in self.Raacs:
                if raac.name == "TraacBest":
                    for traac in self.Traacs:
                        traac.maxCharge -= raac.level
            return traac
        else:
            return None


class Enemy():
    def __init__(self, id, level):
        self.id = id
        self.level = level
        self.born()
    def born(self):

        # top = 0
        # for i in range(1, self.level):
        #     top += log2(i)

        hp = 4 + self.level + random.randrange(0, self.level*2+1)
        dmg = 0.5 + self.level/3 +random.randrange(0, 10)/10
        df = self.level/5
        speed = 20 + self.level*2

        if self.level >= 10:
            hp += (self.level-8)*log2(self.level)
            speed += log2(self.level)

        if self.id == 1: # Normal
            hp = hp
            dmg = dmg
            df = df
            speed = speed
            name = "Normal"
        elif self.id == 2: # Fast
            hp = hp*0.5
            dmg = dmg*0.7
            df = df*0.3
            speed = speed*1.25
            name = "Fast"
        elif self.id == 3: # Armored
            hp = hp*1.2
            dmg = dmg*1.1
            df = df*1.3
            name = "Armored"
            speed = speed*0.7
        elif self.id == 4: # Boss
            hp = hp*1.3
            dmg = dmg*1.15
            df = df*0.9
            speed = speed*0.9
            name = "Boss"


        self.name = name
        self.hp = hp*random.randrange(7, 14)/10
        self.dmg = dmg*random.randrange(7, 14)/10
        self.df = df*random.randrange(7, 14)/10
        self.speed = speed*random.randrange(7, 14)/10

        self.hp = floor(self.hp)
        self.dmg = floor(self.dmg)
        self.df = floor(self.df)
        self.speed = floor(self.speed)
        self.mhp = self.hp

        self.turn = 0
        self.playerTurn = 0
class Altar():
    def __init__(self, id):
        self.recipe = []
        self.products = []
        self.id = id
        self.generate()
        self.uses = self.maxuses
    def generate(self):
        if self.id == 0: # Anvil
            self.maxuses = 1
        elif self.id == 1: # Healing Altar
            self.recipe = [
                ["Bloods", 2],
                ["Clots", 1],
            ]
            self.products = [
                ["Heeds", 1]
            ]
            self.maxuses = 6
        elif self.id == 2: # Feeding Altar
            self.recipe = [
                ["Shots", 2],
                ["Bloods", 1],
            ]
            self.products = [
                ["Feeds", 1]
            ]
            self.maxuses = 10
        elif self.id == 3: # Regen Altar
            self.recipe = [
                ["Pots", 2],
                ["Bloods", 1],
            ]
            self.products = [
                ["Beets", 1]
            ]
            self.maxuses = 3
        elif self.id == 4: # Sharpening Altar
            self.recipe = [
                ["Shots", 1],
                ["Bloods", 1],
                ["Clots", 1],
                ["Pots", 1],
                ["Rocks", 1],
            ]
            self.products = [
                ["Sheets", 1]
            ]
            self.maxuses = 5
        elif self.id == 5: # Armor Altar
            self.recipe = [
                ["Sheets", 2],
                ["Leeds", 3],
            ]
            self.products = [
                ["Daffans", 1]
            ]
            self.maxuses = 2
        elif self.id == 6: # Sacking Altar
            self.recipe = [
                ["Leeds", 1],
                ["Feeds", 1],
                ["Sheets", 1],
            ]
            self.products = [
                ["Sackans", 1]
            ]
            self.maxuses = 4
        elif self.id == 7: # Maxing Altar
            self.recipe = [
                ["Beets", 2],
                ["Heeds", 1],
                ["Leeds", 1],
            ]
            self.products = [
                ["Verdans", 1]
            ]
            self.maxuses = 2
        elif self.id == 8: # Killing Altar
            self.recipe = [
                ["Sheets", 4],
                ["Beets", 2],
            ]
            self.products = [
                ["Callans", 1]
            ]
            self.maxuses = 2
        elif self.id == 9: # Structure Altar
            self.recipe = [
                ["Beets", 2],
                ["Leeds", 2],
            ]
            self.products = [
                ["Radeans", 1]
            ]
            self.maxuses = 2
        elif self.id == 10: # Clot Filter Altar
            self.recipe = [
                ["Clots", 5],
            ]
            self.products = [
                ["Feeds", 1],
                ["Shots", 5],
            ]
            self.maxuses = 2
        elif self.id == 11: # Rock Crusher Altar
            self.recipe = [
                ["Rocks", 5],
            ]
            self.products = [
                ["Heeds", 1],
                ["Pots", 5],
            ]
            self.maxuses = 2
        elif self.id == 12: # Traac Altar
            self.recipe = [
                ["Verdans", 2],
                ["Callans", 1],
                ["Radeans", 1],
                ["Sackans", 1],
            ]
            self.products = [
                ["Bankors", 1],
            ]
            self.maxuses = 1
        elif self.id == 13: # Broot Altar
            self.recipe = [
                ["Postans", 2],
                ["Sackans", 2],
                ["Daffans", 1],
            ]
            self.products = [
                ["Rangors", 1],
            ]
            self.maxuses = 1
        elif self.id == 14: # Cleansing Altar
            self.recipe = [
                ["Xendans", 1],
                ["Clots", 2],
            ]
            self.products = [
                ["Verdans", 1],
            ]
            self.maxuses = 2
        elif self.id == 15: # Slop Altar
            self.recipe = [
                ["Slops", 5],
            ]
            self.products = [
                [random.choice(GQ0), 1],
            ]
            self.maxuses = 7
            while self.products[0][0] == "Slops":
                self.products[0][0] = random.choice(GQ0)
        elif self.id == 16: # Super Weapon Altar
            self.recipe = [
                ["Kollors", 1],
                ["Sheets", 10],
                ["Beets", 5],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Callans", 2],
            ]
            self.maxuses = 2
        elif self.id == 17: # Super Heal Altar
            self.recipe = [
                ["Kollors", 1],
                ["Bloods", 20],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Heeds", 10],
            ]
            self.maxuses = 3
        elif self.id == 18: # Super Defense Altar
            self.recipe = [
                ["Kollors", 1],
                ["Leeds", 10],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Daffans", 3],
            ]
            self.maxuses = 2
        elif self.id == 19: # Super Defense Altar
            self.recipe = [ # Extracting Altar
                ["Kollors", 1],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Feeds", 8],
            ]
            self.maxuses = 4
        elif self.id == 20: # Leed deconstruction Altar
            self.recipe = [
                ["Leeds", 2],
            ]
            self.products = [
                ["Clots", 5],
                ["Pots", 2],
            ]
            self.maxuses = 12
        elif self.id == 21: # Battery Altar
            self.recipe = [
                ["Radeans", 2],
                ["Daffans", 2],
                ["Postans", 5],
            ]
            self.products = [
                ["Kollors", 1],
            ]
            self.maxuses = 1
        elif self.id == 22: # Flower Altar
            self.recipe = [
                ["Verdans", 2],
                ["Xendans", 2],
                ["Radeans", 1],
            ]
            self.products = [
                ["Fencors", 1],
            ]
            self.maxuses = 1
        elif self.id == 23: # Crafting Altar
            self.recipe = [
                ["Shots", 2],
                ["Rocks", 2],
            ]
            self.products = [
                ["Leeds", 1],
            ]
            self.maxuses = 4
        elif self.id == 24: # Stomach Altar
            self.recipe = [
                ["Leeds", 2],
                ["Feeds", 2],
            ]
            self.products = [
                ["Postans", 1],
            ]
            self.maxuses = 3

    def chooseRandomAltar():
        AltarPool = [
            [0, 0], # [PoolWeight, Id]
            [40, 1],
            [15, 2],
            [20, 3],
            [10, 4],
            [8, 5],
            [5, 6],
            [9, 7],
            [10, 8],
            [6, 9],
            [8, 10],
            [8, 11],
            [2, 12],
            [2, 13],
            [4, 14],
            [6, 15],
            [1, 16],
            [1, 17],
            [1, 18],
            [1, 19],
            [4, 20],
            [3, 21],
            [2, 22],
            [4, 23],
        ]

        total = 0
        for altar in AltarPool:
            total += altar[0]

        RNG = random.randrange(1, total+1)
        id = 1
        for altar in AltarPool:
            RNG -= altar[0]
            if RNG <= 0:
                id = altar[1]
                break
        return id
class Room():
    def __init__(self, N, color, type, level, params, Width=13, Height=9):
        self.color = color
        self.type = type
        self.connections = []

        self.Greebles = []
        self.Raacs = []
        self.Traacs = []
        self.Broots = []
        self.Deploys = []
        self.Shops = []
        self.Enemies = []
        self.Altars = []

        self.width = Width
        self.height = Height
        self.objects = []
        for w in range(Width):
            self.objects.append([])
            for h in range(Height):
                self.objects[w].append([w, h, "", None])

        self.id = N
        self.level = level

        self.colored = False
        self.discovered = False


        self.populate(params)
    def findFreePosition(self, object, type, w=-1, h=-1):
        if w == -1:
            w = random.randrange(self.width)
        if h == -1:
            h = random.randrange(self.height)
        possible = 2
        while self.objects[w][h][3] and possible:
            w += 1
            if w >= self.width:
                w = 0
                h += 1
                if h >= self.height:
                    h = 0
                    possible -= 1
        if possible:
            self.objects[w][h][3] = object
            self.objects[w][h][2] = type

            if type == "greeble":
                self.Greebles.append(object)
            elif type == "broot":
                self.Broots.append(object)
            elif type == "deploy":
                self.Deploys.append(object)
            elif type == "raac":
                self.Raacs.append(object)
            elif type == "traac":
                self.Traacs.append(object)
            elif type == "shop":
                self.Shops.append(object)
            elif type == "enemy":
                self.Enemies.append(object)
            elif type == "altar":
                self.Altars.append(object)
        else:
            return
    def freeePosition(self, w, h):
        ob = self.objects[w][h][3]
        type = self.objects[w][h][2]
        if type == "greeble":
            self.Greebles.remove(ob)
        elif type == "broot":
            self.Broots.remove(ob)
        elif type == "deploy":
            self.Deploys.remove(ob)
        elif type == "raac":
            self.Raacs.remove(ob)
        elif type == "traac":
            self.Traacs.remove(ob)
        elif type == "shop":
            self.Shops.remove(ob)
        elif type == "enemy":
            self.Enemies.remove(ob)
        elif type == "altar":
            self.Altars.remove(ob)
        self.objects[w][h][3] = None
        self.objects[w][h][2] = ""
    def populate(self, params):
        if self.color == "red" and self.type == "normal":
            typee = random.randrange(1, 4)
            self.findFreePosition(Enemy(typee, self.level), "enemy")
        elif self.color == "red" and self.type == "plate":
            typee = random.randrange(1, 4)
            self.findFreePosition(Enemy(typee, self.level+2), "enemy")
            self.randomGreeble(1, self.level)
            self.randomGreeble(2, min(round(log2(self.level))-3, 0))
        elif self.color == "yellow" and self.type == "normal":
            temp1 = self.level
            self.randomGreeble(1, temp1+2)
        elif self.color == "yellow" and self.type == "plate":
            temp2 = self.level//5
            self.randomGreeble(2, temp2)
            self.randomGreeble(1, temp2*3)
        elif self.color == "black" and self.type == "normal":
            self.findFreePosition(Enemy(4, self.level), "enemy")
            RNG = random.randrange(10)
            if RNG <= 2:
                RNG = random.randrange(3)
                self.findFreePosition(Traac(RNG), "traac")
            else:
                self.findFreePosition(Raac(Raac.chooseRandomRaac()), "raac")
            self.acquire(["Feeds", 10+round(self.level*1.5)])
        elif self.color == "purple" and self.type == "normal":
            typee = Altar.chooseRandomAltar()
            self.findFreePosition(Altar(typee), "altar")
        elif self.color == "purple" and self.type == "plate":
            self.findFreePosition(Altar(0), "altar")
        elif self.color == "white" and self.type == "normal":
            return
        elif self.color == "gray" and self.type == "normal":
            temp = ceil(log2(self.level+1)) + 1
            self.randomGreeble(0, temp)
        elif self.color == "green" and self.type == "normal":
            temp = self.level*2 +4*params[0]
            while temp > 0:
                RNG = random.randrange(100)
                if RNG <= 5 and temp >= 6:
                    itemtype = "Traac"
                    temp -= 6
                elif RNG <= 20 and temp >= 5:
                    itemtype = "Raac"
                    temp -= 5
                elif RNG <= 40 and temp >= 3:
                    itemtype = "Broot"
                    temp -= 3
                else:
                    itemtype = "Greeble"
                    temp -= 1
                self.randomShop(itemtype, True)
        elif self.color == "green" and self.type == "plate":
            temp = self.level*2 +2*params[0]
            while temp > 0:
                self.randomShop("Greeble", False)
                temp -= 3
    def depopulate(self):
        for w in range(self.width):
            for h in range(self.height):
                self.freeePosition(w, h)
    def acquire(self, greeb):
        if greeb[1] == 0:
            return
        for w in range(self.width):
            for h in range(self.height):
                tile = self.objects[w][h]
                if tile[2] == "greeble" and tile[3][0] == greeb[0]:
                    tile[3][1] += greeb[1]
                    greeb[1] = 0
                    return
        self.findFreePosition(greeb, "greeble")
    def randomGreeble(self, quality, qtd):
        species = len(G[quality])
        Q = [0]*species
        for i in range(qtd):
            RNG = random.randrange(species)
            Q[RNG] += 1
        id = 0
        for key in G[quality]:
            self.acquire([key, Q[id]])
            id += 1
    def checkEnemyLife(self, player):

        Red = False
        for enemy in self.Enemies:
            if enemy.hp > 0:
                Red = True
            elif enemy.id != 0:
                enemy.id = 0
                enemyEnergy = enemy.mhp*enemy.df + enemy.speed*enemy.dmg
                enemy.dmg = 0



                EnemyLoot = 0
                BlackTest = None
                for raac in player.Raacs:
                    if raac.source == "EnemyKill" and enemyEnergy > 0:
                        raac.charge += raac.rate
                        enemyEnergy -= raac.rate
                        if raac.charge > raac.maxCharge:
                            enemyEnergy += (raac.charge-raac.maxCharge)
                            raac.charge = raac.maxCharge
                        if enemyEnergy < 0:
                            raac.charge += enemyEnergy
                            enemyEnergy = 0


                    if raac.name == "EnemyLoot":
                        EnemyLoot += 2*raac.level
                    elif raac.name == "BlackTest":
                        BlackTest = raac
                else:
                    EnemyLoot = 0



                for traac in player.Traacs:
                    if enemyEnergy > 20 and self.color != "black" or enemyEnergy > 40:
                        traac.charge += 1
                        enemyEnergy -= 20
                        if self.color == "black":
                            traac.charge += 2
                            if BlackTest and traac.charge < traac.maxCharge and BlackTest.charged():
                                traac.charge += BlackTest.level
                            enemyEnergy -= 40
                        if traac.charge > traac.maxCharge:
                            enemyEnergy += 20*(traac.charge-traac.maxCharge)
                            traac.charge = traac.maxCharge

                loot = floor(log(enemy.mhp+1, 4)) + EnemyLoot
                if loot > 0:
                    self.randomGreeble(0, loot)

        if self.color == "red" and not Red:
            self.color = "gray"
    def randomShop(self, itemtype, buy):
        # item = ["Raac", "Treasure", 10, "Pots"]

        if buy:
            if itemtype == "Greeble":
                RNG = random.randrange(0, 100)
                if RNG <= 1:
                    name = random.choice(GQ3)
                    value = 22
                elif RNG <= 35:
                    name = random.choice(GQ2)
                    value = 8
                else:
                    name = random.choice(GQ1)
                    value = 2
            elif itemtype == "Raac":
                RNG = random.randrange(len(raacimg))
                temp = Raac(RNG)
                name = temp.name
                value = raacValue[RNG]
            elif itemtype == "Traac":
                RNG = random.randrange(len(traacimg))
                temp = Traac(RNG)
                name = temp.name
                value = traacValue[RNG]
            elif itemtype == "Broot":
                RNG = random.randrange(1, len(brootNumber)-1)
                name = brootNumber[RNG]
                value = brootValue[RNG]

            RNG = random.randrange(100)
            if RNG <= 0:
                coin = random.choice(GQ1)
                cost = ceil(value*1/3)
            elif RNG <= 10:
                coin = random.choice(GQ0)
                cost = value
            else:
                coin = "Pots"
                cost = value
            amount = 1
        else:
            if itemtype == "Greeble":
                RNG = random.randrange(0, 100)
                if RNG <= 1:
                    name = random.choice(GQ3)
                    qtd = 1
                    value = 22
                elif RNG <= 35:
                    name = random.choice(GQ2)
                    qtd = random.randrange(3) + 1
                    value = 8
                else:
                    name = random.choice(GQ1)
                    qtd = random.randrange(6) + 1
                    value = 2
            coin = name
            name = "Pots"
            amount = value*qtd
            cost = qtd
        item = [itemtype, amount, name, cost, coin]
        self.findFreePosition(item, "shop")


class Broot():
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.alive = True
        self.generate()
    def generate(self):
        if self.name == "armed":
            self.hp = 10
            self.dmg = 4
            self.speed = 20
        elif self.name == "defends":
            self.hp = 15
            self.dmg = 1
            self.speed = 30
        elif self.name == "digests":
            self.hp = 25
            self.dmg = 1
            self.speed = 10
        elif self.name == "digs":
            self.hp = 10
            self.dmg = 1
            self.speed = 24
            self.action = 0
            self.cost = 3
        elif self.name == "deconstructs":
            self.hp = 20
            self.dmg = 1
            self.speed = 5
        self.mhp = self.hp
    def deploy(self, x, y, room):
        self.x = x
        self.y = y
        self.room = room
    def damage(self, qtd):
        self.hp -= qtd
        if self.hp <= 0 and self.alive:
            self.dmg = 0
            self.alive = False
    def chooseRandomBroot():
        BrootPool = [
            [0, 0], # [PoolWeight, Id]
            [45, "armed"],
            [30, "defends"],
            [15, "digests"],
            [12, "digs"],
            [18, "deconstructs"],
        ]

        total = 0
        for broot in BrootPool:
            total += broot[0]

        RNG = random.randrange(1, total+1)
        id = "armed"
        for broot in BrootPool:
            RNG -= broot[0]
            if RNG <= 0:
                id = broot[1]
                break

        # BrootPool[id][0] += 3
        return id
class Raac():
    def __init__(self, id):
        self.id = id
        self.level = 1

        self.charge = 0
        self.source = ""
        self.maxCharge = 0
        self.cost = 0
        self.rate = 0
        self.upgrades = [0, 0, 0]

        self.generate()
    def generate(self):
        if self.id == 0:
            self.name = "Treasure"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor divisible by 2, X Yellow Rooms will permanently be added to the pool."
            self.quality = 4

            self.source = "Floor"
            self.maxCharge = 1500
            self.cost = 80
            self.rate = 50
            self.upgrades = [500, 80, 50]
        elif self.id == 1:
            self.name = "BeetHeal"
            self.trigger = "Discover"
            self.description = "Every time you discover a room, X*20% chance for a Beet to be converted to a Heed+Pot if not at max."
            self.quality = 5

            self.source = "Discover"
            self.maxCharge = 500
            self.cost = 8
            self.rate = 12
            self.upgrades = [250, 0, 2]
        elif self.id == 2:
            self.name = "FencorRegen"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor. You get 3*X*Fencor Heeds."
            self.quality = 2

            self.source = "Floor"
            self.maxCharge = 500
            self.cost = 45
            self.rate = 50
            self.upgrades = [500, 45, 40]
        elif self.id == 3:
            self.name = "SaveThrow"
            self.trigger = "Damage"
            self.description = "If you take death damage, convert a Verdan into a Xerdan and add 3 Heeds to the blow. Only activates X times per floor."
            self.quality = 3
            self.used = 0

            self.source = "Floor"
            self.maxCharge = 2000
            self.cost = 35
            self.rate = 50
            self.upgrades = [500, 0, 10]
        elif self.id == 4:
            self.name = "EnemyLoot"
            self.trigger = "EnemyKill"
            self.description = "When an enemy dies, add 2*X Greebles Quality 0 to the room."
            self.quality = 7

            self.source = "EnemyKill"
            self.maxCharge = 3000
            self.cost = 15
            self.rate = 60
            self.upgrades = [750, 15, 10]
        elif self.id == 5:
            self.name = "Altar"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor divisible by 5, X Purple Rooms will permanently be added to the pool."
            self.quality = 4

            self.source = "Floor"
            self.maxCharge = 2000
            self.cost = 120
            self.rate = 60
            self.upgrades = [300, 120, 80]
        elif self.id == 6:
            self.name = "RoomConnectivity"
            self.trigger = "Floor"
            self.description = "Rooms are more connected"
            self.quality = 8

            self.source = "Floor"
            self.maxCharge = 3500
            self.cost = 125
            self.rate = 100
            self.upgrades = [1500, 50, 100]
        elif self.id == 7:
            self.name = "ColoredRoom"
            self.trigger = "Floor"
            self.description = "Random rooms can have their colors revealed"
            self.quality = 6

            self.source = "Floor"
            self.maxCharge = 250
            self.cost = 5
            self.rate = 20
            self.upgrades = [150, 0, 10]
        elif self.id == 8:
            self.name = "LuckyCharm"
            self.trigger = "Discover"
            self.description = "Quality 0 Greebles have chance to become Quality 1"
            self.quality = 5

            self.source = "Discover"
            self.maxCharge = 600
            self.cost = 20
            self.rate = 50
            self.upgrades = [200, 0, 20]
        elif self.id == 9:
            self.name = "Pottery"
            self.trigger = "Discover"
            self.description = "When discovering rooms, chance to transform Shots into Pots."
            self.quality = 3

            self.source = "Discover"
            self.maxCharge = 500
            self.cost = 5
            self.rate = 50
            self.upgrades = [150, 0, 20]
        elif self.id == 10:
            self.name = "ExtraStock"
            self.trigger = "Floor"
            self.description = "Shops have more quality."
            self.quality = 3

            self.source = "Floor"
            self.maxCharge = 1000
            self.cost = 20
            self.rate = 50
            self.upgrades = [400, 20, 25]
        elif self.id == 11:
            self.name = "SplashDamage"
            self.trigger = "Attack"
            self.description = "When attacking enemies, if there are enemies in adjacent rooms, deal 35% damage to X of them."
            self.quality = 5

            self.source = "EnemyKill"
            self.maxCharge = 2000
            self.cost = 15
            self.rate = 20
            self.upgrades = [700, 0, 20]
        elif self.id == 12:
            self.name = "RockCrest"
            self.trigger = "Defend"
            self.description = "If you have 2+X rocks, you receive X defense. On damage, Rocks break into Shots."
            self.quality = 4

            self.source = "Discover"
            self.maxCharge = 1000
            self.cost = 5
            self.rate = 10
            self.upgrades = [120, 0, 2]
        elif self.id == 13:
            self.name = "SlimeFest"
            self.trigger = "Floor"
            self.description = "Each Floor you turn X of each quality 0 Greebles into slime, and add X new gray rooms to the floor permanently."
            self.quality = 2

            self.source = "Floor"
            self.maxCharge = 300
            self.cost = 5
            self.rate = 10
            self.upgrades = [50, 0, 10]
        elif self.id == 14:
            self.name = "LeedQuest"
            self.trigger = "Floor"
            self.description = "Each Floor if you can, lose 3X Leeds, add X red rooms permanently."
            self.quality = 6

            self.source = "Floor"
            self.maxCharge = 600
            self.cost = 40
            self.rate = 60
            self.upgrades = [200, 30, 60]
        elif self.id == 15:
            self.name = "TraacBest"
            self.trigger = "Always"
            self.description = "Traac items have X more max charge."
            self.quality = 7

            self.source = "Floor"
            self.maxCharge = 1000
            self.cost = 60
            self.rate = 40
            self.upgrades = [400, 0, 30]
        elif self.id == 16:
            self.name = "AltarRest"
            self.trigger = "Floor"
            self.description = "If there is an unused altar at the end of the floor, consume it to gain 3X Heexs."
            self.quality = 4

            self.source = "Floor"
            self.maxCharge = 750
            self.cost = 40
            self.rate = 60
            self.upgrades = [250, 40, 60]
        elif self.id == 17:
            self.name = "BlackTest"
            self.trigger = "BossKill"
            self.description = "Killing a Boss gives +X charges to your Traacs"
            self.quality = 5

            self.source = "EnemyKill"
            self.maxCharge = 2500
            self.cost = 20
            self.rate = 45
            self.upgrades = [500, 20, 15]














        else:
            self.name = "ERROR"
            print("ERROR!")
        self.charge = self.maxCharge//2
    def chooseRandomRaac():
        RaacPool = [
            [20, 0],
            [30, 1],
            [20, 2],
            [20, 3],
            [20, 4],
            [20, 5],

            [20, 6],
            [20, 7],
            [20, 8],
            [20, 9],
            [20, 10],
            [20, 11],

            [20, 12],
            [20, 13],
            [20, 14],
            [20, 15],
            [20, 16],
            [20, 17],
        ]

        total = 0
        for raac in RaacPool:
            total += raac[0]

        RNG = random.randrange(1, total+1)
        id = 0
        for raac in RaacPool:
            RNG -= raac[0]
            if RNG <= 0:
                id = raac[1]
                break
        
        RaacPool[id][0] += round(len(RaacPool)*0.5)
        return id
    def namesID(name):
        if name == "Treasure": return 0
        elif name == "BeetHeal": return 1
        elif name == "FencorRegen": return 2
        elif name == "SaveThrow": return 3
        elif name == "EnemyLoot": return 4
        elif name == "Altar": return 5
        elif name == "RoomConnectivity": return 6
        elif name == "ColoredRoom": return 7
        elif name == "LuckyCharm": return 8
        elif name == "Pottery": return 9
        elif name == "ExtraStock": return 10
        elif name == "SplashDamage": return 11
    def charged(self, times=1): # This function will use up energy. Make it the last verification ALWAYS
        value = self.charge >= self.cost*times
        self.charge -= self.cost*value*times
        return value
    def upgrade(self):
        self.level += 1
        self.maxCharge += self.upgrades[0]
        self.cost += self.upgrades[1]
        self.rate += self.upgrades[2]
class Traac():
    def __init__(self, id):
        self.id = id
        self.level = 1
        self.generate()
    def generate(self):

        self.charge = 0
        if self.id == 0:
            self.name = "AltarBoost"
            self.maxCharge = 3
            self.cost = 3
            self.progression = 4
            self.description = "If an unused altar has 6 or more charges, increase it by 1."
            self.quality = 4
        elif self.id == 1:
            self.name = "Crystalize"
            self.maxCharge = 7
            self.cost = 4
            self.progression = 5
            self.description = "Convert a Heed into a Beet."
            self.quality = 5
        elif self.id == 2:
            self.name = "Bomb"
            self.maxCharge = 6
            self.cost = 5
            self.progression = 4
            self.description = "Deal 10X damage on the room."
            self.quality = 2
        else:
            self.name = "ERROR"
            print("ERROR!")
    def upgrade(self):
        self.maxCharge += self.progression
    def chooseRandomTraac():
        TraacPool = [
            [20, 0],
            [20, 1],
            [20, 2],
        ]

        total = 0
        for Traac in TraacPool:
            total += Traac[0]

        RNG = random.randrange(1, total+1)
        id = 0
        for Traac in TraacPool:
            RNG -= Traac[0]
            if RNG <= 0:
                id = Traac[1]
                break

        TraacPool[id][0] += 3
        return id
    def namesID(name):
        if name == "AltarBoost": return 0
        elif name == "Crystalize": return 1
        elif name == "Bomb": return 2


class Floor():
    def __init__(self, level, rooms, broots, params):
        self.level = level
        self.size = 10+2*floor(self.level**1.3) +params[2]
        self.Rooms = []
        self.generate(rooms, broots, params)
    def generate(self, temp, broots, params):
        connectivity = params[0]
        shopStock = params[1]

        rooms = {}
        for key in temp:
            rooms[key] = temp[key]

        self.Rooms.append(Room(0, "white", "normal", self.level, [0]))
        self.size -= 1
        rooms["normal_white"] -= 1

        N = 1
        while self.size > 1:
            self.size -= 1
            newroom = Room(N, "gray", "normal", self.level, [0])
            N += 1
            self.Rooms.append(newroom)
        self.Rooms.append(Room(N, "black", "normal", self.level, [0]))
        self.size -= 1
        rooms["normal_black"] -= 1
        N += 1


        for key in rooms:
            while rooms[key] > 0:
                # print(f"{key} - {rooms[key]}")
                RNG = random.randrange(N)
                loop = 0
                while self.Rooms[RNG].color != "gray":
                    RNG -= 1
                    if RNG < 0:
                        if loop == 1:
                            loop = 2
                            break
                        else:
                            RNG = len(self.Rooms)-1
                            loop = 1
                if loop == 2:
                    break
                rooms[key] -= 1
                type, color = key.split("_")
                self.Rooms[RNG].color = color
                self.Rooms[RNG].type = type
                self.Rooms[RNG].depopulate()
                self.Rooms[RNG].populate([shopStock])
                if color == "yellow":
                    for key2 in broots:
                        if broots[key2] > 0:
                            self.Rooms[RNG].findFreePosition(Broot(key2), "broot")
                            broots[key2] -= 1
                            break

        for room in self.Rooms:
            for i in range(connectivity):
                RNG = random.randrange(0, N)
                if RNG != room.id and RNG not in room.connections:
                    room.connections.append(RNG)
                    self.Rooms[RNG].connections.append(room.id)
        
        if N-1 in self.Rooms[0].connections:
            self.Rooms[0].connections.remove(N-1)
            self.Rooms[N-1].connections.remove(0)


class Game():
    def __init__(self):
        self.wprites = []
        self.screen = display.set_mode((1600, 800))
        self.clock = time.Clock()
        display.set_caption('GreeblesMania 0.4 - Actual Rooms Update')
        self.size = 64
        self.player = Player()
    def escreverCanto(self, texto, tam, pos):
        largeText = font.Font('freesansbold.ttf', tam)
        TextSurf = largeText.render(texto, True, (0, 0, 0))
        self.screen.blit(TextSurf, pos)
    def escrever(self, texto, tam, pos):
        largeText = font.Font('freesansbold.ttf', tam)
        TextSurf = largeText.render(texto, True, (0, 0, 0))
        TextRect = TextSurf.get_rect()
        TextRect.center = ((pos[0], pos[1]))
        self.screen.blit(TextSurf, TextRect)
    def run(self):
        self.rooms = {}

        self.rooms["normal_white"] = 1
        self.rooms["normal_yellow"] = 2
        self.rooms["normal_purple"] = 1
        self.rooms["normal_red"] = -1
        self.rooms["normal_green"] = 4
        self.rooms["normal_orange"] = 0
        self.rooms["normal_black"] = 1

        self.rooms["plate_white"] = 0
        self.rooms["plate_yellow"] = 0
        self.rooms["plate_green"] = 0
        self.rooms["plate_red"] = 0
        self.rooms["plate_purple"] = 0
        self.rooms["plate_gray"] = 0
        self.rooms["plate_orange"] = 0
        self.rooms["plate_black"] = 0



        self.broots = {}
        for broot in brootimg:
            self.broots[broot] = 0
        self.broots["armed"] = 2
        self.broots["defends"] = 1

        self.params = [0, 0, 0]
        self.currentFloor = Floor(0, self.rooms, copy.deepcopy(self.broots), self.params)

        self.level = -1
        self.newFloor()

        plate_yellowCost = 5

        while self.player.Greebles["Heeds"] >= 0:
            value = self.update()
            if value == -1:
                return
            elif value == 1:
                self.newFloor()
    def newFloor(self):
        self.level += 1




        alivecount = 0
        altarcount = 0
        anvilcount = 0
        for rm in self.currentFloor.Rooms:
            if rm.color == "green" and not rm.discovered:
                RNG = random.randrange(100)
                if RNG <= 25:
                    self.rooms["normal_green"] -= 1
                    self.rooms["plate_green"] += 1
            if rm.color == "plate_green" and not rm.discovered:
                RNG = random.randrange(100)
                if RNG <= 25:
                    self.rooms["normal_green"] += 1
                    self.rooms["plate_green"] -= 1
            if rm.color == "red":
                alivecount += 1
            if rm.color == "purple":
                for altar in rm.Altars:
                    if altar.uses == altar.maxuses:
                        if altar.id == 0:
                            anvilcount += 1
                        else:
                            altarcount += 1
        RNG = random.randrange(100)
        if RNG < altarcount*5:
            self.rooms["normal_purple"] -= 1
            self.rooms["plate_purple"] += 1
        if anvilcount > 0:
            self.rooms["normal_purple"] += 1
            self.rooms["plate_purple"] -= 1
        if alivecount == 0 and self.level > 2:
            self.rooms["plate_red"] += 1
            self.rooms["normal_red"] -= 1
        self.rooms["normal_yellow"] += 1
        self.rooms["normal_red"] += 1
        if self.level % 2 == 0:
            for raac in self.player.Raacs:
                if raac.name == "Treasure" and raac.charged():
                    self.rooms["normal_yellow"] += raac.level
                    break
        if self.level % 3 == 0:
            self.rooms["normal_purple"] += 1
            self.rooms["normal_red"] += 1
        if self.level % 4 == 0 and self.level != 0:
            self.rooms["normal_green"] += 1
        if self.level % 5 == 0:
            if self.rooms["normal_yellow"] > plate_yellowCost:
                self.rooms["normal_yellow"] -= 5
                self.rooms["plate_yellow"] += 1
                plate_yellowCost += self.level//3
            
            for raac in self.player.Raacs:
                if raac.name == "Altar":
                    self.rooms["normal_purple"] += raac.level
            self.rooms["normal_red"] += 1

        if self.level != 0:
            typee = Broot.chooseRandomBroot()
            self.broots[typee] += 1

        self.player.Greebles["Kollors"] += self.player.Greebles["Kollors_off"]
        self.player.Greebles["Kollors_off"] = 0





        floorEnergy = 100*self.level

        coloredRack = None


        connectivity = 3
        extraStock = 0
        coloredLevel = 0
        for raac in self.player.Raacs:
            if raac.source == "Floor" and floorEnergy > 0:
                raac.charge += raac.rate
                floorEnergy -= raac.rate
                if raac.charge > raac.maxCharge:
                    floorEnergy += (raac.charge-raac.maxCharge)
                    raac.charge = raac.maxCharge
                if floorEnergy < 0:
                    raac.charge += floorEnergy
                    floorEnergy = 0
                

            if raac.name == "RoomConnectivity" and raac.charged():
                raac.cost += 15
                connectivity += raac.level
            elif raac.name == "ColoredRoom" and raac.charged():
                coloredLevel += raac.level
                coloredLevel += self.player.Greebles["Tannors"]
                coloredRack = raac
            elif raac.name == "ExtraStock" and raac.charged():
                extraStock += raac.level
            elif raac.name == "LeedQuest" and self.player.Greebles["Leeds"] >= 3*raac.level and raac.charged():
                self.rooms["normal_red"] += raac.level
                self.player.Greebles["Leeds"] -= 3*raac.level

            elif raac.name == "AltarRest":
                if altarcount >= raac.level and raac.charged():
                    self.player.acquire(["Heexs", 3*raac.level])
            elif raac.name == "SaveThrow":
                raac.used = 0
            elif raac.name == "FencorRegen":
                amount = raac.level*3
                temp = self.player.Greebles["Fencors"]
                while temp > 0 and self.player.Greebles["Heeds"] < self.player.Greebles["Verdans"] and raac.charged():
                    temp -= 1
                    self.player.acquire(["Heeds", amount])
            elif raac.name == "SlimeFest":
                for greeb in GQ0:
                    if self.player.Greebles[greeb] >= raac.level:
                        self.player.Greebles[greeb] -= raac.level
                        self.player.acquire(["Slops", raac.level])
                self.params[2] += raac.level

        self.params[0] = connectivity
        self.params[1] = extraStock
        self.currentFloor = Floor(self.level, self.rooms, copy.deepcopy(self.broots), self.params)
        for rm in self.currentFloor.Rooms:
            RNG = random.randrange(100)
            if RNG < coloredLevel*10 and coloredRack.charged():
                rm.colored = True


        self.player.room = 0
        self.currentFloor.Rooms[0].discovered = True
        self.currentFloor.Rooms[0].colored = True
    def update(self):
        display.flip()
        mouseXY = mouse.get_pos()
        mouseRect = Rect(mouseXY[0], mouseXY[1], 1, 1)
        game.screen.fill((100, 70, 40))
        options = []
        infoObject = None
        infoType = ""
        room = self.currentFloor.Rooms[self.player.room]


        draw.rect(game.screen, (0, 0, 0), (35, 175, self.size*13+10, self.size*9+10), 5)
        brickimg = bricksimg[room.type+"_"+room.color]
        for x in range(13):
            for y in range(9):
                self.screen.blit(brickimg, (40+self.size*x, 180+self.size*y))





        # Room information
        for w in range(room.width):
            for h in range(room.height):
                object = room.objects[w][h]
                x = 40+self.size*w
                y = 180+self.size*h

                rect = Rect(x, y, self.size, self.size)
                if object[2] == "enemy":
                    self.screen.blit(enemiesimg[object[3].id], (x, y))
                    if object[3].id == 0:
                        options.append([rect, (w, h), "clean"])
                    else:
                        options.append([rect, (w, h), "attack"])
                elif object[2] == "altar":
                    if object[3].id == 0:
                        self.screen.blit(altar2img, (x, y))
                        self.escreverCanto(f"{object[3].uses}/{object[3].maxuses}", 15, (x+5, y+self.size+5))

                        xtemp = 16
                        ytemp = 1
                        id = 0
                        for raac in self.player.Raacs:
                            rect = Rect(self.size*xtemp, self.size*ytemp, self.size, self.size)
                            options.append([rect, (w, h, id), "break"])
                            id += 1
                            xtemp += 1
                            if xtemp >= 24:
                                xtemp = 16
                                ytemp += 1
                    else:
                        self.screen.blit(altarimg, (x, y))
                        # self.escreverCanto(f"{object[3].uses}/{object[3].maxuses}", 15, (x+5, y+5+self.size))

                        options.append([rect, (w, h), "altar"])
                elif object[2] == "greeble":
                    self.screen.blit(greebleimg[object[3][0]], (x, y))
                    if len(room.Enemies) == 0:
                        options.append([rect, (w, h), "greeble"])
                    self.escreverCanto(f"x{object[3][1]}", 15, (x+self.size-20, y))
                elif object[2] == "broot":
                    self.screen.blit(brootimg[object[3].name], (x, y))
                    options.append([rect, (w, h), "broot"])
                elif object[2] == "deploy":
                    if object[3].alive:
                        self.screen.blit(brootimg[object[3].name], (x, y))
                    else:
                        self.screen.blit(brootimg["DEAD"], (x, y))
                elif object[2] == "shop":
                    if object[3][0] == "Broot":
                        self.screen.blit(brootimg[object[3][2]], (x, y))
                    elif object[3][0] == "Raac":
                        self.screen.blit(raacimg[object[3][2]], (x, y))
                    elif object[3][0] == "Traac":
                        self.screen.blit(traacimg[object[3][2]], (x, y))
                    elif object[3][0] == "Greeble":
                        self.screen.blit(greebleimg[object[3][2]], (x, y))
                        self.escrever(f"x{object[3][1]}", 15, (x-15+self.size, y-5+self.size))
                
                    # self.screen.blit(greebleimg[object[3][4]], (x, y+self.size))
                    # self.escrever(f"x{object[3][3]}", 15, (x-15+self.size, y+10+2*self.size))
        
                    options.append([rect, (w, h), "buy"])
                elif object[2] == "raac":
                    self.screen.blit(raacimg[object[3].name], (x, y))
                    self.escrever(f"{object[3].id}", 15, (x, y+self.size))
                    options.append([rect, (w, h), "raac"])
                elif object[2] == "traac":
                    self.screen.blit(traacimg[object[3].name], (x, y))
                    options.append([rect, (w, h), "traac"])


                if Colide(mouseRect, rect):
                    infoObject = object[3]
                    infoType = object[2]








        # HUD
        x = 1
        y = -1
        for rm in room.connections:
            rm = self.currentFloor.Rooms[rm]
            draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)

            if rm.colored:
                color = colorkey[rm.color]
                draw.rect(game.screen, color, (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            else:
                draw.rect(game.screen, (255, 255, 255), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            if rm.discovered:
                if rm.type == "plate":
                    draw.rect(game.screen, (0, 0, 0), (40+self.size*x+5, 160+self.size*y+5, self.size-10, self.size-10), 2)
                self.escrever(str(rm.id), 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))



                leave = False
                for w in range(rm.width):
                    for h in range(rm.height):
                        object = rm.objects[w][h]
                        if object[2] == "greeble":
                            draw.circle(self.screen, (0, 0, 0), (40+self.size*x+5, 160+self.size*y+5), 5)
                            if self.player.Highlights[object[3][0]]:
                                draw.circle(self.screen, (100, 240, 150), (40+self.size*x+5, 160+self.size*y+5), 5)
                                leave = True
                                break
                    if leave:
                        break

            else:
                self.escrever("?", 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
            options.append([rect, rm.id, "walk"])
            x += 1

            if room.color == "black" and len(room.Enemies) == 0:
                draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)
                draw.rect(game.screen, (255, 255, 255), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
                self.escrever("Gate", 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
                rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
                options.append([rect, 0, "next"])

        x = 2
        y = -2
        for i in range(self.player.Greebles["Bankors"]):
            draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)
            draw.rect(game.screen, (255, 255, 0), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            x += 1
        x = 2
        for traac in self.player.Traacs:
            if traac.charge == traac.maxCharge:
                draw.rect(game.screen, (0, 255, 0), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            self.screen.blit(traacimg[traac.name], (40+self.size*x, 160+self.size*y))
            self.escrever(f"{traac.level}", 25, (40+self.size*x+self.size//2, 160+self.size*y-10))
            rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
            options.append([rect, x-2, "active"])
            if Colide(mouseRect, rect):
                infoObject = traac
                infoType = "traac"
            x += 1


        x = 15
        y = 1
        for raac in self.player.Raacs:
            draw.rect(game.screen, (0, 0, 0), (40+self.size*x, self.size*y, self.size, self.size), 1)
            color = (255, 255, 0)
            if raac.id == 3 and raac.used == raac.level:
                color = (0, 0, 0)
            elif raac.charge < raac.cost:
                color = (255, 0, 0)
            elif raac.charge >= 0.9*raac.maxCharge:
                color = (0, 0, 255)

            draw.rect(game.screen, color, (40+self.size*x+1, self.size*y+1, self.size-2, self.size-2))
            self.screen.blit(raacimg[raac.name], (40+self.size*x, self.size*y))

            rect = Rect(40+self.size*x, self.size*y, self.size, self.size)
            if Colide(rect, mouseRect):
                infoObject = raac
                infoType = "raac"


            x += 1
            if x >= 24:
                x = 13
                y += 1



        x = 0
        y = -2
        draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)
        draw.rect(game.screen, (0, 255, 0), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
        if len(self.player.Broots) > 0 and self.player.selectedBroot < len(self.player.Broots) and self.player.selectedBroot >= 0:
            broot = self.player.Broots[self.player.selectedBroot]
            self.screen.blit(brootimg[broot.name], (40+self.size*x, 160+self.size*y))
            rect = [40+self.size*x, 160+self.size*y, self.size, self.size]
            if Colide(mouseRect, rect):
                infoObject = broot
                infoType = "broot"
        self.escrever(f"{len(self.player.Broots)}/{self.player.Greebles["Rangors"]}", 25, (40+self.size*x+self.size//2, 160+self.size*(y+1)+10))


        x = 28
        y = 6
        self.size = 32
        for rm in self.currentFloor.Rooms:
            draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)

            if rm.colored:
                color = colorkey[rm.color]
                draw.rect(game.screen, color, (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            else:
                draw.rect(game.screen, (255, 255, 255), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            if rm.discovered:
                if rm.type == "plate":
                    draw.rect(game.screen, (0, 0, 0), (40+self.size*x+2, 160+self.size*y+2, self.size-4, self.size-4), 1)
                self.escrever(str(rm.id), 12, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
                rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
                options.append([rect, rm.id, "walk"])


                leave = False
                for w in range(rm.width):
                    for h in range(rm.height):
                        object = rm.objects[w][h]
                        if object[2] == "greeble":
                            draw.circle(self.screen, (0, 0, 0), (40+self.size*x+5, 160+self.size*y+5), 5)
                            if self.player.Highlights[object[3][0]]:
                                draw.circle(self.screen, (100, 240, 150), (40+self.size*x+5, 160+self.size*y+5), 5)
                                leave = True
                                break
                    if leave:
                        break

            else:
                self.escrever("?", 12, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            x += 1
            if x > 47:
                x = 28
                y += 1
        self.size = 64







        self.screen.blit(greebleimg["Beets"], (40+10*self.size, 20))
        self.escreverCanto(f"x{self.player.Greebles["Beets"]}/{self.player.Greebles["Radeans"]}", 15, (40+10*self.size, 20+self.size))
        self.screen.blit(greebleimg["Heeds"], (40+11*self.size, 20))
        self.escreverCanto(f"x{self.player.Greebles["Heeds"]}/{self.player.Greebles["Verdans"]}", 15, (40+11*self.size, 20+self.size))
        self.screen.blit(greebleimg["Feeds"], (40+12*self.size, 20))
        self.escreverCanto(f"x{self.player.Greebles["Feeds"]}/{self.player.Greebles["Postans"]}", 15, (40+12*self.size, 20+self.size))


        self.escreverCanto(f"Floor: {self.currentFloor.level}", 25, (50+13*self.size, 20))
        self.escreverCanto(f"Room: {room.id}", 25, (50+13*self.size, 45))



        x = 14
        y = 5
        draw.rect(self.screen, (0, 0, 0), [40+self.size*x, 180+self.size*y, self.size*10, self.size*4])
        draw.rect(self.screen, (200, 200, 200), [40+self.size*x+2, 180+self.size*y+2, self.size*10-4, self.size*4-4])

        if infoObject:
            x = 40+self.size*x + 5
            y = 180+self.size*y + 5
            if infoType == "traac":

                self.escreverCanto(f"{infoObject.name} Lvl. {infoObject.level}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Charge: {infoObject.charge}/{infoObject.maxCharge}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Cost: {infoObject.cost}", 20, (x, y))
                y += 20

                self.escreverCanto(f"{infoObject.description}", 20, (x, y))
                y += 20
            elif infoType == "raac":
                self.escreverCanto(f"{infoObject.name} Lvl. {infoObject.level}", 20, (x, y))
                y += 20

                self.escreverCanto(f"{infoObject.description}", 20, (x, y))
                y += 20

                if infoObject.name == "SaveThrow":
                    self.escreverCanto(f"[{infoObject.level - infoObject.used}] Use(s) left", 20, (x, y))
                    y += 20
            elif infoType == "greeble":
                self.escreverCanto(f"{infoObject[0]} x {infoObject[1]}", 20, (x, y))
                y += 20
            elif infoType == "enemy":
                self.escreverCanto(f"{infoObject.name}", 20, (x, y))
                y += 20

                self.escreverCanto(f"HP: {infoObject.hp}/{infoObject.mhp}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Dmg: {infoObject.dmg}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Df: {infoObject.df}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Speed: {infoObject.speed} [{infoObject.turn}/{infoObject.playerTurn}]", 20, (x, y))
                y += 20
            elif infoType == "altar":
                # self.escreverCanto(f"{infoObject.name}", 20, (x, y))
                # y += 20

                self.escreverCanto(f"Uses: {infoObject.uses}/{infoObject.maxuses}", 20, (x, y))
                y += 20

                # self.escreverCanto(f"Rarity: {infoObject.rarity}", 20, (x, y))
                # y += 20

                self.escreverCanto(f"Requires: ", 20, (x, y))
                x += self.size*1.5
                for greeb in infoObject.recipe:
                    draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 1)
                    self.screen.blit(greebleimg[greeb[0]], (x, y))
                    self.escrever(f"x{greeb[1]}", 20, (x+self.size//2, y+self.size+10))
                    x += self.size
                y += self.size+25
                x -= self.size*(len(infoObject.recipe)+1.5)

                
                self.escreverCanto(f"Produces: ", 20, (x, y))
                x += self.size*1.5
                for greeb in infoObject.products:
                    draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 1)
                    self.screen.blit(greebleimg[greeb[0]], (x, y))
                    self.escrever(f"x{greeb[1]}", 20, (x+self.size//2, y+self.size+10))
                    x += self.size
            elif infoType == "shop":
                self.escreverCanto(f"{infoObject[0]} - {infoObject[2]} x{infoObject[1]}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Costs: ", 20, (x, y))
                x += self.size
                draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 1)
                self.screen.blit(greebleimg[infoObject[4]], (x, y))
                x += self.size//2
                y += self.size+10
                self.escrever(f"x{infoObject[3]}", 20, (x, y))
                y += 20
            elif infoType == "broot":
                self.escreverCanto(f"{infoObject.name}", 20, (x, y))
                y += 20

                self.escreverCanto(f"HP: {infoObject.hp}/{infoObject.mhp}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Power: {infoObject.dmg}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Speed: {infoObject.speed}", 20, (x, y))
                y += 20
            elif infoType == "deploy":
                self.escreverCanto(f"{infoObject.name}", 20, (x, y))
                y += 20

                self.escreverCanto(f"HP: {infoObject.hp}/{infoObject.mhp}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Power: {infoObject.dmg}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Speed: {infoObject.speed}", 20, (x, y))
                y += 20

        # CONTROL
        action = False
        parameter = 0




        for ev in event.get():
            if (ev.type == QUIT):
                return -1
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == BUTTON_LEFT:
                    for option in options:
                        if Colide(option[0], mouseRect):
                            action = option[2]
                            parameter = option[1]
                if ev.button == BUTTON_RIGHT:
                    w = mouseRect.x
                    h = mouseRect.y
                    w -= 40
                    h -= 160
                    w = w//self.size
                    h = h//self.size
                    if w >= 0 and w <= 13 and h >= 0 and h <= 9:
                        action = "deploy"
                        parameter = (w, h)
            elif ev.type == KEYDOWN:
                if ev.key == K_1:
                    self.player.selectedBroot -= 1
                if ev.key == K_2:
                    self.player.selectedBroot += 1
                if ev.key == K_SPACE:
                    if len(room.Enemies) == 0:
                        for w in range(room.width):
                            for h in range(room.height):
                                object = room.objects[w][h]
                                if object[2] == "greeble":
                                    qtd = self.player.acquire(object[3])
                                    object[3][1] = qtd
                                    if object[3][1] == 0:
                                        room.freeePosition(w, h)
                if self.player.selectedBroot >= len(self.player.Broots):
                    self.player.selectedBroot = 0
                elif self.player.selectedBroot < 0:
                    self.player.selectedBroot = len(self.player.Broots)-1
                if ev.key == K_TAB:
                    self.showGreebles()


        if action == "walk":
            self.walkRoom(parameter)
            self.player.walk()
        elif action == "attack":
            self.activate(room.id)
        elif action == "altar":
            altar = room.objects[parameter[0]][parameter[1]][3]
            if altar.uses > 0:
                for rec in altar.recipe:
                    if self.player.Greebles[rec[0]] < rec[1]:
                        break
                else:
                    altar.uses -= 1
                    for rec in altar.recipe:
                        self.player.Greebles[rec[0]] -= rec[1]
                    for prod in altar.products:
                        qtd = self.player.acquire(prod)
                        if qtd > 0:
                            room.acquire(greeb, "greeble")
        elif action == "break":
            altar = room.objects[parameter[0]][parameter[1]][3]
            if altar.uses > 0:
                altar.uses -= 1

                raac = self.player.Raacs.pop(parameter[2])
                room.randomGreeble(2, raac.level*3)
        elif action == "clean":
            room.freeePosition(parameter[0], parameter[1])
        elif action == "next":
            return 1
        elif action == "active":
            if self.player.Traacs[parameter].charge >= self.player.Traacs[parameter].cost:
                sucess = False
                if self.player.Traacs[parameter].name == "AltarBoost":
                    for altar in room.Altars:
                        if altar and altar.uses == altar.maxuses and altar.uses >= 5:
                            altar.uses += 1
                            altar.maxuses += 1
                            sucess = True
                elif self.player.Traacs[parameter].name == "Crystalize" and self.player.Greebles["Heeds"] > 0 and self.player.Greebles["Beets"] < self.player.Greebles["Radeans"]:
                    self.player.Greebles["Heeds"] -= 1
                    self.player.acquire(["Beets", 1])
                    sucess = True
                elif self.player.Traacs[parameter].name == "Bomb":
                    for w in range(room.width):
                        for h in range(room.height):
                            if room.objects[w][h][2] == "enemy":
                                enemy = room.objects[w][h][3]
                                enemy.hp -= 10*self.player.Traacs[parameter].level
                                sucess = True
                            room.checkEnemyLife(self.player)
                if sucess:
                    self.player.Traacs[parameter].charge -= self.player.Traacs[parameter].cost
        elif action == "deploy" and len(self.player.Broots) > 0:
            broot = self.player.Broots.pop(self.player.selectedBroot)
            broot.deploy(parameter[0], parameter[1], room)
            room.findFreePosition(broot, "deploy", parameter[0], parameter[1])
            self.player.selectedBroot -= 1
            if self.player.selectedBroot < 0:
                self.player.selectedBroot = 0
        elif action == "buy":
            item = room.objects[parameter[0]][parameter[1]][3]
            if self.player.Greebles[item[4]] >= item[3]:
                room.freeePosition(parameter[0], parameter[1])
                if item[0] == "Greeble":
                    qtd = self.player.acquire([item[2], item[1]])
                    room.acquire([item[2], qtd])
                elif item[0] == "Broot":
                    if len(self.player.Broots) < self.player.Greebles["Rangors"]:
                        self.player.Broots.append(Broot(item[2]))
                    else:
                        room.findFreePosition("broot", Broot(item[2]), parameter[0], parameter[1])
                elif item[0] == "Raac":
                    room.objects[parameter[0]][parameter[1]][3] = Raac(Raac.namesID(item[2]))
                    room.objects[parameter[0]][parameter[1]][2] = "raac"
                elif item[0] == "Traac":
                    room.objects[parameter[0]][parameter[1]][3] = Traac(Traac.namesID(item[2]))
                    room.objects[parameter[0]][parameter[1]][2] = "traac"

                self.player.Greebles[item[4]] -= item[3]

        enemyAlive = False
        for w in range(room.width):
            for h in range(room.height):
                if room.objects[w][h][2] == "enemy" and room.objects[w][h][3].hp > 0:
                    enemyAlive = True
        if not enemyAlive:
            if action == "traac":
                traac = room.objects[parameter[0]][parameter[1]][3]
                traac = self.player.acquireTraac(traac)
                room.freeePosition(parameter[0], parameter[1])
                if traac:
                    room.findFreePosition(traac, "traac", parameter[0], parameter[1])
            elif action == "greeble":
                greeb = room.objects[parameter[0]][parameter[1]][3]
                qtd = self.player.acquire(greeb)
                if qtd == 0:
                    room.freeePosition(parameter[0], parameter[1])
                else:
                    room.objects[parameter[0]][parameter[1]][3][1] = qtd
            elif action == "raac":
                raac = room.objects[parameter[0]][parameter[1]][3]
                got = self.player.acquireRaac(raac)
                if got:
                    room.freeePosition(parameter[0], parameter[1])
            elif action == "broot":
                if len(self.player.Broots) < self.player.Greebles["Rangors"]:
                    self.player.Broots.append(room.objects[parameter[0]][parameter[1]][3])
                    room.freeePosition(parameter[0], parameter[1])
            

        self.clock.tick(30)
    def walkRoom(self, step):
        if not self.currentFloor.Rooms[step].discovered:
            if self.player.Greebles["Feeds"] > 0:
                self.player.Greebles["Feeds"] -= 1
            else:
                self.player.Greebles["Heeds"] -= 1

            roomEnergy = 15*self.level
            lucklevel = 0
            luckCharmRaac = None
            RNG = random.randrange(100)
            for raac in self.player.Raacs:
                if raac.source == "Floor" and roomEnergy > 0:
                    raac.charge += raac.rate
                    roomEnergy -= raac.rate
                    if raac.charge > raac.maxCharge:
                        roomEnergy += (raac.charge-raac.maxCharge)
                        raac.charge = raac.maxCharge
                    if roomEnergy < 0:
                        raac.charge += roomEnergy
                        roomEnergy = 0

                if raac.name == "LuckyCharm":
                    luckCharmRaac = raac
                    lucklevel += raac.level
                    lucklevel += self.player.Greebles["Tannors"]
                elif raac.name == "Pottery":
                    levelPot = raac.level
                    while RNG < levelPot*4:
                        if self.player.Greebles["Shots"] > 0 and raac.charged():
                            self.player.Greebles["Shots"] -= 1
                            self.player.acquire(["Pots", 1])
                        levelPot -= 25
                        RNG = random.randrange(100)
                elif raac.name == "BeetHeal":
                    if RNG <= 20*raac.level and self.player.Greebles["Heeds"] < self.player.Greebles["Verdans"] and self.player.Greebles["Beets"] > 0 and raac.charged():
                        self.player.Greebles["Beets"] -= 1
                        self.player.acquire(["Heeds", 1])
                        self.player.acquire(["Pots", 1])

            for greeb in self.currentFloor.Rooms[step].Greebles:
                if greeb[0] in GQ0:
                    RNG = random.randrange(100)
                    while RNG < lucklevel*10 and luckCharmRaac.charged():
                        RNG = random.randrange(100)
                        name = ""
                        if greeb[0] == "Shots":
                            name = "Feeds"
                        elif greeb[0] == "Bloods":
                            name = "Heeds"
                        elif greeb[0] == "Clots":
                            name = "Beets"
                        elif greeb[0] == "Pots":
                            name = "Leeds"
                        elif greeb[0] == "Rocks":
                            name = "Sheets"

                        lucklevel -= 1
                        greeb[1] -= 1
                        self.currentFloor.Rooms[step].acquire([name, 1])

                        if greeb[1] == 0:
                            for w in range(self.currentFloor.Rooms[step].width):
                                for h in range(self.currentFloor.Rooms[step].height):
                                    if self.currentFloor.Rooms[step].objects[w][h][3] == greeb:
                                        self.currentFloor.Rooms[step].freeePosition(w, h)
                                        break


            for rm in self.currentFloor.Rooms:
                for deploy in rm.Deploys:
                    if deploy.name == "digests":
                        for greeb in rm.Greebles:
                            if greeb[0] != "Slops":
                                greeb[1] -= 1
                                rm.acquire(["Slops", 1])
                                if greeb[1] == 0:
                                    rm.freeePosition(greeb[1], greeb[2])
                    elif deploy.name == "digs":
                        deploy.action += 1
                        if deploy.action >= deploy.cost:
                            deploy.action -= deploy.cost
                            RNG = random.randrange(100)
                            if RNG <= 20:
                                rm.acquire([random.choice(GQ1), 1])
                            else:
                                rm.acquire([random.choice(GQ0), 1])
                    elif deploy.name == "deconstructs":
                        for altar in rm.Altars:
                            if altar.uses > 0:
                                altar.uses -= 1
                                RNG = random.randrange(150)/altar.maxuses
                                if RNG <= 20:
                                    rm.acquire([random.choice(GQ0), 1])
                                elif RNG <= 40:
                                    rm.acquire([random.choice(GQ1), 1])
                                else:
                                    rm.acquire([random.choice(GQ2), 1])
                                break

        self.player.room = step
        self.activate(step)
    def activate(self, step):
        room = self.currentFloor.Rooms[step]
        room.discovered = True
        room.colored = True



        # Broots and Raacs
        SplashDamage = 0
        for raac in self.player.Raacs:
            if raac.name == "SplashDamage" and raac.charged(raac.level):
                SplashDamage += raac.level
        broot_attack = 0
        broot_defense = 0

        enemyDMG = 0
        for enemy in room.Enemies:
            enemyDMG += enemy.dmg

        for rm in room.connections:
            rm = self.currentFloor.Rooms[rm]
            for enemy in rm.Enemies:
                if enemy.hp > 0 and SplashDamage > 0:
                    enemy.hp -= floor((0.30+SplashDamage*0.05)*self.player.Greebles["Callans"])
                    SplashDamage -= 1
            rm.checkEnemyLife(self.player)
            for deploy in rm.Deploys:
                if deploy.name == "armed":
                    broot_attack += deploy.dmg
                    deploy.damage(enemyDMG)
                elif deploy.name == "defends":
                    broot_defense += deploy.dmg
                    deploy.damage(enemyDMG)


        attack = True
        for enemy in room.Enemies:
            if enemy.id == 0:
                continue
            enemy.hp -= broot_attack

            playerSpeed = self.player.Greebles["Sheets"]
            limit = max(enemy.speed, playerSpeed)
            while attack:
                enemy.turn += enemy.speed
                enemy.playerTurn += playerSpeed

                if enemy.playerTurn >= limit:
                    enemy.playerTurn -= limit
                    enemy.hp -= self.player.Greebles["Callans"]
                    room.acquire(["Bloods", 1])
                    attack = False

                if enemy.turn >= limit and enemy.hp > 0:
                    enemy.turn -= limit
                    qtd = max(0, enemy.dmg - broot_defense)
                    self.player.damage(qtd)

            room.checkEnemyLife(self.player)
    def showGreebles(self):
        tabPressed = True
        while tabPressed:
            display.flip()
            mouseXY = mouse.get_pos()
            mouseRect = Rect(mouseXY[0], mouseXY[1], 1, 1)
            game.screen.fill((80, 140, 60))
            options = []








            x = 40
            y = 50
            total = 0
            color = (255, 255, 255)
            for greeb in GQ0 + ["Slops"]:
                if self.player.Highlights[greeb]:
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, color, [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))
                rect = Rect([x-3, y-3, self.size+6, self.size+6])
                options.append([rect, greeb, "Highlights"])

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                total += self.player.Greebles[greeb]

                x += self.size+6
            total -= self.player.Greebles["Slops"]

            y += self.size
            x -= round((self.size+6)*3.5)
            draw.rect(self.screen, (170, 170, 170), [40-3, y+23, (self.size+6)*5, 20])
            draw.rect(self.screen, (0, 0, 0), [40-3, y+23, (self.size+6)*5, 20], 2)
            self.escrever(f"x{total}/{self.player.Greebles["Sackans"]*5}", 15, (x, y+33))

            x = 40
            y += self.size
            for greeb in GQ1:
                if self.player.Highlights[greeb]:
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, color, [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))
                rect = Rect([x-3, y-3, self.size+6, self.size+6])
                options.append([rect, greeb, "Highlights"])

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ2:
                if self.player.Highlights[greeb]:
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, color, [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))
                rect = Rect([x-3, y-3, self.size+6, self.size+6])
                options.append([rect, greeb, "Highlights"])

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ3:
                if self.player.Highlights[greeb]:
                    color = (255, 255, 0)
                else:
                    color = (255, 255, 255)
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, color, [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))
                rect = Rect([x-3, y-3, self.size+6, self.size+6])
                options.append([rect, greeb, "Highlights"])

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                x += self.size











            for ev in event.get():
                if (ev.type == QUIT):
                    return -1
                if ev.type == MOUSEBUTTONDOWN:
                    if ev.button == BUTTON_LEFT:
                        for opt in options:
                            if Colide(opt[0], mouseRect):
                                self.player.Highlights[opt[1]] = not self.player.Highlights[opt[1]]
                    if ev.button == BUTTON_RIGHT:
                        pass
                elif ev.type == KEYDOWN:
                    if ev.key == K_TAB:
                        tabPressed = not tabPressed





init()
game = Game()
game.run()


print("Killed!!")
print(f"At the dance floor {game.level}")









