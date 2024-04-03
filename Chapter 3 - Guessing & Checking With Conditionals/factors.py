def factors(num):
    '''returns a list of factors of num'''
    factorList=[]
    for i in range(1, num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList

def gfc(num1, num2):
    factorList1 = factors(num1)
    factorList2 = factors(num2)
    gfc = 0
    for i, value1 in enumerate(factorList1):
        for j , value2 in enumerate(factorList2):
            if value1 == value2:
                if value1 > gfc:
                    gfc = factorList1[i]
    return gfc
