from tkinter import *
import random
from pprint import pprint
from math import sqrt
from copy import deepcopy

def d(a,b):
    """нахождение растояния между 2 точками
    если а==б => вернуть 0"""
    if a==b:
        return 0
    return sqrt( (a[0]-b[0])**2 + (a[1]-b[1])**2 )


def D(claster1,claster2):
    '''нахождение растояния между 2 кластерами
    если а==б вернуть 0 (проверить это отеднльно)'''
    if claster1==claster2:
        return 0
    distance = 0
    for point1 in claster1:
        for point2 in claster2:
            checkDistance = d(point1,points)
            if checkDistance>distance:
                distance = checkDistance


points = [] #массив  кортежей из точек

pointsNumber = 10
dawnWall = 0
upWall   = 15

clasters = [] # массив кластеров
dMx = [] # матрица растояний


def initPoint():
    '''инициализирует points случайнми точкми'''
    for n in range(pointsNumber):
        points.append((random.randint(dawnWall, upWall), random.randint(dawnWall, upWall)))




def initClasters():
    '''инициализирует clasters сначала 1 к 1'''
    for x in points:
        clasters.append(x)



def makeD():
    '''заполняет матрицу на основе ткущего состояния кластеров'''
    pass


def main():
    '''основной цикл программы, работаем пока кластеров > 2'''
    initPoint()
    initClasters()
    print(points)
    print(clasters)


def xmain():
    '''графический движок скрипта'''
    pass


if __name__ == '__main__':
    main()
