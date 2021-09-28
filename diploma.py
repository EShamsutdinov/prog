# программа для расчета курсача/диплома
import math
import os
import colorama


class FurnacePerformance:
    def formulas(self):
        formulalist={
          pass
        }

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
                                             self.salt_sugar,self.yeasts))
        print(self.ind_dict)

    def __init__(self):
        self.whatsbake = input("Какая печь: ")
        self.method = input("Опарный или безопарный способ: ")
        self.bakingtime = input("Время выпечки: ")
        self.wheatflour = input("Пшеничная мука,кг (если нет введите -): ")
        self.ryeflour = input("Ржаная мука,кг (если нет введите -): ")
        self.salt_sugar=input("Кол-во соли и сахара (если нет введите -): ")
        self.yeasts=input("Кол-во дрожжей (если нет введите -): ")
        self.settings()


FurnacePerformance()
