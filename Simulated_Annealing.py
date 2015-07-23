#-*- coding:utf-8 -*-
__author__ = 'carl'
##########################
# DATE:20150723
# TSP problem
##########################
import math
class City:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceTo(self,city):
        xDistance=abs(self.x-city.x)
        yDistance=abs(self.y-city.y)
        distance=math.sqrt(xDistance**2+yDistance**2)
        return  distance
    def toString(self):
        return str(self.x)+','+str(self.y)

class Tour:
    def __init__(self,tour):
        self.tour=tour
    def generateIndividual(self):


class SimulatedAnnealing:
