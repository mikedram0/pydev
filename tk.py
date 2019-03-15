import tkinter as tk
import random
import time

top = tk.Tk()
canv=tk.Canvas(top, bg="white", height=250, width=300)
list1=[]

class coll_obj:
    def __init__(self,radius,x,y,vx,vy):
        self.radius=radius
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
	
    def draw(self):
        c = canv.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius)
    def move(self):
        self.x += self.vx
        self.y += self.vy
    def collision(self):
        if self.x  > 300:
            self.x = 300 
            self.vx *= -1
        if self.x < 0:
            self.x = 0
            self.vx *= -1
        if self.y > 250:
            self.y = 250
            self.vy *= -1
        if self.y < 0:
            self.y = 0
            self.vy *= -1
            


for circle in range(1):
    circle = coll_obj(random.randint(25,50),random.randint(0,300),random.randint(0,250),5,2)
    circle.draw()
    list1.append(circle)



while(1):
    canv.delete("all")
    list1[0].move()
    list1[0].collision()
    list1[0].draw()
    time.sleep(0.01)
    canv.pack()
    top.update()
    #top.mainloop()
