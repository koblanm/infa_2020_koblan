import pygame
from pygame.draw import *
import math 
pygame.init()


FPS = 30
screen = pygame.display.set_mode((1100, 500))

colors1 = [(255,223,196),    #skin
          (0,255,0),    #eyes
          (255,255,255),    #nose
          (255,0,0),    #mouth
          (50,50,50),   #dress
          (255,255,0)]    #hair

colors2 = [(255,223,196),    #skin
          (0,0,255),    #eyes
          (100,45,71),    #nose
          (255,0,0),    #mouth
          (50,50,0),   #dress
          (0,255,255)]    #hair

WHITE = (255, 255, 255)
BLACK = (1, 1, 1)
GAMMA = (0, 0, 0)
PINK = (255, 192, 203)

screen.fill(WHITE)

def head(x, y, skin_color, scale):
    A = 100 * scale
    circle(screen, skin_color, (x, y), int(A))
    
def eyes(x, y, eye_color, scale):
    A = 100 * scale
    #Left
    circle(screen, WHITE, (int(x - A/3), int(y - A/10)), int(A/5))
    circle(screen, BLACK, (int(x - A/3), int(y - A/10)), int(A/5), 1)

    circle(screen, eye_color, (int(x - A/3), int(y - A/10)), int(A/10))
    circle(screen, BLACK, (int(x - A/3), int(y - A/10)), int(A/13))
    
    #Right
    circle(screen, WHITE, (int(x + A/3), int(y - A/10)), int(A/5))
    circle(screen, BLACK, (int(x + A/3), int(y - A/10)), int(A/5), 1)

    circle(screen, eye_color, (int(x + A/3), int(y - A/10)), int(A/10))
    circle(screen, BLACK, (int(x + A/3), int(y - A/10)), int(A/13))

def nose(x, y, nose_color, scale):
    A = 100 * scale
    polygon(screen, nose_color, [(int(x + A/15), y),
                            (int(x - A/15), y),
                            (x, int(y + A/9)),
                            (int(x + A/15), y)])
    polygon(screen, BLACK, [(int(x + A/15), y),
                            (int(x - A/15), y),
                            (x, int(y + A/9)),
                            (int(x + A/15), y)], 1)
    
def mouth(x, y, mouth_color, scale):
    A = 100 * scale
    polygon(screen, mouth_color, [(int(x + A/3), int(y + A/3)),
                            (int(x - A/3), int(y + A/3)),
                            (x, int(y + A/2)),
                            (int(x + A/3), int(y + A/3))])
    polygon(screen, BLACK, [(int(x + A/3), int(y + A/3)),
                            (int(x - A/3), int(y + A/3)),
                            (x, int(y + A/2)),
                            (int(x + A/3), int(y + A/3))], 1)

def hair(x, y, hair_color, scale):
    A = 100 * scale
    size = (int(3*A), int(3*A))
    angle = -45
    for i in range(10):
        surface = pygame.Surface(size)
        surface_rect = surface.get_rect(center = (x, y))
        surface.set_colorkey(GAMMA)
        
        polygon(surface, hair_color, [(int(A*1.5) - int(A/8), int(A/2)),
                                      (int(A*1.5), 0),
                                      (int(A*1.5) + int(A/8), int(A/2)),
                                      (int(A*1.5) - int(A/8), int(A/2))])
        polygon(surface, BLACK, [(int(A*1.5) - int(A/8), int(A/2)),
                                 (int(A*1.5), 0),
                                 (int(A*1.5) + int(A/8), int(A/2)),
                                 (int(A*1.5) - int(A/8), int(A/2))], 1)
        
        surface = pygame.transform.rotate(surface,angle)
        surface_rect = surface.get_rect(center = (x, y))
        screen.blit(surface, surface_rect)
        angle += 10

def hands(x, y, skin_color, scale):
    A = 100 * scale
    line(screen, skin_color, (x, y+int(4*A)), (x+int(2.2*A), y - int(2*A)), int(A/5))
    line(screen, skin_color, (x, y+int(4*A)), (x-int(2.2*A), y - int(2*A)), int(A/5))
    circle(screen, skin_color, (x+int(2.2*A), y - int(2*A)), int(A/4))
    circle(screen, skin_color, (x-int(2.2*A), y - int(2*A)), int(A/4))
    
def dress(x, y, dress_color, scale):
    A = 100 * scale
    circle(screen, dress_color, (x, y + int(2*A)), int(1.4*A))
    
    f1 = pygame.font.Font(None, int(A/4))
    mipt = f1.render('ФОПФ', 1, WHITE)
    screen.blit(mipt, (x, y + int(1.2*A)))
    
    
def shoulder(x, y, dress_color, scale, mirror):
    A = 100 * scale
    k = mirror
    r = 0.4 * A
    coordinates = []
    alpha = -0.2
    while alpha < 2*3.14 - 0.2:
        coordinates.append(((x + k*int(1.1*A) - int(r*math.cos(alpha))),
                             (y + int(0.9*A) + int(r*math.sin(alpha)))))
        alpha += 2*3.14/5
        
    polygon(screen, dress_color,(coordinates))
    polygon(screen,BLACK,(coordinates),1)

def poster(x, y, poster_color, scale, text):
    A = 100 * scale
    polygon(screen, poster_color,((x-int(3*A),y-int(3*A)),
                                  (x+int(8*A),y-int(3*A)),
                                  (x+int(8*A),y-int(2*A)),
                                  (x-int(3*A),y-int(2*A))))

    f1 = pygame.font.Font(None, int(A))
    poster_text = f1.render(text, 1, BLACK)

    screen.blit(poster_text, (x-int(2.5*A),y-int(2.9*A)))

#PUNK
def punk(x, y, colors, scale):
    A = 100 * scale
    skin_color = colors[0]
    eye_color = colors[1]
    nose_color = colors[2]
    mouth_color = colors[3]
    dress_color = colors[4]
    hair_color = colors[5]
    
    hands(x, y, skin_color, scale)
    dress(x, y, dress_color, scale)
    head(x, y, skin_color, scale)
    eyes(x, y, eye_color, scale)   
    nose(x, y, nose_color, scale)
    mouth(x, y, mouth_color, scale)
    hair(x, y, hair_color, scale)
    shoulder(x, y, dress_color, scale, 1)
    shoulder(x, y, dress_color, scale, -1)




scale = 1
x = 300
y = 300
punk(x, y, colors1, scale)
punk(x + int(440*scale), y, colors2, scale)
poster(x, y, PINK, scale, 'PYTHON is REALLY AMAZING')
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
