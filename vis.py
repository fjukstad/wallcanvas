from rpcHugs import RPC, Dummy
import pygame

boxw = 10
boxh = 10

spacex = 2
spacey = 2


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

    def update(self):
        r = 255
        g = 255
        b = 255

        self.screen.fill((r,g,b))
        self.draw_pi()

    def draw_pi(self):
        x = 0
        y = 0

        for l in range(len(self.pi)):
            letter = self.pi[l]

            square = pygame.Rect(x,y,boxw,boxh)
            color = get_color(letter)
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
        print self.server_info()
        visman = self.getDummy(('10.1.255.120', 9999))

        screen = self.get_screen()
        visman.set_display(screen)


    def new_surface(self, string):
        pass
        #surface = pygame.image.frombuffer(string, (250,250), 'P')


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
    h = 700
    w = 1000
    vis = Vis(w,h)
    vis.run()



