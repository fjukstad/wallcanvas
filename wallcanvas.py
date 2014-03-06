from rpcHugs import RPC, Dummy
import pygame
import threading

port = 9999
tiles = [
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


class Wallcanvas(RPC):

    def __init__(self, screen):
        # Info about the displaywall
        self.numtiles = 28
        self.tilesx = 7
        self.tilesy = 4
        self.tileres = (1024,768)

        self.screen = screen

        RPC.__init__(self,0)


    def extract_surface(self, x,y,w,h):

        surface = pygame.Surface((w,h))
        surface.blit(self.screen, (0,0), (x,y,h,w))
        return pygame.image.tostring(surface, 'RGBA')
    def send_display(self, client, display):
        client.set_display(display)


    def wallify(self):

        # screen = self.get_screen()
        h = self.height/self.tilesy
        w = self.width/self.tilesx
        x = 0
        y = 0

        for row in tiles:
            x = 0
            for t in row:
                display = self.extract_surface(x,y,w,h)
                visman = self.getDummy(t)
                visman.set_size(w,h)
                visman.set_display(display)
                #t = threading.Thread(target=self.send_display, args=(visman, display))
                #t.start()
                x += w
            y += h


