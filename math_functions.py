# Y - набор значений Y от X 
# eps - промежуток дискретизации
# const - значение конастанты подъёма

def definite (Y,  eps):    
    sum=0
    for y in Y:
        sum+=eps*y
    return sum

def differentiate (Y, eps):
    DifferedFuncY=[]
    for i in range(1, len(Y)):
        DifferedFuncY.append((Y[i]-Y[i-1])/eps)
    return DifferedFuncY
    
def indefinite (Y,  eps, const):    
    IntegratedFuncY=[const]
    for i in range (1,len(Y)):
        IntegratedFuncY.append(IntegratedFuncY[i-1]+eps*Y[i])
    return IntegratedFuncY