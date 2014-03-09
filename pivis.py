import pygame
import random
import threading
import math
from wallcanvas import Wallcanvas


boxw = 5
boxh = 5

spacex = 20
spacey = 20
radius = 3


class Vis(Wallcanvas):
    def __init__(self,width,height):

        pygame.init()
        pygame.display.set_mode((width,height))

        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.running = True
        self.height = height
        self.width = width
        self.circle_coordinates = {}

        with open ("pi.txt", "r") as f:
            self.pi = f.read().replace('\n', '')

        Wallcanvas.__init__(self, self.screen)

    def update(self):
        r = 0
        g = 0
        b = 0

        self.screen.fill((r,g,b))
        self.draw_pi()

    def draw_pi(self):
        x = spacex
        y = spacey

        for l in range(len(self.pi)):

            if y > self.height - spacey:
                #self.write_result(l)
                print "Number of decimals "+ str(l)
                break


            letter = self.pi[l]

            square = pygame.Rect(x,y,boxw,boxh)
            color = get_color(letter)

            pygame.draw.circle(self.screen, color, (x,y), radius, 0)
            self.circle_coordinates[(x,y)] = letter

            x += spacex
            if x > self.width - spacex:
                y += spacey
                x = spacex

        for x, y in self.circle_coordinates:
            self.connect_circles(x,y)

    def write_result(self, digits):
        color = (242,169,0,0)
	font = pygame.font.SysFont("Helvetica Light", 30 )
        text = font.render("The first "+str(digits)+" decimals of pi", 1,color)
        textpos = text.get_rect()
        textpos.centerx = self.screen_rect.centerx
        textpos.centery = self.height - 30
        self.screen.blit(text, textpos)

    def connect_circles(self,x,y):

        d = 1

        circle_color = self.circle_coordinates[(x,y)]
        neighbors = self.get_neighbors(x,y,d)

        same_colored_neighbor = 0
        n_color = 0

        for n in neighbors:
            try:
                n_color = self.circle_coordinates[n]
            except KeyError:
                continue
            if n_color == circle_color:
                color = get_color(n_color)

                # get distance and set thickness accordingly
                d = int(neighbors[n])

                if d <= spacex * 1.5:
                    t = 2
                else:
                    t = 1

                pygame.draw.line(self.screen, color, n,(x,y),t)

                same_colored_neighbor += 1

        if same_colored_neighbor <= 1:
            pass
            #pygame.draw.circle(self.screen, (0,0,0), (x,y), radius, 0)


    # d = distance from circle. 1 = closest neighbors, 2 = one hop out etc.
    def get_neighbors(self, x,y, d):
        startx = x - (spacex*d)
        starty = y - (spacex*d)
        endx = x + (spacex*d)
        endy = y + (spacey*d)

        neighbors = {}

        for i in range(startx,endx+spacex,spacex):
            for j in range(starty,endy+spacey,spacey):
                d = math.floor(math.sqrt((x - i)**2 + (y-j)**2))
                neighbors[(i,j)] = d

        return neighbors

    def draw_box(self):
        x = 50
        y = 50
        h = 150
        w = 150

        square = pygame.Rect(x,y,w,h)
        color = get_color(str(random.randint(0,9)))
        pygame.draw.rect(self.screen, color, square, 0)

    def event_loop(self):
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.running = False

    def run(self):
        while self.running:
            self.event_loop()
            self.update()
            pygame.display.update()
            try:
                self.wallify()
            except:
                pass

    def get_screen(self):
        return pygame.image.tostring(self.screen, 'RGBA')


    def send_display(self, client, display):
        client.set_display(display)



def get_color(letter,a=0):
    # if letter == "0":
    #     return pygame.Color(239,0,108,a)
    # elif letter == "1":
    #     return pygame.Color(238,40,33,a)
    # elif letter == "2":
    #     return pygame.Color(252,85,0,a)
    # elif letter == "3":
    #     return pygame.Color(254,184,0,a)
    # elif letter == "4":
    #     return pygame.Color(255,250,0,a)
    # elif letter == "5":
    #     return pygame.Color(137,208,0,a)
    # elif letter == "6":
    #     return pygame.Color(54,185,35,a)
    # elif letter == "7":
    #     return pygame.Color(18,166,255,a)
    # elif letter == "8":
    #     return pygame.Color(28,35,140,a)
    # else:
    #     return pygame.Color(136,12,136,a)


    if letter == "0":
        return pygame.Color(0,97,127,a)
    elif letter == "1":
        return pygame.Color(0,115,150,a)
    elif letter == "2":
        return pygame.Color(0,156,182,a)
    elif letter == "3":
        return pygame.Color(89,190,201,a)
    elif letter == "4":
        return pygame.Color(203,51,59,a)
    elif letter == "5":
        return pygame.Color(222,124,0,a)
    elif letter == "6":
        return pygame.Color(242,169,0,a)
    elif letter == "7":
        return pygame.Color(166,187,200,a)
    elif letter == "8":
        return pygame.Color(211,212,213,a)
    else:
        return pygame.Color(121,175,7,a)

if __name__ == "__main__":
    #h = 314
    #w = 716
    h = 3144
    w = 7168
    vis = Vis(w,h)
    vis.run()
