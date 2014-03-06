from rpcHugs import RPC, Dummy
import pygame
import random
import threading

boxw = 5
boxh = 5

spacex = 1
spacey = 1

tiles = [('tile-5-3', 9999),
         ('tile-6-3', 9999)]
port = 9999
wallcanvas = [
    [
        ("tile-0-3",port),
        ("tile-1-3",port),
        ("tile-2-3",port),
        ("tile-3-3",port),
        ("tile-4-3",port),
        ("tile-5-3",port),
        ("tile-6-3",port)
    ],

    [
        ("tile-0-2",port),
        ("tile-1-2",port),
        ("tile-2-2",port),
        ("tile-3-2",port),
        ("tile-4-2",port),
        ("tile-5-2",port),
        ("tile-6-2",port)
    ],

    [
        ( "tile-0-1",port),
        ( "tile-1-1",port),
        ( "tile-2-1",port),
        ( "tile-3-1",port),
        ( "tile-4-1",port),
        ( "tile-5-1",port),
        ( "tile-6-1",port)
    ],

    [
        ("tile-0-0", port),
        ("tile-1-0", port),
        ("tile-2-0", port),
        ("tile-3-0", port),
        ("tile-4-0", port),
        ("tile-5-0", port),
        ("tile-6-0", port)
    ]
]

class Vis(RPC):
    def __init__(self,width,height, port=0):

        pygame.init()
        pygame.display.set_mode((width,height))

        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.running = True
        self.height = height
        self.width = width

        with open ("pi.txt", "r") as f:
            self.pi = f.read().replace('\n', '')

        RPC.__init__(self, port)


        # Info about the displaywall
        self.numtiles = 28
        self.tilesx = 7
        self.tilesy = 4
        self.tileres = (1024,768)

    def update(self):
        r = 255
        g = 255
        b = 255

        self.screen.fill((r,g,b))
        self.draw_pi()
        #self.draw_box()
        #self.draw_mazda()
    def draw_pi(self):
        x = 0
        y = 0

        for l in range(len(self.pi)):
            letter = self.pi[l]

            square = pygame.Rect(x,y,boxw,boxh)
            color = get_color(letter)
            #color = get_color(str(random.randint(0,9)))
            pygame.draw.rect(self.screen, color, square, 0)

          #   grey_square = pygame.Rect(x,y,boxw-2,boxh-2)
          #   grey = pygame.Color(135,133,52,0)
          #   pygame.draw.rect(self.screen, grey, grey_square, 0)
            if y >= self.height:
                print l
                break

            x += boxw + spacex
            if x > self.width:
                y += boxh + spacey
                x = 0

    def draw_box(self):
        x = 50
        y = 50
        h = 150
        w = 150

        square = pygame.Rect(x,y,w,h)
        color = get_color(str(random.randint(0,9)))
        pygame.draw.rect(self.screen, color, square, 0)

    def draw_mazda(self):
        img = pygame.image.load('mazda.jpg')
        self.screen.blit(img,(0,0))



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
            self.send_screen()

    def get_screen(self):
        return pygame.image.tostring(self.screen, 'RGBA')

    def send_screen(self):

        # screen = self.get_screen()
        h = self.height/self.tilesy
        w = self.width/self.tilesx
        x = 0
        y = 0

        for row in wallcanvas:
            x = 0
            for t in row:
                display = self.extract_surface(x,y,w,h)
                visman = self.getDummy(t)
                visman.set_size(w,h)
                visman.set_display(display)
                #t = threading.Thread(target=self.send_display, args=(visman, screen))
                #t.start()
                print "sent to", t, x,y,h,w
                x += w
            y += h

        print "sent displays to different tiles"

    def send_display(self, client, display):
        client.set_display(display)

    def new_surface(self, string):
        pass
        #surface = pygame.image.frombuffer(string, (250,250), 'P')

    def extract_surface(self, x,y,w,h):

        surface = pygame.Surface((w,h))
        surface.blit(self.screen, (0,0), (x,y,h,w))
        return pygame.image.tostring(surface, 'RGBA')



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
    h = 1024
    w = 1792
    vis = Vis(w,h)
    vis.run()



