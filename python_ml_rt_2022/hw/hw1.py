import pandas as pd
import numpy as np
from IPython.display import display


data =pd.read_excel("_end_seminar.xlsx", sheet_name="Sheet1")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
#pd.set_option('display.max_colwidth', None)

#print(df.head(5))        вывел 5 первых строк

#def year_2018():

#print(tabl.loc[2])
#def years():    #Сколько было заявок из групп 18-го года набора, а сколько из групп 17-го года?
   # k18 = 0
    #k17 = 0
    #for stud in data["18_group"]:
      #  if stud > 0:
      #     k18 += 1
   # for stud in data["17_group"]:
     #   if stud > 0:
      #      k17 += 1
   # print(k18,k17)


def years():    #Сколько было заявок из групп 18-го года набора, а сколько из групп 17-го года?
    print(data['18_group'].count(), data['17_group'].count())

def empty(): #Есть ли в данных пропуски? В каких колонках? Сколько их в каждой из этих колонок?
    print(data.isna().sum())

def first_time():
    a = []
    for no in data['is_first_time']:
        a.append(no)
    #print(len(data['is_first_time']))
    for i in range(1,len(data['is_first_time'])):
       if str(a[i]) == 'Нет' and str(a[i-1]) == 'Нет':
            str(a[i-1]) = 'Может быть'
       # print(a[i-1], a[i])
    print(data['is_first_time'])




def main():
    #years()
    #empty()
    first_time()

if __name__ =='__main__':
    main()