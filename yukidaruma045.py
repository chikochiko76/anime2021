!rm -rf anime2021  
!git clone https://github.com/kkuramitsu/anime2021.git
import IPython
from anime2021.anime import *  

class Simulator(object):

    def run(self, max=10):
        for t in range(0, max):
            self.show(t)
            self.update()
        self.show(max)

DEAD = 0
ALIVE = 1

class LifeGame(Simulator):
    M:int
    N:int
    fields:list

    def __init__(self, M=8, N=6):
        self.M = M
        self.N = N
        self.fields = [[DEAD] * N for _ in range(M)]
        self.fields[1][1] = ALIVE
        self.fields[1][1] = ALIVE
        self.fields[2][1] = ALIVE
        self.fields[2][1] = ALIVE
        self.fields[3][1] = ALIVE
        self.fields[4][1] = ALIVE
        self.fields[5][1] = ALIVE
        self.fields[6][1] = ALIVE

    def show(self, t):
        print(f'時刻: {t}')
        for y in range(self.N):
            for x in range(self.M):
                if self.fields[x][y] == ALIVE:
                    print('⛄️', end='')
                else:
                    print('💙', end='')
            print()

    def count_lives(self, x, y):
        c = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    c += self.fields[(x+dx)%self.M][(y+dy)%self.N]
        return c

    def update(self):
        lives = {}
        for x in range(self.M):
            for y in range(self.N):
                lives[(x,y)] = self.count_lives(x, y)

        for x in range(self.M):
            for y in range(self.N):
                life = self.fields[x][y]
                c = lives[(x, y)]
                if life == DEAD and c == 3:
                    self.fields[x][y] = ALIVE
                elif life == ALIVE and (c != 2 and c != 3):
                    self.fields[x][y] = DEAD

game = LifeGame(8, 6)
game.run()

COLOR = ['black', 'pink'] 

class LifeGameAnime(LifeGame):

    def __init__(self, M=8, N=6):
        LifeGame.__init__(self, M, N)

    def render(self, canvas: ACanvas, frame: int):
        width = canvas.width   
        height = canvas.height   
        size = int(min(width / self.M, height / self.N))  
        for y in range(self.N):
            for x in range(self.M):
                color = COLOR[self.fields[x][y]]  
                ox = x * size
                oy = y * size
                canvas.draw.rectangle((ox, oy, ox+size-1, oy+size-1), fill=color)

studio = AStudio(300,300)

game = LifeGameAnime(8, 8)
studio.append(game)

for t in range(8):
    studio.render() 
    game.update() 

import IPython
IPython.display.Image(studio.create_anime(delay=300))                
