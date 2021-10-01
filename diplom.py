# программа для расчета курсача/диплома
import math
import os
import colorama
import time
class FurnacePerformance:
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
    def solve_performance(self):
        P_furnace=(self.N*self.n*self.n1*self.m*60)/int(self.bakingtime)
    def __init__(self):
        self.whatsbake = input("Какая печь: ")
        self.method = input("Опарный или безопарный способ: ")
        self.bakingtime = input("Время выпечки: ")
        self.wheatflour = input("Пшеничная мука,кг (если нет введите -): ")
        self.ryeflour = input("Ржаная мука,кг (если нет введите -): ")
        self.salt=input("Кол-во соли (если нет введите -): ")
        self.sugar=input("Кол-во сахара (если нет введите -): ")
        self.yeast=input("Кол-во дрожжей (если нет введите -): ")
        self.result=input("Выход изделия: ")
        self.settings()

        



if __name__=="__main__":
    FurnacePerformance()
    
