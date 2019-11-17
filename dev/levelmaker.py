import random

from gameobjects import Floor
from materials import metal, stone, glass
from block import Block
from enemies import Enemy1, Enemy2


class LevelMaker(object):

    def __init__(self, screen, space, entities):
        self.screen = screen
        self.space = space
        self.entities = entities
        self.levels = [self.level1, self.level2, self.level3]
        random.shuffle(self.levels)

    def makeLevels(self, initialX, player):
        currentX = initialX
        for func in self.levels:
            currentX += func(currentX, player)
    
    def level1(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+490, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 20, 200, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 500), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 800

    def level2(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+200, 230), 20, 200, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 200, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+600, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+110, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal)
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+510, 340), 200, 20, metal)
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+690, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 450), 20, 200, metal)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+600, 450), 20, 200, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 280), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+600, 280), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)
        self.entities.append(blockBottom5)
        self.entities.append(blockBottom6)

        self.entities.append(blockMiddle1)
        self.entities.append(blockMiddle2)
        self.entities.append(blockMiddle3)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)
        self.entities.append(blockUpper4)

        self.entities.append(blockTop1)
        self.entities.append(blockTop2)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 800

    def level3(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+490, 120), 200, 20, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+200, 230), 20, 200, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 200, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+600, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+310, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+490, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 20, 200, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 280), player)
        enemy4 = Enemy1(self.screen, self.space, self.entities, (initialX+600, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)
        self.entities.append(blockBottom5)
        self.entities.append(blockBottom6)

        self.entities.append(blockMiddle1)
        self.entities.append(blockMiddle2)
        self.entities.append(blockMiddle3)
                
        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)
        self.entities.append(enemy4)

        return 800
    
    def level4(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 220), 400, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 220), 400, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+410, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+590, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+500, 230), 20, 200, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+410, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+590, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 430), 20, 200, metal)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+500, 450), 20, 200, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 480), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+500, 60), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+500, 500), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)

        self.entities.append(blockMiddle1)
                
        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)
        self.entities.append(blockTop2)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 800

    def level5(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+470, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+650, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+380, 230), 20, 560, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+470, 340), 200, 20, metal)
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+650, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+470, 450), 20, 380, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+380, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+560, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)

        self.entities.append(blockMiddle1)
                
        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 800
        
    def level6(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+310, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+510, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+310, 230), 20, 420, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+220, 60), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+420, 60), player)
        enemy3 = Enemy2(self.screen, self.space, self.entities, (initialX+620, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)

        self.entities.append(blockMiddle1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 800
        
    def level7(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+690, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+400, 230), 20, 600, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+210, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+590, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+400, 450), 20, 400, metal)

        blockSky1 = Block(self.screen, self.space, self.entities, (initialX+310, 560), 200, 20, metal)
        blockSky2 = Block(self.screen, self.space, self.entities, (initialX+490, 560), 200, 20, metal)

        blockHeaven1 = Block(self.screen, self.space, self.entities, (initialX+400, 690), 20, 200, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 60), player)
        enemy2 = Enemy2(self.screen, self.space, self.entities, (initialX+400, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 500), player)
        enemy4 = Enemy1(self.screen, self.space, self.entities, (initialX+400, 720), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)
                
        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)

        self.entities.append(blockTop1)

        self.entities.append(blockSky1)
        self.entities.append(blockSky2)

        self.entities.append(blockHeaven1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)
        self.entities.append(enemy4)

        return 800
        
    def level8(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 1200)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+110, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom3 = Block(self.screen, self.space, self.entities, (initialX+470, 120), 200, 20, metal)
        blockBottom4 = Block(self.screen, self.space, self.entities, (initialX+650, 120), 200, 20, metal)
        blockBottom5 = Block(self.screen, self.space, self.entities, (initialX+830, 120), 200, 20, metal)
        blockBottom6 = Block(self.screen, self.space, self.entities, (initialX+1010, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+290, 230), 20, 380, metal)
        blockMiddle2 = Block(self.screen, self.space, self.entities, (initialX+830, 230), 20, 200, metal)
        blockMiddle3 = Block(self.screen, self.space, self.entities, (initialX+560, 250), 20, 380, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+110, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal)
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+830, 340), 200, 20, metal)
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+1010, 340), 200, 20, metal)
        blockUpper5 = Block(self.screen, self.space, self.entities, (initialX+470, 360), 200, 20, metal)
        blockUpper6 = Block(self.screen, self.space, self.entities, (initialX+650, 360), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+200, 450), 20, 200, metal)
        blockTop2 = Block(self.screen, self.space, self.entities, (initialX+920, 450), 20, 200, metal)
        blockTop3 = Block(self.screen, self.space, self.entities, (initialX+560, 470), 20, 200, metal)

        enemy1 = Enemy1(self.screen, self.space, self.entities, (initialX+200, 280), player)
        enemy2 = Enemy1(self.screen, self.space, self.entities, (initialX+920, 280), player)
        enemy3 = Enemy1(self.screen, self.space, self.entities, (initialX+560, 300), player)
        enemy4 = Enemy2(self.screen, self.space, self.entities, (initialX+560, 60), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)
        self.entities.append(blockBottom3)
        self.entities.append(blockBottom4)
        self.entities.append(blockBottom5)
        self.entities.append(blockBottom6)

        self.entities.append(blockMiddle1)
        self.entities.append(blockMiddle2)
        self.entities.append(blockMiddle3)
                
        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)
        self.entities.append(blockUpper4)
        self.entities.append(blockUpper5)
        self.entities.append(blockUpper6)

        self.entities.append(blockTop1)
        self.entities.append(blockTop2)
        self.entities.append(blockTop3)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)
        self.entities.append(enemy4)

        return 1200

    def level9(self, initialX, player):
        floor = Floor(self.screen, self.space, self.entities, initialX, 800)

        blockBottom1 = Block(self.screen, self.space, self.entities, (initialX+290, 120), 200, 20, metal)
        blockBottom2 = Block(self.screen, self.space, self.entities, (initialX+470, 120), 200, 20, metal)

        blockMiddle1 = Block(self.screen, self.space, self.entities, (initialX+380, 230), 20, 560, metal)

        blockUpper1 = Block(self.screen, self.space, self.entities, (initialX+110, 340), 200, 20, metal)
        blockUpper2 = Block(self.screen, self.space, self.entities, (initialX+290, 340), 200, 20, metal)
        blockUpper3 = Block(self.screen, self.space, self.entities, (initialX+470, 340), 200, 20, metal)
        blockUpper4 = Block(self.screen, self.space, self.entities, (initialX+650, 340), 200, 20, metal)

        blockTop1 = Block(self.screen, self.space, self.entities, (initialX+380, 450), 20, 560, metal)

        enemy1 = Enemy2(self.screen, self.space, self.entities, (initialX+200, 280), player)
        enemy2 = Enemy2(self.screen, self.space, self.entities, (initialX+380, 280), player)
        enemy3 = Enemy2(self.screen, self.space, self.entities, (initialX+560, 280), player)

        self.entities.append(floor)

        self.entities.append(blockBottom1)
        self.entities.append(blockBottom2)

        self.entities.append(blockMiddle1)

        self.entities.append(blockUpper1)
        self.entities.append(blockUpper2)
        self.entities.append(blockUpper3)
        self.entities.append(blockUpper4)

        self.entities.append(blockTop1)

        self.entities.append(enemy1)
        self.entities.append(enemy2)
        self.entities.append(enemy3)

        return 800