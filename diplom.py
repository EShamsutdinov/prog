# программа для расчета курсача/диплома
import math
import os
import colorama
import time

P_furnace=0



class FurnacePerformance: #FIXME: fix this class
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
        self.N=int(input("N: "))
        self.n=int(input("n: "))
        self.n1=int(input("n1: "))
        self.m=float(input("m: "))


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
        
        self.furnace_performance_settings()

        self.furnace_settings={
               'N':'n',
               'n':'n',
               'n1':'n',
               'm':'n'
                }
        self.furnace_settings['N']=self.N
        self.furnace_settings['n']=self.n
        self.furnace_settings['n1']=self.n1
        self.furnace_settings['m']=self.m
        
        for self.keys,self.values in self.raw_materials_dict.items():
            print(f'{self.keys} >>> {self.values}')
        for self.keys,self.values in self.furnace_settings.items():
            print(f'{self.keys} >>> {self.values}')

        P_furnace=(self.N*self.n*self.n1*self.m*60)/int(self.bakingtime)
        print("Производительность тупиковой печи равна", P_furnace)

    def __init__(self):
        self.ingredients()
        self.settings()
        

        



if __name__=="__main__":
    FurnacePerformance()