from pygame import display, image, draw, time, font, init, transform, QUIT, KEYDOWN, K_TAB, MOUSEBUTTONDOWN, BUTTON_LEFT, BUTTON_RIGHT, event, mouse, Rect, KEYDOWN, K_1, K_2
import random
from math import ceil, floor, log2, log
import copy
from Functions import *

if True: # Pre-processing
    bricksimg = {
        "gray": image.load('Images/brick_gray.png'),
        "yellow": image.load('Images/brick_yellow.png'),
        "red": image.load('Images/brick_red.png'),
        "purple": image.load('Images/brick_purple.png'),
        "white": image.load('Images/brick_white.png'),
        "black": image.load('Images/brick_black.png'),
        "orange": image.load('Images/brick_orange.png'),
        "green": image.load('Images/brick_green.png'),

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
    ]
    traacValue = [
        9,
        7,
        15,
    ]
    brootValue = [
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

        "plate_red": (255, 0, 0),
        "plate_black": (0, 0, 0),
        "plate_yellow": (255, 255, 0),
        "plate_white": (255, 255, 255),
        "plate_purple": (255, 0, 255),
        "plate_gray": (100, 100, 100),
        "plate_orange": (200, 150, 0),
        "plate_green": (0, 255, 0),
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

        # Quality 0 Greebles - Trash greebles, sometimes used as ammo, usually used in crafting higher grade greebles
        self.Greebles["Shots"] = 0 # Used for crafting fuel
        self.Greebles["Bloods"] = 0 # Used for crafting health
        self.Greebles["Pots"] = 0 # Money, also used for some crafts
        self.Greebles["Clots"] = 0 # Advanced Shots
        self.Greebles["Rocks"] = 0 # Advanced Pots
        self.Greebles["Slops"] = 0 # Slop

        # Quality 1 Greebles - Resources, are expandable and are in constant use
        self.Greebles["Heeds"] = 0 # Health
        self.Greebles["Feeds"] = 0 # Fuel
        self.Greebles["Beets"] = 0 # Crystalized health
        self.Greebles["Leeds"] = 0 # Crafting material
        self.Greebles["Sheets"] = 0 # Speed and crafting

        # Quality 2 Greebles - Usually limits the greebles below them, works as storage, or stats
        self.Greebles["Verdans"] = 0 # Max Health
        self.Greebles["Postans"] = 0 # Max Fuel
        self.Greebles["Sackans"] = 0 # Max Q0 inventory*5
        self.Greebles["Callans"] = 0 # Damage
        self.Greebles["Daffans"] = 0 # Defense
        self.Greebles["Radeans"] = 0 # Max Beets, Max Leeds, Max Sheets*4
        self.Greebles["Xendans"] = 0 # Corrupted Health

        # Quality 3 Greebles - Used as power batteries for Raacs, and as catalysts for operations
        self.Greebles["Bankors"] = 0 # Max Traacs
        self.Greebles["Rangors"] = 0 # Max Broots
        self.Greebles["Fencors"] = 0
        self.Greebles["Kollors"] = 0 # Catalist On
        self.Greebles["Kollors_off"] = 0 # Catalist Off
        self.Greebles["Tannors"] = 0

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
        if qtd > 0:
            self.Greebles["Heeds"] -= qtd
            if self.Greebles["Heeds"] < 0:
                for raac in self.Raacs:
                    if raac.name == "SaveThrow":
                        break
                else:
                    raac = None
                while raac and (raac.level - raac.used) > 0 and self.Greebles["Verdans"] > 0:
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

        for raac in self.Raacs:
            if raac.name == "BeetHeal":
                if RNG <= 20*raac.level and self.Greebles["Heeds"] < self.Greebles["Verdans"] and self.Greebles["Beets"] > 0:
                    self.Greebles["Beets"] -= 1
                    self.Greebles["Heeds"] += 1
                    self.Greebles["Pots"] += 1
                break
    def acquireRaac(self, raac):
        for raac2 in self.Raacs:
            if raac2.id == raac.id:
                raac2.level += 1
                return True
        else:
            self.Raacs.append(raac)
            return True
    def acquireTraac(self, traac):
        for traac2 in self.Traacs:
            if traac2.id == traac.id:
                traac2.upgrade()
                return True
        else:
            self.Traacs.append(traac)
        if len(self.Traacs) > self.Greebles["Bankors"]:
            return self.Traacs.pop(0)
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
        if self.id == 1: # Normal
            hp = hp
            dmg = dmg
            df = df
            speed = speed
        elif self.id == 2: # Fast
            hp = hp*0.5
            dmg = dmg*0.7
            df = df*0.3
            speed = speed*1.25
        elif self.id == 3: # Armored
            hp = hp*1.2
            dmg = dmg*1.1
            df = df*1.3
            speed = speed*0.7
        elif self.id == 4: # Boss
            hp = hp*1.3
            dmg = dmg
            df = df*0.9
            speed = speed*0.9


        self.hp = hp*random.randrange(7, 14)/10
        self.dmg = dmg*random.randrange(7, 14)/10
        self.df = df*random.randrange(7, 14)/10
        self.speed = speed*random.randrange(7, 14)/10

        self.hp = floor(self.hp)
        self.dmg = floor(self.dmg)
        self.df = floor(self.df)
        self.speed = floor(self.speed)
        self.mhp = self.hp
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
            self.maxuses = 2
        elif self.id == 5: # Armor Altar
            self.recipe = [
                ["Sheets", 2],
                ["Leeds", 1],
            ]
            self.products = [
                ["Daffans", 1]
            ]
            self.maxuses = 1
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
                ["Beets", 1],
            ]
            self.products = [
                ["Callans", 1]
            ]
            self.maxuses = 1
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
                ["Feeds", 5],
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
    def __init__(self, N, color, level, params):
        self.color = color
        self.Greebles = []
        self.Raacs = []
        self.Traacs = []
        self.Broots = []
        self.Deploys = []
        self.connections = []
        self.Shop = []
        self.id = N
        self.level = level

        self.colored = False
        self.discovered = False

        self.enemy = None
        self.altar = None

        self.populate(params)
    def populate(self, params):
        if self.color == "red":
            typee = random.randrange(1, 4)
            self.enemy = Enemy(typee, self.level)
        elif self.color == "plate_red":
            typee = random.randrange(1, 4)
            self.enemy = Enemy(typee, self.level+2)
            self.randomGreeble(1, self.level)
            self.randomGreeble(2, min(round(log2(self.level))-3, 0))
        elif self.color == "yellow":
            temp1 = self.level
            self.randomGreeble(1, temp1+2)
        elif self.color == "plate_yellow":
            temp2 = self.level//5
            self.randomGreeble(2, temp2)
            self.randomGreeble(1, temp2*3)
        elif self.color == "black":
            self.enemy = Enemy(4, self.level)
            RNG = random.randrange(10)
            if RNG <= 2:
                RNG = random.randrange(3)
                self.Traacs.append(Traac(RNG))
            else:
                self.Raacs.append(Raac(Raac.chooseRandomRaac()))

            self.acquire(["Feeds", 10+self.level*2])
        elif self.color == "purple":
            typee = Altar.chooseRandomAltar()
            self.altar = Altar(typee)
        elif self.color == "plate_purple":
            self.altar = Altar(0)
        elif self.color == "white":
            return
        elif self.color == "gray":
            temp = ceil(log2(self.level+1)) + 1
            self.randomGreeble(0, temp)
        elif self.color == "green":
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
        elif self.color == "plate_green":
            temp = self.level*2 +2*params[0]
            while temp > 0:
                self.randomShop("Greeble", False)
                temp -= 3
    def depopulate(self):
        self.Greebles.clear()
    def acquire(self, greeb):
        if greeb[1] == 0:
            return
        for greeb2 in self.Greebles:
            if greeb2[0] == greeb[0]:
                greeb2[1] += greeb[1]
                break
        else:
            self.Greebles.append(greeb)
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
        if self.enemy.hp <= 0:
            if self.color == "red" or self.color == "plate_red":
                self.color = "gray"

            for raac in player.Raacs:
                if raac.name == "EnemyLoot":
                    EnemyLoot = 2*raac.level
                    break
            else:
                EnemyLoot = 0
            loot = floor(log(self.enemy.mhp+1, 4)) + EnemyLoot
            if loot > 0:
                self.randomGreeble(0, loot)
            for traac in player.Traacs:
                traac.charge += 1
                if self.color == "black":
                    traac.charge += 2
                if traac.charge > traac.maxCharge:
                    traac.charge = traac.maxCharge


            self.enemy = None
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
        self.Shop.append(item)


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
        self.generate()
    def generate(self):
        if self.id == 0:
            self.name = "Treasure"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor divisible by 2, X Yellow Rooms will permanently be added to the pool."
            self.quality = 4
        elif self.id == 1:
            self.name = "BeetHeal"
            self.trigger = "Walk"
            self.description = "Every time you walk, X*20% chance for a Beet to be converted to a Heed if not at max."
            self.quality = 5
        elif self.id == 2:
            self.name = "FencorRegen"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor. You get 2*X*Fencor Heeds."
            self.quality = 2
        elif self.id == 3:
            self.name = "SaveThrow"
            self.trigger = "Damage"
            self.description = "If you take death damage, convert a Verdan into a Xerdan and add 3 Heeds to the blow. Only activates X times per floor."
            self.quality = 3
            self.used = 0
        elif self.id == 4:
            self.name = "EnemyLoot"
            self.trigger = "EnemyKill"
            self.description = "When an enemy dies, add 2*X Greebles Quality 0 to the room."
            self.quality = 7
        elif self.id == 5:
            self.name = "Altar"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor divisible by 2, X Purple Rooms will permanently be added to the pool."
            self.quality = 4
        elif self.id == 6:
            self.name = "RoomConnectivity"
            self.trigger = "Floor"
            self.description = "Rooms are more connected"
            self.quality = 8
        elif self.id == 7:
            self.name = "ColoredRoom"
            self.trigger = "Floor"
            self.description = "Random rooms can have their colors revealed"
            self.quality = 6
        elif self.id == 8:
            self.name = "LuckyCharm"
            self.trigger = "Discover"
            self.description = "Quality 0 Greebles have chance to become Quality 1"
            self.quality = 5
        elif self.id == 9:
            self.name = "Pottery"
            self.trigger = "Discover"
            self.description = "When discovering rooms, chance to transform Shots into Pots."
            self.quality = 3
        elif self.id == 10:
            self.name = "ExtraStock"
            self.trigger = "Floor"
            self.description = "Shops have more quality."
            self.quality = 3
        elif self.id == 11:
            self.name = "SplashDamage"
            self.trigger = "Attack"
            self.description = "When attacking enemies, if there are enemies in adjacent rooms, deal 35% damage to X of them."
            self.quality = 5
    def chooseRandomRaac():
        RaacPool = [
            [20, 0],
            [20, 1],
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
        
        RaacPool[id][0] += 3
        return id
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
class Floor():
    def __init__(self, level, rooms, broots, params):
        self.level = level
        self.size = 10+2*floor(self.level**1.3)
        self.Rooms = []
        self.generate(rooms, broots, params)
    def generate(self, temp, broots, params):
        connectivity = params[0]
        shopStock = params[1]

        rooms = {}
        for key in temp:
            rooms[key] = temp[key]

        self.Rooms.append(Room(0, "white", self.level, [0]))
        self.size -= 1
        rooms["white"] -= 1

        N = 1
        while self.size > 1:
            self.size -= 1
            newroom = Room(N, "gray", self.level, [0])
            N += 1
            self.Rooms.append(newroom)
        self.Rooms.append(Room(N, "black", self.level, [0]))
        self.size -= 1
        rooms["black"] -= 1
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
                self.Rooms[RNG].color = key
                self.Rooms[RNG].depopulate()
                self.Rooms[RNG].populate([shopStock])
                if key == "yellow" or key == "plate_yellow":
                    for key2 in broots:
                        if broots[key2] > 0:
                            self.Rooms[RNG].Broots.append(Broot(key2))
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
        display.set_caption('GreeblesMania 0.2 - Cha-ching Update')
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
        rooms = {}
        rooms["white"] = 1

        rooms["yellow"] = 2
        rooms["purple"] = 2
        rooms["red"] = 0
        rooms["green"] = 0

        rooms["plate_yellow"] = 0
        rooms["plate_green"] = 0
        rooms["plate_red"] = 0
        rooms["plate_purple"] = 0
        rooms["plate_gray"] = 0
        rooms["plate_black"] = 0


        rooms["black"] = 1

        broots = {}
        for broot in brootimg:
            broots[broot] = 0
        broots["armed"] = 2
        broots["defends"] = 1


        level = 0
        connectivity = 3
        extraStock = 0
        coloredLevel = 0
        for raac in self.player.Raacs:
            if raac.name == "RoomConnectivity":
                connectivity += raac.level
            elif raac.name == "ColoredRoom":
                coloredLevel += raac.level
                coloredLevel += self.player.Greebles["Tannors"]
            elif raac.name == "ExtraStock":
                extraStock += raac.level
        self.currentFloor = Floor(level, rooms, broots, [connectivity, extraStock])
        for rm in self.currentFloor.Rooms:
            RNG = random.randrange(100)
            if RNG < coloredLevel*10:
                rm.colored = True


        self.currentFloor.Rooms[0].discovered = True
        self.currentFloor.Rooms[0].colored = True
        plate_yellowCost = 5

        while self.player.Greebles["Heeds"] >= 0:
            value = self.update()
            if value == -1:
                return
            elif value == 1:

                level += 1


                alivecount = 0
                altarcount = 0
                anvilcount = 0
                for rm in self.currentFloor.Rooms:
                    if rm.color == "green" and not rm.discovered:
                        RNG = random.randrange(100)
                        if RNG <= 25:
                            rooms["green"] -= 1
                            rooms["plate_green"] += 1
                    if rm.color == "plate_green" and not rm.discovered:
                        RNG = random.randrange(100)
                        if RNG <= 25:
                            rooms["green"] += 1
                            rooms["plate_green"] -= 1
                    if rm.color == "red" or rm.color == "plate_red":
                        alivecount += 1
                    if rm.color == "purple":
                        if rm.altar.uses == rm.altar.maxuses:
                            if rm.altar.id == 0:
                                anvilcount += 1
                            else:
                                altarcount += 1
                RNG = random.randrange(100)
                if RNG < altarcount*5:
                    rooms["purple"] -= 1
                    rooms["plate_purple"] += 1
                if anvilcount > 0:
                    rooms["purple"] += 1
                    rooms["plate_purple"] -= 1
                if alivecount == 0 and level > 2:
                    rooms["plate_red"] += 1
                    rooms["red"] -= 1
                rooms["yellow"] += 1
                rooms["red"] += 1
                if level % 2 == 0:
                    for raac in self.player.Raacs:
                        if raac.name == "Treasure":
                            rooms["yellow"] += raac.level
                            break
                if level % 3 == 0:
                    rooms["purple"] += 1
                    rooms["red"] += 1
                if level % 4 == 0:
                    rooms["green"] += 1
                if level % 5 == 0:
                    if rooms["yellow"] > plate_yellowCost:
                        rooms["yellow"] -= 5
                        rooms["plate_yellow"] += 1
                        plate_yellowCost += level//3
                    
                    for raac in self.player.Raacs:
                        if raac.name == "Altar":
                            rooms["purple"] += raac.level
                    rooms["red"] += 1


                typee = Broot.chooseRandomBroot()
                broots[typee] += 1

                self.player.Greebles["Kollors"] += self.player.Greebles["Kollors_off"]
                self.player.Greebles["Kollors_off"] = 0

                for raac in self.player.Raacs:
                    if raac.name == "SaveThrow":
                        raac.used = 0
                    elif raac.name == "FencorRegen":
                        self.player.acquire(["Heeds", raac.level*3*self.player.Greebles["Fencors"]])

                connectivity = 3
                coloredLevel = 0
                extraStock = 0
                for raac in self.player.Raacs:
                    if raac.name == "RoomConnectivity":
                        connectivity += raac.level
                    elif raac.name == "ColoredRoom":
                        coloredLevel += raac.level
                        coloredLevel += self.player.Greebles["Tannors"]
                    elif raac.name == "ExtraStock":
                        extraStock += raac.level
                self.currentFloor = Floor(level, rooms, copy.deepcopy(broots), [connectivity, extraStock])

                for rm in self.currentFloor.Rooms:
                    RNG = random.randrange(100)
                    if RNG < coloredLevel*10:
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
        room = self.currentFloor.Rooms[self.player.room]

        self.escreverCanto(f"Floor: {self.currentFloor.level}", 25, (20, 20))
        self.escreverCanto(f"Room: {self.player.room}", 25, (20, 45))

        draw.rect(game.screen, (0, 0, 0), (35, 175, self.size*13+10, self.size*9+10), 5)
        brickimg = bricksimg[room.color]
        for x in range(13):
            for y in range(9):
                self.screen.blit(brickimg, (40+self.size*x, 180+self.size*y))

        x = 6
        y = 4
        if room.enemy:
            self.screen.blit(enemiesimg[room.enemy.id], (40+self.size*x, 180+self.size*y))
            draw.rect(self.screen, (255, 255, 255), [40+self.size*x-1, 180+self.size*(y+1)-1, self.size-1, self.size-1])
            self.escreverCanto(f"{room.enemy.hp}/{room.enemy.mhp}", 15, (45+self.size*x, 185+self.size*(y+1)))
            self.escreverCanto(f"[{room.enemy.dmg}]", 15, (45+self.size*x+self.size//2, 185+self.size*(y+1)))
            rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)
            options.append([rect, 0, "attack"])
        elif room.altar:
            if room.altar.id == 0:
                self.screen.blit(altar2img, (40+self.size*x, 180+self.size*y))
                self.escreverCanto(f"{room.altar.uses}/{room.altar.maxuses}", 15, (45+self.size*x, 185+self.size*(y+1)))



                x = 16
                y = 1
                id = 0
                for raac in self.player.Raacs:
                    draw.rect(game.screen, (0, 0, 0), (40+self.size*x, self.size*y, self.size, self.size), 1)
                    draw.rect(game.screen, (255, 255, 0), (40+self.size*x+1, self.size*y+1, self.size-2, self.size-2))
                    self.screen.blit(raacimg[raac.name], (40+self.size*x, self.size*y))
                    self.escrever(f"{raac.level}", 25, (40+self.size*x+self.size//2, self.size*y-10))

                    rect = Rect(40+self.size*x, self.size*y, self.size, self.size)
                    options.append([rect, id, "break"])
                    id += 1


                    x += 1
                    if x >= 24:
                        x = 21
                        y += 1



            else:
                self.screen.blit(altarimg, (40+self.size*x, 180+self.size*y))
                self.escreverCanto(f"{room.altar.uses}/{room.altar.maxuses}", 15, (45+self.size*x, 185+self.size*(y+1)))
                rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)
                options.append([rect, 0, "altar"])


                for rec in room.altar.recipe:
                    self.screen.blit(greebleimg[rec[0]], (40+self.size*(x+1), 180+self.size*y))
                    self.escreverCanto(f"x{rec[1]}", 15, (40+self.size*(x+1), 180+self.size*y))
                    x += 1
                    if x >= 12:
                        x = 6
                        y += 1
                x = 6
                y += 1
                for prod in room.altar.products:
                    self.screen.blit(greebleimg[prod[0]], (40+self.size*(x+1), 180+self.size*y))
                    self.escreverCanto(f"x{prod[1]}", 15, (40+self.size*(x+1), 180+self.size*y))
                    x += 1
                    if x >= 12:
                        x = 6
                        y += 1




        # Room information
        x = 0
        y = 0
        id = 0
        for greeb in room.Greebles:
            self.screen.blit(greebleimg[greeb[0]], (40+self.size*x, 180+self.size*y))
            rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)
            options.append([rect, id, "greeb"])
            id += 1
            x += 1
            self.escreverCanto(f"x{greeb[1]}", 15, (20+self.size*x, 180+self.size*y))
            if x >= 13:
                x = 0
                y += 1
        id = 0
        for raac in room.Raacs:
            self.screen.blit(raacimg[raac.name], (40+self.size*x, 180+self.size*y))
            rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)
            self.escrever(f"{raac.id}", 15, (40+self.size*x, 180+self.size*(y+1)))
            options.append([rect, id, "raac"])
            id += 1
            x += 1
            if x >= 13:
                x = 0
                y += 1
        id = 0
        for traac in room.Traacs:
            self.screen.blit(traacimg[traac.name], (40+self.size*x, 180+self.size*y))
            rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)
            self.escrever(traac.name, 15, (40+self.size*x, 180+self.size*(y+1)))
            options.append([rect, id, "traac"])
            id += 1
            x += 1
            if x >= 13:
                x = 0
                y += 1
        id = 0
        for broot in room.Broots:
            self.screen.blit(brootimg[broot.name], (40+self.size*x, 180+self.size*y))
            rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)
            self.escrever(broot.name, 15, (40+self.size*x+self.size//2, 190+self.size*(y+1)))
            options.append([rect, id, "broot"])
            id += 1
            x += 1
            if x >= 13:
                x = 0
                y += 1
        for deploy in room.Deploys:
            if deploy.alive:
                self.screen.blit(brootimg[deploy.name], (40+self.size*deploy.x, 180+self.size*deploy.y))
            else:
                self.screen.blit(brootimg["DEAD"], (40+self.size*deploy.x, 180+self.size*deploy.y))
        id = 0
        x = 0
        y = 2
        for item in room.Shop:
            if item[0] == "Broot":
                self.screen.blit(brootimg[item[2]], (40+self.size*x, 180+self.size*y))
            elif item[0] == "Raac":
                self.screen.blit(raacimg[item[2]], (40+self.size*x, 180+self.size*y))
            elif item[0] == "Traac":
                self.screen.blit(traacimg[item[2]], (40+self.size*x, 180+self.size*y))
            elif item[0] == "Greeble":
                self.screen.blit(greebleimg[item[2]], (40+self.size*x, 180+self.size*y))
                self.escrever(f"x{item[3]}", 15, (25+self.size*x+self.size, 175+self.size*(y+1)))

            rect = Rect(40+self.size*x, 180+self.size*y, self.size, self.size)

            self.screen.blit(greebleimg[item[4]], (40+self.size*x, 180+self.size*(y+1)))
            self.escrever(f"x{item[3]}", 15, (25+self.size*x+self.size, 190+self.size*(y+2)))

            options.append([rect, id, "buy"])
            id += 1
            x += 1
            if x >= 13:
                x = 0
                y += 2










        # HUD
        x = 0
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
                self.escrever(str(rm.id), 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            else:
                self.escrever("?", 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
            options.append([rect, rm.id, "walk"])
            x += 1

            if room.color == "black" and not room.enemy:
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
            self.screen.blit(traacimg[traac.name], (40+self.size*x, 160+self.size*y))
            self.escrever(f"{traac.level}", 25, (40+self.size*x+self.size//2, 160+self.size*y-10))
            rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
            options.append([rect, x-2, "active"])
            x += 1


        x = 16
        y = 1
        for raac in self.player.Raacs:
            draw.rect(game.screen, (0, 0, 0), (40+self.size*x, self.size*y, self.size, self.size), 1)
            draw.rect(game.screen, (255, 255, 0), (40+self.size*x+1, self.size*y+1, self.size-2, self.size-2))
            self.screen.blit(raacimg[raac.name], (40+self.size*x, self.size*y))
            self.escrever(f"{raac.level}", 25, (40+self.size*x+self.size//2, self.size*y-10))

            rect = Rect(40+self.size*x, self.size*y, self.size, self.size)
            if Colide(rect, mouseRect):
                self.escrever(f"{raac.name}", 15, (40+self.size*x+self.size//2, self.size*y+10))


            x += 1
            if x >= 24:
                x = 21
                y += 1


        draw.rect(game.screen, (0, 0, 0), (40+self.size*14, 180+self.size*6, self.size, self.size), 1)
        draw.rect(game.screen, (0, 255, 0), (40+self.size*14+1, 180+self.size*6+1, self.size-2, self.size-2))

        if len(self.player.Broots) > 0 and self.player.selectedBroot < len(self.player.Broots) and self.player.selectedBroot >= 0:
            broot = self.player.Broots[self.player.selectedBroot].name
            self.screen.blit(brootimg[broot], (40+self.size*14, 180+self.size*6))
            self.escrever(f"{broot}", 25, (40+self.size*14+self.size//2, 180+self.size*6-10))
        self.escrever(f"{len(self.player.Broots)}/{self.player.Greebles["Rangors"]}", 25, (40+self.size*14+self.size//2, 180+self.size*7+10))


        x = 28
        y = 8
        self.size = 32
        for rm in self.currentFloor.Rooms:
            draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)

            if rm.colored:
                color = colorkey[rm.color]
                draw.rect(game.screen, color, (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            else:
                draw.rect(game.screen, (255, 255, 255), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
            if rm.discovered:
                self.escrever(str(rm.id), 12, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
                rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
                options.append([rect, rm.id, "walk"])
            else:
                self.escrever("?", 12, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            x += 1
            if x > 47:
                x = 28
                y += 1
        self.size = 64







        self.screen.blit(greebleimg["Beets"], (40+10*self.size, 50))
        self.escreverCanto(f"x{self.player.Greebles["Beets"]}/{self.player.Greebles["Radeans"]}", 15, (40+10*self.size, 50+self.size))
        self.screen.blit(greebleimg["Heeds"], (40+11*self.size, 50))
        self.escreverCanto(f"x{self.player.Greebles["Heeds"]}/{self.player.Greebles["Verdans"]}", 15, (40+11*self.size, 50+self.size))
        self.screen.blit(greebleimg["Feeds"], (40+12*self.size, 50))
        self.escreverCanto(f"x{self.player.Greebles["Feeds"]}/{self.player.Greebles["Postans"]}", 15, (40+12*self.size, 50+self.size))











        # CONTROL
        action = False
        parameter = 0
        # while not action:
        for option in options:
            if option[2] == "active":
                if Colide(option[0], mouseRect):
                    self.escrever(f"{self.player.Traacs[option[1]].charge}/{self.player.Traacs[option[1]].maxCharge} [{self.player.Traacs[option[1]].cost}]", 15, (option[0].x+self.size//2, option[0].y+self.size+10))
                    self.escrever(f"{self.player.Traacs[option[1]].name}", 15, (option[0].x+self.size//2, (option[0].y-self.size)+self.size+10))
            if option[2] == "buy":
                if Colide(option[0], mouseRect):
                    self.escrever(f"{room.Shop[option[1]][2]}", 15, (option[0].x+self.size//2, (option[0].y-self.size)+self.size+10))
        x = 6
        y = 4
        if room.enemy and Colide(Rect(40+self.size*x, 160+self.size*y, self.size, self.size), mouseRect):
            y += 1
            self.escrever(f"[{room.enemy.speed}] [{room.enemy.df}]", 15, (40+self.size*x+self.size//2, 220+self.size*y))


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
                    x = mouseRect.x
                    y = mouseRect.y
                    x -= 40
                    y -= 160
                    x = x//self.size
                    y = y//self.size
                    if x >= 0 and x <= 13 and y >= 0 and y <= 9:
                        action = "deploy"
                        parameter = (x, y)
            elif ev.type == KEYDOWN:
                if ev.key == K_1:
                    self.player.selectedBroot -= 1
                if ev.key == K_2:
                    self.player.selectedBroot += 1
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
            if room.altar.uses > 0:
                for rec in room.altar.recipe:
                    if self.player.Greebles[rec[0]] < rec[1]:
                        break
                else:
                    room.altar.uses -= 1
                    for rec in room.altar.recipe:
                        self.player.Greebles[rec[0]] -= rec[1]
                    for prod in room.altar.products:
                        qtd = self.player.acquire(prod)
                        if qtd > 0:
                            for greeb in room.Greebles:
                                if greeb[0] == prod[0]:
                                    greeb[1] += qtd
                                    break
                            else:
                                greeb = [prod[0], qtd]
                                room.Greebles.append(greeb)
        elif action == "break":
            if room.altar.uses > 0:
                room.altar.uses -= 1

                raac = self.player.Raacs.pop(parameter)
                room.randomGreeble(2, raac.level*3)


        elif action == "next":
            return 1
        elif action == "active":
            if self.player.Traacs[parameter].charge >= self.player.Traacs[parameter].cost:
                sucess = False
                if self.player.Traacs[parameter].name == "AltarBoost" and room.altar and room.altar.uses == room.altar.maxuses and room.altar.uses >= 5:
                    room.altar.uses += 1
                    room.altar.maxuses += 1
                    sucess = True
                elif self.player.Traacs[parameter].name == "Crystalize" and self.player.Greebles["Heeds"] > 0 and self.player.Greebles["Beets"] < self.player.Greebles["Radeans"]:
                    self.player.Greebles["Heeds"] -= 1
                    self.player.acquire(["Beets", 1])
                    sucess = True
                elif self.player.Traacs[parameter].name == "Bomb":
                    if room.enemy:
                        room.enemy.hp -= 10*self.player.Traacs[parameter].level
                        room.checkEnemyLife(self.player)
                        sucess = True
                if sucess:
                    self.player.Traacs[parameter].charge -= self.player.Traacs[parameter].cost
        elif action == "deploy" and len(self.player.Broots) > 0:
            broot = self.player.Broots.pop(self.player.selectedBroot)
            broot.deploy(parameter[0], parameter[1], room)
            room.Deploys.append(broot)
            self.player.selectedBroot -= 1
            if self.player.selectedBroot < 0:
                self.player.selectedBroot = 0
        elif action == "buy":
            item = room.Shop[parameter]
            room.Shop.pop(parameter)
            if self.player.Greebles[item[4]] >= item[3]:
                if item[0] == "Greeble":
                    qtd = self.player.acquire([item[2], item[1]])
                    room.acquire([item[2], qtd])
                elif item[0] == "Broot":
                    if len(self.player.Broots) < self.player.Greebles["Rangors"]:
                        self.player.Broots.append(Broot(item[2]))
                    else:
                        room.Broots.append(Broot(item[2]))
                elif item[0] == "Raac":
                    room.Raacs.append(Raac(item[2]))
                    action == "raac"
                    parameter = len(room.Raacs)-1
                elif item[0] == "Traac":
                    action = "traac"
                    room.Traacs.append(Traac(item[2]))
                    parameter = len(room.Traacs)-1

                self.player.Greebles[item[4]] -= item[3]
        if not room.enemy:
            if action == "traac":
                traac = room.Traacs[parameter]
                traac = self.player.acquireTraac(traac)
                room.Traacs.pop(parameter)
                if traac:
                    room.Traacs.append(traac)
            elif action == "greeb":
                greeb = room.Greebles[parameter]
                qtd = self.player.acquire(greeb)
                if qtd == 0:
                    room.Greebles.pop(parameter)
                else:
                    greeb[1] = qtd
            elif action == "raac":
                raac = room.Raacs[parameter]
                got = self.player.acquireRaac(raac)
                if got:
                    room.Raacs.pop(parameter)
            elif action == "broot":
                if len(self.player.Broots) < self.player.Greebles["Rangors"]:
                    broot = room.Broots[parameter]
                    self.player.Broots.append(broot)
                    room.Broots.pop(parameter)
            

        self.clock.tick(30)
    def walkRoom(self, step):
        if not self.currentFloor.Rooms[step].discovered:
            if self.player.Greebles["Feeds"] > 0:
                self.player.Greebles["Feeds"] -= 1
            else:
                self.player.Greebles["Heeds"] -= 1

            lucklevel = 0
            for raac in self.player.Raacs:
                if raac.name == "LuckyCharm":
                    lucklevel += raac.level
                    lucklevel += self.player.Greebles["Tannors"]
                elif raac.name == "Pottery":
                    levelPot = raac.level
                    RNG = random.randrange(100)
                    while RNG < levelPot*4:
                        if self.player.Greebles["Shots"] > 0:
                            self.player.Greebles["Shots"] -= 1
                            self.player.acquire(["Pots", 1])
                        levelPot -= 25
                        RNG = random.randrange(100)




            for greeb in self.currentFloor.Rooms[step].Greebles:
                if greeb[0] in GQ0:
                    RNG = random.randrange(100)
                    while RNG < lucklevel*10:
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
                            self.currentFloor.Rooms[step].Greebles.remove(greeb)
                            break


            for rm in self.currentFloor.Rooms:
                for broot in rm.Deploys:
                    if broot.name == "digests":
                        for greeb in rm.Greebles:
                            if greeb[0] != "Slops":
                                greeb[1] -= 1
                                rm.acquire(["Slops", 1])
                                if greeb[1] == 0:
                                    rm.Greebles.remove(greeb)
                    elif broot.name == "digs":
                        broot.action += 1
                        if broot.action >= broot.cost:
                            broot.action -= broot.cost
                            RNG = random.randrange(100)
                            if RNG <= 20:
                                rm.acquire([random.choice(GQ1), 1])
                            else:
                                rm.acquire([random.choice(GQ0), 1])
                    elif broot.name == "deconstructs":
                        if rm.altar and rm.altar.uses > 0:
                            rm.altar.uses -= 1
                            RNG = random.randrange(100)/rm.altar.maxuses
                            if RNG <= 20:
                                rm.acquire([random.choice(GQ0), 1])
                            elif RNG <= 40:
                                rm.acquire([random.choice(GQ1), 1])
                            else:
                                rm.acquire([random.choice(GQ2), 1])


        self.player.room = step
        self.activate(step)
    def activate(self, step):
        room = self.currentFloor.Rooms[step]
        room.discovered = True
        room.colored = True




        if room.enemy:
            # Broots
            SplashDamage = 0
            for raac in self.player.Raacs:
                if raac.name == "SplashDamage":
                    SplashDamage += raac.level
            broot_attack = 0
            broot_defense = 0
            for rm in room.connections:
                rm = self.currentFloor.Rooms[rm]
                if rm.enemy and SplashDamage > 0:
                    rm.enemy.hp -= floor(0.35*self.player.Greebles["Callans"])
                    rm.checkEnemyLife(self.player)
                    SplashDamage -= 1
                for deploy in rm.Deploys:
                    if deploy.name == "armed":
                        broot_attack += deploy.dmg
                        deploy.damage(room.enemy.dmg)
                    elif deploy.name == "defends":
                        broot_defense += deploy.dmg
                        deploy.damage(deploy.dmg)



            room.enemy.hp -= self.player.Greebles["Callans"] + broot_attack
            room.acquire(["Bloods", 1])

            if self.player.Greebles["Sheets"] < room.enemy.speed or room.enemy.hp > 0:
                qtd = max(0, room.enemy.dmg - broot_defense)
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
            for greeb in GQ0 + ["Slops"]:
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, (255, 255, 255), [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))

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
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, (255, 255, 255), [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ2:
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, (255, 255, 255), [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ3:
                draw.rect(self.screen, (0, 0, 0), [x-3, y-3, self.size+6, self.size+6], 2)
                draw.rect(self.screen, (255, 255, 255), [x-1, y-1, self.size+2, self.size+2])
                self.screen.blit(greebleimg[greeb], (x, y))

                draw.rect(self.screen, (0, 0, 0), [x-3, y-3+self.size+6, self.size+6, 15+6], 2)
                draw.rect(self.screen, (150, 150, 150), [x-1, y-1+self.size+6, self.size+2, 15+2])
                self.escrever(f"x{self.player.Greebles[greeb]}", 15, (x+self.size//2, y+self.size+14))
                x += self.size











            for ev in event.get():
                if (ev.type == QUIT):
                    return -1
                if ev.type == MOUSEBUTTONDOWN:
                    if ev.button == BUTTON_LEFT:
                        pass
                    if ev.button == BUTTON_RIGHT:
                        pass
                elif ev.type == KEYDOWN:
                    if ev.key == K_TAB:
                        tabPressed = not tabPressed





init()
game = Game()
game.run()


print("Killed!!")









