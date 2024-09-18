from CONSTS import *

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Golden Support")
# Creating the screen:
screen3 = pygame.display.set_mode((1500, 1000))
screen3.fill((240, 194, 70))
screen_display = pygame.display
screen3.blit(LOGO, (400, 100))
pygame.display.flip()
phone_num_elder = input("Please enter your phone number to enter the application: ")
if phone_num_elder not in ELDERLY_PHONE_NUM:
    print("We are sorry you are not registered for the application :( ")
    print("contact us to register: 0504667841- Golden Support")
else:
    if phone_num_elder == ELDERLY_PEOPLE_DICT["ELDER1"]:
        screen3 = pygame.display.set_mode((1500, 1000))
        screen3.fill((240, 194, 70))
        screen_display = pygame.display
        screen3.blit(ELDER1, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif phone_num_elder == ELDERLY_PEOPLE_DICT["ELDER2"]:
        screen3 = pygame.display.set_mode((1500, 1000))
        screen3.fill((240, 194, 70))
        screen_display = pygame.display
        screen3.blit(ELDER2, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif phone_num_elder == ELDERLY_PEOPLE_DICT["ELDER3"]:
        screen3 = pygame.display.set_mode((1500, 1000))
        screen3.fill((240, 194, 70))
        screen_display = pygame.display
        screen3.blit(ELDER3, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif phone_num_elder == ELDERLY_PEOPLE_DICT["ELDER4"]:
        screen3 = pygame.display.set_mode((1500, 1000))
        screen3.fill((240, 194, 70))
        screen_display = pygame.display
        screen3.blit(ELDER4, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif phone_num_elder == ELDERLY_PEOPLE_DICT["ELDER5"]:
        screen3 = pygame.display.set_mode((1500, 1000))
        screen3.fill((240, 194, 70))
        screen_display = pygame.display
        screen3.blit(ELDER5, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)

    elif phone_num_elder == ELDERLY_PEOPLE_DICT["ELDER6"]:
        screen3 = pygame.display.set_mode((1500, 1000))
        screen3.fill((240, 194, 70))
        screen_display = pygame.display
        screen3.blit(ELDER6, (400, 100))
        screen.blit(SMALL_LOGO, (20, 20))
        screen_display.update()
        pygame.time.delay(3000)
    pygame.display.flip()

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    screen2 = pygame.display.set_mode((1500, 1000))
                    screen2.fill((255, 228, 181))
                    screen.blit(PEOPLE1, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_2:
                    screen2 = pygame.display.set_mode((1500, 1000))
                    screen2.fill((255, 228, 181))
                    screen.blit(PEOPLE2, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_3:
                    screen2 = pygame.display.set_mode((1500, 1000))
                    screen2.fill((255, 228, 181))
                    screen.blit(PEOPLE3, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_4:
                    screen2 = pygame.display.set_mode((1500, 1000))
                    screen2.fill((255, 228, 181))
                    screen.blit(PEOPLE4, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_5:
                    screen2 = pygame.display.set_mode((1500, 1000))
                    screen2.fill((255, 228, 181))
                    screen.blit(PEOPLE5, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    running = False
                    pygame.time.delay(3000)

                elif event.key == pygame.K_6:
                    screen2 = pygame.display.set_mode((1500, 1000))
                    screen2.fill((255, 228, 181))
                    screen.blit(PEOPLE6, (400, 100))
                    screen.blit(IS_COMING, (400, 800))
                    screen.blit(SMALL_LOGO, (20, 20))
                    screen_display = pygame.display
                    screen_display.update()
                    pygame.time.delay(3000)
                    running = False
            pygame.display.flip()

    last_screen = pygame.display.set_mode((1500, 1000))
    last_screen.fill((240, 194, 70))
    screen_display = pygame.display
    screen.blit(BYE, (550, 200))
    screen.blit(SMALL_LOGO, (20, 20))
    screen_display.update()
    pygame.time.delay(3000)
    pygame.display.flip()
