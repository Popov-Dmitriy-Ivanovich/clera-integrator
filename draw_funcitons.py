import matplotlib.pyplot as plt
from math import sin   #посмотреть на синус можно
from math_functions import differentiate,indefinite

def draw_chart(x1,y1,x2,y2,k): 
    s=1# размер кругов, при достаточно малом шаге его хватает и 1
    c1='red' # цвета кругов
    c2='blue'

    fig, ax = plt.subplots() # здесь задаётся область работы, не трогать
    ax.scatter(x1, y1, s, c1) #рисование исходного уравнения
    ax.scatter(x2, y2, s, c2) #рисование проинтегрированного

    data=[0,0,0,0,0,0]
    LenHor=2*( max( round(max(y1)), round(max(y2)), round(abs(min(y1))), round(abs(min(y2))) ) )+1
    LenVert=2*( max( round(max(x1)), round(max(x2)), round(abs(min(x1))), round(abs(min(x2))) ) )+1
    ax.eventplot(data, colors='black', lineoffsets=0, linelengths = LenVert, orientation='vertical')
    ax.eventplot(data, colors='black', lineoffsets=0, linelengths = LenHor, orientation='horizontal')
    plt.show()  #показывает итоговый результат

def Graphic (InitialFuncY, FuncX, eps, C):
    IndefiniteIntY=indefinite(InitialFuncY,   eps, C)
    draw_chart(FuncX,InitialFuncY,FuncX, IndefiniteIntY, eps)

def Dif_Graphic(InitialFuncY, FuncX, eps, C):
    DifferentiatedFuncY=differentiate(InitialFuncY, eps)
    draw_chart(FuncX,InitialFuncY,FuncX[1:],DifferentiatedFuncY,eps)
