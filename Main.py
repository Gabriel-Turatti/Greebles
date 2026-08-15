from pygame import display, image, draw, time, font, init, transform, QUIT, KEYDOWN, K_TAB, MOUSEBUTTONDOWN, BUTTON_LEFT, BUTTON_RIGHT, event, mouse, Rect, KEYDOWN, K_1, K_2, K_SPACE, K_z
import random
from math import ceil, floor, log2, log, sqrt
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
        "normal_cyan": image.load('Images/brick_cyan.png'),
        "normal_blue": image.load('Images/brick_blue.png'),
        "normal_void": image.load('Images/brick_void.png'),
        "normal_teal": image.load('Images/brick_teal.png'),
        "normal_magenta": image.load('Images/brick_magenta.png'),
        "normal_lilas": image.load('Images/brick_lilas.png'),

        "plate_gray": image.load('Images/plate_gray.png'),
        "plate_yellow": image.load('Images/plate_yellow.png'),
        "plate_red": image.load('Images/plate_red.png'),
        "plate_purple": image.load('Images/plate_purple.png'),
        "plate_white": image.load('Images/plate_white.png'),
        "plate_black": image.load('Images/plate_black.png'),
        "plate_orange": image.load('Images/plate_orange.png'),
        "plate_green": image.load('Images/plate_green.png'),
        "plate_cyan": image.load('Images/plate_cyan.png'),
        "plate_blue": image.load('Images/plate_blue.png'),
        "plate_void": image.load('Images/plate_void.png'),
        "plate_teal": image.load('Images/plate_teal.png'),
        "plate_magenta": image.load('Images/plate_magenta.png'),
        "plate_lilas": image.load('Images/plate_lilas.png'),

        "lock": image.load('Images/lock.png'),
    }
    enemiesimg = {
        0: image.load('Images/enemy_DEAD.png'),
        1: image.load('Images/enemy_normal.png'),
        2: image.load('Images/enemy_fast.png'),
        3: image.load('Images/enemy_armored.png'),
        4: image.load('Images/enemy_boss_generic.png'),
        5: image.load('Images/enemy_slime.png'),
        6: image.load('Images/enemy_wasp.png'),
        7: image.load('Images/enemy_waspNest.png'),
        8: image.load('Images/enemy_Skeleton.png'),
        9: image.load('Images/brick_blue.png'),
        10: image.load('Images/brick_blue.png'),

        50: image.load('Images/enemy_vine.png'),

        97: image.load('Images/enemy_Scorpion.png'),
        98: image.load('Images/enemy_FireBreather.png'),
        99: image.load('Images/enemy_envinerator.png'),
    }
    altarimg = image.load('Images/altar_generic.png')
    altar2img = image.load('Images/altar_break_generic.png')
    swordimg = image.load('Images/brick_darkred.png')
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
        "Heexs": image.load('Images/Greebles/Heexs.png'),

        "Sackans": image.load('Images/Greebles/Sackans.png'),
        "Postans": image.load('Images/Greebles/Postans.png'),
        "Callans": image.load('Images/Greebles/Callans.png'),
        "Verdans": image.load('Images/Greebles/Verdans.png'),
        "Daffans": image.load('Images/Greebles/Daffans.png'),
        "Radeans": image.load('Images/Greebles/Radeans.png'),
        "Xendans": image.load('Images/Greebles/Xendans.png'),

        "Fallers": image.load('Images/Greebles/Fallers.png'),
        "Rallers": image.load('Images/Greebles/Rallers.png'),
        "Pallers": image.load('Images/Greebles/Pallers.png'),
        "Sallers": image.load('Images/Greebles/Sallers.png'),
        "Vallers": image.load('Images/Greebles/Vallers.png'),

        "Bankors": image.load('Images/Greebles/Bankors.png'),
        "Rangors": image.load('Images/Greebles/Rangors.png'),
        "Kollors": image.load('Images/Greebles/Kollors.png'),
        "Kollors_off": image.load('Images/Greebles/Kollors_off.png'),
        "Tannors": image.load('Images/Greebles/Tannors.png'),
        "Alators": image.load('Images/Greebles/Alators.png'),
        "Lunnors": image.load('Images/Greebles/Lunnors.png'),
    }
    raacimg = {
        "Treasure": image.load('Images/Raacs/raac_treasure.png'), # Yellow Room spawn
        "BeetHeal": image.load('Images/Raacs/raac_BeetHeal.png'), # Beets decompose into Heeds
        "FencorRegen": image.load('Images/Raacs/raac_FencorRegen.png'), # Fencor regenerate Heeds
        "SaveThrow": image.load('Images/Raacs/raac_SaveThrow.png'), # If you were to die, corrupt Verdans instead to heal X Heeds
        "EnemyLoot": image.load('Images/Raacs/raac_EnemyLoot.png'), # Enemies drop 2 Q0 greebles
        "Altar": image.load('Images/Raacs/raac_Altar.png'), # Adds An Altar for each 5 floors

        "RoomConnectivity": image.load('Images/Raacs/raac_RoomConnectivity.png'), # Increases how many connections rooms have
        "ColoredRoom": image.load('Images/Raacs/raac_ColoredRoom.png'), # Reveals by chance room's colors, affected by Tannors
        "LuckyCharm": image.load('Images/Raacs/raac_LuckyCharm.png'), # Chance to transform Q0 into Q1
        "Pottery": image.load('Images/Raacs/raac_Pottery.png'), # Shots have a chance to turn into Pots
        "ExtraStock": image.load('Images/Raacs/raac_ExtraStock.png'), # Shops have more stock
        "SplashDamage": image.load('Images/Raacs/raac_SplashDamage.png'), # Gives 50% of your damage to X enemy room's

        "RockCrest": image.load('Images/Raacs/raac_RockCrest.png'), # If you have 2+X rocks, you receive X defense. On damage, Rocks break into Shots
        "SlimeFest": image.load('Images/Raacs/raac_SlimeFest.png'), # Each Floor you turn X of each quality 0 Greebles into slime, and add a new gray room to the floor.
        "LeedQuest": image.load('Images/Raacs/raac_LeedQuest.png'), # Each Floor, lose 3X Leeds, add X red rooms.
        "TraacBest": image.load('Images/Raacs/raac_TraacBest.png'), # Traac items have X more max charge.
        "AltarRest": image.load('Images/Raacs/raac_AltarRest.png'), # Destroy an unused altar to gain 3X Heexs.
        "BlackTest": image.load('Images/Raacs/raac_BlackTest.png'), # Killing a Boss gives +X charges to your Traacs

        "Vampire": image.load('Images/Raacs/raac_generic.png'), # Everytime you kill an enemy, consume 2X Bloods to recover X Heed
        "FrostAspect": image.load('Images/Raacs/raac_generic.png'), # Your attacks slows enemies down by 2+Tannors speed.
        "Squire": image.load('Images/Raacs/raac_generic.png'), # Increases Broots abilities
        "Hammlet": image.load('Images/Raacs/raac_generic.png'), # your attacks break 0.5 armor
        "Revishot": image.load('Images/Raacs/raac_generic.png'), # Every floor, remove 2 Shot and gain a temporary Def point. 
        "MagicEye": image.load('Images/Raacs/raac_generic.png'), # Blue rooms are revealed if connected to a purple room.













    }
    traacimg = {
        "AltarBoost": image.load('Images/Traacs/traac_AltarBoost.png'), # Altars have more charge in exchange for rocks
        "Crystalize": image.load('Images/Traacs/traac_Crystalize.png'), # Convert Heed into Beet
        "Bomb": image.load('Images/Traacs/traac_Bomb.png'), # Deals 10 damage to enemies in room

        "TumbleBox": image.load('Images/Traacs/traac_TumbleBox.png'), # Creates random Q0 Greebles in room
        "Reinforce": image.load('Images/Traacs/traac_Reinforce.png'), # Gives 4 temporary DF points, loses 1 per explored room
        "RaacRerox": image.load('Images/Traacs/traac_RaacRerox.png'), # Rerolls T/Raacs in the room

        "Crafting": image.load('Images/Raacs/raac_generic.png'), # Consumes 6 leeds to create a random Q2 greeble
        "Ordering": image.load('Images/Raacs/raac_generic.png'), # Creates a random Shop
        "Drafting": image.load('Images/Raacs/raac_generic.png'), # Rerolls Q0 Greebles in the room, reduces it by 1.
    }
    brootimg = {
        "DEAD": image.load('Images/brick_darkred.png'),
        "armed": image.load('Images/Broot_armed.png'),
        "defends": image.load('Images/Broot_defends.png'),

        "digests": image.load('Images/Broot_digests.png'),
        "digs": image.load('Images/Broot_digs.png'),
        "deconstructs": image.load('Images/Broot_deconstructs.png'),

        "detector": image.load('Images/plate_green.png'),
        "final": image.load('Images/plate_green.png'),
        "fights": image.load('Images/plate_green.png'),

        "frosts": image.load('Images/plate_purple.png'),
        "pierces": image.load('Images/plate_purple.png'),
        "walks": image.load('Images/plate_purple.png'),
    }
    zoodiacimg = {}
    zoodiacColor = {
        "Aries": "red",
        "Taurus": "orange",
        "Gemini": "yellow",
        "Cancer": "white",
        "Leo": "green",
        "Virgo": "cyan",
        "Libra": "gray",
        "Scorpio": "teal",
        "Sagitarius": "blue",
        "Capricorn": "purple",
        "Aquarius": "black",
        "Pisces": "magenta",
    }
    for i in range(12):
        for j in range(12):
            for k in range(2):
                file = f'Images/Zoodiacs/Sign{i+1}-{j+1+12*k}.png'
                zoodiacimg[f"{i+1}-{j+1}-{k+1}"] = image.load(file)
    raacNumber = []
    traacNumber = []
    brootNumber = []
    zoodiacNumber = []
    for key in raacimg:
        raacNumber.append(key)
    for key in traacimg:
        traacNumber.append(key)
    for key in brootimg:
        brootNumber.append(key)
    for key in zoodiacimg:
        zoodiacNumber.append(key)
    GQ0 = ["Shots", "Bloods", "Pots", "Clots", "Rocks"]
    GQ1 = ["Heeds", "Feeds", "Beets", "Leeds", "Sheets"]
    GQ2 = ["Verdans", "Postans", "Sackans", "Callans", "Daffans", "Radeans"]
    GQ3 = ["Fallers", "Rallers", "Pallers", "Sallers", "Vallers"]
    GQ4 = ["Bankors", "Rangors", "Kollors", "Kollors_off", "Alators", "Tannors"]
    GQ0b = ["Slops"]
    GQ1b = ["Heexs"]
    GQ2b = ["Xendans"]
    GQ3b = []
    GQ4b = ["Lunnors"]
    G = [GQ0, GQ1, GQ2, GQ3, GQ4]

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

        18,
        15,
        22,
        14,
        6,
        10,
    ]
    traacValue = [
        9,
        7,
        15,

        13,
        10,
        20,

        9,
        6,
        11,
    ]
    brootValue = [
        0,

        4,
        11,

        3,
        7,
        10,

        6,
        13,
        5,

        9,
        7,
        10,
    ]
    zoodiacValue = [
        0,
    ]

    colorkey = {
        "red": (255, 0, 0),
        "black": (50, 50, 50),
        "yellow": (255, 255, 0),
        "white": (255, 255, 255),
        "purple": (255, 0, 255),
        "gray": (140, 140, 140),
        "orange": (200, 150, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "void": (0, 0, 0),
        "teal": (2, 63, 120),
        "lilas": (118, 0, 111),
        "magenta": (150, 1, 79),
    }
    for key in bricksimg:
        bricksimg[key] = transform.scale(bricksimg[key], (64, 64))
    for key in enemiesimg:
        enemiesimg[key] = transform.scale(enemiesimg[key], (64, 64))
    for key in greebleimg:
        greebleimg[key] = transform.scale(greebleimg[key], (64, 64))
    altarimg = transform.scale(altarimg, (64, 64))
    altar2img = transform.scale(altar2img, (64, 64))
    swordimg = transform.scale(swordimg, (64, 64))
    for key in raacimg:
        raacimg[key] = transform.scale(raacimg[key], (64, 64))
    for key in traacimg:
        traacimg[key] = transform.scale(traacimg[key], (64, 64))
    for key in brootimg:
            brootimg[key] = transform.scale(brootimg[key], (64, 64))
    for key in zoodiacimg:
        zoodiacimg[key] = transform.scale(zoodiacimg[key], (64, 64))


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

    [20, 18],
    [20, 19],
    [20, 20],
    [20, 21],
    [20, 22],
    [20, 23],
]
    TraacPool = [
        [40, 0],
        [40, 1],
        [40, 2],

        [40, 3],
        [40, 4],
        [20, 5],

        [40, 6],
        [40, 7],
        [30, 8],
    ]
    BrootPool = [
        [0, 0], # [PoolWeight, Id]

        [90, "armed"],
        [60, "defends"],

        [30, "digests"],
        [24, "digs"],
        [36, "deconstructs"],

        [24, "detector"],
        [20, "final"],
        [50, "fights"],

        [16, "frosts"],
        [28, "pierces"],
        [5, "walks"],
    ]

    
# Energy Thermodynamics
# Common Altar charge: 4
# Rare Altar charge: 10
# Unique Altar charge: 25


class Player():
    def __init__(self):
        self.Broots = []
        self.selectedBroot = 0
        self.Zoodiacs = []
        self.selectedZoodiac = 0
        self.Raacs = []
        self.Traacs = []
        self.room = 0

        self.dmg = 0
        self.df = 0
        self.speed = 0

        self.tempDmg = 0
        self.tempDf = 0
        self.tempSpeed = 0

        self.vined = False
        self.lastZoodiacUsed = (4, 11, 0)

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
        # Quality 2b Greebles - ???
        self.Greebles["Xendans"] = 0 # V=56 Corrupted Health

        # Quality 3 Greebles - Maximum Stats and crafting material.
        self.Greebles["Fallers"] = 0 # V=321 Max max HP
        self.Greebles["Rallers"] = 0 # V=505 Crafting
        self.Greebles["Pallers"] = 0 # V=327 Max Max Sackans
        self.Greebles["Sallers"] = 0 # V=626 Max Max Stats
        self.Greebles["Vallers"] = 0 # V=372 Max Xendans

        # Quality 4 Greebles - Maximum of powerful objects, and catalists
        self.Greebles["Bankors"] = 0 # V=2252  Max Traacs
        self.Greebles["Rangors"] = 0 # V=1337  Max Broots
        self.Greebles["Kollors"] = 0 # V=1610  Catalist On
        self.Greebles["Kollors_off"] = 0 # V=1410 Catalist Off
        self.Greebles["Tannors"] = 0 # V=1194  Max Zoodiacs
        self.Greebles["Alators"] = 0 # V=2242 Max Of Q3
        # Quality 4b Greebles - Powerful with Raacs, not to easily find
        self.Greebles["Lunnors"] = 0 # V=  Luck Greeble




        # Quality 5 Greebles - Used in super powerful actions
        self.Greebles["black Star"] = 0
        self.Greebles["purple Note"] = 0
        self.Greebles["white Diamond"] = 0
        self.Greebles["Cyan Heart"] = 0
        self.Greebles["red Flower"] = 0




        self.Highlights = {}
        self.MaxGreebles = {}
        for key in self.Greebles:
            self.Highlights[key] = False
            self.MaxGreebles[key] = 0


        self.Highlights["Heeds"] = True

        for greeb in GQ4+GQ4b:
            self.MaxGreebles[greeb] = 1000
    def initPlayer(self, char):
        if char == -1:
            char = random.randrange(6)
        if char == 0:
            self.acquire(["Bankors", 1+random.randrange(4)]) # Max Traacs
            self.acquire(["Rangors", 2+random.randrange(4)]) # Max Broots
            self.acquire(["Alators", 1+random.randrange(1)]) # Max Broots

            self.acquire(["Fallers", 1+random.randrange(3)]) #
            self.acquire(["Rallers", 0+random.randrange(2)]) #
            self.acquire(["Pallers", 1+random.randrange(2)]) #
            self.acquire(["Sallers", 2+random.randrange(3)]) #
            self.acquire(["Vallers", 0+random.randrange(2)]) #

            self.acquire(["Verdans", 6+random.randrange(10)]) # Max Health
            self.acquire(["Postans", 6+random.randrange(10)]) # Max Food
            self.acquire(["Sackans", 6+random.randrange(10)]) # Max Q0 inventory*4
            self.acquire(["Callans", 1+random.randrange(5)]) # Damage
            self.acquire(["Daffans", 0+random.randrange(4)]) # Defense
            self.acquire(["Radeans", 3+random.randrange(5)]) # Max Health2, Max Health3, Max Energy/2
            self.acquire(["Xendans", 0+random.randrange(2)]) # Corrupted Health

            self.acquire(["Heeds", 6+random.randrange(10)]) # Health
            self.acquire(["Feeds", 15+random.randrange(20)]) # Food
            self.acquire(["Beets", 0+random.randrange(7)]) # Health2
            self.acquire(["Leeds", 0+random.randrange(7)]) # Health3
            self.acquire(["Sheets", 12+random.randrange(20)]) # Energy



            self.acquireRaac(Raac(Raac.chooseRandomRaac(RaacPool)))
            self.acquireTraac(Traac(Traac.chooseRandomTraac(TraacPool)))
        elif char == -2: # Classic
            self.acquire(["Bankors", 5]) # Max Traacs
            self.acquire(["Rangors", 7]) # Max Broots
            self.acquire(["Alators", 1]) # Max Broots

            self.acquire(["Fallers", 2]) #
            self.acquire(["Rallers", 0]) #
            self.acquire(["Pallers", 1]) #
            self.acquire(["Sallers", 3]) #
            self.acquire(["Vallers", 1]) #

            self.acquire(["Verdans", 8]) # Max Health
            self.acquire(["Postans", 10]) # Max Food
            self.acquire(["Sackans", 10]) # Max Q0 inventory*4
            self.acquire(["Callans", 3]) # Damage
            self.acquire(["Daffans", 0]) # Defense
            self.acquire(["Radeans", 6]) # Max Health2, Max Health3, Max Energy/2
            self.acquire(["Xendans", 0]) # Corrupted Health

            self.acquire(["Heeds", 8]) # Health
            self.acquire(["Feeds", 30]) # Food
            self.acquire(["Beets", 6]) # Health2
            self.acquire(["Leeds", 3]) # Health3
            self.acquire(["Sheets", 20]) # Energy

            # self.acquire(["Pots", 50]) # Money

            self.acquireTraac(Traac(6))
            self.acquireTraac(Traac(7))
            self.acquireTraac(Traac(8))
        elif char == 1: # Aries
            self.acquire(["Bankors", 1]) # Max Traacs
            self.acquire(["Rangors", 6]) # Max Broots
            self.acquire(["Alators", 1]) # Max Q3

            self.acquire(["Fallers", 3]) #
            self.acquire(["Rallers", 1]) #
            self.acquire(["Pallers", 1]) #
            self.acquire(["Sallers", 2]) #
            self.acquire(["Vallers", 1]) #

            self.acquire(["Verdans", 16]) # Max Health
            self.acquire(["Postans", 12]) # Max Food
            self.acquire(["Sackans", 7]) # Max Q0 inventory*4
            self.acquire(["Callans", 4]) # Damage
            self.acquire(["Daffans", 0]) # Defense
            self.acquire(["Radeans", 5]) # Leeds/Beets
            self.acquire(["Xendans", 0]) # Corrupted Health

            self.acquire(["Heeds", 14]) # Health
            self.acquire(["Feeds", 30]) # Food
            self.acquire(["Beets", 2]) # Health2
            self.acquire(["Leeds", 0]) # Health3
            self.acquire(["Sheets", 20]) # Energy


            self.acquireRaac(Raac(11))
            self.acquireTraac(Traac(2))
        elif char == 2: # Taurus
            self.acquire(["Bankors", 4]) # Max Traacs
            self.acquire(["Rangors", 1]) # Max Broots
            self.acquire(["Alators", 1]) # Max Q3

            self.acquire(["Fallers", 2]) #
            self.acquire(["Rallers", 0]) #
            self.acquire(["Pallers", 2]) #
            self.acquire(["Sallers", 3]) #
            self.acquire(["Vallers", 0]) #

            self.acquire(["Verdans", 12]) # Max Health
            self.acquire(["Postans", 8]) # Max Food
            self.acquire(["Sackans", 12]) # Max Q0 inventory*4
            self.acquire(["Callans", 3]) # Damage
            self.acquire(["Daffans", 1]) # Defense
            self.acquire(["Radeans", 7]) # Leeds/Beets
            self.acquire(["Xendans", 0]) # Corrupted Health

            self.acquire(["Heeds", 12]) # Health
            self.acquire(["Feeds", 25]) # Food
            self.acquire(["Beets", 0]) # Health2
            self.acquire(["Leeds", 4]) # Health3
            self.acquire(["Sheets", 18]) # Energy


            self.acquireRaac(Raac(15))
            self.acquireRaac(Raac(15))
            # self.acquireTraac(Traac(3))
        elif char == 3: # Gemini
            self.acquire(["Bankors", 2]) # Max Traacs
            self.acquire(["Rangors", 2]) # Max Broots
            self.acquire(["Alators", 2]) # Max Q3

            self.acquire(["Fallers", 3]) #
            self.acquire(["Rallers", 1]) #
            self.acquire(["Pallers", 3]) #
            self.acquire(["Sallers", 3]) #
            self.acquire(["Vallers", 1]) #

            self.acquire(["Verdans", 14]) # Max Health
            self.acquire(["Postans", 10]) # Max Food
            self.acquire(["Sackans", 12]) # Max Q0 inventory*4
            self.acquire(["Callans", 2]) # Damage
            self.acquire(["Daffans", 0]) # Defense
            self.acquire(["Radeans", 8]) # Leeds/Beets
            self.acquire(["Xendans", 2]) # Corrupted Health

            self.acquire(["Heeds", 14]) # Health
            self.acquire(["Feeds", 30]) # Food
            self.acquire(["Beets", 0]) # Health2
            self.acquire(["Leeds", 2]) # Health3
            self.acquire(["Sheets", 22]) # Speed


            self.acquireRaac(Raac(8))
            # self.acquireRaac(Raac(15))
            self.acquireTraac(Traac(3))
        elif char == 4: # Cancer
            self.acquire(["Bankors", 2]) # Max Traacs
            self.acquire(["Rangors", 4]) # Max Broots
            self.acquire(["Alators", 1]) # Max Q3

            self.acquire(["Fallers", 2]) #
            self.acquire(["Rallers", 0]) #
            self.acquire(["Pallers", 2]) #
            self.acquire(["Sallers", 2]) #
            self.acquire(["Vallers", 2]) #

            self.acquire(["Verdans", 12]) # Max Health
            self.acquire(["Postans", 15]) # Max Food
            self.acquire(["Sackans", 14]) # Max Q0 inventory*4
            self.acquire(["Callans", 3]) # Damage
            self.acquire(["Daffans", 0]) # Defense
            self.acquire(["Radeans", 6]) # Leeds/Beets
            self.acquire(["Xendans", 1]) # Corrupted Health

            self.acquire(["Heeds", 12]) # Health
            self.acquire(["Feeds", 40]) # Food
            self.acquire(["Beets", 2]) # Health2
            self.acquire(["Leeds", 4]) # Health3
            self.acquire(["Sheets", 20]) # Speed


            self.acquireRaac(Raac(3))
            # self.acquireRaac(Raac(15))
            self.acquireTraac(Traac(5))
        elif char == 5: # Leo
            self.acquire(["Bankors", 3]) # Max Traacs
            self.acquire(["Rangors", 3]) # Max Broots
            self.acquire(["Alators", 1]) # Max Q3

            self.acquire(["Fallers", 2]) #
            self.acquire(["Rallers", 0]) #
            self.acquire(["Pallers", 3]) #
            self.acquire(["Sallers", 2]) #
            self.acquire(["Vallers", 0]) #

            self.acquire(["Verdans", 13]) # Max Health
            self.acquire(["Postans", 9]) # Max Food
            self.acquire(["Sackans", 9]) # Max Q0 inventory*4
            self.acquire(["Callans", 3]) # Damage
            self.acquire(["Daffans", 2]) # Defense
            self.acquire(["Radeans", 4]) # Leeds/Beets
            self.acquire(["Xendans", 0]) # Corrupted Health

            self.acquire(["Heeds", 13]) # Health
            self.acquire(["Feeds", 25]) # Food
            self.acquire(["Beets", 0]) # Health2
            self.acquire(["Leeds", 4]) # Health3
            self.acquire(["Sheets", 18]) # Speed


            self.acquireRaac(Raac(10))
            self.acquireRaac(Raac(10))
            # self.acquireTraac(Traac(5))
    def damage(self, qtd, game):
        qtd -= self.df//3
        for raac in self.Raacs:
            if raac.name == "RockCrest" and qtd > 0 and self.Greebles["Rocks"] >= 2+raac.level and raac.charged():
                qtd -= raac.level
                self.unacquire(["Rocks", 1])
                self.acquire(["Shots", 1])

        if qtd > 0:
            self.unacquire(["Heeds", qtd])
            if self.Greebles["Heeds"] < 0:
                for deploy in self.room.Deploys:
                    deploy = deploy[0]
                    if deploy.name == "final" and deploy.alive:
                        self.Greebles["Heeds"] = 0
                        deploy.dmg -= 1
                        game.log.append(["final", 1])
                        if deploy.dmg <= 0:
                            deploy.alive = False
                        return qtd
                for raac in self.Raacs:
                    if raac.name == "SaveThrow":
                        break
                else:
                    raac = None
                used = 0
                while raac and raac.used < raac.level and self.Greebles["Verdans"] > 0 and self.Greebles["Heeds"] < 0:
                    self.unacquire(["Verdans", 1])
                    self.acquire(["Xendans", 1])
                    self.acquire(["Heeds", 3])
                    raac.used += 1
                    used += 1
                if used > 0:
                    game.log.append(["SaveThrow", used])
        else:
            qtd = 0
        return qtd
    def acquire(self, greeb):
        name = greeb[0]
        self.Greebles[name] += greeb[1]
        qtd = 0

        if self.Greebles[name] > self.MaxGreebles[name]:
            qtd = self.Greebles[name] -self.MaxGreebles[name]
            self.Greebles[name] = self.MaxGreebles[name]
        else:
            qtd = 0

        amount = greeb[1] - qtd
        if name == "Callans":
            self.dmg += amount
        elif name == "Daffans":
            self.df += amount
        elif name == "Radeans":
            self.MaxGreebles["Sheets"] += 4*amount
            self.MaxGreebles["Leeds"] += amount
            self.MaxGreebles["Beets"] += amount
        elif name == "Verdans":
            self.MaxGreebles["Heeds"] += amount
            self.MaxGreebles["Slops"] += 10*amount
        elif name == "Xendans":
            self.MaxGreebles["Heexs"] += 3*amount
        elif name == "Postans":
            self.MaxGreebles["Feeds"] += 3*amount
        elif name == "Sackans":
            self.MaxGreebles["Shots"] += 10*amount
            self.MaxGreebles["Bloods"] += 10*amount
            self.MaxGreebles["Clots"] += 10*amount
            self.MaxGreebles["Pots"] += 10*amount
            self.MaxGreebles["Rocks"] += 10*amount
        elif name == "Sheets":
            self.speed += amount

        elif name == "Fallers":
            self.MaxGreebles["Verdans"] += 10*amount
            self.MaxGreebles["Postans"] += 10*amount
        elif name == "Pallers":
            self.MaxGreebles["Sackans"] += 15*amount
        elif name == "Sallers":
            self.MaxGreebles["Daffans"] += 10*amount
            self.MaxGreebles["Callans"] += 10*amount
            self.MaxGreebles["Radeans"] += 10*amount
        elif name == "Vallers":
            self.MaxGreebles["Xendans"] += 3*amount

        elif name == "Alators":
            self.MaxGreebles["Fallers"] += 4*amount
            self.MaxGreebles["Rallers"] += 4*amount
            self.MaxGreebles["Pallers"] += 4*amount
            self.MaxGreebles["Sallers"] += 4*amount
            self.MaxGreebles["Vallers"] += 4*amount


        if name in ["Daffans", "Callans", "Radeans"]:
            for name2 in ["Daffans", "Callans", "Radeans"]:
                self.MaxGreebles[name2] -= amount
            self.MaxGreebles[name] += amount
        if name in GQ0:
            for name2 in GQ0:
                self.MaxGreebles[name2] -= amount
            self.MaxGreebles[name] += amount





        return qtd
    def unacquire(self, greeb):
        name = greeb[0]
        self.Greebles[name] -= greeb[1]
        if name == "Callans":
            self.dmg -= greeb[1]
        elif name == "Daffans":
            self.df -= greeb[1]
        elif name == "Radeans":
            self.MaxGreebles["Sheets"] -= 4*greeb[1]
            self.MaxGreebles["Leeds"] -= greeb[1]
            self.MaxGreebles["Beets"] -= greeb[1]
        elif name == "Verdans":
            self.MaxGreebles["Heeds"] -= greeb[1]
            self.MaxGreebles["Slops"] -= 10*greeb[1]
        elif name == "Xendans":
            self.MaxGreebles["Heexs"] -= 3*greeb[1]
        elif name == "Postans":
            self.MaxGreebles["Feeds"] -= 3*greeb[1]
        elif name == "Sackans":
            self.MaxGreebles["Shots"] -= 10*greeb[1]
            self.MaxGreebles["Bloods"] -= 10*greeb[1]
            self.MaxGreebles["Clots"] -= 10*greeb[1]
            self.MaxGreebles["Pots"] -= 10*greeb[1]
            self.MaxGreebles["Rocks"] -= 10*greeb[1]
        elif name == "Sheets":
            self.speed -= greeb[1]

        elif name == "Fallers":
            self.MaxGreebles["Verdans"] -= 10*greeb[1]
            self.MaxGreebles["Postans"] -= 10*greeb[1]
        elif name == "Pallers":
            self.MaxGreebles["Sackans"] -= 15*greeb[1]
        elif name == "Sallers":
            self.MaxGreebles["Daffans"] -= 10*greeb[1]
            self.MaxGreebles["Callans"] -= 10*greeb[1]
            self.MaxGreebles["Radeans"] -= 10*greeb[1]
        elif name == "Vallers":
            self.MaxGreebles["Xendans"] -= 3*greeb[1]


        elif name == "Alators":
            self.MaxGreebles["Fallers"] -= 4*greeb[1]
            self.MaxGreebles["Rallers"] -= 4*greeb[1]
            self.MaxGreebles["Pellers"] -= 4*greeb[1]
            self.MaxGreebles["Sallers"] -= 4*greeb[1]
            self.MaxGreebles["Vallers"] -= 4*greeb[1]

        if name in ["Daffans", "Callans", "Radeans"]:
            for name2 in ["Daffans", "Callans", "Radeans"]:
                self.MaxGreebles[name2] += greeb[1]
            self.MaxGreebles[name] -= greeb[1]
        if name in GQ0:
            for name2 in GQ0:
                self.MaxGreebles[name2] += greeb[1]
            self.MaxGreebles[name] -= greeb[1]

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
                    traac.maxCharge += raac.level
            self.Traacs.append(traac)
        if len(self.Traacs) > self.Greebles["Bankors"]:
            traac = self.Traacs.pop(0)
            for raac in self.Raacs:
                if raac.name == "TraacBest":
                    traac.maxCharge -= raac.level
            return traac
        else:
            return None


class Enemy():
    def __init__(self, id, type, level):
        self.id = id
        self.type = type
        self.level = level
        self.born()
    def born(self):


        hp = 5 + self.level + random.randrange(0, self.level*2+1)
        dmg = 0.5 + self.level/3 +random.randrange(0, 10)/10
        df = self.level/5
        speed = 20 + self.level*2

        if self.level >= 10:
            hp += (self.level-8)*log2(self.level)
            speed += log2(self.level)
            dmg = dmg * 1.2**(self.level/10)



        if self.id == 1: # Common
            hp = hp
            dmg = dmg
            df = df
            speed = speed
            name = "Common"
            description = "Boring enemy"
        elif self.id == 2: # Fast
            hp = hp*0.5
            dmg = dmg*0.7
            df = df*0.3
            speed = speed*1.25
            name = "Fast"
            description = "Higher Speed"
        elif self.id == 3: # Armored
            hp = hp*1.2
            dmg = dmg*1.1
            df = df*1.3
            name = "Armored"
            speed = speed*0.7
            description = "Higher Defense"
        elif self.id == 4: # Plated
            hp = hp*1.4
            dmg = dmg*0.8
            df = df*1.2
            name = "Plated"
            speed = speed*0.5
            description = "Grants +1 Defense for adjacent enemies"
        elif self.id == 5: # Slime
            hp = hp*1.45
            dmg = dmg*1.1
            df = df*0.6
            name = "Slime"
            speed = speed*0.7
            description = "Splits in two on death."
        elif self.id == 6: # Wasp
            hp = hp*0.75
            dmg = dmg*0.8
            df = df*0.9
            name = "Wasp"
            speed = speed*1.1
            description = "Weak."
        elif self.id == 7: # Wasp Nest
            hp = hp*1.5
            dmg = dmg*0.6
            df = df*1.25
            name = "Wasp Nest"
            speed = speed*0.8
            description = "Generates Wasps in adjacent rooms."
            self.genNum = self.level
        elif self.id == 8: # Skeleton
            hp = hp*1
            dmg = dmg*1.1
            df = df*1.4
            name = "Skeleton"
            speed = speed*1.1
            description = "Patrols through adjacent rooms."



        elif self.id == 50: # Vine
            hp = hp*0.5
            dmg = dmg*0.7
            df = df*0.3
            name = "Vine"
            speed = speed*1.2
            description = "Can't leave the Room until killed"




        elif self.id == 97: # Scorpion
            hp = hp*0.8
            dmg = dmg*1.75
            df = df*2
            name = "Scorpion"
            speed = speed*0.9
            description = "Attacks you if you get close to the room"
        elif self.id == 98: # FireBreather
            hp = hp*1.8
            dmg = dmg*0.9
            df = df*1.8
            name = "FireBreather"
            speed = speed*0.7
            description = "Steals Greebles from Floor"
        elif self.id == 99: # Envinerator
            hp = hp*1.5
            dmg = dmg*1.3
            df = df*1.6
            name = "Envinerator"
            speed = speed*0.9
            description = "Spawns Vines in the entire Floor"
            self.genNum = self.level
        else:
            name = "ERROR"
            print("ERROR")
            print(self.id)


        if self.type == "King": # King
            hp = hp*2
            dmg = dmg*1.45
            df = df*1.2
            speed = speed*1.1
            name = "The " + name
            self.charge = 10
        elif self.type == "Boss": # Boss
            hp = hp*1.75
            dmg = dmg*1.35
            df = df*1.1
            speed = speed
            name = "Boss " + name
            self.charge = 4
        elif self.type == "Elite": # Elite
            hp = hp*1.25
            dmg = dmg*1.3
            df = df*0.9
            speed = speed*0.9
            name = "Elite " + name
            self.charge = 2
        else:
            self.charge = 1

        self.name = name
        self.hp = hp*random.randrange(7, 14)/10
        self.dmg = dmg*random.randrange(7, 14)/10
        self.df = df*random.randrange(7, 14)/10
        self.speed = speed*random.randrange(7, 14)/10

        self.hp = floor(self.hp)
        self.dmg = max(1, floor(self.dmg))
        self.df = self.df
        self.speed = floor(self.speed)
        self.mhp = self.hp

        self.description = description
        self.turn = 0
        self.playerTurn = 0
    def damage(self, qtd):
        qtd -= self.df
        if qtd > 0:
            self.hp -= qtd
    def chooseRandomEnemy():
        RNG = random.randrange(1, 9)
        return RNG
    def chooseRandomBoss():
        return random.randrange(97, 100)

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
            self.rarity = "Unique"
        elif self.id == 1: # Heeds Altar
            self.recipe = [
                ["Bloods", 2],
                ["Clots", 1],
            ]
            self.products = [
                ["Heeds", 1]
            ]
            self.maxuses = 6
            self.rarity = "Common"
        elif self.id == 2: # Feeds Altar
            self.recipe = [
                ["Shots", 2],
                ["Bloods", 1],
            ]
            self.products = [
                ["Feeds", 1]
            ]
            self.maxuses = 10
            self.rarity = "Common"
        elif self.id == 3: # Beets Altar
            self.recipe = [
                ["Pots", 2],
                ["Bloods", 1],
            ]
            self.products = [
                ["Beets", 1]
            ]
            self.maxuses = 3
            self.rarity = "Uncommon"
        elif self.id == 4: # Sheets Altar
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
            self.rarity = "Common"
        elif self.id == 5: # Daffans Altar
            self.recipe = [
                ["Sheets", 2],
                ["Leeds", 3],
            ]
            self.products = [
                ["Daffans", 1]
            ]
            self.maxuses = 2
            self.rarity = "Rare"
        elif self.id == 6: # Sackans Altar
            self.recipe = [
                ["Leeds", 1],
                ["Feeds", 1],
                ["Sheets", 1],
            ]
            self.products = [
                ["Sackans", 1]
            ]
            self.maxuses = 4
            self.rarity = "Uncommon"
        elif self.id == 7: # Verdans Altar
            self.recipe = [
                ["Beets", 2],
                ["Heeds", 1],
                ["Leeds", 1],
            ]
            self.products = [
                ["Verdans", 1]
            ]
            self.maxuses = 2
            self.rarity = "Uncommon"
        elif self.id == 8: # Callans Altar
            self.recipe = [
                ["Sheets", 4],
                ["Beets", 2],
            ]
            self.products = [
                ["Callans", 1]
            ]
            self.maxuses = 2
            self.rarity = "Rare"
        elif self.id == 9: # Radeans Altar
            self.recipe = [
                ["Beets", 2],
                ["Leeds", 2],
            ]
            self.products = [
                ["Radeans", 1]
            ]
            self.maxuses = 2
            self.rarity = "Rare"
        elif self.id == 10: # Clot Filter Altar
            self.recipe = [
                ["Clots", 5],
            ]
            self.products = [
                ["Feeds", 1],
                ["Shots", 5],
            ]
            self.maxuses = 5
            self.rarity = "Common"
        elif self.id == 11: # Rock Crusher Altar
            self.recipe = [
                ["Rocks", 5],
            ]
            self.products = [
                ["Heeds", 1],
                ["Pots", 5],
            ]
            self.maxuses = 5
            self.rarity = "Common"
        elif self.id == 12: # Pallers Altar
            self.recipe = [
                ["Radeans", 2],
                ["Sackans", 3],
            ]
            self.products = [
                ["Pallers", 1],
            ]
            self.maxuses = 1
            self.rarity = "Mythical"
        elif self.id == 13: # Sallers Altar
            self.recipe = [
                ["Daffans", 2],
                ["Callans", 2],
                ["Radeans", 2],
            ]
            self.products = [
                ["Sallers", 1],
            ]
            self.maxuses = 1
            self.rarity = "Mythical"
        elif self.id == 14: # Cleansing Altar
            self.recipe = [
                ["Xendans", 1],
                ["Clots", 2],
            ]
            self.products = [
                ["Verdans", 1],
            ]
            self.maxuses = 2
            self.rarity = "Uncommon"
        elif self.id == 15: # Anti Slop Altar
            self.recipe = [
                ["Slops", 5],
            ]
            self.products = [
                [random.choice(GQ0), 1],
            ]
            self.maxuses = 7
            self.rarity = "Common"
        elif self.id == 16: # Super Callans Altar
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
            self.rarity = "Common"
        elif self.id == 17: # Super Heeds Altar
            self.recipe = [
                ["Kollors", 1],
                ["Bloods", 20],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Heeds", 10],
            ]
            self.maxuses = 3
            self.rarity = "Common"
        elif self.id == 18: # Super Daffans Altar
            self.recipe = [
                ["Kollors", 1],
                ["Leeds", 10],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Daffans", 3],
            ]
            self.maxuses = 2
            self.rarity = "Common"
        elif self.id == 19: # Super Feeds Altar
            self.recipe = [
                ["Kollors", 1],
            ]
            self.products = [
                ["Kollors_off", 1],
                ["Feeds", 8],
            ]
            self.maxuses = 4
            self.rarity = "Common"
        elif self.id == 20: # Anti Leed Altar
            self.recipe = [
                ["Leeds", 2],
            ]
            self.products = [
                ["Clots", 5],
                ["Pots", 2],
            ]
            self.maxuses = 12
            self.rarity = "Rare"
        elif self.id == 21: # KOLLORS Altar
            self.recipe = [
                ["Rallers", 2],
                ["Sallers", 1],
            ]
            self.products = [
                ["Kollors", 1],
            ]
            self.maxuses = 1
            self.rarity = "Unique"
        elif self.id == 22: # Fallers Altar
            self.recipe = [
                ["Verdans", 2],
                ["Xendans", 2],
                ["Radeans", 1],
            ]
            self.products = [
                ["Fallers", 1],
            ]
            self.maxuses = 1
            self.rarity = "Mythical"
        elif self.id == 23: # Leeds Altar
            self.recipe = [
                ["Shots", 2],
                ["Rocks", 2],
            ]
            self.products = [
                ["Leeds", 1],
            ]
            self.maxuses = 4
            self.rarity = "Uncommon"
        elif self.id == 24: # Postans Altar
            self.recipe = [
                ["Leeds", 2],
                ["Feeds", 2],
            ]
            self.products = [
                ["Postans", 1],
            ]
            self.maxuses = 3
            self.rarity = "Uncommon"
        elif self.id == 25: # Radaeans2 Altar
            self.recipe = [
                ["Leeds", 2],
                ["Heexs", 2],
            ]
            self.products = [
                ["Radeans", 1],
            ]
            self.maxuses = 8
            self.rarity = "Uncommon"
        elif self.id == 26: # Vallers Altar
            self.recipe = [
                ["Verdans", 3],
                ["Xendans", 3],
            ]
            self.products = [
                ["Vallers", 1],
            ]
            self.maxuses = 2
            self.rarity = "Mythical"
        elif self.id == 27: # Rallers Altar
            self.recipe = [
                ["Verdans", 1],
                ["Postans", 1],
                ["Sackans", 1],
                ["Callans", 1],
                ["Daffans", 1],
                ["Radeans", 1],
            ]
            self.products = [
                ["Rallers", 1],
            ]
            self.maxuses = 2
            self.rarity = "Mythical"
        elif self.id == 28: # BANKORS Altar
            self.recipe = [
                ["Rallers", 2],
                ["Sallers", 2],
            ]
            self.products = [
                ["Bankors", 1],
            ]
            self.maxuses = 1
            self.rarity = "Unique"
        elif self.id == 29: # RANGORS Altar
            self.recipe = [
                ["Rallers", 2],
                ["Pallers", 1],
            ]
            self.products = [
                ["Rangors", 1],
            ]
            self.maxuses = 2
            self.rarity = "Unique"
        elif self.id == 30: # TANNORS Altar
            self.recipe = [
                ["Rallers", 1],
                ["Fallers", 1],
                ["Vallers", 1],
            ]
            self.products = [
                ["Tannors", 1],
            ]
            self.maxuses = 1
            self.rarity = "Unique"
        elif self.id == 31: # ALATORS Altar
            self.recipe = [
                ["Vallers", 1],
                ["Sallers", 3],
            ]
            self.products = [
                ["Alators", 1],
            ]
            self.maxuses = 1
            self.rarity = "Unique"
        elif self.id == 32: # Xendans Altar
            self.recipe = [
                ["Heeds", 1],
                ["Heexs", 3],
            ]
            self.products = [
                ["Xendans", 1],
            ]
            self.maxuses = 4
            self.rarity = "Rare"
        elif self.id == 32: # Anti Heexs Altar
            self.recipe = [
                ["Shots", 2],
                ["Heexs", 1],
            ]
            self.products = [
                ["Pots", 2],
            ]
            self.maxuses = 7
            self.rarity = "Common"
    def chooseRandomAltar():
        AltarPool = [
            [0, 0], # [PoolWeight, Id]
            [80, 1],
            [30, 2],
            [40, 3],
            [20, 4],
            [16, 5],
            [10, 6],
            [18, 7],
            [20, 8],
            [12, 9],
            [16, 10],
            [16, 11],
            [7, 12],
            [20, 13],
            [8, 14],
            [12, 15],

            [3, 16],
            [3, 17],
            [3, 18],
            [3, 19],

            [8, 20],
            [5, 21],
            [8, 22],
            [8, 23],
            [8, 24],
            [24, 25],

            [8, 26],
            [8, 27],

            [3, 28],
            [3, 29],
            [3, 30],
            [3, 31],

            [9, 32],
            [13, 33],
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
        self.Zoodiacs = []

        self.objects = []


        self.width = Width
        self.height = Height
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
            if type == "greeble":
                object.append((w, h))
            self.objects[w][h][3] = [object, w, h]
            self.objects[w][h][2] = type

            if type == "greeble":
                self.Greebles.append(self.objects[w][h][3])
            elif type == "broot":
                self.Broots.append(self.objects[w][h][3])
            elif type == "deploy":
                self.Deploys.append(self.objects[w][h][3])
            elif type == "raac":
                self.Raacs.append(self.objects[w][h][3])
            elif type == "traac":
                self.Traacs.append(self.objects[w][h][3])
            elif type == "shop":
                self.Shops.append(self.objects[w][h][3])
            elif type == "enemy":
                self.Enemies.append(self.objects[w][h][3])
            elif type == "altar":
                self.Altars.append(self.objects[w][h][3])
            elif type == "zoodiac":
                self.Zoodiacs.append(self.objects[w][h][3])
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
        elif type == "zoodiac":
            self.Zoodiacs.remove(ob)
        self.objects[w][h][3] = None
        self.objects[w][h][2] = ""
    def populate(self, params):
        if self.color == "red" and self.type == "normal":
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Normal", self.level), "enemy")
        elif self.color == "red" and self.type == "plate":
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Normal", self.level+2), "enemy")
            self.randomGreeble(1, self.level)
            self.randomGreeble(2, min(round(log2(self.level))-3, 0))
        elif self.color == "yellow" and self.type == "normal":
            temp1 = self.level
            self.randomGreeble(1, temp1+2)
            RNG = random.randrange(100)
            if RNG < params[4]:
                self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")
        elif self.color == "yellow" and self.type == "plate":
            temp2 = self.level//5
            self.randomGreeble(2, temp2)
            self.randomGreeble(1, temp2*3)
            RNG = random.randrange(100)
            if RNG < params[4]*3:
                self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")
        elif self.color == "black" and self.type == "normal":
            if self.level % 5 == 0 and self.level != 0:
                self.type = "plate"
            else:
                self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Boss", self.level), "enemy")
                RNG = random.randrange(100)
                if RNG <= 20:
                    self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
                else:
                    self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
                self.acquire(["Feeds", 5+round(self.level*1.5)])
        elif self.color == "purple" and self.type == "normal":
            self.findFreePosition(Altar(Altar.chooseRandomAltar()), "altar")
        elif self.color == "purple" and self.type == "plate":
            self.findFreePosition(Altar(0), "altar")
        elif self.color == "white" and self.type == "normal":
            return
        elif self.color == "gray" and self.type == "normal":
            temp = ceil(log2(self.level+1)) + 1
            self.randomGreeble(0, temp)
        elif self.color == "gray" and self.type == "plate":
            temp = ceil(2*log2(self.level+1)) + 2
            self.randomGreeble(0, temp)
        elif self.color == "green" and self.type == "normal":
            temp = self.level*2 +4*params[0]
            self.randomShop(temp, True)
        elif self.color == "green" and self.type == "plate":
            temp = self.level*2 +2*params[0]
            self.randomShop(temp, False)
        elif self.color == "orange" and self.type == "normal":
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Elite", self.level), "enemy")
            RNG = random.randrange(100)
            if RNG <= 80:
                self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
            else:
                self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
            temp1 = self.level
            self.randomGreeble(1, temp1-2)
        elif self.color == "orange" and self.type == "plate":
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Elite", self.level+1), "enemy")
            typee = Enemy.chooseRandomEnemy()
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Elite", self.level+1), "enemy")
            for i in range(3):
                RNG = random.randrange(100)
                if RNG <= 40:
                    self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
                else:
                    self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
            temp1 = self.level
            self.randomGreeble(1, 2*temp1)
            self.randomGreeble(2, temp1//5)
        elif self.color == "blue" and self.type == "normal":
            RNG = random.randrange(100)
            if RNG <= 50:
                pass
            if RNG <= 55:
                self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
            else:
                self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
            temp1 = self.level
            self.randomGreeble(1, temp1)
            self.randomGreeble(2, temp1//3)
        elif self.color == "cyan" and self.type == "normal":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 3
                RNG = random.randrange(1, len(brootNumber)-1)
                broot = Broot(RNG, 1+params[3])
                self.findFreePosition(broot)
        elif self.color == "cyan" and self.type == "plate":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 2
                RNG = random.randrange(1, len(brootNumber)-1)
                broot = Broot(RNG, 2+params[3])
                self.findFreePosition(broot)
        elif self.color == "magenta" and self.type == "normal":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 7
                self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")
        elif self.color == "magenta" and self.type == "plate":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 5
                self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")

        if self.color == "black" and self.type == "plate":
            for i in range(2):
                RNG = random.randrange(100)
                if RNG <= 20:
                    self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
                else:
                    self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
            self.acquire(["Feeds", 10+round(self.level*2)])
            self.findFreePosition(Enemy(Enemy.chooseRandomBoss(), "King", self.level), "enemy")
    def depopulate(self):
        for w in range(self.width):
            for h in range(self.height):
                self.freeePosition(w, h)
    def acquire(self, greeb):
        if greeb[1] == 0:
            return
        for greeb2 in self.Greebles:
            if greeb2[0][0] == greeb[0]:
                greeb2[0][1] += greeb[1]
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
    def checkEnemyLife(self, player, game):

        Red = False
        for enemy in self.Enemies:
            enemy = enemy[0]
            if enemy.hp > 0:
                Red = True
            elif enemy.id != 0:
                enemyEnergy = 20+3*round(sqrt(enemy.mhp*(enemy.df+1)*enemy.speed*enemy.dmg))
                enemyCharge = enemy.charge
                print(enemyEnergy)

                if enemy.id == 5:
                    hp = enemy.mhp/3
                    dmg = enemy.dmg/2
                    df = enemy.df/2
                    if hp > 5 and dmg > 1:
                        em1 = Enemy(enemy.id, "Normal", self.level)
                        em2 = Enemy(enemy.id, "Normal", self.level)
                        em1.hp = hp
                        em1.mhp = hp
                        em1.dmg = dmg
                        em1.df = df

                        em2.hp = hp
                        em2.mhp = hp
                        em2.dmg = dmg
                        em2.df = df
                        for rm2 in self.connections:
                            if em1 == None:
                                break
                            if rm2.color == "gray":
                                rm2.findFreePosition(em1, "enemy")
                                rm2.color = "red"
                                em1 = em2
                                em2 = None
                elif enemy.id == 4:
                    for rm2 in self.connections:
                        for enemy2 in rm2.Enemies:
                            enemy2 = enemy2[0]
                            enemy2.df -= 1

                EnemyLoot = 0
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


                    if raac.name == "EnemyLoot" and raac.charged():
                        EnemyLoot += 2*raac.level
                    elif raac.name == "BlackTest" and enemy.type in ["Boss", "King"] and raac.charged():
                        enemyCharge += raac.level*2
                    elif raac.name == "Vampire":
                        times = raac.level
                        while player.Greebles["Bloods"] > 2 and player.Greebles["Heeds"] < player.MaxGreebles["Heeds"] and times > 0 and raac.charged():
                            times -= 1
                            player.unacquire(["Bloods", 2])
                            player.acquire(["Heeds", 1])
                else:
                    EnemyLoot = 0


                enemy.id = 0
                traacCost = 20+self.level*5

                
                RNG = random.randrange(100)
                if RNG < game.params[4]:
                    self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")

                for traac in player.Traacs:
                    temp = enemyCharge
                    while enemyEnergy >= traacCost and temp > 0:
                        temp -= 1
                        traac.charge += 1
                        enemyEnergy -= traacCost
                        if traac.charge > traac.maxCharge:
                            enemyEnergy += traacCost
                            traac.charge -= 1
                            break

                loot = floor(log(enemy.mhp+1, 4)) + EnemyLoot
                if loot > 0:
                    if enemy.id == 5:
                        self.acquire(["Slops", loot])
                    elif enemy.id == 4:
                        self.acquire(["Rocks", loot//2])
                        self.randomGreeble(0, 1+loot//2)
                    else:
                        self.randomGreeble(0, loot)

        if self.color == "red" and not Red:
            self.color = "gray"
    def randomShop(self, temp, buy):
        # item = ["Raac", "Treasure", 10, "Pots"]

        while temp > 0:
            if buy:
                RNG = random.randrange(100)
                if RNG <= 4 and temp >= 6:
                    itemtype = "Traac"
                    temp -= 6
                elif RNG <= 16 and temp >= 5:
                    itemtype = "Raac"
                    temp -= 5
                elif RNG <= 25 and temp >= 8:
                    itemtype = "Zoodiac"
                    temp -= 8
                elif RNG <= 40 and temp >= 3:
                    itemtype = "Broot"
                    temp -= 3
                else:
                    itemtype = "Greeble"
                    temp -= 1
            else:
                itemtype = "Greeblbe"
                temp -= 3

            if buy:
                if itemtype == "Greeble":
                    RNG = random.randrange(1000)
                    if RNG <= 1:
                        name = random.choice(GQ4)
                        value = 54
                    elif RNG <= 22:
                        name = random.choice(GQ3)
                        value = 22
                    elif RNG <= 150:
                        name = random.choice(GQ2)
                        value = 8
                    else:
                        name = random.choice(GQ1)
                        value = 2
                elif itemtype == "Raac":
                    RNG = random.randrange(len(raacimg))
                    raacTemp = Raac(RNG)
                    name = raacTemp.name
                    value = raacValue[RNG]
                elif itemtype == "Traac":
                    RNG = random.randrange(len(traacimg))
                    traacTemp = Traac(RNG)
                    name = traacTemp.name
                    value = traacValue[RNG]
                elif itemtype == "Broot":
                    RNG = random.randrange(1, len(brootNumber)-1)
                    name = brootNumber[RNG]
                    value = brootValue[RNG]
                elif itemtype == "Zoodiac":
                    idd = Zoodiac.chooseRandomZoodiac()
                    name = str(idd[0]+1) + "-" + str(idd[1]+1) + "-" + str(idd[2]+1)
                    value = 15
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
                        name = random.choice(GQ4)
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
    def prize(self):
        if self.color == "red":
            typee = Enemy.chooseRandomEnemy()
            self.findFreePosition(Enemy(typee, "Normal", self.level), "enemy")
            self.findFreePosition(Enemy(typee, "Normal", self.level), "enemy")
            self.randomGreeble(1, self.level//2)
            if self.type == "plate":
                self.randomGreeble(2, self.level//4)
                typee = Enemy.chooseRandomEnemy()
                self.findFreePosition(Enemy(typee, "Normal", self.level), "enemy")

            RNG = random.randrange(100)
            if RNG <= 20:
                self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
            else:
                self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
        elif self.color == "orange":
            self.randomGreeble(2, self.level//3)
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 5
                self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
                if self.type == "plate":
                    self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
                    temp1 -= 2
        elif self.color == "yellow":
            self.randomGreeble(1, self.level)
            self.randomGreeble(2, self.level//3)
            self.randomGreeble(3, self.level//7)
            if self.type == "plate":
                self.randomGreeble(3, self.level//5)
        elif self.color == "white":
            self.randomGreeble(2, self.level//5)
            self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
            self.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac")
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Normal", self.level), "enemy")
            self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")
            self.findFreePosition(Broot(Broot.chooseRandomBroot(BrootPool), 1), "broot")
            self.randomShop(15, True)
            self.findFreePosition(Altar(Altar.chooseRandomAltar()), "altar")
        elif self.color == "green":
            self.randomShop(5*self.level, True)
            if self.type == "plate":
                self.randomShop(5*self.level, False)
        elif self.color == "cyan":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 2
                RNG = random.randrange(1, len(brootNumber)-1)
                level = 1
                if self.type == "plate":
                    level += 2
                broot = Broot(RNG, level)
                self.findFreePosition(broot)
        elif self.color == "gray":
            self.randomGreeble(0, self.level*2)
            if self.type == "plate":
                self.randomGreeble(1, self.level)
        elif self.color == "teal":
            pass
        elif self.color == "blue":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 3
                self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
        elif self.color == "black":
            self.acquire(["Feeds", 5*self.level])
            self.randomGreeble(1, self.level)
            self.randomGreeble(2, self.level//3)
            self.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac")
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Boss", self.level), "enemy")
            self.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Boss", self.level), "enemy")
            self.findFreePosition(Zoodiac((3, 3, 1)), "zoodiac")
            pass
        elif self.color == "purple":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 2
                self.findFreePosition(Altar(Altar.chooseRandomAltar()), "altar")
                if self.type == "plate":
                    self.findFreePosition(Altar(0), "altar")
                    temp1 -= 1
        elif self.color == "magenta":
            temp1 = self.level
            while temp1 > 0:
                temp1 -= 2
                self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")
                if self.type == "plate":
                    self.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac")
                    temp1 -= 1

class Broot():
    def __init__(self, id, squireLevel = 1):
        self.id = id
        self.x = 0
        self.y = 0
        self.alive = True
        self.generate(squireLevel)
    def generate(self, squireLevel):
        if self.id == 1: # Armed
            self.hp = 10*squireLevel
            self.dmg = 4*squireLevel
            self.speed = 20+5*squireLevel
            self.name = "armed"
            self.trueName = "One who is Armed at Intersections"
        elif self.id == 2: # Defends
            self.hp = 15*squireLevel
            self.dmg = 1*squireLevel
            self.speed = 30+5*squireLevel
            self.name = "defends"
            self.trueName = "One who Defends at Intersections"
        elif self.id == 3: # Digests
            self.hp = 25*squireLevel
            self.dmg = 1*squireLevel
            self.speed = 10+5*squireLevel
            self.name = "digests"
            self.trueName = "It Eats greebles and turn them to Slop"
        elif self.id == 4: # Dig
            self.hp = 10*squireLevel
            self.dmg = 1*squireLevel
            self.speed = 24+4*squireLevel
            self.action = 0
            self.cost = 3
            self.name = "digs"
            self.trueName = "It Digs for Greebles and does not Stop"
        elif self.id == 5: # Deconstructs
            self.hp = 20*squireLevel
            self.dmg = 1*squireLevel
            self.speed = 5*squireLevel
            self.name = "deconstructs"
            self.trueName = "It Deconstructs Altars for Greebles"
        elif self.id == 6: # Detector
            self.hp = 35*squireLevel
            self.dmg = 1*squireLevel
            self.speed = 10*squireLevel
            self.name = "detector"
            self.trueName = "Its Detection will reveal Secret Rooms"
        elif self.id == 7: # Final
            self.hp = 15*squireLevel
            self.dmg = 1*squireLevel
            self.speed = 5*squireLevel
            self.name = "final"
            self.trueName = "Its life will be Sacrificed for you"
        elif self.id == 8: # Fights
            self.hp = 30*squireLevel
            self.dmg = 5*squireLevel
            self.speed = 15+10*squireLevel
            self.name = "fights"
            self.trueName = "Its life will be spent fighting in the Room"
        elif self.id == 9: # Frosts
            self.hp = 15*squireLevel
            self.dmg = 3*squireLevel
            self.speed = 25+12*squireLevel
            self.name = "frosts"
            self.trueName = "Enemies will be slown down by it"
        elif self.id == 10: # Pierces
            self.hp = 40*squireLevel
            self.dmg = 2*squireLevel
            self.speed = 25+7*squireLevel
            self.name = "pierces"
            self.trueName = "Enemies armor will break by it"
        elif self.id == 11: # Walks
            self.hp = 40*squireLevel
            self.dmg = 5*squireLevel
            self.speed = 25+10*squireLevel
            self.name = "walks"
            self.trueName = "Enemies will be hunt down by it"


        self.level = squireLevel

        self.mhp = self.hp
    def namesID(name):
        if name == "DEAD": return 0
        elif name == "armed": return 1
        elif name == "defends": return 2

        elif name == "digests": return 3
        elif name == "digs": return 4
        elif name == "deconstructs": return 5

        elif name == "detector": return 6
        elif name == "final": return 7
        elif name == "fights": return 8

        elif name == "frosts": return 9
        elif name == "pierces": return 10
        elif name == "walks": return 11
    def deploy(self, x, y, room):
        self.x = x
        self.y = y
        self.room = room
    def damage(self, qtd):
        self.hp -= qtd
        if self.hp <= 0 and self.alive:
            self.dmg = 0
            self.alive = False
    def chooseRandomBroot(BrootPool, affectPool = True):
        total = 0
        for broot in BrootPool:
            total += broot[0]

        RNG = random.randrange(1, total+1)
        id = 0
        for broot in BrootPool:
            RNG -= broot[0]
            if RNG <= 0:
                break
            id += 1

        if affectPool:
            BrootPool[id][0] += round(len(BrootPool)*0.5)
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
        if self.id == 0: # Altar
            self.name = "Treasure"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor divisible by 2, X Yellow Rooms will permanently be added to the pool."
            self.quality = 4

            self.source = "Floor"
            self.maxCharge = 1500
            self.cost = 80
            self.rate = 50
            self.upgrades = [500, 80, 50]
        elif self.id == 1: # BeetHeal
            self.name = "BeetHeal"
            self.trigger = "Discover"
            self.description = "Every time you discover a room, X*20% chance for a Beet to be converted to a Heed+Pot if not at max."
            self.quality = 5

            self.source = "Discover"
            self.maxCharge = 500
            self.cost = 8
            self.rate = 12
            self.upgrades = [250, 0, 2]
        elif self.id == 2: # FencorRegen
            self.name = "FencorRegen"
            self.trigger = "Floor"
            self.description = "Every time you enter a floor. You get 3*X*Fencor Heeds."
            self.quality = 2

            self.source = "Floor"
            self.maxCharge = 500
            self.cost = 45
            self.rate = 50
            self.upgrades = [500, 45, 40]
        elif self.id == 3: # SaveThrow
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
        elif self.id == 5: # Altar
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
        elif self.id == 7: # ColoredRoom
            self.name = "ColoredRoom"
            self.trigger = "Floor"
            self.description = "Random rooms can have their colors revealed"
            self.quality = 6

            self.source = "Floor"
            self.maxCharge = 250
            self.cost = 5
            self.rate = 20
            self.upgrades = [150, 0, 10]
        elif self.id == 8: # LuckyCharm
            self.name = "LuckyCharm"
            self.trigger = "Discover"
            self.description = "Quality 0 Greebles have chance to become Quality 1"
            self.quality = 5

            self.source = "Discover"
            self.maxCharge = 600
            self.cost = 20
            self.rate = 50
            self.upgrades = [200, 0, 20]
        elif self.id == 9: # Pottery
            self.name = "Pottery"
            self.trigger = "Discover"
            self.description = "When discovering rooms, chance to transform Shots into Pots."
            self.quality = 3

            self.source = "Discover"
            self.maxCharge = 500
            self.cost = 5
            self.rate = 50
            self.upgrades = [150, 0, 20]
        elif self.id == 10: # ExtraStock
            self.name = "ExtraStock"
            self.trigger = "Floor"
            self.description = "Shops have more quality."
            self.quality = 3

            self.source = "Floor"
            self.maxCharge = 1000
            self.cost = 20
            self.rate = 50
            self.upgrades = [400, 20, 25]
        elif self.id == 11: # SplashDamage
            self.name = "SplashDamage"
            self.trigger = "Attack"
            self.description = "When attacking enemies, if there are enemies in adjacent rooms, deal 35% damage to X of them."
            self.quality = 5

            self.source = "EnemyKill"
            self.maxCharge = 2000
            self.cost = 5
            self.rate = 20
            self.upgrades = [700, 0, 20]
        elif self.id == 12: # RockCrest
            self.name = "RockCrest"
            self.trigger = "Defend"
            self.description = "If you have 2+X rocks, you receive X defense. On damage, Rocks break into Shots."
            self.quality = 4

            self.source = "Discover"
            self.maxCharge = 1000
            self.cost = 5
            self.rate = 10
            self.upgrades = [120, 0, 2]
        elif self.id == 13: # SlimeFest
            self.name = "SlimeFest"
            self.trigger = "Floor"
            self.description = "Each Floor you turn X of each quality 0 Greebles into slime, and add X new gray rooms to the floor permanently."
            self.quality = 2

            self.source = "Floor"
            self.maxCharge = 300
            self.cost = 5
            self.rate = 10
            self.upgrades = [50, 0, 10]
        elif self.id == 14: # LeedQuest
            self.name = "LeedQuest"
            self.trigger = "Floor"
            self.description = "Each Floor if you can, lose 3X Leeds, add X red rooms permanently."
            self.quality = 6

            self.source = "Floor"
            self.maxCharge = 600
            self.cost = 40
            self.rate = 60
            self.upgrades = [200, 30, 60]
        elif self.id == 15: # TraacBest
            self.name = "TraacBest"
            self.trigger = "Always"
            self.description = "Traac items have X more max charge."
            self.quality = 7

            self.source = "Floor"
            self.maxCharge = 1000
            self.cost = 60
            self.rate = 40
            self.upgrades = [400, 0, 30]
        elif self.id == 16: # AltarRest
            self.name = "AltarRest"
            self.trigger = "Floor"
            self.description = "If there is an unused altar at the end of the floor, consume it to gain 3X Heexs."
            self.quality = 4

            self.source = "Floor"
            self.maxCharge = 750
            self.cost = 40
            self.rate = 60
            self.upgrades = [250, 40, 60]
        elif self.id == 17: # BlackTest
            self.name = "BlackTest"
            self.trigger = "BossKill"
            self.description = "Bosses will give +2X charges to your Traacs"
            self.quality = 5

            self.source = "EnemyKill"
            self.maxCharge = 2500
            self.cost = 20
            self.rate = 45
            self.upgrades = [500, 20, 15]
        elif self.id == 18:
            self.name = "Vampire"
            self.trigger = "EnemyKill"
            self.description = "Everytime you kill an enemy, consume 2X Bloods to recover X Heeds"
            self.quality = 4

            self.source = "EnemyKill"
            self.maxCharge = 500
            self.cost = 10
            self.rate = 30
            self.upgrades = [250, 10, 10]
        elif self.id == 19: # FrostAspect
            self.name = "FrostAspect"
            self.trigger = "Attack"
            self.description = "Your attacks slows enemies down by X(2+Tannor) speed."
            self.quality = 5

            self.source = "Floor"
            self.maxCharge = 1500
            self.cost = 15
            self.rate = 50
            self.upgrades = [500, 15, 25]
        elif self.id == 20:
            self.name = "Squire"
            self.trigger = "Always"
            self.description = "Increases General Broots abilities."
            self.quality = 8

            self.source = "Floor"
            self.maxCharge = 2000
            self.cost = 30
            self.rate = 100
            self.upgrades = [1000, 30, 50]
        elif self.id == 21: # Hammlet
            self.name = "Hammlet"
            self.trigger = "Attack"
            self.description = "Your attacks break 0.5X armor"
            self.quality = 4

            self.source = "Floor"
            self.maxCharge = 3000
            self.cost = 5
            self.rate = 50
            self.upgrades = [300, 5, 0]
        elif self.id == 22: # Revishot
            self.name = "Revishot"
            self.trigger = "Floor"
            self.description = "Every Floor, remove 2X Shots and gain X temporary Def points."
            self.quality = 2

            self.source = "EnemyKill"
            self.maxCharge = 1000
            self.cost = 10
            self.rate = 15
            self.upgrades = [500, 10, 5]
        elif self.id == 23: # MagicEye
            self.name = "MagicEye"
            self.trigger = "Discover"
            self.description = "Blue Rooms are revealed when connected to purple rooms. Up to X times"
            self.quality = 4
            self.used = 0

            self.source = "Discover"
            self.maxCharge = 1500
            self.cost = 10
            self.rate = 20
            self.upgrades = [250, 10, 5]














        else:
            self.name = "ERROR"
            print("ERROR!")
        self.charge = self.maxCharge//2
    def chooseRandomRaac(RaacPool):

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

        elif name == "RockCrest": return 12
        elif name == "SlimeFest": return 13
        elif name == "LeedQuest": return 14
        elif name == "TrackBest": return 15
        elif name == "AltarRest": return 16
        elif name == "BlackTest": return 17

        elif name == "Vampire": return 18
        elif name == "FrostAspect": return 19
        elif name == "Squire": return 20
        elif name == "Hammlet": return 21
        elif name == "Revishot": return 22
        elif name == "MagicEye": return 23
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
        if self.id == 0: # AltarBoost
            self.name = "AltarBoost"
            self.maxCharge = 3
            self.cost = 3
            self.progression = 4
            self.description = "Increase the amount of uses of a Common unused Altar by 1."
            self.quality = 4
        elif self.id == 1: # Crystalize
            self.name = "Crystalize"
            self.maxCharge = 7
            self.cost = 4
            self.progression = 5
            self.description = "Convert a Heed into a Beet."
            self.quality = 5
        elif self.id == 2: # Bomb
            self.name = "Bomb"
            self.maxCharge = 6
            self.cost = 5
            self.progression = 4
            self.description = "Deal 10X damage on the room."
            self.quality = 2

        elif self.id == 3: # TumbleBox
            self.name = "TumbleBox"
            self.maxCharge = 5
            self.cost = 3
            self.progression = 2
            self.description = "Creates 2+X random Q0 Greebles in the room."
            self.quality = 5
        elif self.id == 4: # Reinforce
            self.name = "Reinforce"
            self.maxCharge = 9
            self.cost = 5
            self.progression = 3
            self.description = "Gives 3+X temporary DF points. Loses a point everytime you discover a room."
            self.quality = 5
        elif self.id == 5: # RaacRerox
            self.name = "RaacRerox"
            self.maxCharge = 20
            self.cost = 15
            self.progression = 5
            self.description = "Rerolls all Raacs in the Room."
            self.quality = 10

        elif self.id == 6: # Crafting
            self.name = "Crafting"
            self.maxCharge = 15
            self.cost = 10
            self.progression = 7
            self.description = "Consumes 6 leeds to create a random Q2 greeble."
            self.quality = 6
        elif self.id == 7: # Ordering
            self.name = "Ordering"
            self.maxCharge = 12
            self.cost = 4
            self.progression = 4
            self.description = "Creates a random Shop."
            self.quality = 4
        elif self.id == 8: # Drafting
            self.name = "Drafting"
            self.maxCharge = 15
            self.cost = 7
            self.progression = 5
            self.description = "Rerolls Q0 Greebles in the room, reduces it by 1."
            self.quality = 6





        else:
            self.name = "ERROR"
            print("ERROR!")
    def upgrade(self):
        self.maxCharge += self.progression
        self.level += 1
    def chooseRandomTraac(TraacPool):

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

        return id
    def namesID(name):
        if name == "AltarBoost": return 0
        elif name == "Crystalize": return 1
        elif name == "Bomb": return 2

        elif name == "TumbleBox": return 3
        elif name == "Reinforce": return 4
        elif name == "RaacRerox": return 5

        elif name == "Crafting": return 6
        elif name == "Ordering": return 7
        elif name == "Drafting": return 8
class Zoodiac():
    def __init__(self, id, level = 1):
        self.id = id
        self.level = level
        self.family = "NONE"
        self.aspect = "NONE"
        self.sway   = "NONE"

        self.name = "NONE"
        self.generate()
    def generate(self):
        family = self.id[0]
        aspect = self.id[1]
        sway = self.id[2]
        if True:
            if family == 0:
                self.family = "Aries" # Enemies
            elif family == 1:
                self.family = "Taurus" # Traacs
            elif family == 2:
                self.family = "Gemini" # Greebles
            elif family == 3:
                self.family = "Cancer" # Player
            elif family == 4:
                self.family = "Leo" # Shop
            elif family == 5:
                self.family = "Virgo" # Broots
            elif family == 6:
                self.family = "Libra" # Floor
            elif family == 7:
                self.family = "Scorpio" # 
            elif family == 8:
                self.family = "Sagitarius" # Raacs
            elif family == 9:
                self.family = "Capricorn" # 
            elif family == 10:
                self.family = "Aquarius" # Altars
            elif family == 11:
                self.family = "Pisces" # Signs
        if True:
            if aspect == 0:
                self.aspect = "Light"
            elif aspect == 1:
                self.aspect = "Void"
            elif aspect == 2:
                self.aspect = "Time"
            elif aspect == 3:
                self.aspect = "Space"
            elif aspect == 4:
                self.aspect = "Heart"
            elif aspect == 5:
                self.aspect = "Mind"
            elif aspect == 6:
                self.aspect = "Hope"
            elif aspect == 7:
                self.aspect = "Rage"
            elif aspect == 8:
                self.aspect = "Breath"
            elif aspect == 9:
                self.aspect = "Blood"
            elif aspect == 10:
                self.aspect = "Life"
            elif aspect == 11:
                self.aspect = "Doom"
        if True:
            if sway == 0:
                self.sway = "Prospit"
            if sway == 1:
                self.sway = "Derse"

        self.superid = f"{family+1}-{aspect+1}-{sway+1}"
        self.name = f"Sign {self.superid}"
        self.getName(family, aspect+12*sway)
    def getName(self, f, a):
        names = [
            [
                "Aries",
                "Arsces",
                "Arrius",
                "Ariborn",
                "Arittarius",
                "Arpia",
            ],
            [
                "Taurus",
                "Taurist",
                "Taursci",
                "Taurnius",
                "Tauricorn",
                "Taurittanius",
            ],
            [
                "Gemini",
                "Germun",
                "Gemries",
                "Gemsces",
                "Gemrius",
                "Gemiborn",
            ],
            [
                "Cancer",
                "Camino",
                "Canus",
                "Canrist",
                "Cansci",
                "Cannius",
            ],
            [
                "Leo",
                "Lecen",
                "Lemini",
                "Leun",
                "Leries",
                "Lesces",
            ],
            [
                "Virgo",
                "Virlo",
                "Vircer",
                "Virmino",
                "Virus",
                "Virist",
            ],
            [
                "Libra",
                "Ligo",
                "Liblo",
                "Licer",
                "Limino",
                "Libus",
            ],
            [
                "Scorpio",
                "Scorra",
                "Scorgo",
                "Scorlo",
                "Scorcer",
                "Scormino",
            ],
            [
                "Sagitarius",
                "Sagipia",
                "Sagiza",
                "Sagiga",
                "Sagio",
                "Sagicen",
            ],
            [
                "Capricorn",
                "Caprittanius",
                "Capripio",
                "Caprira",
                "Caprigo",
                "Caprilo",
            ],
            [
                "Aquarius",
                "Aquiborn",
                "Aquittarius",
                "Aquipia",
                "Aquaza",
                "Aquaga",
            ],
            [
                "Pisces",
                "Pirius",
                "Piborn",
                "Pittarius",
                "Pipia",
                "Piza",
            ],
        ]
        description = [
            [
                "Turns current room red permanently, rerolls room.",
                "If current room is red, extract color permanently to give rewards.",
                "Rerolls enemies in the room.",
                "Sends all Enemies in the Floor to next Floor.",
                "Reduce Enemies' Defenses, Attacks, and Speeds in the room",
                "Upgrades Enemies' tiers in the room",
                "",
                "",],
            [
                "Turns current room Orange permanently, rerolls room.",
                "If current room is Orange, extract color permanently to give rewards.",
                "Rerolls Traacs in the room.",
                "Sends all Traacs in the Floor to next Floor.",
                "Recharges your Traacs",
                "Permanently increases your current Traacs max charge by +2",
                "",
                "",],
            [
                "Turns current room Yellow permanently, rerolls room.",
                "If current room is Yellow, extract color permanently to give rewards.",
                "Rerolls Greebles in the room.",
                "Sends all Greebles in the Floor to next Floor.",
                "Cleanses the Greebles you hold",
                "Raises the quality of greebles in room",
                "",
                "",],
            [
                "Turns current room White permanently, rerolls room.",
                "If current room is White, extract color permanently to give rewards.",
                "Rerolls Player Stats.",
                "Send the Player to next Floor.",
                "Temporarily buffs player",
                "Gives player a permanent small buff to stats",
                "",
                "",],
            [
                "Turns current room Green permanently, rerolls room.",
                "If current room is Green, extract color permanently to give rewards.",
                "Rerolls the Shop.",
                "Sends all Shop items in the Floor to next Floor.",
                "Discounts all items in shop by 30%",
                "Restocks all shops in the floor",
                "",
                "",],
            [
                "Turns current room Cyan permanently, rerolls room.",
                "If current room is Cyan, extract color permanently to give rewards.",
                "Rerolls Broots in the room.",
                "Sends all Broots in the Floor to next Floor.",
                "Heals Broots in the floor",
                "Upgrades all Broots in the floor and in hand",
                "",
                "",],
            [
                "Turns current room Gray permanently, rerolls room.",
                "If current room is Gray, extract color permanently to give rewards.",
                "Rerolls ??? in the room.",
                "Sends current room to next Floor.",
                "Repopulates all gray rooms in the Floor",
                "Adds 3 normal and plated gray rooms to the Floor pool",
                "",
                "",],
            [
                "Turns current room Teal permanently, rerolls room.",
                "If current room is Teal, extract color permanently to give rewards.",
                "Rerolls ??? in the room.",
                "Sends all ??? in the Floor to next Floor.",
                "All ??? is restricted inside ???",
                "Makes all ??? do double of effect",
                "",
                "",],
            [
                "Turns current room Blue permanently, rerolls room.",
                "If current room is Blue, extract color permanently to give rewards.",
                "Rerolls Raacs in the room.",
                "Sends all Raacs in the Floor to next Floor.",
                "Recharges all your Raacs",
                "Upgrades the level of all raacs in the room by 1",
                "",
                "",],
            [
                "Turns current room Purple permanently, rerolls room.",
                "If current room is Purple, extract color permanently to give rewards.",
                "Rerolls unused Altars in the room.",
                "Sends all unused Altars in the Floor to next Floor.",
                "Recharges all Altars in the room.",
                "Increases the max usage of Altars in the room depending on rarity",
                "",
                "",],
            [
                "Turns current room Black permanently, rerolls room.",
                "If current room is Black, extract color permanently to give rewards.",
                "Rerolls Boss in the room.",
                "Sends all Bosses in the Floor to next Floor.",
                "Spawns a boss in the black room along with prizes",
                "Boosts Boss stats, increase the amount of charges acquire by killing them by 5",
                "",
                "",],
            [
                "Turns current room Magenta permanently, rerolls room.",
                "If current room is Magenta, extract color permanently to give rewards.",
                "Rerolls Zoodiacs in the room.",
                "Sends all Zoodiacs in the Floor to next Floor.",
                "recreates the last Zoodiac you used",
                "Raises chance of finding Zoodiacs by 1%",
                "",
                "",],
        ]


        self.name = names[f][a]
        self.description = description[f][a]
    def chooseRandomZoodiac():
        # family = random.randrange(12)
        # aspect = random.randrange(12)
        # sway = random.randrange(2)
        family = random.randrange(12)
        aspect = random.randrange(6)
        sway = random.randrange(1)
        return (family, aspect, sway)

class Floor():
    def __init__(self, level, rooms, broots, game):
        self.level = level
        self.game = game
        self.size = rooms["normal_gray"] + rooms["plate_gray"]
        if self.level == -1:
            self.size = 1
        self.Rooms = []
        self.generate(rooms, broots, self.game.params)
    def generate(self, temp, broots, params):
        connectivity = params[0]
        shopStock = params[1]

        rooms = {}
        for key in temp:
            rooms[key] = temp[key]

        self.Rooms.append(Room(0, "white", "normal", self.level, params))
        self.size -= 1
        rooms["normal_white"] -= 1

        N = 1
        while self.size > 1:
            self.size -= 1
            newroom = Room(N, "gray", "normal", self.level, params)
            N += 1
            self.Rooms.append(newroom)

        blackRoom = None
        if self.size > 0:
            self.Rooms.append(Room(N, "black", "normal", self.level, params))
            blackRoom = self.Rooms[-1]
            self.size -= 1
            rooms["normal_black"] -= 1
            N += 1


        for key in rooms:
            if key == "normal_gray":
                continue
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
                self.Rooms[RNG].populate(params)
                if color == "yellow" or color == "orange" or color == "cyan":
                    for key2 in broots:
                        if broots[key2] > 0:
                            self.Rooms[RNG].findFreePosition(Broot(Broot.namesID(key2), 1+params[3]), "broot")
                            broots[key2] -= 1
                            break

        for room in self.game.ExtraRooms:
            room.id = N
            self.Rooms.append(room)
            N += 1
        self.game.ExtraRooms.clear()

        for room in self.Rooms:
            for i in range(connectivity):
                RNG = random.randrange(0, N)
                if RNG != room.id and self.Rooms[RNG] not in room.connections:
                    room.connections.append(self.Rooms[RNG])
                    self.Rooms[RNG].connections.append(self.Rooms[room.id])
        
        if blackRoom in self.Rooms[0].connections:
            self.Rooms[0].connections.remove(blackRoom)
            blackRoom.connections.remove(self.Rooms[0])



class Game():
    def __init__(self):
        self.wprites = []
        self.width = 1600
        self.height = 1000
        self.screen = display.set_mode((self.width, self.height))
        self.clock = time.Clock()
        display.set_caption('GreeblesMania 0.7 - Actual Playable Characters')
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

        self.rooms["normal_gray"] = 10
        self.rooms["normal_white"] = 1
        self.rooms["normal_yellow"] = 2
        self.rooms["normal_purple"] = 1
        self.rooms["normal_red"] = -1
        self.rooms["normal_green"] = 0
        self.rooms["normal_orange"] = 0
        self.rooms["normal_black"] = 1
        self.rooms["normal_blue"] = 0
        self.rooms["normal_cyan"] = 0
        self.rooms["normal_teal"] = 0
        self.rooms["normal_magenta"] = 0
        self.rooms["normal_lilas"] = 0
        self.rooms["normal_void"] = 0




        self.rooms["plate_gray"] = 0
        self.rooms["plate_white"] = 0
        self.rooms["plate_yellow"] = 0
        self.rooms["plate_purple"] = 0
        self.rooms["plate_red"] = 0
        self.rooms["plate_green"] = 0
        self.rooms["plate_gray"] = 0
        self.rooms["plate_orange"] = 0
        self.rooms["plate_black"] = 0
        self.rooms["plate_blue"] = 0
        self.rooms["plate_cyan"] = 0
        self.rooms["plate_teal"] = 0
        self.rooms["plate_magenta"] = 0
        self.rooms["plate_lilas"] = 0
        self.rooms["plate_void"] = 0

        
        self.broots = {}
        for broot in brootimg:
            self.broots[broot] = 0
        self.broots["armed"] = 2
        self.broots["defends"] = 1
        # self.broots["frosts"] = 1
        # self.broots["pierces"] = 1
        # self.broots["walks"] = 1


        self.roomsReveal = {}
        self.brootsReveal = {}
        for typee in self.rooms:
            if self.rooms[typee] > 0:
                self.roomsReveal[typee] = True
            else:
                self.roomsReveal[typee] = False
        for typee in self.broots:
            if self.broots[typee] > 0:
                self.brootsReveal[typee] = True
            else:
                self.brootsReveal[typee] = False


        self.ExtraRooms = []
        self.ExtraObjects = []
        self.oldFloors = []

        self.log = []

        self.params = [0, 0, 0, 0, 8, 0, 0, 0, 0]
        self.currentFloor = Floor(-1, self.rooms, copy.deepcopy(self.broots), self)

        self.plate_yellowCost = 5
        self.level = -1
        # self.player.acquire(["Verdans", 25])
        # self.player.acquire(["Heeds", 25])
        self.newFloor()

        self.infoObject = None
        self.infoType = ""
        self.TrackGreebles = []
        self.TrackGreebles.append("Heeds")
        self.TrackGreebles.append("Feeds")
        self.TrackGreebles.append("Beets")


        while self.player.Greebles["Heeds"] >= 0:
            value = self.update()
            if value == -1:
                return
            elif value == 1:
                self.newFloor()
    def newFloor(self):
        self.level += 1
        self.rooms["normal_gray"] += floor(3 +(self.level**1.1)/3)




        alivecount = 0
        altarcount = 0
        anvilcount = 0
        orangeScore = 0
        raacScore = 0
        exploreScore = 0
        cleanscore = True
        zoodiacScore = 0
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
            alivecount += len(rm.Enemies)
            if rm.color == "white" and rm.type == "plate":
                self.ExtraRooms.append(rm)
            if rm.color == "purple":
                for altar in rm.Altars:
                    altar = altar[0]
                    if altar.uses == altar.maxuses:
                        if altar.id == 0:
                            anvilcount += 1
                        else:
                            altarcount += 1
            if rm.color == "orange":
                if len(rm.Raacs) > 0:
                    orangeScore += 20
            if rm.color != "blue":
                raacScore += 30*(len(rm.Raacs)+len(rm.Traacs))
                zoodiacScore += 5*len(rm.Zoodiacs)
                if not rm.discovered:
                    exploreScore += 1
            if len(rm.Greebles) > 0 and rm.color != "blue":
                cleanscore = False

        orangeProb = self.rooms["normal_red"] + self.rooms["plate_red"]*2
        orangeProb -= alivecount
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
        if RNG < orangeScore:
            self.rooms["plate_orange"] += 1
            self.rooms["normal_orange"] -= 1
        if cleanscore:
            self.rooms["normal_blue"] += 1
        if RNG < raacScore:
            self.rooms["normal_magenta"] += 1
        if RNG < zoodiacScore:
            if self.rooms["normal_magenta"] > 0:
                self.rooms["normal_magenta"] -= 1
                self.rooms["plate_magenta"] += 1
        if exploreScore == 0:
            self.rooms["normal_gray"] -= 1
            self.rooms["plate_gray"] += 1

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
            if self.rooms["normal_yellow"] > self.plate_yellowCost:
                self.rooms["normal_yellow"] -= 5
                self.rooms["plate_yellow"] += 1
                self.plate_yellowCost += self.level//3


            RNG = random.randrange(100)

            if RNG <= orangeProb:
                self.rooms["normal_orange"] += 1


            for raac in self.player.Raacs:
                if raac.name == "Altar":
                    self.rooms["normal_purple"] += raac.level
            self.rooms["normal_red"] += 1

        if self.level != 0:
            typee = Broot.chooseRandomBroot(BrootPool)
            self.broots[brootNumber[typee]] += 1

        self.player.acquire(["Kollors", self.player.Greebles["Kollors_off"]])
        self.player.unacquire(["Kollors_off", self.player.Greebles["Kollors_off"]])





        floorEnergy = 100*self.level

        coloredRack = None


        connectivity = 3
        extraStock = 0
        coloredLevel = 0
        Squire = 0
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
                coloredLevel += self.player.Greebles["Lunnors"]
                coloredRack = raac
            elif raac.name == "ExtraStock" and raac.charged():
                extraStock += raac.level
            elif raac.name == "LeedQuest" and self.player.Greebles["Leeds"] >= 3*raac.level and raac.charged():
                self.rooms["normal_red"] += raac.level
                self.player.unacquire(["Leeds", 3*raac.level])
            elif raac.name == "AltarRest":
                if altarcount >= raac.level and raac.charged():
                    self.player.acquire(["Heexs", 3*raac.level])
            elif raac.name in ["SaveThrow", "MagicEye"]:
                raac.used = 0
            elif raac.name == "FencorRegen":
                amount = raac.level*3
                temp = self.player.Greebles["Fallers"]
                while temp > 0 and self.player.Greebles["Heeds"] < self.player.Greebles["Verdans"] and raac.charged():
                    temp -= 1
                    self.player.acquire(["Heeds", amount])
            elif raac.name == "SlimeFest" and raac.charged():
                for greeb in GQ0:
                    if self.player.Greebles[greeb] >= raac.level:
                        self.player.unacquire([greeb, raac.level])
                        self.player.acquire(["Slops", raac.level])
                self.rooms["normal_gray"] += raac.level
            elif raac.name == "Squire" and raac.charged():
                Squire += raac.level
            elif raac.name == "Revishot":
                temp = raac.level
                while self.player.Greebles["Shots"] >= 2 and temp > 0 and raac.charged():
                    self.player.df += 1
                    self.player.tempDf += 1
                    self.player.unacquire(["Shots", 2])
                    temp -= 1
        self.params[0] = connectivity
        self.params[1] = extraStock
        # gray rooms DEPRECATED
        self.params[3] = Squire
        # Zoodiac chance
        self.oldFloors.append(self.currentFloor)
        self.currentFloor = Floor(self.level, self.rooms, copy.deepcopy(self.broots), self)



        for rm in self.currentFloor.Rooms:
            RNG = random.randrange(100)
            if RNG < coloredLevel*10 and coloredRack.charged():
                rm.colored = True

            if len(rm.Enemies) > 0:
                for enemy in rm.Enemies:
                    enemy = enemy[0]
                    if enemy.id == 4:
                        for rm2 in rm.connections:
                            for enemy2 in rm2.Enemies:
                                enemy2 = enemy2[0]
                                enemy2.df += 1

        self.player.room = self.currentFloor.Rooms[0]
        self.currentFloor.Rooms[0].discovered = True
        self.currentFloor.Rooms[0].colored = True


        for object in self.ExtraObjects:
            self.player.room.findFreePosition(object[0], object[1])


        for typee in self.rooms:
            if self.rooms[typee] > 0:
                self.roomsReveal[typee] = True
            else:
                self.roomsReveal[typee] = False
        for typee in self.broots:
            if self.broots[typee] > 0:
                self.brootsReveal[typee] = True
            else:
                self.brootsReveal[typee] = False
    def update(self):
        display.flip()
        mouseXY = mouse.get_pos()
        mouseRect = Rect(mouseXY[0], mouseXY[1], 1, 1)
        game.screen.fill((100, 70, 40))
        options = []
        room = self.player.room
        self.player.vined = False




        draw.rect(game.screen, (0, 0, 0), (35, 175, self.size*13+10, self.size*9+10), 5)
        brickimg = bricksimg[room.type+"_"+room.color]
        for x in range(13):
            for y in range(9):
                self.screen.blit(brickimg, (40+self.size*x, 180+self.size*y))






        # Room information
        priority = 0
        for w in range(room.width):
            for h in range(room.height):
                type = room.objects[w][h][2]
                object = room.objects[w][h][3]
                x = 40+self.size*w
                y = 180+self.size*h
                if type == '':
                    continue
                object = object[0]

                rect = Rect(x, y, self.size, self.size)
                temp = 0
                if type == "enemy":
                    temp = 9
                    self.screen.blit(enemiesimg[object.id], (x, y))
                    if object.id == 50:
                        self.player.vined = True
                    if object.id == 0:
                        options.append([rect, (w, h), "clean"])
                    else:
                        options.append([rect, (w, h), "attack"])
                        draw.rect(self.screen, (0, 0, 0), [x, y+self.size, self.size, 10])
                        fact = object.hp/object.mhp
                        draw.rect(self.screen, (255, 0, 0), [x, y+self.size, fact*self.size, 10])
                elif type == "altar":
                    temp = 7
                    if object.id == 0:
                        self.screen.blit(altar2img, (x, y))
                        self.escreverCanto(f"{object.uses}/{object.maxuses}", 15, (x+5, y+self.size+5))
                    else:
                        self.screen.blit(altarimg, (x, y))
                        # self.escreverCanto(f"{object.uses}/{object.maxuses}", 15, (x+5, y+5+self.size))

                        options.append([rect, (w, h), "altar"])
                elif type == "greeble":
                    temp = 1
                    self.screen.blit(greebleimg[object[0]], (x, y))
                    options.append([rect, (w, h), "greeble"])
                    self.escreverCanto(f"x{object[1]}", 15, (x+self.size-20, y))
                elif type == "broot":
                    temp = 3
                    self.screen.blit(brootimg[object.name], (x, y))
                    options.append([rect, (w, h), "broot"])
                elif type == "deploy":
                    temp = 4
                    if object.alive:
                        self.screen.blit(bricksimg["plate_cyan"], (x, y))
                        self.screen.blit(brootimg[object.name], (x, y))
                    else:
                        self.screen.blit(brootimg["DEAD"], (x, y))
                elif type == "shop":
                    temp = 2
                    if object[0] == "Broot":
                        self.screen.blit(brootimg[object[2]], (x, y))
                    elif object[0] == "Raac":
                        self.screen.blit(raacimg[object[2]], (x, y))
                    elif object[0] == "Traac":
                        self.screen.blit(traacimg[object[2]], (x, y))
                    elif object[0] == "Greeble":
                        self.screen.blit(greebleimg[object[2]], (x, y))
                        self.escrever(f"x{object[1]}", 15, (x-15+self.size, y-5+self.size))
                    elif object[0] == "Zoodiac":
                        self.screen.blit(zoodiacimg[object[2]], (x, y))
                        self.escrever(f"x{object[1]}", 15, (x-15+self.size, y-5+self.size))

                    self.screen.blit(bricksimg["lock"], (x, y))
                    # self.screen.blit(greebleimg[object[4]], (x, y+self.size))
                    # self.escrever(f"x{object}", 15, (x-15+self.size, y+10+2*self.size))
        
                    options.append([rect, (w, h), "buy"])
                elif type == "raac":
                    temp = 5
                    self.screen.blit(raacimg[object.name], (x, y))
                    options.append([rect, (w, h), "raac"])
                elif type == "traac":
                    temp = 6
                    self.screen.blit(traacimg[object.name], (x, y))
                    options.append([rect, (w, h), "traac"])
                elif type == "zoodiac":
                    temp = 8
                    self.screen.blit(zoodiacimg[object.superid], (x, y))
                    options.append([rect, (w, h), "zoodiac"])



                if temp > priority and not self.infoObject:
                    self.infoObject = object
                    self.infoType = type
                    priority = temp

                if Colide(mouseRect, rect) and object:
                    self.infoObject = object
                    self.infoType = type
                    priority = 30

        y = 180
        x += self.size
        for efnum in self.log:
            if efnum[0] == "attack":
                self.screen.blit(swordimg, (x, y))
                y += self.size
                self.escreverCanto(f"x{efnum[1]}", 15, (x+self.size-20, y-10))
            elif efnum[0] == "SaveThrow":
                self.screen.blit(raacimg["SaveThrow"], (x, y))
                y += self.size
                self.escreverCanto(f"x{efnum[1]}", 15, (x+self.size-20, y-10))
            elif efnum[0] == "Final":
                self.screen.blit(brootimg["final"], (x, y))
                y += self.size
                self.escreverCanto(f"x{efnum[1]}", 15, (x+self.size-20, y-10))





        # HUD
        x = 0
        y = -1
        reds = 0
        for rm in room.connections:
            if rm.color == "blue" and not rm.colored:
                continue
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



                for greeble in rm.Greebles:
                    greeble = greeble[0]
                    draw.circle(self.screen, (0, 0, 0), (40+self.size*x+5, 160+self.size*y+5), 5)
                    if self.player.Highlights[greeble[0]]:
                        draw.circle(self.screen, (100, 240, 150), (40+self.size*x+5, 160+self.size*y+5), 5)
                        break

            else:
                self.escrever("?", 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
            options.append([rect, rm, "walk"])
            x += 1

            if room.color == "black" and len(room.Enemies) == 0:
                draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)
                draw.rect(game.screen, (255, 255, 255), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
                self.escrever("Gate", 25, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
                rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
                options.append([rect, 0, "gate"])
            if rm.color == "red":
                reds += 1

        x = 40
        y = 160
        for i in range(reds):
            draw.rect(game.screen, (255, 0, 0), (x, y, 10, 10))
            x+=10



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
                self.infoObject = traac
                self.infoType = "traac"
            x += 1


        x = 14
        y = 0
        id = 0
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
                self.infoObject = raac
                self.infoType = "raac"


            breakAltar = None
            for altar in room.Altars:
                altar = altar[0]
                if altar.id == 0 and altar.uses > 0:
                    breakAltar = altar
            if breakAltar:
                options.append([rect, (breakAltar, id), "break"])
                id += 1

            x += 1
            if x >= 24:
                x = 14
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
                self.infoObject = broot
                self.infoType = "broot"
        self.escrever(f"{len(self.player.Broots)}/{self.player.Greebles["Rangors"]}", 25, (40+self.size*x+self.size//2, 160+self.size*y-10))

        x = 1
        draw.rect(game.screen, (0, 0, 0), (40+self.size*x, 160+self.size*y, self.size, self.size), 1)
        draw.rect(game.screen, (0, 255, 0), (40+self.size*x+1, 160+self.size*y+1, self.size-2, self.size-2))
        if len(self.player.Zoodiacs) > 0 and self.player.selectedZoodiac < len(self.player.Zoodiacs) and self.player.selectedZoodiac >= 0:
            zoodiac = self.player.Zoodiacs[self.player.selectedZoodiac]
            self.screen.blit(zoodiacimg[zoodiac.superid], (40+self.size*x, 160+self.size*y))
            rect = Rect(40+self.size*x, 160+self.size*y, self.size, self.size)
            if Colide(mouseRect, rect):
                self.infoObject = zoodiac
                self.infoType = "zoodiac"
            options.append([rect, 0, "sign"])
        self.escrever(f"{len(self.player.Zoodiacs)}/{self.player.Greebles["Fallers"]}", 25, (40+self.size*x+self.size//2, 160+self.size*y-10))



        x = 28
        y = 6
        self.size = 32
        for rm in self.currentFloor.Rooms:
            if rm.color == "blue" and not rm.colored:
                continue
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
                options.append([rect, rm, "walk"])

                for greeble in rm.Greebles:
                    greeble = greeble[0]
                    draw.circle(self.screen, (0, 0, 0), (40+self.size*x+5, 160+self.size*y+5), 5)
                    if self.player.Highlights[greeble[0]]:
                        draw.circle(self.screen, (100, 240, 150), (40+self.size*x+5, 160+self.size*y+5), 5)

            else:
                self.escrever("?", 12, (40+self.size*x+self.size//2, 160+self.size*y+self.size//2))
            x += 1
            if x > 47:
                x = 28
                y += 1
        self.size = 64





        x = 40+14*self.size
        y = 180+0*self.size
        for name in self.TrackGreebles:
            self.screen.blit(greebleimg[name], (x, y))
            self.escreverCanto(f"x{self.player.Greebles[name]}/{self.player.MaxGreebles[name]}", 15, (x, y+self.size))
            x += self.size
            if x >= self.width-self.size:
                x = 40+14*self.size
                y += self.size+20



        draw.rect(self.screen, (0, 0, 0),  [36, 186+self.size*9, 840, 35], 2)
        draw.rect(self.screen, (150, 150, 150),  [38, 188+self.size*9, 836, 31])
        self.escreverCanto(f"Floor: {self.currentFloor.level}", 25, (40, 190+self.size*9))
        self.escreverCanto(f"Room: {room.id}", 25, (40+self.size*3, 190+self.size*9))

        broot_defense = 0
        for rm in room.connections:
            for deploy in rm.Deploys:
                deploy = deploy[0]
                if deploy.name == "defends":
                    broot_defense += 3*deploy.level
        defText = ""
        if broot_defense > 0:
            defText = "+"+str(broot_defense)
        self.escreverCanto(f"Dmg: {self.player.dmg}", 25, (40+self.size*6, 190+self.size*9))
        self.escreverCanto(f"Df: {self.player.df}{defText}", 25, (40+self.size*8, 190+self.size*9))
        self.escreverCanto(f"Speed: {self.player.speed}", 25, (40+self.size*10, 190+self.size*9))



        x = 14
        y = 5
        draw.rect(self.screen, (0, 0, 0), [40+self.size*x, 180+self.size*y, self.size*10, self.size*4])
        draw.rect(self.screen, (200, 200, 200), [40+self.size*x+2, 180+self.size*y+2, self.size*10-4, self.size*4-4])

        if self.infoObject:
            x = 40+self.size*x + 5
            y = 180+self.size*y + 5
            if self.infoType == "traac":

                self.escreverCanto(f"{self.infoObject.name} Lvl. {self.infoObject.level}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Charge: {self.infoObject.charge}/{self.infoObject.maxCharge}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Cost: {self.infoObject.cost}", 20, (x, y))
                y += 20

                self.escreverCanto(f"{self.infoObject.description}", 20, (x, y))
                y += 20
            elif self.infoType == "raac":
                self.escreverCanto(f"{self.infoObject.name} Lvl. {self.infoObject.level}", 20, (x, y))
                y += 20

                self.escreverCanto(f"{self.infoObject.description}", 20, (x, y))
                y += 20

                if self.infoObject.name in ["SaveThrow", "MagicEye"]:
                    self.escreverCanto(f"[{self.infoObject.level - self.infoObject.used}] Use(s) left", 20, (x, y))
                    y += 20
            elif self.infoType == "greeble":
                self.escreverCanto(f"{self.infoObject[0]} x {self.infoObject[1]}", 20, (x, y))
                y += 20
            elif self.infoType == "enemy":
                self.escreverCanto(f"{self.infoObject.name}", 20, (x, y))
                y += 20

                self.escreverCanto(f"HP: {ceil(self.infoObject.hp)}/{self.infoObject.mhp}", 20, (x, y))
                y += 20


                self.escreverCanto(f"Dmg: {max(self.infoObject.dmg-self.player.Greebles["Daffans"]//3, 0)}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Df: {self.infoObject.df:.1f}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Speed: {self.infoObject.speed} [{self.infoObject.turn}/{self.infoObject.playerTurn}]", 20, (x, y))
                y += 20
            elif self.infoType == "altar":
                # self.escreverCanto(f"{self.infoObject.name}", 20, (x, y))
                # y += 20

                self.escreverCanto(f"Uses: {self.infoObject.uses}/{self.infoObject.maxuses}", 20, (x, y))
                y += 20
                self.escreverCanto(f"Rarity: {self.infoObject.rarity}", 20, (x, y))
                y += 20

                # self.escreverCanto(f"Rarity: {self.infoObject.rarity}", 20, (x, y))
                # y += 20

                self.escreverCanto(f"Requires: ", 20, (x, y))
                x += self.size*1.5
                for greeb in self.infoObject.recipe:
                    draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 1)
                    self.screen.blit(greebleimg[greeb[0]], (x, y))
                    self.escrever(f"x{greeb[1]}", 20, (x+self.size//2, y+self.size+10))
                    x += self.size
                y += self.size+25
                x -= self.size*(len(self.infoObject.recipe)+1.5)

                
                self.escreverCanto(f"Produces: ", 20, (x, y))
                x += self.size*1.5
                for greeb in self.infoObject.products:
                    draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 1)
                    self.screen.blit(greebleimg[greeb[0]], (x, y))
                    self.escrever(f"x{greeb[1]}", 20, (x+self.size//2, y+self.size+10))
                    x += self.size
            elif self.infoType == "shop":
                self.escreverCanto(f"{self.infoObject[0]} - {self.infoObject[2]} x{self.infoObject[1]}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Costs: ", 20, (x, y))
                x += self.size
                draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 1)
                self.screen.blit(greebleimg[self.infoObject[4]], (x, y))
                x += self.size//2
                y += self.size+10
                self.escrever(f"x{self.infoObject[3]}", 20, (x, y))
                y += 20
            elif self.infoType == "broot":
                self.escreverCanto(f"{self.infoObject.trueName}", 20, (x, y))
                y += 20

                self.escreverCanto(f"HP: {self.infoObject.hp}/{self.infoObject.mhp}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Power: {self.infoObject.dmg}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Speed: {self.infoObject.speed}", 20, (x, y))
                y += 20
            elif self.infoType == "deploy":
                self.escreverCanto(f"{self.infoObject.trueName}", 20, (x, y))
                y += 20

                self.escreverCanto(f"HP: {self.infoObject.hp}/{self.infoObject.mhp}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Power: {self.infoObject.dmg}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Speed: {self.infoObject.speed}", 20, (x, y))
                y += 20
            elif self.infoType == "zoodiac":
                self.escreverCanto(f"{self.infoObject.name}", 20, (x, y))
                y += 20

                self.escreverCanto(f"description: {self.infoObject.description}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Family: {self.infoObject.family}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Aspect: {self.infoObject.aspect}", 20, (x, y))
                y += 20

                self.escreverCanto(f"Sway: {self.infoObject.sway}", 20, (x, y))
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
                    self.player.selectedZoodiac -= 1
                if ev.key == K_2:
                    self.player.selectedBroot += 1
                    self.player.selectedZoodiac += 1
                if ev.key == K_SPACE:
                    if len(room.Enemies) == 0:
                        i = 0
                        while i < len(room.Greebles):
                            greeb = room.Greebles[i]
                            qtd = self.player.acquire(greeb[0])
                            greeb[0][1] = qtd
                            i += 1
                            if greeb[0][1] == 0:
                                i -= 1
                                room.freeePosition(greeb[1], greeb[2])
                if self.player.selectedBroot >= len(self.player.Broots):
                    self.player.selectedBroot = 0
                elif self.player.selectedBroot < 0:
                    self.player.selectedBroot = len(self.player.Broots)-1
                if self.player.selectedZoodiac >= len(self.player.Zoodiacs):
                    self.player.selectedZoodiac = 0
                elif self.player.selectedZoodiac < 0:
                    self.player.selectedZoodiac = len(self.player.Zoodiacs)-1
                if ev.key == K_TAB:
                    self.showGreebles()
                if ev.key == K_z:
                    w = mouseRect.x
                    h = mouseRect.y
                    w -= 40
                    h -= 160
                    w = w//self.size
                    h = h//self.size
                    if w >= 0 and w <= 13 and h >= 0 and h <= 9:
                        action = "sign"
                        parameter = (w, h)

        if action == "walk" and not self.player.vined:
            self.infoObject = None
            self.infoType = ""
            self.walkRoom(parameter)
            self.player.walk()
        elif action == "attack":
            self.activate(room)
        elif action == "altar":
            altar = room.objects[parameter[0]][parameter[1]][3][0]
            if altar.uses > 0:
                for rec in altar.recipe:
                    if self.player.Greebles[rec[0]] < rec[1]:
                        break
                else:
                    altar.uses -= 1
                    for rec in altar.recipe:
                        self.player.unacquire([rec[0], rec[1]])
                    for prod in altar.products:
                        qtd = self.player.acquire(prod)
                        if qtd > 0:
                            room.acquire([prod[0], qtd])
        elif action == "break":
            altar = parameter[0]
            if altar.uses > 0:
                altar.uses -= 1

                raac = self.player.Raacs.pop(parameter[1])
                room.randomGreeble(2, raac.level*3)
        elif action == "clean":
            room.freeePosition(parameter[0], parameter[1])
        elif action == "gate":
            return 1
        elif action == "active":
            if self.player.Traacs[parameter].charge >= self.player.Traacs[parameter].cost:
                sucess = False
                name = self.player.Traacs[parameter].name
                lvl = self.player.Traacs[parameter].level
                if name == "AltarBoost":
                    for altar in room.Altars:
                        altar = altar[0]
                        if altar and altar.uses == altar.maxuses and altar.rarity == "Common":
                            altar.uses += 1
                            altar.maxuses += 1
                            sucess = True
                elif name == "Crystalize" and self.player.Greebles["Heeds"] > 0 and self.player.Greebles["Beets"] < self.player.Greebles["Radeans"]:
                    self.player.unacquire(["Heeds", 1])
                    self.player.acquire(["Beets", 1])
                    sucess = True
                elif name == "Bomb":
                    for w in range(room.width):
                        for h in range(room.height):
                            if room.objects[w][h][2] == "enemy":
                                enemy = room.objects[w][h][3]
                                enemy.hp -= 10*lvl
                                sucess = True
                            room.checkEnemyLife(self.player, self)
                elif name == "TumbleBox":
                    room.randomGreeble(0, 2+traac.level)
                    sucess = True
                elif name == "Reinforce":
                    self.player.df += 3+lvl
                    self.player.tempDf += 3+lvl
                    sucess = True
                elif name == "RaacRerox":
                    for raac in room.Raacs:
                        room.freeePosition(raac[1], raac[2])
                        level = raac[0].level-1
                        RNG = random.randrange(100)
                        if RNG <= 5:
                            traac = Traac(Traac.chooseRandomTraac(TraacPool))
                            room.findFreePosition(traac, "traac", raac[1], raac[2])
                            if level > 0:
                                for i in range(level-1):
                                    traac.upgrade()
                        else:
                            newRaac = Raac(Raac.chooseRandomRaac(RaacPool))
                            room.findFreePosition(newRaac, "raac", raac[1], raac[2])
                            if level > 0:
                                for i in range(level-1):
                                    newRaac.upgrade()
                        sucess = True
                elif name == "Crafting":
                    if self.player.Greebles["Leeds"] >= 6:
                        self.player.unacquire(["Leeds", 6])
                        room.randomGreeble(2, 1)
                        sucess = True
                elif name == "Ordering":
                    room.randomShop(5*lvl, True)
                    sucess = True
                elif name == "Drafting":
                    for greeble in room.Greebles:
                        greeb = greeble[0]
                        if greeb[0] in GQ0+GQ0b:
                            room.freeePosition(greeble[1], greeble[2])
                            greeb[1] -= 1
                            if greeb[1] > 0:
                                room.findFreePosition([random.choice(GQ0), greeb[1]], "greeble", greeble[1], greeble[2])
                                sucess = True
                if sucess:
                    self.player.Traacs[parameter].charge -= self.player.Traacs[parameter].cost
        elif action == "deploy" and len(self.player.Broots) > 0:
            broot = self.player.Broots.pop(self.player.selectedBroot)
            broot.deploy(parameter[0], parameter[1], room)
            room.findFreePosition(broot, "deploy", parameter[0], parameter[1])
            self.player.selectedBroot -= 1
            if self.player.selectedBroot < 0:
                self.player.selectedBroot = 0


            if broot.name == "detector":
                for rm2 in room.connections:
                    if rm2.color == "blue":
                        rm2.colored = True
        elif action == "buy":
            item = room.objects[parameter[0]][parameter[1]][3][0]
            if self.player.Greebles[item[4]] >= item[3]:
                room.freeePosition(parameter[0], parameter[1])
                if item[0] == "Greeble":
                    qtd = self.player.acquire([item[2], item[1]])
                    room.acquire([item[2], qtd])
                elif item[0] == "Broot":
                    newBroot = Broot(item[2], 1)
                    if len(self.player.Broots) < self.player.Greebles["Rangors"]:
                        self.player.Broots.append(newBroot)
                    else:
                        room.findFreePosition(newBroot, "broot", parameter[0], parameter[1])
                    self.broots[newBroot.name] += 1
                elif item[0] == "Raac":
                    room.findFreePosition(Raac(Raac.namesID(item[2])), "raac", parameter[0], parameter[1])
                elif item[0] == "Traac":
                    room.findFreePosition(Traac(Traac.namesID(item[2])), "traac", parameter[0], parameter[1])
                elif item[0] == "Zoodiac":
                    idd = item[2].split('-')
                    idd = [int(x)-1 for x in idd]
                    newZoodiac = Zoodiac(idd)
                    if len(self.player.Zoodiacs) < self.player.Greebles["Fallers"]:
                        self.player.Zoodiacs.append(newZoodiac)
                    else:
                        room.findFreePosition(newZoodiac, "zoodiac", parameter[0], parameter[1])


                self.player.unacquire([item[4], item[3]])
        elif action == "sign" and len(self.player.Zoodiacs) > 0:
            self.zoodiacActivate()
        enemyAlive = False
        for enemy in room.Enemies:
            if enemy[0].hp > 0:
                enemyAlive = True
                break
        if not enemyAlive:
            if action == "traac":
                traac = room.objects[parameter[0]][parameter[1]][3][0]
                TraacPool[traac.id][0] += round(len(TraacPool)*0.5)
                traac = self.player.acquireTraac(traac)
                room.freeePosition(parameter[0], parameter[1])
                if traac:
                    TraacPool[traac.id][0] -= round(len(TraacPool)*0.5)
                    room.findFreePosition(traac, "traac", parameter[0], parameter[1])
            elif action == "greeble":
                greeb = room.objects[parameter[0]][parameter[1]][3][0]
                qtd = self.player.acquire(greeb)
                if qtd == 0:
                    room.freeePosition(parameter[0], parameter[1])
                else:
                    room.objects[parameter[0]][parameter[1]][3][0][1] = qtd
            elif action == "raac":
                raac = room.objects[parameter[0]][parameter[1]][3][0]
                RaacPool[raac.id][0] += round(len(RaacPool)*0.5)
                got = self.player.acquireRaac(raac)
                if got:
                    room.freeePosition(parameter[0], parameter[1])
            elif action == "broot":
                if len(self.player.Broots) < self.player.Greebles["Rangors"]:
                    self.player.Broots.append(room.objects[parameter[0]][parameter[1]][3][0])
                    room.freeePosition(parameter[0], parameter[1])
            elif action == "zoodiac":
                if len(self.player.Zoodiacs) < self.player.Greebles["Fallers"]:
                    self.player.Zoodiacs.append(room.objects[parameter[0]][parameter[1]][3][0])
                    room.freeePosition(parameter[0], parameter[1])
   

        self.clock.tick(30)
    def walkRoom(self, room):
        if not room.discovered:
            if self.player.Greebles["Feeds"] > 0:
                self.player.unacquire(["Feeds", 1])
            else:
                self.player.unacquire(["Heeds", 1])

            if self.player.tempDf > 0:
                self.player.tempDf -= 1
                self.player.df -= 1
            if self.player.tempDmg > 0:
                self.player.tempDmg -= 1
                self.player.dmg -= 1
            if self.player.tempSpeed > 0:
                self.player.tempSpeed -= 1
                self.player.speed -= 1
            roomEnergy = 15*self.level
            lucklevel = 0
            luckCharmRaac = None
            RNG = random.randrange(100)
            for raac in self.player.Raacs:
                if raac.source == "Discover" and roomEnergy > 0:
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
                    lucklevel += self.player.Greebles["Lunnors"]
                elif raac.name == "Pottery":
                    levelPot = raac.level
                    while RNG < levelPot*4:
                        if self.player.Greebles["Shots"] > 0 and raac.charged():
                            self.player.unacquire(["Shots", 1])
                            self.player.acquire(["Pots", 1])
                        levelPot -= 25
                        RNG = random.randrange(100)
                elif raac.name == "BeetHeal":
                    if RNG <= 20*raac.level and self.player.Greebles["Heeds"] < self.player.Greebles["Verdans"] and self.player.Greebles["Beets"] > 0 and raac.charged():
                        self.player.unacquire(["Beets", 1])
                        self.player.acquire(["Heeds", 1])
                        self.player.acquire(["Pots", 1])
                elif raac.name == "MagicEye":
                    if room.color == "purple":
                        for rm in room.connections:
                            if rm.color == "blue" and raac.used < raac.level and raac.charged():
                                rm.colored = True
                                raac.used += 1

            for greeb in room.Greebles:
                greeb = greeb[0]
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
                        room.acquire([name, 1])

                        if greeb[1] == 0:
                            room.freeePosition(greeb[2][0], greeb[2][1])


            for rm in self.currentFloor.Rooms:
                for deploy in rm.Deploys:
                    deploy = deploy[0]
                    if deploy.name == "digests":
                        for greeb in rm.Greebles:
                            greeb = greeb[0]
                            if greeb[0] != "Slops":
                                greeb[1] -= 1
                                qtd = 0
                                if greeb[0] in GQ0+GQ0b:
                                    qtd = 1
                                elif greeb[0] in GQ1+GQ1b:
                                    qtd = 2
                                elif greeb[0] in GQ2+GQ2b:
                                    qtd = 5
                                elif greeb[0] in GQ4+GQ4b:
                                    qtd = 10
                                rm.acquire(["Slops", qtd])
                                if greeb[1] == 0:
                                    rm.freeePosition(greeb[2][0], greeb[2][1])
                    elif deploy.name == "digs":
                        deploy.action += deploy.level
                        while deploy.action >= deploy.cost:
                            deploy.action -= deploy.cost
                            RNG = random.randrange(100)
                            if RNG <= 20:
                                rm.acquire([random.choice(GQ1), 1])
                            else:
                                rm.acquire([random.choice(GQ0), 1])
                    elif deploy.name == "deconstructs":
                        for altar in rm.Altars:
                            altar = altar[0]
                            if altar.uses > 0:
                                altar.uses -= 1
                                RNG = random.randrange(100)
                                if altar.rarity == "Uncommon":
                                    RNG = RNG/2
                                elif altar.rarity == "Rare":
                                    RNG = RNG/4
                                elif altar.rarity == "Mythical":
                                    RNG = RNG/8
                                if RNG <= 10:
                                    rm.acquire([random.choice(GQ2), 1])
                                elif RNG <= 35:
                                    rm.acquire([random.choice(GQ1), 1])
                                else:
                                    rm.acquire([random.choice(GQ0), 1])
                                break
                for enemyObj in rm.Enemies:
                    enemy = enemyObj[0]
                    if enemy.id == 7 and enemy.genNum > 0:
                        RNG = random.randrange(100)
                        if RNG <= 35:
                            enemy.genNum -= 1
                            newWasp = Enemy(6, "Normal", self.level)
                            for rm2 in rm.connections:
                                if rm2.color == "gray":
                                    rm2.findFreePosition(newWasp, "enemy")
                                    rm2.color = "red"
                    elif enemy.id == 99 and enemy.genNum > 0:
                        RNG = random.randrange(100)
                        if RNG <= 50:
                            enemy.genNum -= 1
                            newWasp = Enemy(50, "Normal", self.level)
                            for rm2 in rm.connections:
                                if rm2.color == "gray" or rm2.color == "red":
                                    rm2.findFreePosition(newWasp, "enemy")
                                    rm2.color = "red"

                    elif enemy.id == 8 and rm.color == "red":
                        RNG = random.randrange(100)
                        if RNG <= 50:
                            for rm2 in rm.connections:
                                if rm2.color == "gray":
                                    rm.freeePosition(enemyObj[1], enemyObj[2])
                                    rm2.findFreePosition(enemy, "enemy")
                                    rm2.color = "red"
                                    if len(rm.Enemies) == 0:
                                        rm.color = "gray"
                                    break


        stealer = -1
        blackroom = self.currentFloor.Rooms[-1]
        for enemy in blackroom.Enemies:
            enemy = enemy[0]
            if enemy.id == 98:
                stealer = random.randrange(len(self.currentFloor.Rooms))
        for rm in self.currentFloor.Rooms:
            for deploy in rm.Deploys:
                deploy = deploy[0]
                if deploy.name == "fights" and deploy.alive:
                    for enemy in rm.Enemies:
                        enemy = enemy[0]
                        if enemy.id != 0:
                            enemy.hp -= deploy.dmg
                            deploy.damage(enemy.dmg)
                            rm.checkEnemyLife(self.player, self)
                elif deploy.name == "walks" and deploy.alive:
                    for enemy in rm.Enemies:
                        enemy = enemy[0]
                        if enemy.id != 0:
                            enemy.hp -= deploy.dmg
                            deploy.damage(enemy.dmg)
                            rm.checkEnemyLife(self.player, self)
                            break

                    rm2 = random.choice(rm.connections)
                    for deploy2 in rm.Deploys:
                        if deploy2[0] == deploy:
                            break
                    rm.freeePosition(deploy2[1], deploy2[2])
                    rm2.findFreePosition(deploy, "deploy")
                    deploy.room = room


            if stealer == 0 and len(rm.Greebles) > 0:
                greeb = rm.Greebles[0][0]
                rm.freeePosition(greeb[2][0], greeb[2][1])
                blackroom.acquire([greeb[0], greeb[1]])
            stealer -= 1

        self.log.clear()

        for deploy in self.player.room.Deploys:
            deploy = deploy[0]
            if deploy.name == "final" and deploy.alive:
                for deploy2 in self.player.room.Deploys:
                    if deploy2[0] == deploy:
                        break
                self.player.room.freeePosition(deploy2[1], deploy2[2])
                room.findFreePosition(deploy, "deploy")
                deploy.room = room


        self.player.room = room
        self.activate(room)
    def activate(self, room):
        room.discovered = True
        room.colored = True



        # Broots and Raacs
        SplashDamage = 0
        FrostAspect = 0
        Hammlet = 0
        for raac in self.player.Raacs:
            if raac.name == "SplashDamage" and raac.charged(raac.level):
                SplashDamage += raac.level
            if raac.name == "FrostAspect" and raac.charged():
                FrostAspect += (2+self.player.Greebles["Tannors"])*raac.level
            if raac.name == "Hammlet" and raac.charged():
                Hammlet += raac.level/2
        broot_attack = 0
        broot_defense = 0
        effects = {
            "frost": 0,
            "pierce": 0,
        }

        enemyDMG = 0
        for enemy in room.Enemies:
            enemy = enemy[0]
            if enemy.id != 0:
                enemyDMG += enemy.dmg

        for rm in room.connections:
            for enemy in rm.Enemies:
                enemy = enemy[0]
                if enemy.id == 97 and enemy.id != 0:
                    self.player.damage(max(enemy.dmg//2, 1), self)
                if enemy.hp > 0 and SplashDamage > 0:
                    enemy.hp -= floor((0.30+SplashDamage*0.05)*self.player.dmg)
                    SplashDamage -= 1
            rm.checkEnemyLife(self.player, self)
            for deploy in rm.Deploys:
                deploy = deploy[0]
                if deploy.name == "armed":
                    broot_attack += deploy.dmg
                    deploy.damage(enemyDMG)
                elif deploy.name == "defends":
                    broot_defense += deploy.dmg
                    deploy.damage(enemyDMG)
                elif deploy.name == "frosts":
                    broot_attack += deploy.dmg
                    effects["frost"] += deploy.dmg/3
                    deploy.damage(enemyDMG)
                elif deploy.name == "pierces":
                    broot_attack += deploy.dmg
                    effects["pierce"] += deploy.dmg/10
                    deploy.damage(enemyDMG)



        attack = True
        brootAttack = True
        playerSpeed = self.player.speed
        enemyAlive = True
        while attack and enemyAlive:
            enemyAlive = False
            for enemy in room.Enemies:
                enemy = enemy[0]
                if enemy.id == 0:
                    continue
                enemyAlive = True


                if brootAttack:
                    enemy.hp -= broot_attack
                    for effect in effects:
                        if effects[effect] > 0:
                            if effect == "frost":
                                enemy.speed -= round(effects[effect])
                            elif effect == "pierce":
                                enemy.df -= effects[effect]
                    brootAttack = False


                for deploy in room.Deploys:
                    deploy = deploy[0]
                    if deploy.name == "fights" and deploy.alive:
                        enemy.hp -= deploy.dmg
                        deploy.damage(enemy.dmg)

                limit = max(enemy.speed, playerSpeed)
                enemy.turn += enemy.speed
                if attack:
                    enemy.playerTurn += playerSpeed

                if enemy.playerTurn >= limit and attack:
                    enemy.playerTurn -= limit
                    dmgcause = enemy.hp
                    enemy.damage(self.player.dmg)
                    dmgcause = dmgcause - enemy.hp
                    enemy.speed -= FrostAspect
                    enemy.df -= Hammlet
                    if enemy.df < 0:
                        enemy.df = 0

                    if dmgcause > 0:
                        room.acquire(["Bloods", 1])
                    attack = False

                if enemy.turn >= limit:
                    enemy.turn -= limit
                    if enemy.hp > 0 or enemy.turn > enemy.playerTurn:
                        qtd = max(0, enemy.dmg - broot_defense)
                        qtd = self.player.damage(qtd, self)
                        self.log.append(["attack", qtd])

        room.checkEnemyLife(self.player, self)
    def showGreebles(self):
        tabPressed = True
        while tabPressed:
            display.flip()
            mouseXY = mouse.get_pos()
            mouseRect = Rect(mouseXY[0], mouseXY[1], 1, 1)
            game.screen.fill((80, 140, 60))
            options = []






            # All The Greebles MAX and MIN

            x = 40
            y = 50
            color = (255, 255, 255)
            for greeb in GQ0 + GQ0b:
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
                maxx = self.player.MaxGreebles[greeb]
                if maxx >= 1000:
                    maxx = ""
                else:
                    maxx = "/" + str(maxx)
                self.escrever(f"x{self.player.Greebles[greeb]}{maxx}", 15, (x+self.size//2, y+self.size+14))

                if greeb in self.TrackGreebles:
                    draw.circle(self.screen, (0, 0, 255), (x+8, y+8), 10)

                x += self.size+6

            y += self.size
            x -= round((self.size+6)*3.5)
            # draw.rect(self.screen, (170, 170, 170), [40-3, y+23, (self.size+6)*5, 20])
            # draw.rect(self.screen, (0, 0, 0), [40-3, y+23, (self.size+6)*5, 20], 2)
            # self.escrever(f"x{total}/{self.player.MaxGreebles[GQ0[0]]}", 15, (x, y+33))

            x = 40
            y += self.size
            for greeb in GQ1 + GQ1b:
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
                self.escrever(f"x{self.player.Greebles[greeb]}/{self.player.MaxGreebles[greeb]}", 15, (x+self.size//2, y+self.size+14))


                if greeb in self.TrackGreebles:
                    draw.circle(self.screen, (0, 0, 255), (x+8, y+8), 10)

                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ2 + GQ2b:
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

                maxx = self.player.MaxGreebles[greeb]
                if maxx >= 1000:
                    maxx = ""
                else:
                    maxx = "/" + str(maxx)
                self.escrever(f"x{self.player.Greebles[greeb]}{maxx}", 15, (x+self.size//2, y+self.size+14))


                if greeb in self.TrackGreebles:
                    draw.circle(self.screen, (0, 0, 255), (x+8, y+8), 10)
                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ3 + GQ3b:
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

                maxx = self.player.MaxGreebles[greeb]
                if maxx >= 1000:
                    maxx = ""
                else:
                    maxx = "/" + str(maxx)
                self.escrever(f"x{self.player.Greebles[greeb]}{maxx}", 15, (x+self.size//2, y+self.size+14))


                if greeb in self.TrackGreebles:
                    draw.circle(self.screen, (0, 0, 255), (x+8, y+8), 10)
                x += self.size

            x = 40
            y += self.size*2
            for greeb in GQ4 + GQ4b:
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
                maxx = self.player.MaxGreebles[greeb]
                if maxx >= 1000:
                    maxx = ""
                else:
                    maxx = "/" + str(maxx)
                self.escrever(f"x{self.player.Greebles[greeb]}{maxx}", 15, (x+self.size//2, y+self.size+14))



                if greeb in self.TrackGreebles:
                    draw.circle(self.screen, (0, 0, 255), (x+8, y+8), 10)
                x += self.size









            # All the Rooms And Broots Blunt Rotation information


            gray = self.rooms["normal_gray"]
            for roomType in self.rooms:
                if roomType != "normal_gray":
                    gray -= self.rooms[roomType]
            gray = max(gray, 0)
            x = 800
            y = 50
            i = 0
            for roomType in self.rooms:
                if not self.roomsReveal[roomType]:
                    continue
                self.screen.blit(bricksimg[roomType], (x, y))
                if roomType == "normal_gray":
                    self.escreverCanto(f"x{gray}", 25, (x+self.size, y-12+self.size//2))
                else:
                    self.escreverCanto(f"x{self.rooms[roomType]}", 25, (x+self.size, y-12+self.size//2))
                y += self.size+2
                i += 1
                if i >= 14:
                    y = 50
                    i = 0
                    x += self.size*2




            x = 1100
            y = 50
            i = 0
            for brootType in self.broots:
                if not self.brootsReveal[brootType]:
                    continue
                draw.rect(self.screen, (0, 0, 0), [x, y, self.size, self.size], 2)
                draw.rect(self.screen, (155, 155, 155), [x+2, y+2, self.size-4, self.size-4])
                self.screen.blit(brootimg[brootType], (x, y))
                self.escreverCanto(f"x{self.broots[brootType]}", 25, (x+self.size, y-12+self.size//2))
                y += self.size+2
                i += 1
                if i >= 14:
                    y = 50
                    i = 0
                    x += self.size*2





            for ev in event.get():
                if (ev.type == QUIT):
                    return -1
                if ev.type == MOUSEBUTTONDOWN:
                    if ev.button == BUTTON_LEFT:
                        for opt in options:
                            if Colide(opt[0], mouseRect):
                                self.player.Highlights[opt[1]] = not self.player.Highlights[opt[1]]
                    if ev.button == BUTTON_RIGHT:
                        for opt in options:
                            if Colide(opt[0], mouseRect):
                                if opt[1] in self.TrackGreebles:
                                    self.TrackGreebles.remove(opt[1])
                                else:
                                    self.TrackGreebles.append(opt[1])
                elif ev.type == KEYDOWN:
                    if ev.key == K_TAB:
                        tabPressed = not tabPressed
    def zoodiacActivate(self):
            room = self.player.room
            zoodiac = self.player.Zoodiacs.pop(self.player.selectedZoodiac)
            sucess = False
            self.player.selectedZoodiac -= 1
            if self.player.selectedZoodiac < 0:
                self.player.selectedZoodiac = 0


            if zoodiac.sway == "Prospit":
                if zoodiac.aspect == "Light": # [1-1 | 12-1]
                    newColor = zoodiacColor[zoodiac.family]

                    color = room.color
                    typee = room.type
                    self.rooms[typee + "_" + color] -= 1
                    self.rooms[typee + "_" + newColor] += 1
                    room.color = newColor
                    # room.depopulate()
                    room.populate(self.params)
                    sucess = True
                elif zoodiac.aspect == "Void" and zoodiacColor[zoodiac.family] == room.color: # [1-2 | 12-2]
                    color = room.color
                    typee = room.type
                    self.rooms[typee + "_" + color] -= 1
                    self.rooms[typee+"_void"] += 1
                    room.depopulate()
                    room.prize()
                    room.color = "void"
                    sucess = True
                elif zoodiac.aspect == "Time":
                    color = zoodiacColor[zoodiac.family]
                    sucess = True

                    if color in ["white", "gray", "green"]:
                        if color == "white":
                            self.player.dmg += random.randrange(-2, 5)
                            self.player.df += random.randrange(-2, 5)
                            self.player.speed += random.randrange(-4, 7)
                        elif color == "gray":
                            room.depopulate()
                            room.color = random.choice(list(colorkey))
                            room.populate(self.params)
                        elif color == "green":
                            shopScore = 0
                            sellScore = 0
                            shopRemove = []
                            for shop in room.Shops:
                                shopRemove.append(shop)
                            for shop in shopRemove:
                                if shop[0][4] == "pots":
                                    sellScore += 3
                                else:
                                    if shop[0][0] == "traac":
                                        shopScore += 6
                                    elif shop[0][0] == "raac":
                                        shopScore += 5
                                    elif shop[0][0] == "zoodiac":
                                        shopScore += 8
                                    elif shop[0][0] == "raac":
                                        shopScore += 3
                                    else:
                                        shopScore += 1
                                room.freeePosition(shop[1], shop[2])
                            room.randomShop(sellScore, False)
                            room.randomShop(shopScore, True)
                    else:
                        for w in range(room.width):
                            for h in range(room.height):
                                type = room.objects[w][h][2]
                                object = room.objects[w][h][3]
                                take = False
                                room.freeePosition(w, h)
                                if (type == "enemy" and color == "red"):
                                    room.findFreePosition(Enemy(Enemy.chooseRandomEnemy()), "enemy", w, h)
                                elif (type == "raac" and color == "blue"):
                                    room.findFreePosition(Raac(Raac.chooseRandomRaac(RaacPool)), "raac", w, h)
                                elif (type == "greeble" and color == "yellow"):
                                    greeble = object[0]
                                    if greeble[0] in GQ0+GQ0b:
                                        Q = 0
                                    elif greeble[0] in GQ1+GQ1b:
                                        Q = 1
                                    elif greeble[0] in GQ2+GQ2b:
                                        Q = 2
                                    elif greeble[0] in GQ3+GQ3b:
                                        Q = 3
                                    elif greeble[0] in GQ4+GQ4b:
                                        Q = 4

                                    RNG = random.randrange(100)
                                    if RNG < 5:
                                        Q -= 1
                                        if Q < 0:
                                            Q = 0

                                    room.randomGreeble(Q, greeble[1])
                                    # room.findFreePosition(greeble, "greeble", w, h)
                                elif (type == "broot" and color == "cyan"):
                                    room.findFreePosition(Broot(Broot.chooseRandomBroot(BrootPool, False)), "broot", w, h)
                                elif (type == "traac" and color == "orange"):
                                    room.findFreePosition(Traac(Traac.chooseRandomTraac(TraacPool)), "traac", w, h)
                                elif (type == "altar" and color == "purple"):
                                    room.findFreePosition(Altar(Altar.chooseRandomAltar()), "altar", w, h)
                                elif (type == "zoodiac" and color == "magenta"):
                                    room.findFreePosition(Zoodiac(Zoodiac.chooseRandomZoodiac()), "zoodiac", w, h)
                                if (type == "enemy" and color == "black"):
                                    room.findFreePosition(Enemy(Enemy.chooseRandomEnemy(), "Boss", self.level), "enemy", w, h)
                elif zoodiac.aspect == "Space":
                    color = zoodiacColor[zoodiac.family]
                    sucess = True
                    if color in ["white", "gray"]:
                        if color == "white":
                            return 1
                        elif color == "gray":
                            copyroom = copy.deepcopy(room)
                            copyroom.connections.clear()
                            self.ExtraRooms.append(copyroom)
                            room.depopulate()
                            room.color = "void"
                    else:
                        for rm in self.currentFloor.Rooms:
                            tempObjects = []
                            for w in range(rm.width):
                                for h in range(rm.height):
                                    type = rm.objects[w][h][2]
                                    object = rm.objects[w][h][3]
                                    take = False
                                    if (type == "enemy" and color == "red" and rm.color != "black") or \
                                        (type == "raac" and color == "blue") or \
                                        (type == "greeble" and color == "yellow") or \
                                        (type == "broot" and color == "cyan") or \
                                        (type == "traac" and color == "orange") or \
                                        (type == "altar" and color == "purple") or \
                                        (type == "shop" and color == "green") or \
                                        (type == "zoodiac" and color == "magenta") or \
                                        (type == "enemy" and color == "black" and rm.color == "black"):
                                        take = True
                                    if take:
                                        self.ExtraObjects.append([object[0], type])
                                        tempObjects.append([w, h])
                            for place in tempObjects:
                                rm.freeePosition(place[0], place[1])
                elif zoodiac.aspect == "Heart":
                    color = zoodiacColor[zoodiac.family]



                    if color == "red":
                        for enemy in room.Enemies:
                            enemy[0].df -= 3
                            enemy[0].dmg -= 3
                            enemy[0].speed -= 5
                            if enemy[0].df < 0:
                                enemy.df = 0
                            sucess = True
                    elif color == "orange":
                        for traac in self.player.Traacs:
                            traac.charge += 15
                            traac.charge = min(traac.charge, traac.maxCharge)
                            sucess = True
                    elif color == "yellow":
                        qtdX = self.player.Greebles["Xendans"]
                        qtdX = min(qtdX, 4)
                        self.player.unacquire(["Xendans", qtdX])
                        self.player.acquire(["Verdans", qtdX])

                        qtdX = self.player.Greebles["Kollors_off"]
                        qtdX = min(qtdX, 3)
                        self.player.unacquire(["Kollors_off", qtdX])
                        self.player.acquire(["Kollors", qtdX])

                        qtdX = self.player.Greebles["Shots"]
                        qtdX = min(qtdX, 20)
                        self.player.unacquire(["Shots", qtdX])
                        self.player.acquire(["Clots", qtdX//2])

                        qtdX = self.player.MaxGreebles["Heeds"]
                        qtdX = min(qtdX, 10)
                        self.player.acquire(["Heeds", qtdX])

                        sucess = True
                    elif color == "white":
                        self.player.df += 5
                        self.player.dmg += 5
                        self.player.speed += 10
                        self.player.tempDf += 5
                        self.player.tempDmg += 5
                        self.player.tempSpeed += 10
                        sucess = True
                    elif color == "green":
                        for shop in room.Shops:
                            shop[0][3] = round(shop[0][3]*0.7)
                            sucess = True
                    elif color == "cyan":
                        for rm in self.currentFloor.Rooms:
                            for deploy in rm.Deploys:
                                deploy[0].hp += 50
                                deploy[0].hp = min(deploy[0].hp, deploy[0].mhp)
                                sucess = True
                    elif color == "gray":
                        for rm in self.currentFloor.Rooms:
                            if rm.color == "void":
                                rm.color = "gray"
                            if rm.color == "gray":
                                rm.populate(self.params)
                                sucess = True
                    elif color == "teal":
                        pass
                    elif color == "blue":
                        for raac in self.player.Raacs:
                            raac[0].charge = raac[0].maxCharge
                            sucess = True
                    elif color == "purple":
                        for altar in room.Altars:
                            altar[0].uses = altar[0].maxuses
                            sucess = True
                    elif color == "black":
                        if rm.color == "black":
                            room.populate(self.params)
                            sucess = True
                    elif color == "magenta":
                        idZ = self.player.lastZoodiacUsed
                        if not idZ:
                            idZ = (4, 11, 0)
                        room.findFreePosition(Zoodiac(idZ))
                        sucess = True
                elif zoodiac.aspect == "Mind":
                    color = zoodiacColor[zoodiac.family]


                    
                    if color == "red":
                        for enemy in room.Enemies:
                            if enemy[0].type == "Boss":
                                enemy[0] = Enemy(Enemy.chooseRandomBoss(), "King", self.level)
                            if enemy[0].type == "Elite":
                                enemy[0] = Enemy(Enemy.chooseRandomEnemy(), "Boss", self.level)
                            else:
                                enemy[0] = Enemy(Enemy.chooseRandomEnemy(), "Elite", self.level)
                            sucess = True
                    elif color == "orange":
                        for traac in self.player.Traacs:
                            traac.maxCharge += 2
                            sucess = True
                    elif color == "yellow":
                        for greeble in room.Greebles:
                            RNG = random.randrange(100)
                            if greeble[0][0] in GQ0+GQ0b:
                                if RNG <= 80:
                                    greeble[0][0] = random.choice(GQ1)
                            elif greeble[0][0] in GQ1+GQ1b:
                                if RNG <= 20:
                                    greeble[0][0] = random.choice(GQ2)
                            elif greeble[0][0] in GQ2+GQ2b:
                                if RNG <= 1:
                                    greeble[0][0] = random.choice(GQ3)
                            sucess = True
                    elif color == "white":
                        self.player.df += 1
                        self.player.dmg += 1
                        self.player.speed += 1
                        sucess = True
                    elif color == "green":
                        for rm in self.currentFloor.Rooms:
                            if rm.color == "green":
                                rm.randomShop(self.level)
                                sucess = True
                    elif color == "cyan":
                        squireLevel = 1
                        for raac in self.player.Raacs:
                            if raac.name == "Squire":
                                squireLevel += raac.level
                        for rm in self.currentFloor.Rooms:
                            for broot in rm.Broots:
                                broot[0] = Broot(broot[0].id, squireLevel)
                                sucess = True
                            for broot in self.player.Broots:
                                broot = Broot(broot.id, squireLevel)
                                sucess = True
                    elif color == "gray":
                        self.rooms["normal_gray"] += 3
                        self.rooms["plate_gray"] += 3
                    elif color == "teal":
                        pass
                    elif color == "blue":
                        for raac in room.Raacs:
                            raac[0].level += 1
                            sucess = True
                    elif color == "purple":
                        for altar in room.Altars:
                            qtd = 6
                            if altar[0].rarity == "Unique":
                                qtd = 0
                            elif altar[0].rarity == "Mythical":
                                qtd = 1
                            elif altar[0].rarity == "Rare":
                                qtd = 2
                            elif altar[0].rarity == "Uncommon":
                                qtd = 4
                            altar[0].uses += qtd
                            altar[0].maxuses += qtd
                            sucess = True
                    elif color == "black":
                        for enemy in room.Enemies:
                            if enemy[0].type == "Boss":
                                enemy[0].mhp = round(enemy[0].mhp*1.5)
                                enemy[0].hp = min(round(enemy[0].hp*1.5), enemy[0].mhp)
                                enemy[0].dmg = round(enemy[0].dmg*1.35)
                                enemy[0].df = round(enemy[0].df*1.6)
                                enemy[0].speed = round(enemy[0].speed*1.4)
                                enemy[0].charge += 5
                        if rm.color == "black":
                            room.populate(self.params)
                            sucess = True
                    elif color == "magenta":
                        self.params[4] += 2
                        sucess = True



            if sucess:
                self.player.lastZoodiacUsed = zoodiac.id
            else:
                self.player.Zoodiacs.append(zoodiac)




init()
game = Game()
game.run()


print("Killed!!")
print(f"At the dance floor {game.level}")









