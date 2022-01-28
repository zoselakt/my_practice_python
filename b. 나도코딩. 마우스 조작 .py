import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("practice")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/GD/Desktop/pythonworkspace/background.png")
character = pygame.image.load("C:/Users/GD/Desktop/pythonworkspace/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 1

running = True
while running:
    dt = clock.tick(90)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEMOTION:
            to_x, to_y = pygame.mouse.get_pos()
            pygame.draw.circle(background, (255, 0, 255), (to_x, to_y), 10)
        if event.type == pygame.MOUSEBUTTONDOWN:                        
            if event.button == 1:
                print("왼쪽 클릭")
            if event.button == 2:
                print("휠 클릭")
            if event.button == 3:
                print("오른쪽 클릭")
            if event.button == 4:
                print("휠 올리기")
            if event.button == 5:
                print("휠 내리기")
                
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        
        
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
                
    screen.blit(background, (0, 0))
    screen.blit(character,(character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
