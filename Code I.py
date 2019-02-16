import pandas as pd
import csv
import time
df=pd.read_csv("new.csv")
col_1=(df.sort_values("Query 1",ascending=False)).iloc[0:1000,0:1]
col_2=(df.sort_values("Query 2",ascending=False)).iloc[0:1000,0:1]
col_3=(df.sort_values("Query 3",ascending=False)).iloc[0:1000,0:1]
col_4=(df.sort_values("Query 4",ascending=False)).iloc[0:1000,0:1]
col_5=(df.sort_values("Query 5",ascending=False)).iloc[0:1000,0:1]
col_6=(df.sort_values("Query 6",ascending=False)).iloc[0:1000,0:1]
col_7=(df.sort_values("Query 7",ascending=False)).iloc[0:1000,0:1]
c1=col_1.values.T.tolist()[0]
c2=col_2.values.T.tolist()[0]
c3=col_3.values.T.tolist()[0]
c4=col_4.values.T.tolist()[0]
c5=col_5.values.T.tolist()[0]
c6=col_6.values.T.tolist()[0]
c7=col_7.values.T.tolist()[0]
data = pd.read_csv('Qrel.txt', sep=" ", header=None)
q1,q2,q3,q4,q5,q6,q7 = ([] for i in range(7))
for i in range(0,2140):
    if data[0][i]=="FMT1":
        q1.append(data[2][i])
    if data[0][i]=="FMT2":
        q2.append(data[2][i])
    if data[0][i]=="FMT3":
        q3.append(data[2][i])
    if data[0][i]=="FMT4":
        q4.append(data[2][i])
    if data[0][i]=="FMT5":
        q5.append(data[2][i])
    if data[0][i]=="FMT6":
        q6.append(data[2][i])
    if data[0][i]=="FMT7":
        q7.append(data[2][i])
o1=list(set(c1).intersection(q1))
o2=list(set(c2).intersection(q2))
o3=list(set(c3).intersection(q3))
o4=list(set(c4).intersection(q4))
o5=list(set(c5).intersection(q5))
o6=list(set(c6).intersection(q6))
o7=list(set(c7).intersection(q7))
print len(q1),len(o1)
print len(q2),len(o2)
print len(q3),len(o3)
print len(q4),len(o4)
print len(q5),len(o5)
print len(q6),len(o6)
print len(q7),len(o7)
