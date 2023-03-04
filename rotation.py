from utility import *
import pygame,random
from math import sqrt,cos,sin,pi
vec = pygame.math.Vector2
from rorationParticle import *

class Rotation():
    def __init__(self,main,x,y,color):
        self.main = main
        self.position = vec(x,y)
        self.velocity = vec(0,0).rotate(0)
        self.acceleration = vec(0,0)
        #number of particles emmited
        self.particle_count = 50
        #random color sequence 
        # self.colour = random.choice(GRADIENDTS)
        self.colour = color
        #time of birth as a reference
        self.birthTime = pygame.time.get_ticks()
        #time in millisecond to die
        self.lifespan = 7000
        #initail rotation = 0 degrees
        self.rotation = 0
        #dR is by how much degrees will the spinner be rotated each time
        self.dR = 16
        #self.size is Radius of SpinnerBody
        self.size=5
        #play sound
        EXPLOSION_SOUNDS[0].play()

    def draw(self):
        #draw a circle with the specified colour and radius in the given position 
        pygame.draw.circle(self.main.screen,self.colour,(int(self.position.x),int(self.position.y)),self.size)

    
    def update(self):
        #if survived more than lifespan then kill
        now = pygame.time.get_ticks()
        if now-self.birthTime > self.lifespan:
            self.main.RotationContainer.remove(self)
        #rotate
        self.rotate()
        #calcuating X and Y spwan position of 4 particles each 90 degrees apart
        Xoffset1 = self.position.x + self.size*sin(self.rotation*pi/180)
        Yoffset1 = self.position.y - self.size*cos(self.rotation*pi/180)
        Xoffset2 = self.position.x + self.size*sin((self.rotation+180)*pi/180)
        Yoffset2 = self.position.y - self.size*cos((self.rotation+180)*pi/180)
        Xoffset3 = self.position.x + self.size*sin((self.rotation+90)*pi/180)
        Yoffset3 = self.position.y - self.size*cos((self.rotation+90)*pi/180)
        Xoffset4 = self.position.x + self.size*sin((self.rotation-90)*pi/180)
        Yoffset4 = self.position.y - self.size*cos((self.rotation-90)*pi/180)
        for i in range(self.particle_count):
            t1 = RorationParticle(self.main,Xoffset1,Yoffset1,self.colour,self.rotation)
            t2 = RorationParticle(self.main,Xoffset2,Yoffset2,self.colour,self.rotation+180)
            t3 = RorationParticle(self.main,Xoffset3,Yoffset3,self.colour,self.rotation+90)
            t4 = RorationParticle(self.main,Xoffset4,Yoffset4,self.colour,self.rotation-90)
            self.main.RotationContainer.append(t1)
            self.main.RotationContainer.append(t2)
            self.main.RotationContainer.append(t3)
            self.main.RotationContainer.append(t4)

    def rotate(self):
        #increases rotation value each frame
        self.rotation += self.dR

