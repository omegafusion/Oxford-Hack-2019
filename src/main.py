import sys
import time
import math
import random
import os

import pygame
import pymunk
from pymunk.pygame_util import DrawOptions

pygame.mixer.pre_init(22050, -16, 2, 512)
pygame.mixer.init()
pygame.init()
pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)


from gameobjects import TargetLine, Character, Projectile, Floor
from materials import Material, metal, stone, glass
from block import Block
from levelmaker import LevelMaker
from parallax import BackgroundLayer
import functions

FRAMERATE = 60
INITIAL_X = 1800



def gameloop(func):
    def wrapper(*args, **kwargs):
        while True:
            func(*args, **kwargs)
    return wrapper


#class GameOverWindow(object):

#    def __init__(self, screenX, screenY, score, win=False):
#        self.screen = pygame.display.get_surface()
#        self.clock = pygame.time.Clock()


class GameWindow(object):

    def __init__(self, screenX, screenY):
        self._setupGeneral()
        self._setupPygame(screenX, screenY)
        self._setupSpace()
        self._setupCollisionHandlers()
        self._backgroundSetup()

    def _setupGeneral(self):
        self.entities = []
        self.count = 0
        self.dt = 0

    def _setupPygame(self, screenX, screenY):
        self.screen = pygame.display.get_surface()
        self.screenX = screenX
        self.screenY = screenY
        self.options = DrawOptions(self.screen)
        self.clock = pygame.time.Clock()

        songs = ["sounds\music\drive_with_me_looped.wav","sounds\music\motivation_looped.wav"]

        dir_path = os.path.dirname(os.path.realpath(__file__))
        pygame.mixer.music.load(os.path.join(dir_path, random.choice(songs)))
        pygame.mixer.music.play(-1,0.0)
        pygame.mixer.music.set_volume(0.85)

        self.font = pygame.font.SysFont("Arial Black", 16)
        self.score = 0
        self.alive = True

    def _setupSpace(self):
        self.space = pymunk.Space()
        self.space.gravity = 0, -1000

        self.player = Character(self.screen, self.space, self.entities, (100, 600))
        self.entities.append(self.player)
        self.entities.append(Floor(self.screen, self.space, self.entities, -100, 5*self.screen.get_width()))

        # Make the level parts

        LevelMaker(self.screen, self.space, self.entities).makeLevels(INITIAL_X, self.player)
        #self.entities.append(Block(self.screen, self.space, self.entities, (900, 120), 200, 120, glass))
        #floor = Floor(self.screen, self.space, self.entities, 200, 200)

        #self.floor = pymunk.Segment(self.space.static_body, (0, 5), (self.screenX, 5), 10)
        #self.floor.body.position = 0, 5
        #self.floor.elasticity = 0.2
        #self.floor.friction = 0.2

        #self.space.add(self.floor)

    def _setupCollisionHandlers(self):

        def projectileDestroyOnImpact(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 1:
                    try:
                        self.entities.remove(shape.body.entity_ref)
                    except ValueError:
                        #print("Exception Handled. list.remove(x): x not in list")
                        pass
                    self.space.remove(shape.body, shape)

        def enemyProjectileIgnoreBlocks(arbiter, space, data):
            return False

        def projectileIgnoreEnemyProjectile(arbiter, space, data):
            return False

        def enemyProjectileIgnoreEnemy(arbiter, space, data):
            return False

        def projectileDamageBlockEnemy(arbiter, space, data):
            impulse = functions.magnitude(arbiter.total_impulse)
            damage = impulse / 10000
            for shape in arbiter.shapes:
                if shape.collision_type in (3, 4):
                    if damage >= 15:
                        self.score += shape.body.entity_ref.takeDamage(damage)
            projectileDestroyOnImpact(arbiter, space, data)

        def damageBlockEnemy(arbiter, space, data):
            impulse = functions.magnitude(arbiter.total_impulse)
            damage = impulse / 10000
            for shape in arbiter.shapes:
                if shape.collision_type in (3, 4):
                    if damage >= 15:
                        self.score += shape.body.entity_ref.takeDamage(damage) // 2

        def enemyProjectileDamageCharacter(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 2:
                    impulse = functions.magnitude(shape.body.velocity) * shape.body.mass
            damage = impulse / 10000
            for shape in arbiter.shapes:
                if shape.collision_type == 5:
                    self.alive = shape.body.entity_ref.takeDamage(damage)
                elif shape.collision_type == 2:
                    try:
                        self.entities.remove(shape.body.entity_ref)
                    except ValueError:
                        #print("Exception Handled. list.remove(x): x not in list")
                        pass
                    self.space.remove(shape.body, shape)
            return False

        def enemyDamageCharacter(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 5:
                    #print("You touched an enemy and died!")
                    self.alive = False
            return False

        def blockDamageCharacter(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 5:
                    #print("You touched a block and died!")
                    self.alive = False
            return False

        def floorDamageEnemy(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 2:
                    impulse = functions.magnitude(shape.body.velocity) * shape.body.mass
            damage = impulse / 10000
            for shape in arbiter.shapes:
                if shape.collision_type == 4:
                    if damage >= 5:
                        self.score += shape.body.entity_ref.takeDamage(damage) // 2

        def floorDamageBlock(arbiter, space, data):
            for shape in arbiter.shapes:
                if shape.collision_type == 2:
                    impulse = functions.magnitude(shape.body.velocity) * shape.body.mass
            damage = impulse / 10000
            for shape in arbiter.shapes:
                if shape.collision_type == 3:
                    if damage >= 5:
                        self.score += shape.body.entity_ref.takeDamage(damage) // 2

        self.enemyProjectileIgnoreBlocks_handler = self.space.add_collision_handler(2,3)
        self.enemyProjectileIgnoreBlocks_handler.begin = enemyProjectileIgnoreBlocks

        self.projectileDestroyOnImpact_handler = self.space.add_wildcard_collision_handler(1)
        self.projectileDestroyOnImpact_handler.post_solve = projectileDestroyOnImpact

        self.projectileIgnoreEnemyProjectile_handler = self.space.add_collision_handler(1,2)
        self.projectileIgnoreEnemyProjectile_handler.begin = projectileIgnoreEnemyProjectile

        self.enemyProjectileIgnoreEnemy_hander = self.space.add_collision_handler(2,4)
        self.enemyProjectileIgnoreEnemy_hander.begin = enemyProjectileIgnoreEnemy

        self.projectileDamageBlock_handler = self.space.add_collision_handler(1,3)
        self.projectileDamageBlock_handler.post_solve = projectileDamageBlockEnemy

        self.projectileDamageEnemy_handler = self.space.add_collision_handler(1,4)
        self.projectileDamageEnemy_handler.post_solve = projectileDamageBlockEnemy

        self.enemyDamageBlock_handler = self.space.add_collision_handler(3,4)
        self.enemyDamageBlock_handler.post_solve = damageBlockEnemy

        self.enemyProjectileDamageCharacter_handler = self.space.add_collision_handler(2,5)
        self.enemyProjectileDamageCharacter_handler.pre_solve = enemyProjectileDamageCharacter

        self.enemyDamageCharacter_handler = self.space.add_collision_handler(4,5)
        self.enemyDamageCharacter_handler.pre_solve = enemyDamageCharacter

        self.blockDamageCharacter_handler = self.space.add_collision_handler(3,5)
        self.blockDamageCharacter_handler.pre_solve = blockDamageCharacter

        self.floorDamageEnemy_handler = self.space.add_collision_handler(4,6)
        self.floorDamageEnemy_handler.pre_solve = floorDamageEnemy

        self.floorDamageBlock_handler = self.space.add_collision_handler(3,6)
        self.floorDamageBlock_handler.pre_solve = floorDamageBlock

    def _backgroundSetup(self):
        self.bg1 = pygame.image.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "background/bg.png")).convert_alpha()
        self.bgs = [BackgroundLayer(self.screen, "bg_mountains.png", 0.25, self.screen.get_size()[1]-900),
                    BackgroundLayer(self.screen, "bg_hills.png", 0.75, self.screen.get_size()[1]-500),
                    BackgroundLayer(self.screen, "bg_foreground.png", 1.5, self.screen.get_size()[1]-299)]

    @gameloop
    def gameLoop(self):
        self.dt = self.clock.tick(FRAMERATE) / 1000
        self._handleEvents()
        self._executeLogic()
        self._drawObjects()

    def _handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and self.alive is None and event.key == pygame.K_RETURN:
                self.__init__(self.screenX, self.screenY)
            if self.alive:
                for entity in self.entities:
                    entity.handleEvent(event)


    def _executeLogic(self):
        if not self.alive:
            if self.alive is not None:
                del self.space
                del self.entities
                self.alive = None
        else:
            self.space.step(1/(2*FRAMERATE))
            for entity in self.entities:
                entity.update(self.dt)
            for entity in self.entities:
                entity.sidescroll()
        for bg in self.bgs:
            bg.update()

    def _drawObjects(self):
        pygame.display.set_caption("FPS: " + str(self.clock.get_fps()))
        self.screen.blit(self.bg1, (0,0))
        for bg in self.bgs:
            bg.draw()
        #self.space.debug_draw(self.options)
        if self.alive:
            for entity in self.entities:
                entity.draw()

            floorRect = pygame.Rect(0, self.screen.get_height()-20, self.screen.get_width(), 20)
            pygame.draw.rect(self.screen, (64,64,64), floorRect)

            healthText = self.font.render("Health:".format(round(self.player.health)), True, (0,0,0))
            healthTextRect = healthText.get_rect()
            healthTextRect.left = 10
            healthTextRect.top = 10
            self.screen.blit(healthText, healthTextRect)
            
            rectHealth = healthText.get_rect()
            rectHealth.width = self.player.health
            rectHealth.left = healthTextRect.right + 15
            rectHealth.top = 10
            pygame.draw.rect(self.screen, (255,0,0), rectHealth)

            rectHealth.width = 500
            rectHealth.left = healthTextRect.right + 15
            rectHealth.top = 10
            pygame.draw.rect(self.screen, (0,0,0), rectHealth, 4)

            scoreText = self.font.render("Score: {0}".format(self.score), True, (0,0,0))
            scoreTextRect = healthText.get_rect()
            scoreTextRect.left = 10
            scoreTextRect.top = 50
            self.screen.blit(scoreText, scoreTextRect)

        else:
            font1 = pygame.font.SysFont("Arial Black", 192)
            text1 = font1.render("Game Over", True, (0,0,0))
            rect1 = text1.get_rect()
            rect1.center = (self.screen.get_width()//2, 300)
            self.screen.blit(text1, rect1)

            font2 = pygame.font.SysFont("Arial Black", 72)
            text2 = font2.render("Score: {0}".format(self.score), True, (0,0,0))
            rect2 = text2.get_rect()
            rect2.center = (self.screen.get_width()//2, 520)
            self.screen.blit(text2, rect2)

            font3 = pygame.font.SysFont("Arial Black", 16)
            text3 = font3.render("Press enter to play again", True, (0,0,0))
            rect3 = text3.get_rect()
            rect3.center = (self.screen.get_width()//2, self.screen.get_height()-50  )
            self.screen.blit(text3, rect3)

        pygame.display.flip()

    def run(self):
        self.gameLoop()
        pygame.quit()


if __name__ == "__main__":
    myWindow = GameWindow(1800, 900)
    myWindow.run()