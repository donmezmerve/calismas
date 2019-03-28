import pandas


def read_file(filename):
    data = pandas.read_csv(filename, sep="\t", header=None)
    result=[]
    for debit,credit in zip(data[2], data[3]):
        debit=float(debit.replace(",","."))
        credit=float(credit.replace(",","."))
        result.append((debit,credit))
       # print(debit,credit)
    return result

def calculate_data(data):
    sum=0
    #sum_debit=0
    #sum_credit=0
    for debit,credit in data:
        sum += debit-credit
        #if debit>credit:
            #print("this account balance is",sum,"(debit)")
       # else:
          #  print ("gh",sum,"credit")
    if sum<0:
        print("this account balance is",abs(sum),"credit")
    else :
        print("this account balance is",abs(sum),"debit")
    return sum
    #sum_debit += data[2]
    #sum_credit += data[3]

data=read_file("Tab SeperatedLedger.txt")
difference=calculate_data(data)


