import pandas as pd
import csv
import time
out=[500]
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
df=pd.read_csv("new.csv")
sum=0
for i in out:
    col_1=(df.sort_values("Query 1",ascending=False)).iloc[0:i,0:1]
    c1=col_1.values.T.tolist()[0]
    o1=list(set(c1).intersection(q1))
    precision=(float(len(o1)))/float(i)
    recall= (float(len(o1)))/(float(len(q1)))
    print "For 500"
    #print "precision for Query 1 is",precision
    print "recall for Query 1 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c1):
        if p in q1 and p not in c1[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q1:
        print "0.0"
    ap_1=score/len(q1)
    #print "Average Precision for Query 1 is ",ap_1

    col_2=(df.sort_values("Query 2",ascending=False)).iloc[0:i,0:1]
    c2=col_2.values.T.tolist()[0]
    o2=list(set(c2).intersection(q2))
    precision=(float(len(o2)))/float(i)
    recall= (float(len(o2)))/(float(len(q2)))
    #print "precision for Query 2 is",precision
    print "recall for Query 2 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c2):
        if p in q2 and p not in c2[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q2:
        print "0.0"
    ap_2=score/len(q2)
    #print "Average Precision for Query 2 is ",ap_2

    col_3=(df.sort_values("Query 3",ascending=False)).iloc[0:i,0:1]
    c3=col_3.values.T.tolist()[0]
    o3=list(set(c3).intersection(q3))
    precision=(float(len(o3)))/float(i)
    recall= (float(len(o3)))/(float(len(q3)))
    #print "precision for Query 3 is",precision
    print  "recall for Query 3 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c3):
        if p in q3 and p not in c3[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q3:
        print "0.0"
    ap_3=score/len(q3)
    #print "Average Precision for Query 3 is ",ap_3    

    col_4=(df.sort_values("Query 4",ascending=False)).iloc[0:i,0:1]
    c4=col_4.values.T.tolist()[0]
    o4=list(set(c4).intersection(q4))
    precision=(float(len(o4)))/float(i)
    recall= (float(len(o4)))/(float(len(q4)))
    #print "precision for Query 4 is",precision
    print "recall for Query 4 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c4):
        if p in q4 and p not in c4[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q4:
        print "0.0"
    ap_4=score/len(q4)
    #print "Average Precision for Query 4 is ",ap_4

    col_5=(df.sort_values("Query 5",ascending=False)).iloc[0:i,0:1]
    c5=col_5.values.T.tolist()[0]
    o5=list(set(c5).intersection(q5))
    precision=(float(len(o5)))/float(i)
    recall= (float(len(o5)))/(float(len(q5)))
    #print "precision for Query 5 is",precision
    print "recall for Query 5 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c5):
        if p in q5 and p not in c5[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q5:
        print "0.0"
    ap_5=score/len(q5)
    #print "Average Precision for Query 5 is ",ap_5

    col_6=(df.sort_values("Query 6",ascending=False)).iloc[0:i,0:1]
    c6=col_6.values.T.tolist()[0]
    o6=list(set(c6).intersection(q6))
    precision=(float(len(o6)))/float(i)
    recall= (float(len(o6)))/(float(len(q6)))
    #print "precision for Query 6 is",precision
    print "recall for Query 6 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c6):
        if p in q6 and p not in c6[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q6:
        print "0.0"
    ap_6=score/len(q6)
    #print "Average Precision for Query 6 is ",ap_6

    col_7=(df.sort_values("Query 7",ascending=False)).iloc[0:i,0:1]
    c7=col_7.values.T.tolist()[0]
    o7=list(set(c7).intersection(q7))
    precision=(float(len(o7)))/float(i)
    recall= (float(len(o7)))/(float(len(q7)))
    #print "precision for Query 7 is",precision
    print "recall for Query 7 is",recall
    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(c7):
        if p in q7 and p not in c7[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)
    if not q7:
        print "0.0"
    ap_7=score/len(q7)
    #print "Average Precision for Query 7 is ",ap_7
    ma=(ap_1+ap_2+ap_3+ap_4+ap_5+ap_6+ap_7)/7
    #print "Mean Average Precision ",ma
