import pygame
from wallcanvas import Wallcanvas



class Vis(Wallcanvas):
    def __init__(self):
        # Make sure they are divisible by 7 and 4
        # 1792/7 = 256 and 1024/256
        self.width = 1792
        self.height = 1024

        self.running = True

        pygame.init()
        pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.get_surface()

        # Init wallcanvas
        Wallcanvas.__init__(self, self.screen)


    def draw_box(self):
        x = 50
        y = 50
        h = 150
        w = 150

        square = pygame.Rect(x,y,w,h)
        color = 0xffaabb
        pygame.draw.rect(self.screen, color, square, 0)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.running = False

            self.draw_box()
            pygame.display.update()

            # send pygame window to displaywall
            self.wallify()


if __name__=="__main__":
    v = Vis()
    v.run()

