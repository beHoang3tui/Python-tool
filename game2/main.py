import pygame
import time
import random
from objects import Road, Player, Nitro, Tree, Button, \
					Obstacle, Coins, Fuel

pygame.init()
SCREEN = WIDTH, HEIGHT = 350, 622

info = pygame.display.Info()
width = info.current_w
height = info.current_h

# Set screen , title , icon
win = pygame.display.set_mode(SCREEN)
pygame.display.set_caption('RACING CAR')
Icon = pygame.image.load('Assets/logo.png')
pygame.display.set_icon(Icon)

clock = pygame.time.Clock()
FPS = 60

lane_pos = [50, 95, 142, 190]

# COLORS 

WHITE = (255, 255, 255)
BLUE = (30, 144,255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 20)

# FONTS 
font = pygame.font.SysFont('consolas', 25)
font_cf = pygame.font.SysFont('consolas', 15) # font of fuel
select_car = font.render('Select Your Car', True, WHITE)

# IMAGES 

bg = pygame.image.load('Assets/bgr.png')
home_img = pygame.image.load('Assets/home2.png')
play_img = pygame.image.load('Assets/buttons/play.png')
end_img = pygame.image.load('Assets/end.jpg')
end_img = pygame.transform.scale(end_img, (WIDTH, HEIGHT))
game_over_img = pygame.image.load('Assets/game_over.png')
game_over_img = pygame.transform.scale(game_over_img, (220, 220))
coin_img = pygame.image.load('Assets/coins/1.png')
high_score_img = pygame.image.load('Assets/highcore.png')
dodge_img = pygame.image.load('Assets/car_dodge.png')
load_img = pygame.image.load('Assets/load.png')
left_arrow = pygame.image.load('Assets/buttons/arrow.png')
right_arrow = pygame.transform.flip(left_arrow, True, False)
no_img = pygame.image.load('Assets/no.png')
home_btn_img = pygame.image.load('Assets/buttons/home.png')
replay_img = pygame.image.load('Assets/buttons/replay.png')
sound_off_img = pygame.image.load("Assets/buttons/soundOff.png")
sound_on_img = pygame.image.load("Assets/buttons/soundOn.png")

# list car
cars = []
car_type = 0
for i in range(1, 9):
	img = pygame.image.load(f'Assets/cars/{i}.png')
	img = pygame.transform.scale(img, (59, 101))
	cars.append(img)

nitro_frames = []
nitro_counter = 0
for i in range(6):
	img = pygame.image.load(f'Assets/nitro/{i}.gif')
	img = pygame.transform.flip(img, False, True)
	img = pygame.transform.scale(img, (18, 36))
	nitro_frames.append(img)

# FUNCTIONS *******************************************************************
def center(image):
	return (WIDTH // 2) - image.get_width() // 2

# BUTTONS *********************************************************************
play_btn = Button(play_img, (150, 50), center(play_img), HEIGHT-150)
la_btn = Button(left_arrow, (32, 42), 40, 180)
ra_btn = Button(right_arrow, (32, 42), WIDTH-60, 180)

home_btn = Button(home_btn_img, (24, 24), WIDTH // 4 - 18, HEIGHT - 80)
replay_btn = Button(replay_img, (36,36), WIDTH // 2  - 18, HEIGHT - 86)
sound_btn = Button(sound_on_img, (24, 24), WIDTH - WIDTH // 4 - 18, HEIGHT - 80)

# SOUNDS **********************************************************************

click_fx = pygame.mixer.Sound('Sounds/click.mp3')
fuel_fx = pygame.mixer.Sound('Sounds/fuel.wav')
start_fx = pygame.mixer.Sound('Sounds/start.mp3')
restart_fx = pygame.mixer.Sound('Sounds/restart.mp3')
coin_fx = pygame.mixer.Sound('Sounds/coin.mp3')

pygame.mixer.music.load('Sounds/mixkit-tech-house-vibes-130.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.6)

# OBJECTS *********************************************************************
road = Road()
nitro = Nitro(WIDTH-80, HEIGHT-80)
p = Player(100, HEIGHT-120, car_type)

tree_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

# VARIABLES *******************************************************************
home_page = True
car_page = False
game_page = False
over_page = False

move_left = False
move_right = False
move_up = False
move_down = False
nitro_on = False
sound_on = True

counter = 0
counter_inc = 1
speed = 3
dodged = 0
coins = 0
cfuel = 100
high_score = 0
endx, enddx = 0, 0.5
gameovery = -50

running = True
while running:
	win.fill(BLACK)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# update car up , down 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				running = False

			if event.key == pygame.K_LEFT:
				move_left = True

			if event.key == pygame.K_RIGHT:
				move_right = True

			if event.key == pygame.K_UP:
				move_up = True

			if event.key == pygame.K_DOWN:
				move_down = True

			if event.key == pygame.K_SPACE :
				nitro_on = True
			
				
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				move_left = False

			if event.key == pygame.K_RIGHT:
				move_right = False

			if event.key == pygame.K_UP:
				move_up = False

			if event.key == pygame.K_DOWN:
				move_down = False

			if event.key == pygame.K_SPACE:
				nitro_on = False
				speed = 3
				counter_inc = 1

		if event.type == pygame.MOUSEBUTTONDOWN :
			x, y = event.pos

			if nitro.rect.collidepoint((x, y)):
				nitro_on = True
			else:
				if x <= WIDTH // 2:
					move_left = True
				else:
					move_right = True

		if event.type == pygame.MOUSEBUTTONUP:
			move_left = False
			move_right = False
			move_up = False
			move_down = False
			nitro_on = False
			speed = 5
			counter_inc = 1

	if home_page:
		win.blit(home_img, (0,0))
		win.blit(load_img, (80, 530))
		counter += 1
		if counter % 60 == 0:
			home_page = False
			car_page = True

	if car_page:
		win.blit(select_car, (center(select_car), 80))

		win.blit(cars[car_type], (WIDTH//2-30, 150))
		if la_btn.draw(win):
			car_type -= 1
			click_fx.play()
			if car_type < 0:
				car_type = len(cars) - 1

		if ra_btn.draw(win):
			car_type += 1
			click_fx.play()
			if car_type >= len(cars):
				car_type = 0

		if play_btn.draw(win):
			car_page = False
			game_page = True

			start_fx.play()

			p = Player(100, HEIGHT-120, car_type)
			counter = 0

	if over_page:
		win.blit(end_img, (endx, 0))
		endx += enddx
		if endx >= 10 or endx<=-10:
			enddx *= -1

		win.blit(game_over_img, (center(game_over_img), gameovery))
		if gameovery < 16:
			gameovery += 1

		num_coin_img = font.render(f'{coins}', True, WHITE)
		num_dodge_img = font.render(f'{dodged}', True, WHITE)
		# Score = coins + dodged
		distance_img = font.render(f'Score : {coins+dodged} ', True, WHITE)
		# High score 
		if (coins+dodged > high_score):
			high_score = coins+dodged 
		num_high_score_img = font.render(f'{high_score}', True, WHITE)

		win.blit(high_score_img, (120, 205))
		win.blit(num_high_score_img, (200, 217))

		win.blit(coin_img, (120, 425))
		win.blit(num_coin_img, (200, 430))

		win.blit(distance_img, (center(distance_img), (480)))

		if home_btn.draw(win):
			over_page = False
			home_page = True

			coins = 0
			dodged = 0
			counter = 0
			nitro.gas = 0
			cfuel = 100

			endx, enddx = 0, 0.5
			gameovery = -50

		if replay_btn.draw(win):
			over_page = False
			game_page = True

			coins = 0
			dodged = 0
			counter = 0
			nitro.gas = 0
			cfuel = 100

			endx, enddx = 0, 0.5
			gameovery = -50

			restart_fx.play()

		if sound_btn.draw(win):
			sound_on = not sound_on

			if sound_on:
				sound_btn.update_image(sound_on_img)
				pygame.mixer.music.play(loops=-1)
			else:
				sound_btn.update_image(sound_off_img)
				pygame.mixer.music.stop()

	if game_page:
		win.blit(bg, (0,0))
		road.update(speed)
		road.draw(win)
		# increase the time -> the speed also increases
		if(counter%50==0):
			speed += 0.1
		counter += counter_inc
		# many trees by the roadside 
		if counter % 10 == 0:
			tree = Tree(random.choice([-5, WIDTH-35]), -20)
			tree_group.add(tree)

		if counter % 270 == 0:
			type = random.choices([1, 2], weights=[6, 4], k=1)[0]
			x = random.choice(lane_pos)+10
			if type == 1:
				count = random.randint(1, 3)
				for i in range(count):
					coin = Coins(x,-100 - (25 * i))
					coin_group.add(coin)
			elif type == 2:
				fuel = Fuel(x, -100)
				fuel_group.add(fuel)
		elif counter % 90 == 0:
			obs = random.choices([1, 2, 3], weights=[6,2,2], k=1)[0]
			obstacle = Obstacle(obs)
			obstacle_group.add(obstacle)

		if nitro_on and nitro.gas > 0:
			x, y = p.rect.centerx - 8, p.rect.bottom - 10
			win.blit(nitro_frames[nitro_counter], (x, y))
			nitro_counter = (nitro_counter + 1) % len(nitro_frames)

			speed = 10
			if counter_inc == 1:
				counter = 0
				counter_inc = 5

		if nitro.gas <= 0:
			speed = 3
			counter_inc = 1

		nitro.update(nitro_on)
		nitro.draw(win)
		obstacle_group.update(speed)
		obstacle_group.draw(win)
		tree_group.update(speed)
		tree_group.draw(win)
		coin_group.update(speed)
		coin_group.draw(win)
		fuel_group.update(speed)
		fuel_group.draw(win)

		p.update(move_left, move_right , move_up , move_down)
		p.draw(win)

		if cfuel > 0:
			pygame.draw.rect(win, GREEN, (20, 20, cfuel, 15), border_radius=5)
		pygame.draw.rect(win, WHITE, (20, 20, 100, 15), 2, border_radius=5)
		cfuel -= 0.05
		# remaining fuel display
		numcf = font_cf.render(f'{cfuel:.2f}/100 ', True, BLACK)
		win.blit(numcf, (25, 20))
		# out of fuel -> lose
		if(cfuel<=0):
			pygame.draw.rect(win, RED, p.rect, 1)
			speed = 0

			game_page = False
			over_page = True

			tree_group.empty()
			coin_group.empty()
			fuel_group.empty()
			obstacle_group.empty()

		# COLLISION DETECTION & KILLS
		for obstacle in obstacle_group:
			if obstacle.rect.y >= HEIGHT:
				if obstacle.type == 1:
					dodged += 1
				obstacle.kill() 
				
			if pygame.sprite.collide_mask(p, obstacle):
				# obstacle collision -> explosion
				win.blit(no_img, (p.rect.x-7, p.rect.y))
				pygame.display.update()
				# sleep 1s
				time.sleep(1)
				speed = 0

				game_page = False
				over_page = True

				tree_group.empty()
				coin_group.empty()
				fuel_group.empty()
				obstacle_group.empty()
				
			
				
				

		if pygame.sprite.spritecollide(p, coin_group, True):
			coins += 1
			coin_fx.play()

		if pygame.sprite.spritecollide(p, fuel_group, True):
			cfuel += 25
			fuel_fx.play()
			if cfuel >= 100:
				cfuel = 100

	pygame.draw.rect(win, BLUE, (0, 0, WIDTH, HEIGHT), 3)
	clock.tick(FPS)
	pygame.display.update()

pygame.quit()