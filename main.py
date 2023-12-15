# Bullet Challenge 
import pygame 
import random
 
# Define colors 
Grey = [128, 128, 128] 
White = [255, 255, 255] 
Blue = [0, 0, 255]  
Red = [255, 0, 0] 
Green = [0, 255, 0]  
Black = [0, 0, 0] 
randColor = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]

# Player Class 
class Player():
    def __init__(self, x, y, w, h):
        self.x = x 
        self.y = y 
        self.w = w 
        self.h = h  
    def drawPlayer(self, screen): 
        pygame.draw.ellipse(screen, White, [self.x, self.y, self.w, self.h]) 

# Circle Class 
class Circle():
    def __init__(self, x, y, w, h, c):  
        self.h = h
        self.w = w 
        self.x = x 
        self.y = y   
        self.xspeed = random.choice([-3, -2, -1, 1, 2, 3])
        self.yspeed = random.choice([-3, -2, -1, 1, 2, 3]) 
        self.c = c
    def drawCircle(self, screen):
        pygame.draw.ellipse(screen, self.c, [self.x, self.y, self.w, self.h], 2)  
    def moveCircle(self):
        self.x += self.xspeed 
        self.y += self.yspeed  

# List of Circles 
circles = [] 
for i in range(15): 
    randColor = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
    wHRan = random.randrange(30, 40)
    circles.append(Circle(random.randrange(0, 770), random.randrange(0, 375), wHRan, wHRan, randColor))       

# Wall Collision 
def wallCollision(rect): 
    if rect.x >= 800 - rect.w:
        rect.xspeed = -rect.xspeed
        rect.yspeed = rect.yspeed  
    elif rect.x <= 0:
        rect.xspeed = -rect.xspeed
        rect.yspeed = rect.yspeed
    elif rect.y >= 500 - rect.h:
        rect.yspeed = -rect.yspeed
        rect.xspeed = rect.xspeed  
    elif rect.y <= 0:
        rect.yspeed = -rect.yspeed 
        rect.xspeed = rect.xspeed  

player = Player(375, 550, 50, 50)
# Main function 
def main():
    pygame.init() 
    # Canvas
    size = (800, 600)
    screen = pygame.display.set_mode(size)  
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Main Program Loop 
    while not done:
        # Main event loop
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True   
            # Check Key Pressed for Player Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.x += -2 
            elif keys[pygame.K_RIGHT]:
                player.x += 2 
        
        screen.fill(Black)
        pygame.draw.rect(screen, White, [0, 500, 800, 10]) 
        player.drawPlayer(screen)  
        for i in range(len(circles)):
            circles[i].drawCircle(screen)  
            wallCollision(circles[i])
            circles[i].moveCircle()
        pygame.display.flip()
 
        # --- Limit frames
        clock.tick(60)  

     # Close window
    pygame.quit()  

main()