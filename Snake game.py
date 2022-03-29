import pygame
from time import sleep
from random import randint

pygame.init()
WIDTH = 601
HEIGHT = 601
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ran san moi')
running = True
RED = (255,0,0)
GREEN = (0,200,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
snakes = [[5,6]]
direction = ""
apple = (randint(0,19), randint(0,19))
font = pygame.font.SysFont("sans", 30)
scores = 0
is_gameover = False
clock = pygame.time.Clock()

while running:
	clock.tick(60)
	screen.fill(BLACK)
	tail = [snakes[0][0], snakes[0][1]]

	#Draw grid, snake, bait, scores
	# for i in range(0,21):
	# 	pygame.draw.line(screen, WHITE, (0,i*30), (WIDTH,i*30))
	# for i in range(0,21):
	# 	pygame.draw.line(screen, WHITE, (i*30,0), (i*30,HEIGHT))
	for snake in snakes:
		pygame.draw.rect(screen, GREEN, (snake[0]*30, snake[1]*30, 30, 30))
	pygame.draw.rect(screen, RED, (apple[0]*30, apple[1]*30, 30, 30))
	scores_txt = font.render("Scores: " + str(scores), True, WHITE)
	screen.blit(scores_txt,(5,5))

	#Move snake
	if is_gameover == False:
		if direction == "up":
			snakes.append((snakes[-1][0],snakes[-1][1]-1))
			snakes.pop(0)
			sleep(0.05)
		if direction == "right":
			snakes.append((snakes[-1][0]+1,snakes[-1][1]))
			snakes.pop(0)
			sleep(0.05)
		if direction == "down":
			snakes.append((snakes[-1][0],snakes[-1][1]+1))
			snakes.pop(0)
			sleep(0.05)
		if direction == "left":
			snakes.append((snakes[-1][0]-1,snakes[-1][1]))
			snakes.pop(0)
			sleep(0.05)
	head = [snakes[-1][0], snakes[-1][1]]

	#Snake take the apple
	if (head[0] == apple[0]) and (head[1] == apple[1]):
		snakes.insert(0, tail)
		scores += 1
		apple = [randint(0,19), randint(0,19)]
		head = [snakes[-1][0], snakes[-1][1]]

	#Check GameOver (Up Right Down Left)
	if (snakes[-1][1] < 0) or (snakes[-1][0] > 19) or (snakes[-1][1] > 19) or (snakes[-1][0] < 0):
		is_gameover = True
	for i in range(0, len(snakes)-1):
		if (snakes[i][0] == head[0]) and (snakes[i][1] == head[1]):
			is_gameover = True

	#Game Over
	if is_gameover:
		direction = ""
		gameover_txt = font.render("Game Over", True, WHITE)
		screen.blit(gameover_txt, (220,200))
		playagain_txt = font.render("Press Space to play again", True, WHITE)
		screen.blit(playagain_txt, (140,250))

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_UP) and (direction != "down"):
				direction = "up"
			if (event.key == pygame.K_RIGHT) and (direction != "left"):
				direction = "right"
			if (event.key == pygame.K_DOWN) and (direction != "up"):
				direction = "down"
			if (event.key == pygame.K_LEFT) and (direction != "right"):
				direction = "left"
			if event.key == pygame.K_SPACE and is_gameover == True:
				snakes = [[5,6]]
				apple = [randint(0,19), randint(0,19)]
				scores = 0
				is_gameover = False
			if event.key == pygame.K_p:
				print("snakes: " + str(snakes))
				print("snakes[-1]: " + str(snakes[-1]))
				print("head: " + str(head) + " tail: " + str(tail))
				print("head: " + str(head) + " apple: " + str(apple))
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()