import os
import pygame
from pygame import key
from pygame.constants import K_RIGHT, K_SPACE

pygame.init() 

screen_width = 640
screen_height = 480 
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("nado pang") 

clock = pygame.time.Clock()
# -------------------------------------------------------------
# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__) # 현재파일의 위치반환
image_path = os.path.join(current_path, "pang") # pang 폴더위치반환

# 배경
background = pygame.image.load(os.path.join(image_path, "background.png"))
# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size [1] # 스테이지의 높이 위에 두기 위해 사용

# 케릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 케릭터 이동방향
character_to_x = 0
# 케릭터 이동속도
character_speed = 5
# 케릭터 무기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
# 여러발 발사하기
weapons = []
# 무기 이동속도
weapon_speed = 10

# 공만들기(4개크기에 대해 따로 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]
# 공 크기에 따른 스피드
ball_speed_y = [-18, -15, -12, -9] # index 0, 1, 2, 3 에 해당
#공 들
balls = []
balls.append({
    "pos_x" : 50,  # 공의 x 좌표
    "pos_y" : 50,  # 공의 y 좌표
    "img_idx" : 0, # 이미지 인덱스
    "to_x": 3,  # x축 이동방향 -3 왼쪽 3 오른쪽
    "to_y": -6, # y축 이동방향
    "init_spd_y": ball_speed_y[0]}) # y 최초속도

# 발사후 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

# font 정의
game_font = pygame.font.Font(None, 40)
total_time = 50
start_ticks = pygame.time.get_ticks()  # 시작시간
# 게임종료 메세지 / timeout, missoin complete, game over
game_result = "game over"

running = True
while running:
    dt = clock.tick(60) 
# -------------------------------------------------------------
# 2. 이벤트 처리

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False  
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # 왼쪽으로
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: 
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기발사
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2) # 무기발사위치
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
            
# 3. 게임 케릭터 / 화면 위치 정의     
    character_x_pos += character_to_x
      
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        
        # 무기 위치조정 
        # 100, 200 → 180, 160, 140 ...
        # 500, 200 → 180, 160, 140 ... : y 위치 변경
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons] # 발사시 무기 위로 나가기
    
    #천장에 닿은 무기 없애기
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
      
        # 공위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]
        
        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        # 벽에 닿았을때 튕겨나오는 효과
        if ball_pos_x <= 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1
        # 바닥에 닿았을때 튕겨나오는 효과
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그외의 모든 경우에는 속도 증가
            ball_val["to_y"] += 0.5
            
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    
# 4. 충돌처리
    # 케릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    for ball_idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
                
    # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
    # 공과 케릭터 충돌처리
    if character_rect.colliderect(ball_rect):
        running = False
        break
    # 공과 무기 충돌처리
    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_pos_x = weapon_val[0]
        weapon_pos_y = weapon_val[1]
    # 무기 rect 정보 업데이트
        weapon_rect = weapon.get_rect()
        weapon_rect.left = weapon_pos_x
        weapon_rect.top = weapon_pos_y
    # 충돌체크
        if weapon_rect.colliderect(ball_rect): 
            weapon_to_remove = weapon_idx   # 해당무기 없애기 위한값
            ball_to_remove = ball_idx # 해당 공 없애기 위한 값
            
            # 공 나누기
            if ball_img_idx < 3: # 가장작은 크기의 공이 아니라면 나누기
                # 현재 공 크기 정보
                ball_width = ball_rect.size[0]
                ball_height = ball_rect.size[1]
                # 나누어 진 공 정보
                small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                small_ball_width = small_ball_rect.size[0]
                small_ball_height = small_ball_rect.size[1]
                
                #왼쪽으로 튕겨 나가는 공
                balls.append({
                     "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                     "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),  # 공의 y 좌표
                     "img_idx" : ball_img_idx + 1 , # 이미지 인덱스
                     "to_x": -3,  # x축 이동방향 -3 왼쪽 3 오른쪽
                     "to_y": -6, # y축 이동방향
                     "init_spd_y": ball_speed_y[ball_img_idx + 1]}) # y 최초속도
                #오른쪽으로 튕겨 나가는 공
                balls.append({
                     "pos_x" : ball_pos_x + (ball_width / 2) - (small_ball_width / 2), # 공의 x 좌표
                     "pos_y" : ball_pos_y + (ball_height / 2) - (small_ball_height / 2),  # 공의 y 좌표
                     "img_idx" : ball_img_idx + 1 , # 이미지 인덱스
                     "to_x":  3,  # x축 이동방향 -3 왼쪽 3 오른쪽
                     "to_y": -6, # y축 이동방향
                     "init_spd_y": ball_speed_y[ball_img_idx + 1]}) # y 최초속도
            break 
         
# 충돌된 공 or 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1
# 모든 공을 없앤 경우 끝내기
    if len(balls) == 0:
        game_result = "mission complete"
        running = False

# 5. 화면에 그리기
    screen.blit(background, (0, 0))      
    
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
        
    for ball_idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y)) 
        
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
# 경과시간 계산
    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000 
    timer = game_font.render("time : {}".format(int(total_time - elapsed_time)), True,(255, 255, 255))
    screen.blit(timer, (10, 10))
    
# 시간 초과 시
    if total_time - elapsed_time <= 0:
        game_result = "time over"
        running = False

    pygame.display.update()     
# 게임오버 메세지    
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()
 # 2초 대기 후 게임오버
pygame.time.delay(2000)
 
pygame.quit()