import random

'''generálj 5 véletlen számot
10 és 35 között'''

def veletlen():
    list = []
    '''listában azonos alapú adatok legyenek'''
    i:int=0
    while i < 5:
        szam=random.random()*26+10
        '''lista végéhez fűzöm az aktuális elemet'''
        list.append(szam)
    
        i += 1
    return list
        

listam=veletlen()
'''Írjuk ki egymás alá a lista elemeit'''
def lista_liir(lista):
    for i in range(0,len(lista)-1,1):
        print(f"A lista {i}. eleme: {list[i]}")


lista_liir(listam)

def lista_liir(lista):
    n:int = 0
    while n<len(lista):
        print(f"A lista {i}. eleme: {list[i]}")
    n += 1

