import random
import math


def myFunction(x1,x2):
    if (x1<=10 and x1>=-10) and (x2<=10 and x2>=-10):
        return (4-2.1*(x1**2)+((x1**4)/3))*(x1**2) + (x1*x2) + (-4+4*(x2**2))*(x2**2)
    else:
        return "ndak bisa"

#def SimulatedAnnealing():
   # solusiSementara  =

def myA(x1):
      if (x1<=10 and x1>=-10) :
        return (4-2.1*(x1**2)+((x1**4)/3))*(x1**2)
      else:
        return "ndak bisa"

def myB(x1,x2):
    if (x1<=10 and x1>=-10) and (x2<=10 and x2>=-10):
        return x1*x2
    else:
        return "ndak bisa"

def myC(x1):
    if (x1<=10 and x1>=-10) :
        return  (-4+4*(x1**2))*(x1**2)
    else:
        return "ndak bisa"

def productionRule(x1,x2):
    if (x1 >= 0 and x2 < 0):
        temp = random.randint(1,3)
    elif (x2 >= 0 and x1 < 0):
        temp = random.randint(4,6)
    elif (x1 > 0 and x2 > 0):
        temp = 7
    elif (x2 < 0 and x1 < 0):
        temp = 8
    else:
        temp = random.randint(1,8)

    if (temp == 1):
        x1 -= random.random()
        x2 += random.random()
        return x1,x2
    elif (temp == 2):
        x1 -= random.random()
        return x1,x2
    elif (temp == 3):
        x2 += random.random()
        return x1,x2
    elif (temp == 4):
        x1 += random.random()
        return x1,x2
    elif (temp == 5):
        x2 -= random.random()
        return x1,x2
    elif (temp == 6):
        x1 += random.random()
        x2 -= random.random()
        return x1,x2
    elif (temp == 7):
        x1 -= random.random()
        x2 -= random.random()
        return x1,x2
    elif (temp == 8):
        x1 += random.random()
        x2 += random.random()
        return x1,x2

def sigmoid(gamma):
    if gamma < 0:
        return 1 - 1 / (1 + math.exp(gamma))
    return 1 / (1 + math.exp(-gamma))

def simmulatedAnnealing(x1,x2):
    literasi = 0
    goalState = -1.03162
    initialState = myFunction(x1,x2)
    if (initialState<=goalState):
        return initialState
    else:
        currentState = initialState
    bestsofar = currentState
    T = 100
    while (currentState>=goalState):
        literasi += 1
        a,b = productionRule(x1,x2)
        newstate = myFunction(a,b)
        deltaE = currentState - newstate
        if (newstate<=goalState):
            return newstate,literasi,a,b
        elif (deltaE>0):
            currentState = newstate
            bestsofar = newstate
        elif (deltaE<0):
            currentState = sigmoid(deltaE)
        T *= 0.00000001
    print "literasi=" + str(literasi)
    return bestsofar,literasi,a,b

def findbestSolutionSA():
    tableResult = []
    tableX = []
    tableY = []
    min = 100
    bestX = 0
    bestY = 0
    stack = []
    for i in range(1,51):
        result,iterasi,optimalx,optimalY = simmulatedAnnealing(0,0)
        tableResult.append(result)
        tableX.append(optimalX)
        tableY.append(optimalY)
        print "Sedang meload data ke-", i

def showResultSA(tableResult,tableX,tableY):
    for j in range(0,50):
        print tableResult[j],tableX[j],tableY[j]
        if (min>tableResult[j]):
            min = tableResult[j]
            bestX = tableX[j]
            bestY = tableY[j]


###Program utama###
result,iterasi,optimalX,optimalY = simmulatedAnnealing(0,0)
#print result
#print "Iterasi = " + str(iterasi)
#print "Optimal x = " + str(optimalX)
#print "Optimal y = " + str(optimalY)


bestX = -0.0906077281389
bestY = 0.712604457597
print "Nilai terkecil fungsi heureustik : ", min
print "Nilai terbaik untuk X : ",bestX
print "Nilai terbaik untuk Y : ",bestY

print myFunction(-0.0906077281389,0.712604457597)