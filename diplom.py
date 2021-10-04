# программа для расчета курсача/диплома
import math
import os
import colorama
import time

P_furnace=0
N=0
n=0
n1=0
m=0
a=0
b=0
c=0
d=0


class FurnacePerformance:
    def ingredients(self):
        self.whatsbake = input("Какая печь: ")
        self.method = input("Опарный или безопарный способ: ")
        self.bakingtime = input("Время выпечки: ")
        self.wheatflour = input("Пшеничная мука,кг (если нет введите 0): ")
        self.ryeflour = input("Ржаная мука,кг (если нет введите 0): ")
        self.salt=input("Кол-во соли (если нет введите 0): ")
        self.sugar=input("Кол-во сахара (если нет введите 0): ")
        self.yeast=input("Кол-во дрожжей (если нет введите 0): ")
        self.result=input("Выход изделия: ")
    
    def furnace_performance_settings(self):
        N=int(input("N: "))
        n=int(input("n: "))
        n1=int(input("n1: "))
        m=int(input("m: "))


    def settings(self=None):
        self.typesofbakes={
            'dead_end':"тупиковая",
        }
        self.raw_materials_dict = { 
            'flour':self.wheatflour,
            'yeast':self.yeast,
            'ryeflour':self.ryeflour,
            'salt':self.salt,
            'sugar':self.sugar,
            'result':self.result

        }
        self.furnace_settings={
               'N':'',
               'n'='',
               'n1'='',
               'm'=''
                }
        self.furnace_settings['N']=N
        self.furnace_settings['n']=n
        self.furnace_settings['n1']=n1
        self.furnace_settings['m']=m
        
        for self.keys,self.values in self.raw_materials_dict.items():
            print(f'{self.keys} >>> {self.values}')

    def solve_performance(self):
        P_furnace=(N*n*n1*m*60)/int(self.bakingtime)


    def __init__(self):
        self.ingredients()
        self.settings()

        



if __name__=="__main__":
    FurnacePerformance()
    
