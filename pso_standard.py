#-*_coding:utf-8 -*-
import random
import copy
import math

optimization_function=int (raw_input('Select the optimization_function:\n'
                                     '1 for Ackley\'s function \n'
                                     '2 for Sphere function\n'
                                     '3 for Rosenbrock function\n'))

if optimization_function==1 or optimization_function==3:
    birds=int(raw_input('Input the number of swarm: '))
    xcount=2
else:
    birds=int(raw_input('Input the number of swarm: '))
    xcount=int(raw_input('Input length of vector: '))

def GenerateRandVec(list):
    if optimization_function==1:
        for i in range(xcount):
            list.append(random.randrange(-5,5))
    if optimization_function==2 or optimization_function==3:
        for i in range(xcount):
            list.append(random.randrange(-100,100))

def CalDis(list): #适用度函数  optimization function
    if optimization_function==1:  #f(0,0)=0
        dis=-20*math.exp(-0.2*math.sqrt(0.5*(list[0]**2+list[1]**2)))\
            -math.exp(0.5*(math.cos(2*math.pi*list[0])+math.cos(2*math.pi*list[1])))+math.exp(1)+20
        return dis
    if optimization_function==2:  #f(0,0,,,,,0)=0
        dis=0.0
        for i in list:
            dis+=i**2
        return dis
    else:                   #f(1,1)=0
        dis=100*(list[1]-list[0]**2)**2+(list[0]-1)**2
        return dis

def FindBirdsMostPos():
    best=CalDis(bestpos[0])
    index=0
    for i in range(birds):
        temp=CalDis(bestpos[i])
        if temp<best:
            best=temp
            index=i
    return bestpos[index]

def NumMulVec(num,list):         #result is in list
    for i in range(len(list)):
        list[i]*=num
    return list

def VecSubVec(list1,list2):   #result is in list1
    for i in range(len(list1)):
        list1[i]-=list2[i]
    return list1

def VecAddVec(list1,list2):      #result is in list1
    for i in range(len(list1)):
        list1[i]+=list2[i]
    return list1

def UpdateSpeed():
    #global speed
    r1=random.random()
    r2=random.random()
    for i in range(birds):

        temp1=NumMulVec(w,speed[i][:]) #wV

        temp2=VecSubVec(bestpos[i][:],pos[i]) # c1*r1*(bestpos[]-pos[])
        temp2=NumMulVec(c1*r1,temp2[:])

        temp1=VecAddVec(temp1[:],temp2)  #wV+c1*r1*(bestpos[]-pos[])

        temp2=VecSubVec(birdsbestpos[:],pos[i])#c2*r2*(bidsbestpos[]-pos[])
        temp2=NumMulVec(c2*r2,temp2[:])

        speed[i]=VecAddVec(temp1,temp2)#wV+c1*r1*(bestpos[]-pos[])+c2*r2*(bidsbestpos[]-pos[])

def UpdatePos():
    global bestpos,birdsbestpos
    for i in range(birds):
        VecAddVec(pos[i],speed[i])
        if CalDis(pos[i])<CalDis(bestpos[i]):
            bestpos[i]=copy.deepcopy(pos[i])
    birdsbestpos=FindBirdsMostPos()


optimal_value=[]
for j in range(30):
    pos=[]  #lists  for position
    speed=[] # lists for speed
    bestpos=[]  # each bird's best position
    birdsbestpos=[] #the best position for all birds
    w=1.0
    c1=2.0
    c2=2.0
    #r1=random.random()
    #r2=random.random()
    for m in range(birds):
        pos.append([])
        speed.append([])
        bestpos.append([])
    for n in range(birds):          #initial all birds' pos,speed
        GenerateRandVec(pos[n])
        GenerateRandVec(speed[n])
        bestpos[n]=copy.deepcopy(pos[n])

    birdsbestpos=FindBirdsMostPos()   #initial birdsbestpos
    for i in range(100):
        UpdateSpeed()
        UpdatePos()
    print 'birdsbestpos as: ',birdsbestpos
    print 'optimal found as',CalDis(birdsbestpos)
    optimal_value.append(CalDis(birdsbestpos))

#for statistics
optimal_avg=sum(optimal_value)/len(optimal_value)
print 'the best optimal found is: ',sorted(optimal_value)[0]
print 'the average optimal found is: ',optimal_avg

temp_sum=0.0
for i in optimal_value:
    temp_sum=temp_sum+(i-optimal_avg)**2
print 'standard deviation of optiaml value: ' ,math.sqrt(temp_sum/len(optimal_value))