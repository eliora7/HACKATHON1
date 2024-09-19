from CONSTS import *

pygame.init()
# Creating logo screen:
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Golden Support")
screen.fill((240, 194, 70))
screen_display = pygame.display
screen.blit(LOGO, (400, 100))
screen_display.update()
playsound('song.mp3')

# Creating phone_num screen:
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1500, 1000])
base_font = pygame.font.Font(None, 100)
user_text = ''
input_rect = pygame.Rect(520, 500, 430, 100)
color_passive = pygame.Color("black")
color = color_passive

pygame.mixer.init()
pygame.mixer.music.load('relax_song.mp3')
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
user_text = ''
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode

            if len(user_text) == 10:
                pygame.mixer.music.stop()
                running = False
    screen.fill((240, 194, 70))
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 15))
    screen.blit(PHONE_NUM_TITLE, (385, 100))
    screen.blit(SMALL_LOGO, (20, 20))
    pygame.display.flip()

# Creating not registered screen:
user_name = ''
if user_text not in ELDERLY_PHONE_NUM:  # or in database
    pygame.time.delay(500)
    screen = pygame.display.set_mode((1500, 1000))
    screen.fill((240, 194, 70))
    screen_display = pygame.display
    screen.blit(SMALL_LOGO, (20, 20))
    screen.blit(NOT_REGISTERED, (350, 100))
    screen_display.update()
    playsound('sad_song.mp3')
    run = True
    while run:
        for event in pygame.event.get():
            # Clicking on the red X:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_PLUS:
                    clock = pygame.time.Clock()
                    screen = pygame.display.set_mode([1500, 1000])
                    base_font = pygame.font.Font(None, 100)
                    user_name = ''
                    input_rect = pygame.Rect(520, 500, 430, 100)
                    color_passive = pygame.Color("black")
                    color = color_passive

                    pygame.mixer.init()
                    pygame.mixer.music.load('relax_song.mp3')
                    pygame.mixer.music.set_volume(0.7)
                    pygame.mixer.music.play()
                    running = True
                    while running:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_BACKSPACE:
                                    user_name = user_name[:-1]
                                else:
                                    user_name += event.unicode

                                if event.key == pygame.K_RETURN:
                                    user_name = user_name[:-1]
                                    running = False

                        screen.fill((240, 194, 70))
                        pygame.draw.rect(screen, color, input_rect)
                        text_surface = base_font.render(user_name, True, (255, 255, 255))
                        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 15))
                        screen.blit(ENTER_NAME, (385, 100))
                        screen.blit(SMALL_LOGO, (20, 20))
                        pygame.display.flip()
                        if not running:
                            screen = pygame.display.set_mode((1500, 1000))
                            screen.fill((240, 194, 70))
                            screen_display = pygame.display
                            screen.blit(TEXT_GLAD, (350, 350))
                            screen.blit(SMALL_LOGO, (20, 20))
                            screen_display.update()
                            ELDERLY_PEOPLE_DICT[user_name] = user_text
                            with open("dict_file.txt", "w") as file:
                                for name, num in ELDERLY_PEOPLE_DICT.items():
                                    file.write(name + " " + num + "\n")
                            ELDERLY_PHONE_NUM.append(user_text)
                            with open("list_file.txt", "w") as file:
                                for tel in ELDERLY_PHONE_NUM:
                                    file.write(tel + "\n")

                            # print(ELDERLY_PEOPLE_DICT)
                            # print(ELDERLY_PHONE_NUM)
                            pygame.time.delay(1000)
                            pygame.quit()
                            sys.exit()

                elif event.key == pygame.K_KP_MINUS:
                    pygame.quit()
                    sys.exit()


# Creating hello elder screen:
else:
    pygame.time.delay(500)
    if user_text == ELDERLY_PEOPLE_DICT["ELDER1"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER1, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        playsound('elder1.mp3')

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER2"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER2, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        playsound('elder2.mp3')

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER3"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER3, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        playsound('elder3.mp3')

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER4"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER4, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        playsound('elder4.mp3')

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER5"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER5, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        playsound('elder5.mp3')

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER6"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER6, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        playsound('elder6.mp3')
    pygame.display.flip()

    # Creating did you see well screen:
    WHAT_PRESS = 9
    run = True
    screen = pygame.display.set_mode((1500, 1000))
    screen.fill((240, 194, 70))
    screen_display = pygame.display
    screen.blit(SMALL_LOGO, (20, 20))
    screen.blit(BLIND, (350, 100))
    screen_display.update()
    playsound('did_you_see_well.mp3')
    while run:
        for event in pygame.event.get():
            # Clicking on the red X:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    WHAT_PRESS = 0
                elif event.key == pygame.K_1:
                    WHAT_PRESS = 1
                if event.key == pygame.K_1 or event.key == pygame.K_0:
                    # Creating activity screen:
                    pygame.time.delay(500)
                    if WHAT_PRESS == 1:
                        pygame.mixer.init()
                        pygame.mixer.music.load('cant_see_well.mp3')
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play()
                    elif WHAT_PRESS == 0:
                        pygame.mixer.init()
                        pygame.mixer.music.load('relax_song.mp3')
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.play()
                    running = True
                    while running:
                        screen.fill((240, 194, 70))
                        screen.blit(TITLE, (400, 50))
                        screen.blit(FOOD, (200, 250))
                        screen.blit(CLEAN, (600, 250))
                        screen.blit(FIX, (1050, 250))
                        screen.blit(STUFF, (200, 600))
                        screen.blit(TALKING, (600, 600))
                        screen.blit(LAWYER, (1050, 600))
                        screen.blit(SMALL_LOGO, (20, 20))

                        # Performing actions in the game:
                        for event in pygame.event.get():
                            # Clicking on the red X:
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            # Creating is coming screen:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_1:
                                    pygame.mixer.music.stop()
                                    screen = pygame.display.set_mode((1500, 1000))
                                    screen.fill((255, 228, 181))
                                    screen.blit(PEOPLE1, (400, 100))
                                    screen.blit(IS_COMING, (400, 800))
                                    screen.blit(SMALL_LOGO, (20, 20))
                                    screen_display = pygame.display
                                    screen_display.update()
                                    running = False
                                    if WHAT_PRESS == 1:
                                        playsound("people1_coming.mp3")
                                    else:
                                        playsound("is_coming_song.mp3")

                                elif event.key == pygame.K_2:
                                    pygame.mixer.music.stop()
                                    screen = pygame.display.set_mode((1500, 1000))
                                    screen.fill((255, 228, 181))
                                    screen.blit(PEOPLE2, (400, 100))
                                    screen.blit(IS_COMING, (400, 800))
                                    screen.blit(SMALL_LOGO, (20, 20))
                                    screen_display = pygame.display
                                    screen_display.update()
                                    running = False
                                    if WHAT_PRESS == 1:
                                        playsound("people2_coming.mp3")
                                    else:
                                        playsound("is_coming_song.mp3")

                                elif event.key == pygame.K_3:
                                    pygame.mixer.music.stop()
                                    screen = pygame.display.set_mode((1500, 1000))
                                    screen.fill((255, 228, 181))
                                    screen.blit(PEOPLE3, (400, 100))
                                    screen.blit(IS_COMING, (400, 800))
                                    screen.blit(SMALL_LOGO, (20, 20))
                                    screen_display = pygame.display
                                    screen_display.update()
                                    running = False
                                    if WHAT_PRESS == 1:
                                        playsound("people3_coming.mp3")
                                    else:
                                        playsound("is_coming_song.mp3")

                                elif event.key == pygame.K_4:
                                    pygame.mixer.music.stop()
                                    screen = pygame.display.set_mode((1500, 1000))
                                    screen.fill((255, 228, 181))
                                    screen.blit(PEOPLE4, (400, 100))
                                    screen.blit(IS_COMING, (400, 800))
                                    screen.blit(SMALL_LOGO, (20, 20))
                                    screen_display = pygame.display
                                    screen_display.update()
                                    running = False
                                    if WHAT_PRESS == 1:
                                        playsound("people4_coming.mp3")
                                    else:
                                        playsound("is_coming_song.mp3")

                                elif event.key == pygame.K_5:
                                    pygame.mixer.music.stop()
                                    screen = pygame.display.set_mode((1500, 1000))
                                    screen.fill((255, 228, 181))
                                    screen.blit(PEOPLE5, (400, 100))
                                    screen.blit(IS_COMING, (400, 800))
                                    screen.blit(SMALL_LOGO, (20, 20))
                                    screen_display = pygame.display
                                    screen_display.update()
                                    running = False
                                    if WHAT_PRESS == 1:
                                        playsound("people5_coming.mp3")
                                    else:
                                        playsound("is_coming_song.mp3")

                                elif event.key == pygame.K_6:
                                    pygame.mixer.music.stop()
                                    screen = pygame.display.set_mode((1500, 1000))
                                    screen.fill((255, 228, 181))
                                    screen.blit(PEOPLE6, (400, 100))
                                    screen.blit(IS_COMING, (400, 800))
                                    screen.blit(SMALL_LOGO, (20, 20))
                                    screen_display = pygame.display
                                    screen_display.update()
                                    if WHAT_PRESS == 1:
                                        playsound("people6_coming.mp3")
                                    else:
                                        playsound("is_coming_song.mp3")
                                    running = False
                            pygame.display.flip()

                    # Creating last screen:
                    last_screen = pygame.display.set_mode((1500, 1000))
                    last_screen.fill((240, 194, 70))
                    screen_display = pygame.display
                    screen.blit(BYE, (550, 200))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display.update()
                    pygame.time.delay(200)
                    playsound('bye.mp3')
                    pygame.display.flip()
                    pygame.quit()
                    sys.exit()
