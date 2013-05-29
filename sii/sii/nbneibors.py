	#! /usr/bin/env python3.1
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      student
#
# Created:     03.04.2013 # Copyright:   (c) student 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from tkinter import *
import random
from pprint import pprint
from math import sqrt
from copy import deepcopy


class mdNeighbor:
    debug
    numberpoints = 5
    intervalA = 0
    intervalB=500
    points =[[]]
    classes = [[]]

    def d(self, a,b):
      '''
      нахождение растояния между 2 точками'''
      return sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )

    def classIter(self):
      return 

    def __init__(self):
        #if self.debug:
        #заполняем случаными точками
        self.points = [[(random.randint(self.intervalA, self.intervalB),random.randint(self.intervalA, self.intervalB)) 
        for j in range(self.numberpoints)] for i in range(self.numberpoints)]
        #создаем классы
        self.deepcopy()
        for line in self.points:
          self.classes.append ([])
        self.classes
        #pprint(self.points)
        print(self.numberpoints)

    def creatPoint(self,x,y):
      oval = canv.create_oval(10,10,10,10,width=5,fill="black")




class windows:
    debug = True
    lineColor = "blue"
    bg = "lightblue"
    root=Tk()
    width = 5
    canv = Canvas(root,width=500,height=500,bg="lightblue",
          cursor="pencil")
    oval = canv.create_oval(100,10,100,100,width=5,fill="black")

    storage = [[]]
    def __init__(self):
        if not self.debug:
            self.canv.pack()
            self.root.mainloop()
    def __init__(self, blob):
        assert isinstance(blob.points, object)
        pprint(blob.points)
    

  #def __init__(self, blob):
   # for x in blob.points:
   #   oval = canv.create_oval(10,10,5,20,width=5,fill="black")
    




def main():
    

    blob = mdNeighbor()
    windows(blob)


if __name__ == '__main__':
    main()



def mooove(event):
  canv.move(oval,0,10)
  canv.bind('<Button-1>',mooove)



class controller:
  debug = True
  def __init__(self):
    self.debug=False
    return
  def print(self, points):
    if self.debug:
      points(points)
    return
      

