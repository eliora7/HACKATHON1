import pygame
import sys
from soundplay import playsound
from gtts import gTTS
import os

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
PHONE_NUM_TITLE = pygame.image.load("phone_num.png")
PHONE_NUM_TITLE = pygame.transform.scale(PHONE_NUM_TITLE, (700, 200), )
NOT_REGISTERED = pygame.image.load("not_registered.png")
NOT_REGISTERED = pygame.transform.scale(NOT_REGISTERED, (800, 700), )
BLIND = pygame.image.load("blind.png")
BLIND = pygame.transform.scale(BLIND, (800, 700), )
ENTER_NAME = pygame.image.load("enter_name.png")
ENTER_NAME = pygame.transform.scale(ENTER_NAME, (800, 200), )
TEXT_GLAD = pygame.image.load("text_glad.png")
TEXT_GLAD = pygame.transform.scale(TEXT_GLAD, (800, 300), )

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
with open("dict_file.txt") as f:
    for line in f:
        (k, v) = line.split()
        ELDERLY_PEOPLE_DICT[k] = v
# Play the text:
LANGUAGE = 'en'

with open("list_file.txt") as f:
    for line in f:
        if line[:-1] not in ELDERLY_PHONE_NUM:
            ELDERLY_PHONE_NUM.append(line[:-1])
HELLO_ELDER1 = 'Hello Ruth'
my_obj = gTTS(text=HELLO_ELDER1, lang=LANGUAGE, slow=False)
my_obj.save("elder1.mp3")

HELLO_ELDER2 = 'Hello Anna'
my_obj = gTTS(text=HELLO_ELDER2, lang=LANGUAGE, slow=False)
my_obj.save("elder2.mp3")

HELLO_ELDER3 = 'Hello Rivka'
my_obj = gTTS(text=HELLO_ELDER3, lang=LANGUAGE, slow=False)
my_obj.save("elder3.mp3")

HELLO_ELDER4 = 'Hello Moshe'
my_obj = gTTS(text=HELLO_ELDER4, lang=LANGUAGE, slow=False)
my_obj.save("elder4.mp3")

HELLO_ELDER5 = 'Hello Shlomi'
my_obj = gTTS(text=HELLO_ELDER5, lang=LANGUAGE, slow=False)
my_obj.save("elder5.mp3")

HELLO_ELDER6 = 'Hello Avi'
my_obj = gTTS(text=HELLO_ELDER6, lang=LANGUAGE, slow=False)
my_obj.save("elder6.mp3")

BYE_BYE = 'Thank you for using our application, bye bye'
my_obj = gTTS(text=BYE_BYE, lang=LANGUAGE, slow=False)
my_obj.save("bye.mp3")

CANT_SEE_WELL = ("Please choose the service. for food service enter 1, for cleaning service enter 2 "
                 "for fixing service enter 3, for carrying heavy loads service enter 4, "
                 "for listener service enter 5 and for lawyer service enter 6 ")
my_obj = gTTS(text=CANT_SEE_WELL, lang=LANGUAGE, slow=False)
my_obj.save("cant_see_well.mp3")

PEOPLE1_COMING = "Tal food is coming, her phone number is 0525675673"
my_obj = gTTS(text=PEOPLE1_COMING, lang=LANGUAGE, slow=False)
my_obj.save("people1_coming.mp3")

PEOPLE2_COMING = "Gal cleaning is coming, her phone number is 0525675671"
my_obj = gTTS(text=PEOPLE2_COMING, lang=LANGUAGE, slow=False)
my_obj.save("people2_coming.mp3")

PEOPLE3_COMING = "Bar fixing is coming, his phone number is 0525675670"
my_obj = gTTS(text=PEOPLE3_COMING, lang=LANGUAGE, slow=False)
my_obj.save("people3_coming.mp3")

PEOPLE4_COMING = "Noam carrying heavy loads is coming, his phone number is 0525675674"
my_obj = gTTS(text=PEOPLE4_COMING, lang=LANGUAGE, slow=False)
my_obj.save("people4_coming.mp3")

PEOPLE5_COMING = "Stav listener is coming, her phone number is 0525675672"
my_obj = gTTS(text=PEOPLE5_COMING, lang=LANGUAGE, slow=False)
my_obj.save("people5_coming.mp3")

PEOPLE6_COMING = "Rotem lawyer is coming, his phone number is 0525675675"
my_obj = gTTS(text=PEOPLE6_COMING, lang=LANGUAGE, slow=False)
my_obj.save("people6_coming.mp3")

DID_YOU_SEE_WELL = "If you can't see well? press 1. else press 0"
my_obj = gTTS(text=DID_YOU_SEE_WELL, lang=LANGUAGE, slow=False)
my_obj.save("did_you_see_well.mp3")

DATABASE = "file.txt"
