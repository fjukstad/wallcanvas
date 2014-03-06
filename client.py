from rpcHugs import RPC, Dummy
import pygame
import sys
import os

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

        self.surface = None
        self.running = True

        os.environ['SDL_VIDEO_WINDOW_POS'] = "250,250"

    def set_display(self, surfaceString):
        self.surface = pygame.image.frombuffer(surfaceString, (self.width,self.height), 'RGBA')
        print "updated screen"
        return 0

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            #pygame.display.update()
            if self.surface:
                self.screen.blit(self.surface, (0,0))
                #pygame.display.flip()
                pygame.display.update()

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
