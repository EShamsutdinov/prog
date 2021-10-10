import os
import time

FURNACE_TYPE=input("Какая печь: ")
N=int(input("Количество рабочих люлек в печи, шт: "))
B=int(input("Длина люльки печи,мм : "))
L=int(input("Длина листа,мм: "))
a=int(input("Зазор между изделиями, мм: "))
m=float(input("Масса изделия,кг: "))
B1=int(input("Ширина изделия, мм: "))
l1=int(input("Длина изделия, мм: "))
tbake=int(input("Время выпечки, мин: "))
baking_time_on_schedule=input("Продолжительность выпечки по графику, кг: ")


class Diploma():
    '''Этот класс отвечает за расчет курсовой и дипломной работы по хлебу'''

    def furnace_productivity(self=None):
        '''Расчет производительности печи и суточной мощности линии'''
        self.sheets_on_cradle=(B-a)/(l+a)
        self.row_in_lenght_of_sheet=(L-a)/(b+a)
        self.row_in_width_of_sheet=(B1-a)/(l1+a)
        self.hmproducts_on_sheet=self.row_in_lenght_of_sheet*self.row_in_width_of_sheet
        

        self.furnace_hourly_productivity=(N*n*n1*m*60)/tbake
        self.daily_line_power=self.furnace_hourly_productivity*baking_time_on_schedule

        print(self.furnace_hourly_productivity, 'кг\ч')
        print(self.daily_line_power)
        
        


    def calculation_raw_materials(self=None):
        '''Расчет сырья'''
        pass
    
    
    def calculation_and_selection_equipment(self=None):
        '''Расчет оборудования и его подбор'''
        pass

    def package_calculation(self=None):
        '''Расчет упаковки'''
        pass

    
    def __init__(self):
        time.sleep(0.2)


Diploma.furnace_productivity()
