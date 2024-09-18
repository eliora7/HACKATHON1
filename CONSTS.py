import pygame
import sys

pygame.init()

# Pictures:
FOOD = pygame.image.load("food.png")
FOOD = pygame.transform.scale(FOOD, (250, 250), )
CLEAN = pygame.image.load("clean.png")
CLEAN = pygame.transform.scale(CLEAN, (250, 250), )
FIX = pygame.image.load("fix.png")
FIX = pygame.transform.scale(FIX, (250, 250), )
STUFF = pygame.image.load("stuff.png")
STUFF = pygame.transform.scale(STUFF, (250, 250), )
TALKING = pygame.image.load("talking.png")
TALKING = pygame.transform.scale(TALKING, (250, 250), )
LAWYER = pygame.image.load("lawyer.png")
LAWYER = pygame.transform.scale(LAWYER, (250, 250), )
LOGO = pygame.image.load("logo.png")
LOGO = pygame.transform.scale(LOGO, (670, 700), )
SMALL_LOGO = pygame.image.load("logo.png")
SMALL_LOGO = pygame.transform.scale(SMALL_LOGO, (150, 150), )
TITLE = pygame.image.load("title.png")
TITLE = pygame.transform.scale(TITLE, (700, 200), )
BYE = pygame.image.load("bye.png")
BYE = pygame.transform.scale(BYE, (500, 600), )
IS_COMING = pygame.image.load("is_coming.png")
IS_COMING = pygame.transform.scale(IS_COMING, (700, 200), )

# Photos of the volunteers:
PEOPLE1 = pygame.image.load("people1.png")
PEOPLE1 = pygame.transform.scale(PEOPLE1, (670, 700), )
PEOPLE2 = pygame.image.load("people2.png")
PEOPLE2 = pygame.transform.scale(PEOPLE2, (670, 700), )
PEOPLE3 = pygame.image.load("people3.png")
PEOPLE3 = pygame.transform.scale(PEOPLE3, (670, 700), )
PEOPLE4 = pygame.image.load("people4.png")
PEOPLE4 = pygame.transform.scale(PEOPLE4, (670, 700), )
PEOPLE5 = pygame.image.load("people5.png")
PEOPLE5 = pygame.transform.scale(PEOPLE5, (670, 700), )
PEOPLE6 = pygame.image.load("people6.png")
PEOPLE6 = pygame.transform.scale(PEOPLE6, (670, 700), )

# Photos of the elderly people:
ELDER1 = pygame.image.load("elder1.png")
ELDER1 = pygame.transform.scale(ELDER1, (670, 700), )
ELDER2 = pygame.image.load("elder2.png")
ELDER2 = pygame.transform.scale(ELDER2, (670, 700), )
ELDER3 = pygame.image.load("elder3.png")
ELDER3 = pygame.transform.scale(ELDER3, (670, 700), )
ELDER4 = pygame.image.load("elder4.png")
ELDER4 = pygame.transform.scale(ELDER4, (670, 700), )
ELDER5 = pygame.image.load("elder5.png")
ELDER5 = pygame.transform.scale(ELDER5, (670, 700), )
ELDER6 = pygame.image.load("elder6.png")
ELDER6 = pygame.transform.scale(ELDER6, (670, 700), )

ELDERLY_PEOPLE_LIST = [["0509887622", ELDER1], ["0544478914", ELDER2], ["0529883455", ELDER3],
                       ["0501665897", ELDER4], ["0522115633", ELDER5], ["0525593288", ELDER6]]
ELDERLY_PHONE_NUM = ["0509887622", "0544478914", "0529883455", "0501665897", "0522115633", "0525593288"]
ELDERLY_PEOPLE_DICT = {"ELDER1": "0509887622", "ELDER2": "0544478914", "ELDER3": "0529883455", "ELDER4": "0501665897",
                       "ELDER5": "0522115633", "ELDER6": "0525593288"}
