import pygame
import sys


#initialize pygame

pygame.init()

#Screen dimensions

width, height = 1000, 1000


screen = pygame.display.set_mode((width,height))

pygame.display.set_caption('Gon and Killua');

#colors

WHITE = (255,255,255)
BLACK = (0,0,0)

#Load images of Gon and Killua

gon_image = pygame.image.load('gonFreecs.png')
killua_image = pygame.image.load('killuaZoldyck.png')

#Set Gon and Killua Position


gon_pos = (width // 2, height //2);
killua_pos = [100,100]

#set font

font = pygame.font.Font(None,74)


# set size

gon_image = pygame.transform.scale(gon_image,(200,200))
killua_image = pygame.transform.scale(killua_image,(220,250))

#Main

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #get the keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        killua_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        killua_pos[1] += 5
    if keys[pygame.K_LEFT]:
        killua_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        killua_pos[0] += 5



    #Clear the screen 
    screen.fill(WHITE)


    #Draw Gon and Killua

    screen.blit(gon_image,gon_pos)
    screen.blit(killua_image,killua_pos)

    #Check if Killua reaches Gon


    if (killua_pos[0] + killua_image.get_width() // 2 >= gon_pos[0] and killua_pos[0] <= gon_pos[0] + gon_image.get_width() and killua_pos[1] + killua_image.get_height() // 2 >= gon_pos[1] and killua_pos[1] <= gon_pos[1] + gon_image.get_width()):
        text = font.render("Killua loves Gon!",True,BLACK)
        screen.blit(text,((width - text.get_width()) // 2,(height - text.get_height()) // 2))



    #update the display


    pygame.display.flip()
    pygame.time.delay(10)    


