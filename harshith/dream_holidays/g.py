import pandas as pd

'''print("---------------------------------------------")
print("\t\t list of integers ")
l1 = [1,2,3,4]
s1 = pd.Series(data = l1)
print(s1)

print("---------------------------------------------")
print("\t\t list of strings ")
print()
l2 = ['Jaswanth','Abhi','John', 'Byro']
s2 = pd.Series( l2,['first boy','Second boy ' , 'Third boy','Fourth boy'])
print("No. of the Boy ", "Name")
print(s2)'''

print("---------------------------------------------")
print("\t\t Tuple of integers ")
t1 = (1,2,3,4)
s3 = pd.Series(data = t1 )
print(s3)
'''
print("---------------------------------------------")
print("\t\t Tuple of strings ")
t2 = ('Jaswanth','Abhi','John', 'Byro')
s4 = pd.Series(data = t1 , index=['first boy','Second boy ' , 'Third boy','Fourth boy'] )
print(s4)

print("---------------------------------------------")
print("\t\t  Dictionary of integers ")
d1 = {8:2 , 2:5 , 4:8 }
s5 = pd.Series(data = d1 )
print(s5)

print("---------------------------------------------")
print("\t\t  Dictionary of strings ")
d2 = {"A":"D","B":"E","C":"F"}
s6 = pd.Series(d2)
print(s5)

print("---------------------------------------------")
print("\t\t This is the sample data to refer  ")
sample_data = [1,2,5,6,8,9,4]
sample_index = (0,5,3,8,9,8,6)
s7 = pd.Series(sample_data,sample_index,"int16")
print(s7)

print("---------------------------------------------")
print("\t\t Head and Tail functions ")
print(s7.head(2))
print(s7.tail(2))

print("---------------------------------------------")
print("\t\t Scaler value ")
s7 = pd.Series(3,(1,2,3,4))
print(s7)

print("---------------------------------------------")
print("\t\t MATHEMATICAL OPERATIONS ")
print(s1)
print(s3)
print("\t\t\t THIS IS THE (ADDITION) COMBINATION OF BOTH TOP SERIES")
print(s1+s3)
print("\t\t\t THIS IS THE (SUBTRACTION) COMBINATION OF BOTH TOP SERIES")
print(s7-s3)

print("---------------------------------------------")
print("\t\t  Indexing and Slicing ")

'''