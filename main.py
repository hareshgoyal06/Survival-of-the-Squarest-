import pygame, sys
import random
from pygame.locals import QUIT
from pygame import mixer

pygame.init()
#assigning simple varaibles 
clock = pygame.time.Clock()
width = 1000
height = 1000
grey = (69, 71, 75 )
black = (0,0,0)
backgroundx = 0
backgroundy= 0
pygame.mixer.init()
mixer.music.load("gun.mp3")
#opens the text file for high score
f = open("scores.txt", 'r')
scr = f.readlines()
list = scr[0]
scores = list.split()
score_list = []
for el in scores:
  score_list.append(int(el))
score_list.sort()
#Finds the highest score
high_score = score_list[-1]
f.close()

  
#blits/images used within our game 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Survival of the Squarest!')
  #sets the parameters of the font 
font = pygame.font.SysFont('Georgia',40,bold=True)
font2 = pygame.font.SysFont('Arial',30,bold=False)
  #assigns a font's properties to a variable
play = font.render('Play Game', True, 'white') 
how =  font.render('How to Play', True, 'white')
imp = pygame.image.load("Title.png").convert()
  #each variable is assigned to a image // pygame.transform allows us to change an image's scale  
inactive = pygame.image.load("box.png").convert()
inactive = pygame.transform.scale(inactive, (255,80))
inactive1 = pygame.transform.scale(inactive, (285,80))
active = pygame.image.load("lightbox.png").convert()
active = pygame.transform.scale(active, (255,80))
active1 = pygame.transform.scale(active, (285,80))
howtoplay = pygame.image.load("Play.png").convert()
okay = pygame.image.load("okay.png").convert()
okay = pygame.transform.scale(okay, (260,80))
okay1 = pygame.image.load("okay1.png").convert()
okay1 = pygame.transform.scale(okay1, (260,80))
key = pygame.image.load("key.png").convert()
key = pygame.transform.scale(key, (260,80))
  #convert_alpha will allow us to keep a transparent background for an image
ball = pygame.image.load("circles.png").convert_alpha()
ball = pygame.transform.scale(ball, (30,30))
square = pygame.image.load("square.png").convert_alpha()
square = pygame.transform.scale(square, (15,45))
square2 = pygame.transform.scale(square, (45,15))
end = pygame.image.load("End.png").convert_alpha()
tank_up = pygame.image.load("tank.png").convert_alpha()
tank_right = pygame.image.load("tankR.png").convert_alpha()
tank_left = pygame.image.load("tankL.png").convert_alpha()
tank_down = pygame.image.load("tankD.png").convert_alpha()
heart = pygame.image.load("Heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (40,40))
heart_powerup = pygame.image.load("heart_boost.png").convert_alpha()
ammo_draw = pygame.image.load("star.png").convert_alpha()
ammo_draw = pygame.transform.scale(ammo_draw, (40,40))
tryagain = pygame.image.load("TryAgain.png").convert_alpha()
tryagain = pygame.transform.scale(tryagain, (240,100))
tryagain_inactive = pygame.image.load("TryAgainInactive.png").convert_alpha()
tryagain_inactive = pygame.transform.scale(tryagain_inactive, (240,100))
thankyou = pygame.image.load("ThankYou.png").convert_alpha()
thankyou = pygame.transform.scale(thankyou, (700,700))
steps = pygame.image.load("Nextsteps.png").convert_alpha()
steps = pygame.transform.scale(steps, (300,300))

mainloop = True 
done = True
instructions = True


while done:
  screen.fill((173,173,173))
  #Creates the ball animation
  for i in range(5):
    ballx = random.randrange(0, 1000) #random x position 
    bally = random.randrange(0, 1000) #random y position 
    for num in range(5):
      screen.blit(ball, (ballx,bally)) #every new frame, 5 balls will take a new random position across the screen
      #this creates the illusion that the balls are constantly moving 
        
  #Finds mouse position          
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  #based on mouse position and button pressed, you either progress to the game or a how to play screen
    #sets it so that the mouse's x and y coordinates must be within specific parameters
    #the parameters are based on the width/length of the box and of the place it is placed 
  if (390 + 255 > mouse[0] > 255) and (390 + 80 > mouse[1] > 390): 
    screen.blit(active, (390, 390))
    if click[0] == 1: #if click = True 
      done = False #breaks out of the loop 
  else:
    screen.blit(inactive, (390, 390))
  if (370 + 285 > mouse[0] > 285) and (600 + 80 > mouse[1] > 600):
    screen.blit(active1, (370, 590))
    if click[0] == 1:
      while instructions == True: #creates a new loop 
        screen.fill(black)
        screen.blit(howtoplay, (80, 10)) #creates a new screen with instructions 
        screen.blit(key, (360,690))
        for event in pygame.event.get():    
           if event.type == pygame.KEYDOWN: #if any key is pressed, it breaks out of the loop
             instructions = False #the game will now commence
        pygame.display.update()
      break     
        
  else:
    screen.blit(inactive1, (370, 590))
  
  screen.blit(play, (400, 400))
  screen.blit(how, (380, 600))
  screen.blit(imp, (150, 30))
  pygame.display.update()
  for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()   

#Creates rect objects for the player and enemy hitbox
player = pygame.Rect(500, 500, 30, 30)
player_hitbox1 = pygame.Rect(500, 505, 75, 50)
player_hitbox2 = pygame.Rect(505, 500, 50, 75)
bullet_hitbox1 = pygame.Rect(500, 500, 15, 45)
bullet_hitbox2 = pygame.Rect(500, 500, 15, 45)
enemy_hitbox = pygame.Rect(500,500, 30, 30)
#Creates a health bar
health = 400
hel = pygame.Rect(50, 30, 40, 40 )
bar = pygame.Rect((hel.x + 38), 33, health, 30)
max_bar = pygame.Rect((hel.x + 38), 33, 400, 30)
#Creates empty list for bullet and enemies
enemy = []
bullet = []
bullet_num = 0
bullet_max = 0
vel = 2
enemy_vel = 1
x_speed = 0
y_speed = 0  
damage = 20
#Boolean valeus dictate which way the bullets move, and the tank faces
canshoot = True
up = True
down = False
left = False
right = False
shoot = False
bullet_up = False
bullet_down = False
bullet_left = False
bullet_right = False

  

wave = 1
ammo = None
score = 0
#Function to spawn in a new wave of enemies
def newwave(lev):
  del enemy[:]
  for i in range(lev):
    enemy.append(pygame.Rect(random.randrange(0, width), 10, 25, 25))
  for i in range(lev):
    enemy.append(pygame.Rect(random.randrange(0, width), 990, 25, 25))
  for i in range(lev):
    enemy.append(pygame.Rect(10,random.randrange(0, height), 25, 25))
  for i in range(lev):
    enemy.append(pygame.Rect(990, random.randrange(0, height), 25, 25))
newwave(wave)
#Function to add ammo
def reload():
  for i in range(30):
    bullet.append(pygame.Rect(0, 0, 15, 15))
    

reload()
pygame.time.delay(200)

while True: 
  while mainloop == True:
      screen.fill(black)
      for num1 in range(50):
            for num in range(50):
              pygame.draw.rect(screen, grey, [backgroundx,backgroundy,20,20], 1)      
              backgroundx = 20 * num
              if num == 49:
                backgroundy = 20 * num1
      
      ammo = len(bullet)
      for event in pygame.event.get():
          if event.type == QUIT:
              pygame.quit()
              sys.exit()
          keys = pygame.key.get_pressed()
          #Checks to see if the player is able to shoot
          if keys[pygame.K_SPACE] and canshoot and ammo >1:               
            mixer.music.play()
            #Checks direction of the tank
            if up == True:
              bullet_up = True
              bullet_down = False
              bullet_left = False
              bullet_right = False
            if down == True:
              bullet_up = False
              bullet_down = True
              bullet_left = False
              bullet_right = False
            if left == True:
              bullet_up = False
              bullet_down = False
              bullet_left = True
              bullet_right = False
            if right == True:
              bullet_up = False
              bullet_down = False
              bullet_left = False
              bullet_right = True
            
            #Sets coridantes for the bullet
            bullet[bullet_num].x = player.x + 15
            bullet[bullet_num].y = player.y           
            shoot = True
            
            
            
          #if you are holding down this key, the character will move in that direction
          if event.type == pygame.KEYDOWN:
            #Checks to see which key is press, and moves the tank accordingly
            if event.key == pygame.K_UP or event.key == pygame.K_w:	
              y_speed -= vel
              up = True
              down = False
              left = False
              right = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
              y_speed += vel
              up = False
              down = True
              left = False
              right = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:	
              x_speed += vel
              up = False
              down = False
              left = False
              right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
              x_speed -= vel   
              up = False
              down = False
              left = True
              right = False
          #Once you let go the character stops moving
          if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
              y_speed += vel
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
              y_speed -= vel
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:	
              x_speed -= vel
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
              x_speed += vel
          # screen.fill(black)
      #The character is moved here, the hitbox moves accordingly
      if (player.x >= 20) and (player.x <= 980):
        if (player.y >= 20) and (player.y <= 980):
          player.y += y_speed
          player.x += x_speed
          player_hitbox1.y += y_speed
          player_hitbox1.x += x_speed
          player_hitbox2.y += y_speed
          player_hitbox2.x += x_speed
          
      
    #Creates a border for the player and hitbox
      if player.top <= 20:
        player.top = 20      
        player_hitbox2.x = player.x
        player_hitbox2.y = player.y
        player_hitbox1.x = player.x
        player_hitbox1.y = player.y
      if player.bottom >= (height-20):
        player.bottom = (height -20)
        player_hitbox2.x = player.x
        player_hitbox2.y = player.y
        player_hitbox1.x = player.x
        player_hitbox1.y = player.y     
      if player.left <= 20:
        player.left = 20
        player_hitbox2.x = player.x
        player_hitbox2.y = player.y
        player_hitbox1.x = player.x
        player_hitbox1.y = player.y
      if player.right >= (width-20):
        player.right = (width - 20)
        player_hitbox2.x = player.x
        player_hitbox2.y = player.y
        player_hitbox1.x = player.x
        player_hitbox1.y = player.y
      
      #Spawn in enemies and their hitboxes
      for num in range(len(enemy)):
          num -= 1 
          try:
            screen.blit(ball, enemy[num]) 
            enemy_hitbox.x = enemy[num].x
            enemy_hitbox.y = enemy[num].y
          except:
            continue
          
          #Moves the enemies and hitboxes according to the players location
          if len(enemy) > 0:
            if player.x > enemy[num].x:
              enemy[num].x += enemy_vel
              pygame.draw.rect(screen, (0,0,0), enemy_hitbox, 1)
            if player.x < enemy[num].x:
              enemy[num].x -= enemy_vel
              pygame.draw.rect(screen, (0,0,0), enemy_hitbox, 1)
  
            if player.y > enemy[num].y:
              enemy[num].y += enemy_vel
              pygame.draw.rect(screen, (0,0,0), enemy_hitbox, 1)
  
            if player.y < enemy[num].y:
              enemy[num].y -= enemy_vel
              pygame.draw.rect(screen, (0,0,0), enemy_hitbox, 1)
            #If the enemy hits the player remove health
            if enemy_hitbox.colliderect(player_hitbox1):
              bar.width -= damage
              enemy.remove(enemy[num])
              pygame.time.delay(50)
              if bar.width <= 0: 
                mainloop = False 
                num = str(score)
                #Writes a new High score
                f = open('scores.txt', 'a' )
                f.write(" "+ num)
                f.close()
            #Checks to see if bullet and enemy collide
            try:
              if enemy_hitbox.colliderect(bullet[bullet_num]):
                enemy.remove(enemy[num])
                bullet.remove(bullet[bullet_num])
                score += 1
            except:
              continue
      # Checks to see if there are any enemies left on screen, if not creates a new wave   
      if len(enemy) == 0:
        pygame.time.delay(200)
        damage += 2
        wave += 1
        newwave(wave) 
        reload()
      if ammo < 5:
        reload()
        
      
      #Direction of tank
      if up == True:
        screen.blit(tank_up, player)  
      if down == True:
        screen.blit(tank_down, player) 
      if right == True:
        screen.blit(tank_right, player)  
      if left == True:
        screen.blit(tank_left, player) 
      #heart/ammo logos
      screen.blit(heart, hel)
      screen.blit(ammo_draw, (60,90))
      Total = font.render("Score: {}".format(score), False,(255, 255,255))
      hs = font.render("High Score: {}".format(high_score), False, (255,255,255))
      screen.blit(Total,(100,90))
      screen.blit(hs, (600, 80))
        #Checks to see if you can shoot
      if shoot:
        canshoot = False
        #Direction of bullet
        if bullet_up == True:           
           pygame.draw.rect(screen, (240,240,240), bullet[bullet_num])
           bullet[bullet_num].y -= 5

          
        elif bullet_right == True:
          pygame.draw.rect(screen, (240,240,240), bullet[bullet_num])
          bullet[bullet_num].x += 5


        elif bullet_down == True:          
          pygame.draw.rect(screen, (240,240,240), bullet[bullet_num])
          bullet[bullet_num].y += 5
        elif bullet_left == True:
          pygame.draw.rect(screen, (240,240,240), bullet[bullet_num])         
          bullet[bullet_num].x -= 5
  
        #Removes bullet if it travels off screen   
        if bullet[bullet_num].x > 970:
          bullet.remove(bullet[bullet_num])
          shoot = False
          canshoot = True        
        elif bullet[bullet_num].y < 30:
          bullet.remove(bullet[bullet_num])
          shoot = False
          canshoot = True
        elif bullet[bullet_num].x < 30:
          bullet.remove(bullet[bullet_num])
          shoot = False
          canshoot = True        
        elif bullet[bullet_num].y > 970:
          bullet.remove(bullet[bullet_num])
          shoot = False
          canshoot = True
        
        
      
      #Draws health bar  
      pygame.draw.rect(screen, (220,20,60), bar)
      pygame.draw.rect(screen, (225,225,225), max_bar, 2 )
      #Draws player hitbox  
      if left == True or right == True:
        pygame.draw.rect(screen, (255,255,255), player_hitbox1, 1)
      if up == True or down == True:
        pygame.draw.rect(screen, (255,255,255), player_hitbox2, 1) 
        
    
    
      clock.tick(120)
      pygame.display.update()
 
  ending = True  
  while mainloop == False: 
    screen.fill((153, 153, 153))
    screen.blit(end, (170,30))
    screen.blit(Total,(390,300))
    screen.blit(steps,(250,400))
    for event in pygame.event.get():    
      if event.type == pygame.KEYDOWN:
        #Checks to see if the player wants to quit or restart
             if event.key == pygame.K_r:
               #if restart, it resets all the info 
               print("hello")
               wave = 0
               score = 0
               del enemy [:]
               del bullet [:]
               player.x = 500
               player.y = 500
               bar.width = health
               player_hitbox1.x = 500
               player_hitbox2.x = 500
               player_hitbox1.y = 500
               player_hitbox2.y = 500
               damage = 20 
               x_speed = 0
               y_speed = 0
               #Goes back to the main loop
               mainloop = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
              #Displays a bye bye screen and quits game
              screen.fill((166,166,166))
              screen.blit(thankyou, (150,0))
              pygame.display.flip()
              pygame.time.delay(2000)
              pygame.quit()
              
              

    
    clock.tick(80)
    pygame.display.update()

  
   
    
