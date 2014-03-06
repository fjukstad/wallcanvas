from rpcHugs import RPC, Dummy
import pygame
import sys
import os
import threading

class Client(RPC):
    def __init__(self, port=0):
        RPC.__init__(self, port)

        self.height = 768
        self.width = 1024

        pygame.init()
        pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()

        pygame.mouse.set_visible(False)

        self.inputsurface = None
        self.surface = None
        self.running = True

        os.environ['SDL_VIDEO_WINDOW_POS'] = "250,250"


    def set_size(self, w, h):
        self.w = w
        self.h = h

    def set_display(self, surfaceString):

        print len(surfaceString)

        self.inputsurface = pygame.image.frombuffer(surfaceString,
                (self.w,self.h), 'RGBA')
        t = threading.Thread(target=self.render)
        t.start()
        print "updated screen"
        return 0

    def stop(self):
        self.running = False

    def render(self):
        self.surface = pygame.transform.scale(self.inputsurface, (self.width, self.height))

        self.screen.blit(self.surface, (0,0))
        pygame.display.update()

    def run(self):
        while self.running:
            continue

        pygame.quit()



if __name__ == "__main__":
    try:
        c = Client(9999)
        print c.server_info()
        c.run()

    except:
        sys.stdout.write("\n")
        sys.stdout.flush()
        raise
