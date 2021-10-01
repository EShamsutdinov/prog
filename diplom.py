# программа для расчета курсача/диплома
import math
import os
import colorama
import time
class FurnacePerformance:
    def formulas(self):
        self.formula_dead_end=f'P=(N*n*n1*m*60)/{self.baking time}'
        self.formulas_dict=[self.formula_dead_end]

    

    def settings(self=None):
        self.typesofbakes={
            'dead_end':"тупиковая",
            'Other':"other"
        }
        self.whatsbake=whatsbake
        self.ind_dict=[]
        
        self.ind_dict.append((self.whatsbake,self.method,self.bakingtime,
                                             self.wheatflour,
                                             self.ryeflour,
                                             self.salt_sugar,
                                             self.yeasts))


        if self.whatsbake in self.typesofbakes:
           perf=self.formulas_dict[0]

        print(self.ind_dict,perf)


    def __init__(self):
        self.whatsbake = input("Какая печь: ")
        self.method = input("Опарный или безопарный способ: ")
        self.bakingtime = input("Время выпечки: ")
        self.wheatflour = input("Пшеничная мука,кг (если нет введите -): ")
        self.ryeflour = input("Ржаная мука,кг (если нет введите -): ")
        self.salt_sugar=input("Кол-во соли и сахара (если нет введите -): ")
        self.yeasts=input("Кол-во дрожжей (если нет введите -): ")
        self.settings()



if __name__=="__main__":
    FurnacePerformance()
    
