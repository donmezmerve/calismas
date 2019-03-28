import pandas
import numpy


def read_file(filename): # fonksıyon tanımle
    data = pandas.read_csv(filename, delim_whitespace=True) #data dıye degıskene kaydettık 
    temp_list=numpy.asarray(data['Temperature']) #dosya formatını gormek ıcın
    return temp_list

def calculate_costs(temp): # bır tane data poınt alacak o yuzden temp dedık
    heating_cost= 0 # heatıng cost olmayabılır
    if temp<8 :
        heating_cost= 8-temp
    cooling_cost=0
    if temp>16:
        cooling_cost= temp-16
    #print(temp,heating_cost, cooling_cost)
    return (heating_cost, cooling_cost)

def calculate_avg(temp_list):
    total_heating_cost=0 #toplu dereceler
    total_cooling_cost=0
    for temp in temp_list:
        cost1,cost2=calculate_costs(temp)
        total_heating_cost += cost1
        total_cooling_cost += cost2
    nyears= 2018-1951 +1
    return (total_heating_cost/nyears, total_cooling_cost/nyears)


#Read File
temp_list=read_file("Schiphol.txt")
#for temp in temp_list:
#    calculate_costs(temp) #forun ıcıne yazdıgını paranteze yaz
avg_heating,avg_cooling = calculate_avg(temp_list)
print("heating:" , avg_heating, "cooling:", avg_cooling)