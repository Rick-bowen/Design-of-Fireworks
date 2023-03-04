from utility import *
import pygame,random
from math import sqrt
vec = pygame.math.Vector2
from particle import *
from particlepoint import *
from thrust import *
from rekindle import *
from design import *

class Root(Particle):
    def __init__(self,main,x,y,destination,category="C",color=0):
        self.main = main
        self.position =  vec(x,self.main.canvasHeight)
        #calculate required initial velocity to reach mouse pointer
        self.velocity_value = sqrt(60*destination*10)
        self.velocity = vec(0,-self.velocity_value).rotate(0)
        self.acceleration = vec(0,0)
        self.particle_count = 1000
        self.category = category
        self.color = color
        if self.category == "R":
            self.RekindleCount = 60
        if self.category == "S":
            self.ringCo = random.choice(GRADIENDTS)

    def draw(self):
        pygame.draw.circle(self.main.screen,self.color,(int(self.position.x),int(self.position.y)),6)

    
    def update(self):
        self.thrust()
        self.update_position() #from Particle class 
        #burst at topmost point
        if self.velocity.y > 0:
            self.burst()

    def burst(self):
        #choose random sound and play
        temp = random.choice([2,3])
        EXPLOSION_SOUNDS[temp].play()
        #generate particles
        for i in range(self.particle_count):
            t = ParticlePoint(self.main,self.position.x,self.position.y,self.color)
            self.main.ParticleContainer.append(t)
        #if S then also genetate subnode
        if self.category == "R":
            for i in range(self.RekindleCount):
                t = Rekindle(self.main,self.position.x,self.position.y,self.color)
                self.main.RekindleContainer.append(t)
        #if b then also generate Ring
        if self.category == "S":
            for i in range(1000):
                t = ParticlePoint(self.main,self.position.x,self.position.y,self.color)
                self.main.ParticleContainer.append(t)
            for i in range(4000):
                t = ParticlePoint(self.main,self.position.x,self.position.y,self.color,nerfCount="RING")
                self.main.ParticleContainer.append(t)
        #remove self after bang
        self.main.StageContainer.remove(self)

    #generate thrust
    def thrust(self):
        l = sqrt(self.velocity.x**2 + self.velocity.y**2)
        num = l/10
        n = int(num)
        for i in range(n):
            v = (self.velocity.x,self.velocity.y)
            t = ThrustPoint(self.main,v,self.position.x,self.position.y,self.color)
            self.main.ThrustContainer.append(t)
