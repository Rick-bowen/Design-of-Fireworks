import pygame,os,time,random
from particle import *
from utility import *
# import cv2
import numpy
from PIL import Image as im
import threading
import tkinter as tk
from tkinter import *
import easygui as g
from root import *
from fountain import *
from rotation import *
from buttonve import *
from design import *
import subprocess
# from video_audio_cap import VideoCapThread,FFmpegThread,SoundRecThread

pygame.init()
class Main():
    ''' main class that controls the entire programm '''
    def __init__(self):
        #主窗口
        self.WIDTH = 1200
        self.HEIGHT = 900
        self.TITLE = "Fireworks!!"
        #副窗口
        self.width = 0
        self.height = 0
        self.model = 0
        #height of canvas for fireworks
        self.canvasHeight = 900
        self.FPS = 30
        self.color = (0,0,0)
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.img = pygame.image.load("image/bg.jfif").convert_alpha()
        self.bg_img = pygame.transform.scale(self.img, (1200,900))
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.otp = False
        self.play = False
        self.on = False
        #clickstate is index of current firework
        self.clickState = 1
        self.run()




    
    def run(self):
        self.isPlaying = True
        # these groups will hold add objects
        self.StageContainer = []
        self.ParticleContainer = []
        self.ThrustContainer = []
        self.RekindleContainer = []
        self.FountainContainer = []
        self.RotationContainer = []
        # self.Bottons = []
        self.FireworkContainer = []

        while self.isPlaying:
            self.clock.tick(self.FPS)
            self.dt = self.clock.tick(self.FPS)/1000

            # self.ready()

            self.createButtons()
            self.Btn1.clicked = True
            self.events()
            self.update()
            self.draw()




    def ready(self):
        if self.play and not self.otp:
            count = 1
            # self.spwan(count)
            self.play = False
            


    def origin(self,count,x,y,d,t,c):

        for i in range(count):
            temp = random.choice([4,6])
            EXPLOSION_SOUNDS[temp].play()
            t = Root(self,x,y,d,t,c)
            self.StageContainer.append(t)
    
    def checkBtnState(self):
        # checks btn state
        if self.clickState==1:
            self.Btn1.clicked = True
        if self.clickState==2:
            self.Btn2.clicked = True
        # if self.clickState==3:
        #     self.Btn3.clicked = True
        # if self.clickState==4:
        #     self.Btn4.clicked = True
        # if self.clickState==5:
        #     self.Btn5.clicked = True
        # if self.clickState==6:
        #     self.Btn5.clicked = True

    def resetClick(self):
        #resets click 
        self.Btn1.clicked = False
        self.Btn2.clicked = False
        # self.Btn3.clicked = False
        # self.Btn4.clicked = False
        # self.Btn5.clicked = False
        # self.Btn6.clicked = False
        
    def createButtons(self):
        self.Btn1 = Buttonve(self, self.screen, 300, 835, 290, 60, RED, "design of fireworks")
        self.Btn2 = Buttonve(self, self.screen, 610, 835, 290, 60, ORANGECORAL, "set off fireworks")
        # self.Btn1 = Buttonve(self,self.screen,5,600,114,100,RED,"Rocket 1")
        # self.Btn2 = Buttonve(self,self.screen,124,600,114,100,ORANGECORAL,"Rocket 2")
        # self.Btn3 = Buttonve(self,self.screen,243,600,114,100,YELLOW,"Rocket 3")
        # self.Btn4 = Buttonve(self,self.screen,362,600,114,100,GREEN,"Fountain")
        # self.Btn5 = Buttonve(self,self.screen,481,600,114,100,BLUE," Spinner")
        # self.Btn6 = Button(self,self.screen,5,495,114,100,PURPINE,"design ")

    def events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.isPlaying:
                    self.isPlaying = False
                self.isRunning = False
            # if event.type == pygame.KEYDOWN:
            #     self.play = True
            #mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1 :
                mouse_x, mouse_y = event.pos
                #handling click for btns
                if mouse_y>800 and mouse_y<900:
                    if mouse_x>300 and mouse_x<590:
                        self.clickState =1
                        # self.fireworks_num = g.integerbox('您想设计几款烟花？请输入1-99的数字！（一款烟花设计完成点击保存关闭窗口会再次打开设计窗口）','设计烟花个数',lowerbound=1)
                        win = Tk()
                        win.title('烟花设计窗口')
                        win.geometry('400x400+100+100')
                        win.resizable(0, 0)
                        d = Design(win,self)

                        def callback(event):
                            win.update()
                            x,y =win.winfo_x(),win.winfo_y()
                            m_x,m_y = event.x_root-x,event.y_root-y
                            #print("当前位置：",m_x,m_y)
                            if m_y>365 and m_y<380:
                                if m_x>10 and m_x<85:
                                    g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(
                                        self.FireworkContainer[0].color, self.FireworkContainer[0].height,
                                        self.FireworkContainer[0].width, self.FireworkContainer[0].model)),
                                             title='显示烟花信息')
                                if m_x>92 and m_x<167:
                                    g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(
                                        self.FireworkContainer[1].color, self.FireworkContainer[1].height,
                                        self.FireworkContainer[1].width, self.FireworkContainer[1].model)),
                                        title='显示烟花信息')
                                if m_x>174 and m_x<249:
                                    g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(
                                        self.FireworkContainer[2].color, self.FireworkContainer[2].height,
                                        self.FireworkContainer[2].width, self.FireworkContainer[2].model)),
                                        title='显示烟花信息')
                                if m_x>256 and m_x<331:
                                    g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(
                                        self.FireworkContainer[3].color, self.FireworkContainer[3].height,
                                        self.FireworkContainer[3].width, self.FireworkContainer[3].model)),
                                        title='显示烟花信息')
                                if m_x > 338 and m_x < 413:
                                    g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(
                                        self.FireworkContainer[4].color, self.FireworkContainer[4].height,
                                        self.FireworkContainer[4].width, self.FireworkContainer[4].model)),
                                        title='显示烟花信息')
                                if m_x > 420 and m_x < 495:
                                    g.msgbox(msg=('混合颜色:{:}\n\n烟花燃放高度:{}\n\n烟花燃放位置:{}\n\n烟花爆炸样式:{}'.format(
                                        self.FireworkContainer[5].color, self.FireworkContainer[5].height,
                                        self.FireworkContainer[5].width, self.FireworkContainer[5].model)),
                                        title='显示烟花信息')

                        win.bind("<ButtonRelease-1>",callback)
                        win.mainloop()
                        # g.msgbox('所有烟花设计完成啦！')



                    if mouse_x > 610 and mouse_x < 900:
                        self.clickState = 2
                        for i in self.FireworkContainer:
                            self.color = i.color
                            self.width = i.width
                            self.height = i.height
                            self.model = i.model

                            if self.model == 'Common':
                                self.origin(1,self.width,self.WIDTH+100,self.height,"C",self.color)
                            if self.model == 'Rekindle':
                                self.origin(1,self.width,self.WIDTH+100,self.height,"R",self.color)
                            if self.model == 'Sunflower':
                                self.origin(1,self.width,self.WIDTH+100,self.height,"S",self.color)
                            if self.model == 'Fountain':
                                t = Fountain(self,self.width,self.color)
                                self.FountainContainer.append(t)
                            if self.model == 'Rotation':
                                t = Rotation(self,self.width,self.canvasHeight-self.height,self.color)
                                self.RotationContainer.append(t)
                            # pygame.time.wait(5000)





    def update(self):
        #resetclick
        self.resetClick()
        #check for btn state
        self.checkBtnState()
        #update each group
        for i in self.StageContainer:
            i.update()
        for i in self.ParticleContainer:
            i.update()
        for i in self.ThrustContainer:
            i.update()
        for i in self.RekindleContainer:
            i.update()
        for i in self.FountainContainer:
            i.update()
        for i in self.RotationContainer:
            i.update()
        # update each btn
        self.Btn1.update()
        self.Btn2.update()
        # self.Btn3.update()
        # self.Btn4.update()
        # self.Btn5.update()

    def draw(self):
        self.screen.blit(self.bg_img, (0, 0))
        # self.screen.fill(BACKGROUND)
        #draw each groups

        for i in self.StageContainer:
            i.draw()
        for i in self.ParticleContainer:
            i.draw()
        for i in self.ThrustContainer:
            i.draw()
        for i in self.RekindleContainer:
            i.draw()
        for i in self.FountainContainer:
            i.draw()
        for i in self.RotationContainer:
            i.draw()


        #draw background for bts
        #pygame.draw.rect(self.screen,(25,25,25),(0,800,1200,100))

        # draw each btns
        self.Btn1.draw()
        self.Btn2.draw()
        # self.Btn3.draw()
        # self.Btn4.draw()
        # self.Btn5.draw()
        # self.Btn6.draw()
        pygame.display.update()






if __name__ == "__main__":
    # output_path = './shipin/'
    # avi_file = output_path + 'tmp.avi'
    # wav_file = output_path + 'tmp.wav'
    # t1 = VideoCapThread(avi_file)
    # t2 = SoundRecThread(wav_file)
    # t1.start()
    # t2.start()
    temp = Main()
    pygame.quit()
    pygame.display.quit()
    # t1.stoprecord()
    # t2.stoprecord()
    # output_path = './shipin/'
    # mp4_file = output_path + 'result.mp4'
    # v = FFmpegThread(avi_file, wav_file, mp4_file)
    # v.run()


