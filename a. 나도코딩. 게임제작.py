import pygame
from pygame.constants import K_DOWN, K_UP

pygame.init() # 초기화 반드시설정

# 화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀설정
pygame.display.set_caption("nado game") # 게임이름

#FPS : Frame per second / 초당 주사율
clock = pygame.time.Clock()

# 여기까지 필수조치
# --------------------------------------------------------------
# 1. 배경화면, 캐릭터설정 , 좌표, 속도, 폰트 등

# 배경화면 
background = pygame.image.load("C:/Users/GD/Desktop/pythonworkspace/background.png")

# 내 캐릭터 
character = pygame.image.load("C:/Users/GD/Desktop/pythonworkspace/character.png")
character_size = character.get_rect().size # 케릭터 사이즈
character_width = character_size[0]        # 케릭터 가로 크기
character_height = character_size[1]       # 캐릭터 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로 절반크기에 위치
character_y_pos = screen_height - character_height # 화면세로크기 가장아래에 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 케릭터
enemy = pygame.image.load("C:/Users/GD/Desktop/pythonworkspace/enemy.png")
enemy_size = enemy.get_rect().size 
enemy_width = enemy_size[0]        
enemy_height = enemy_size[1]       
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) 
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)

# 폰트
game_font = pygame.font.Font(None, 40) # 폰트종류와 크기

# 총 시간
total_time = 10
# 시작 시간
start_tick = pygame.time.get_ticks() # 시작 시간틱

# ---------------------------------------------------------------
# 2. 이벤트 처리 (키보드, 마우스 조작 등)

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) #  FPS / 초당 프레임 수
    print("fps : " + str(clock.get_fps()))
    
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False  #게임이 진행중이 아님.
            
        # 키보드로 움직이기 / 미리 좌표를 계산하여 입력
        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지.
            if event.key == pygame.K_LEFT: # 왼쪽으로
                to_x -= character_speed  # 왼쪽으로 입력값 또는 이동속도 설정만큼 이동 (x좌표라 마이너스)
            elif event.key == pygame.K_RIGHT: # 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 아래로
                to_y += character_speed
                
        if event.type == pygame.KEYUP: # 방향키 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                 to_y = 0
    
#----------------------------------------------------------------
# 3. 게임 케릭터 위치 정의
    # 케릭터 위치 값
    character_x_pos += to_x * dt # 멈추기 위해 0을 더하는 것. 
    character_y_pos += to_y * dt # * dt 는 이동 속도 

    # 가로 화면밖으로 안나가게 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    
    # 세로 화면밖으로 안나가게 처리   
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height
        
# ---------------------------------------------------------------------
# 4. 게임 충돌 처리 /  체크 

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
         print("충돌했습니다.")
         running = False
            
#----------------------------------------------------------------
# 5. 화면표시

    screen.blit(background, (0, 0)) # 배경화면 위치 x,y 좌표
    
    screen.blit(character, (character_x_pos, character_y_pos)) # 내 케릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 케릭터 그리기
    
    # 타이머 (시간경과)
    elapsed_time = (pygame.time.get_ticks() - start_tick) / 1000 # 경과시간(ms)을 1000으로 나누어서 초 단위로 표시
    # 타이머표시
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 타이머
    screen.blit(timer, (10, 10))
    # 시간 0 이하면 종료
    if total_time - elapsed_time <= 0:
        print("시간종료")
        running = False
    
    pygame.display.update() # 배경화면 업데이트 (적용)
    # screen.fill((0, 0, 255)) RGB 값도 가능
    
     # 0초 지나도 잠시 대기
pygame.time.delay(2000) # 초단위로 변경하려면 천을 뒤에 더해줘야함,(ms sec)

# 종료
pygame.quit()