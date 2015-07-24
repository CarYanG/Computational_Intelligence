#-*- coding:utf-8 -*-
__author__ = 'carl'
##########################
# DATE:20150723
# TSP problem
##########################
import math
import random
class City:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distanceTo(self,city):
        xDistance=abs(self.x-city.x)
        yDistance=abs(self.y-city.y)
        distance = math.sqrt(xDistance**2+yDistance**2)
        return distance
    def toString(self):
        return str(self.x)+','+str(self.y)

class Tour:   #一个tour即一条路线（一个解决方案）
    def __init__(self,tour=None):
        if tour is not None:
            self.tour =[]
            for item in tour:
                self.tour.append(item)
    def generateIndividual(self,citynum,city_list):
        self.tour = []
        for i in range(citynum):
            self.tour.append(city_list[i])
        random.shuffle(self.tour)

    def getDistance(self):
        tourDistance = 0.0
        for i in range(len(self.tour)):
            fromCity = self.tour[i]
            if i+1<len(self.tour):
                destinationCity=self.tour[i+1]
            else:
                destinationCity=self.tour[0]
            tourDistance += fromCity.distanceTo(destinationCity)
        return tourDistance

    def toString(self):
        geneString = "|"
        for i in range(len(self.tour)):
            geneString += str(self.tour[i].toString())+"|"
        return geneString

def acceptanceProbability(energy,newEnergy,temperature):
    if (newEnergy < energy):
        return 1.0
    else:
        return math.exp(float((energy - newEnergy) / temperature))

def SimulatedAnnealing(citynum,city_list):
    temp=10000.0   #初始化温度
    coolingRate=0.003  #冷却概率

    currentSolution=Tour()
    currentSolution.generateIndividual(citynum,city_list)
    print "Initial solution distance: ",currentSolution.getDistance()

    bestSolution=Tour(currentSolution.tour)
    while(temp>1):
        newSolution=Tour(currentSolution.tour)
        #获取随机位置
        random_pos1=random.randint(0,len(newSolution.tour)-1)
        random_pos2=random.randint(0,len(newSolution.tour)-1)
        #交换
        swapcity1=newSolution.tour[random_pos1]
        swapcity2=newSolution.tour[random_pos2]
        newSolution.tour[random_pos1]=swapcity2
        newSolution.tour[random_pos2]=swapcity1

        currentEnergy=currentSolution.getDistance()
        newEnergy=newSolution.getDistance()

        #决定是否接受新的方案
        if(acceptanceProbability(currentEnergy,newEnergy,temp)>random.random()):
            currentSolution=Tour(newSolution.tour)

        #记录找到的最优方案
        if(currentSolution.getDistance()<bestSolution.getDistance()):
            bestSolution=Tour(currentSolution.tour)

        # 冷却
        temp*=(1-coolingRate)
    return bestSolution

def init():
    city_list=[City(60,200),City(180,200),City(80,180),City(140,180),City(20,160),City(100,160),City(200,160),City(140,140),City(40,120)
                ,City(100, 120),City(180,100), City(60,80),City(120, 80),City(180,60),City(20,40), City(100,40),City(200, 40),City(20,20)
                ,City(60,20),City(160,20)]
    return city_list

city_list=init()
bestSolution=SimulatedAnnealing(len(city_list),city_list)
print "Final solution distance: ",bestSolution.getDistance()
print "Tour: ",bestSolution.toString()

