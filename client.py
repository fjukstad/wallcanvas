from rpcHugs import RPC, Dummy
import pygame
import sys

class Client(RPC):
    def __init__(self, port=0):
        RPC.__init__(self, port)

        self.height = 700
        self.width = 1000

        pygame.init()
        pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()


        self.surface = None
        self.running = True

    def set_display(self, surfaceString):
        self.surface = pygame.image.frombuffer(surfaceString, (self.width,self.height), 'RGBA')
        #self.surface = pygame.image.fromstring(surfaceString, (self.height,self.width), 'RGBA')
        #self.screen = pygame.Surface((self.height, self.width), 0, surface)
        #self.screen_rect = self.screen.get_rect()
        #pygame.display.update()
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
