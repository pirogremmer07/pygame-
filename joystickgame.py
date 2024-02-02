import pygame
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((700,400))
col1=(255,0,0)
col2=(0,0,255)
sprite=pygame.image.load('C:\\Users\\HP\\Desktop\\DBZ\\goku_sprite\\1.png')
bg=pygame.image.load('C:\\Users\\HP\\Desktop\\DBZ\\visual img\\arena.jpg')
bg=pygame.transform.scale(bg,(700,400))
def text_char(message, textFont, textSize, textColor):
    newFont=pygame.font.SysFont(textFont, textSize,True)
    newText=newFont.render(message, 0, textColor)
    return newText
font = "monospace"

def load_char(c,x,y,r,l,j):
        if c>2 and r==False and l==False and j==False:
            screen.blit(pygame.transform.scale(sprite,(1420,1412)),(x,y),(164*2,0,2*55,2*90))
        elif r==True:
            screen.blit(pygame.transform.scale(sprite,(1420,1412)),(x,y),(545*2,0,2*55,2*90))
        elif l==True:
            screen.blit(pygame.transform.scale(sprite,(1420,1412)),(x,y),(490*2,0,2*55,2*90))
        elif j==True and r==False and l==False:
            screen.blit(pygame.transform.scale(sprite,(1420,1412)),(x,y),(600*2,0,2*55,2*90))

        else:
            j=False
            r=False 
            l=False
            screen.blit(pygame.transform.scale(sprite,(1420,1412)),(x,y),(226*2,0,2*48,2*90))
            
        
def disp():
    run=True
    right,left,jump=False,False,False
    xi,yi=250,200
    count=0
    jumpcount1=9
    font="monospace"
    while run:
        key=pygame.key.get_pressed()
        if key[pygame.K_RIGHT] and xi<610:
            right=True
            xi=xi+5
        else: right=False
        if key[pygame.K_LEFT] and xi>0:
            left=True
            xi=xi-5
        else:left=False
        if key[pygame.K_UP] and yi>0:
            jump=True
        if jump :
            if jumpcount1>= -9:
                neg=0.4
                if jumpcount1 <0:
                    neg= -0.4
                yi-=(jumpcount1**2)*0.5*neg
                jumpcount1-= 0.3
            else:
                jump=False
                jumpcount1=9
        else:jump=False

        if key[pygame.K_BACKSPACE]:
            run=False
            pygame.quit()
            quit()       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        screen.blit(bg,(0,0))
        count+=0.1 #tweaking count
        if count>3:
            count=0
        load_char(count,xi,yi,right,left,jump) #tweaking load character
        clock.tick(60)
        pygame.display.flip()

disp()