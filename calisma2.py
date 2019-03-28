import pandas
import numpy

def read_file(filename):
    data = pandas.read_csv(filename, sep="\t", header=None)
    result=[]
    for entry,leave in zip(data[0], data[1]): #zıp ıkı lıstede aynı anda gezınmemızı saglar
        entry=float(entry)
        if numpy.isnan(leave):
            leave=2018.0
        result.append((entry,leave))
        #print(entry,leave)
    return result
    #print(result)

def calculate_turnover(data):
    sum=0
    for entry,leave in data:
        sum += leave - entry
    avg= sum/ len(data)
    return avg

data=read_file("employees.txt")
avg=calculate_turnover(data)
print("avg turnoever is:"avg)

