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
pygame.display.flip()

# Creating phone_num screen:
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1500, 1000])
base_font = pygame.font.Font(None, 100)
user_text = ''
input_rect = pygame.Rect(520, 500, 430, 100)
color_passive = pygame.Color("black")
color = color_passive

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
                running = False
    screen.fill((240, 194, 70))
    pygame.draw.rect(screen, color, input_rect)
    text_surface = base_font.render(user_text, True, (255,255,255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 15))
    screen.blit(PHONE_NUM_TITLE, (385, 100))
    screen.blit(SMALL_LOGO, (20, 20))
    pygame.display.flip()

# Creating hello elder screen:
if user_text not in ELDERLY_PHONE_NUM:
    pygame.time.delay(500)
    screen = pygame.display.set_mode((1500, 1000))
    screen.fill((240, 194, 70))
    screen_display = pygame.display
    screen.blit(SMALL_LOGO, (20, 20))
    screen.blit(NOT_REGISTERED, (400, 100))
    screen_display.update()
    pygame.time.delay(3000)

else:
    pygame.time.delay(500)
    if user_text == ELDERLY_PEOPLE_DICT["ELDER1"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER1, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER2"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER2, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER3"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER3, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER4"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER4, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER5"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER5, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif user_text == ELDERLY_PEOPLE_DICT["ELDER6"]:
        screen = pygame.display.set_mode((1500, 1000))
        screen.fill((240, 194, 70))
        screen_display = pygame.display
        screen.blit(ELDER6, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)
    pygame.display.flip()

    # Creating activity screen:
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
                    screen = pygame.display.set_mode((1500, 1000))
                    screen.fill((255, 228, 181))
                    screen.blit(PEOPLE1, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_2:
                    screen = pygame.display.set_mode((1500, 1000))
                    screen.fill((255, 228, 181))
                    screen.blit(PEOPLE2, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_3:
                    screen = pygame.display.set_mode((1500, 1000))
                    screen.fill((255, 228, 181))
                    screen.blit(PEOPLE3, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_4:
                    screen = pygame.display.set_mode((1500, 1000))
                    screen.fill((255, 228, 181))
                    screen.blit(PEOPLE4, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_5:
                    screen = pygame.display.set_mode((1500, 1000))
                    screen.fill((255, 228, 181))
                    screen.blit(PEOPLE5, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_6:
                    screen = pygame.display.set_mode((1500, 1000))
                    screen.fill((255, 228, 181))
                    screen.blit(PEOPLE6, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    pygame.time.delay(3000)
                    running = False
            pygame.display.flip()

    # Creating last screen:
    last_screen = pygame.display.set_mode((1500, 1000))
    last_screen.fill((240, 194, 70))
    screen_display = pygame.display
    screen.blit(BYE, (550, 200))
    screen.blit(SMALL_LOGO, (20, 20))
    screen_display.update()
    pygame.time.delay(3000)
    pygame.display.flip()

