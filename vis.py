import pygame
import random
import threading
from wallcanvas import Wallcanvas

boxw = 5
boxh = 5

spacex = 15
spacey = 15
radius = 2


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
        #self.draw_box()
        #self.draw_mazda()
    def draw_pi(self):
        x = spacex
        y = spacey

        for l in range(len(self.pi)):

            if y > self.height - spacey:
                break


            letter = self.pi[l]

            square = pygame.Rect(x,y,boxw,boxh)
            color = get_color(letter)
            #pygame.draw.rect(self.screen, color, square, 0)

            pygame.draw.circle(self.screen, color, (x,y), radius, 0)
            #self.screen.set_at((x,y),color)


            self.circle_coordinates[(x,y)] = letter

            #x += boxw + spacex
            #if x > self.width:
            #    y += boxh + spacey
            #    x = 0

            x += spacex
            if x > self.width - spacex:
                y += spacey
                x = spacex

        for x, y in self.circle_coordinates:
            self.connect_circles(x,y)
            #pass

    def connect_circles(self,x,y):

        circle_color = self.circle_coordinates[(x,y)]
        neighbors = self.get_neighbors(x,y)
        n_color = 0
        for n in neighbors:
            try:
                n_color = self.circle_coordinates[n]
            except KeyError:
                continue
            if n_color == circle_color:
                pygame.draw.line(self.screen, get_color(n_color), n,(x,y),1)

    def get_neighbors(self, x,y):
        neighbors = [
                (x-spacex, y-spacey),
                (x, y-spacey),
                (x+spacex, y-spacey),
                (x-spacex, y),
                (x+spacex, y),
                (x-spacex, y+spacey),
                (x, y+spacey),
                (x+spacex, y+spacey)]
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



def get_color(letter):
    if letter == "0":
        return pygame.Color(239,0,108,0)
    elif letter == "1":
        return pygame.Color(238,40,33,0)
    elif letter == "2":
        return pygame.Color(252,85,0,0)
    elif letter == "3":
        return pygame.Color(254,184,0,0)
    elif letter == "4":
        return pygame.Color(255,250,0,0)
    elif letter == "5":
        return pygame.Color(137,208,0,0)
    elif letter == "6":
        return pygame.Color(54,185,35,0)
    elif letter == "7":
        return pygame.Color(18,166,255,0)
    elif letter == "8":
        return pygame.Color(28,35,140,0)
    else:
        return pygame.Color(136,12,136,0)

if __name__ == "__main__":
    h = 3144
    w = 7168
    vis = Vis(w,h)
    vis.run()
