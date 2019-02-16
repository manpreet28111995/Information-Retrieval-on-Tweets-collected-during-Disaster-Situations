import regex as re
import time
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
import json_lines
import time
import re,math
from new import *
import csv
import sys
from collections import Counter
topics=[]
rep = {"A": "", "message": "","mention": "", "must": "","relevant": "", "However": "",".": "","(": "","/": " ",")": "",
       ",": "","Messages": "", "like": "","also": "", "informing": "","would": "","etc":""}
rep = dict((re.escape(k), v) for k, v in rep.iteritems())
pattern = re.compile("|".join(rep.keys()))
stop_words = set(stopwords.words('english'))
with open('Unclean Topics.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
m = re.findall('Narrative:(.+?)</top>', data)
for i in m:
    i=i.rsplit('.',2)[0]
    i = pattern.sub(lambda m: rep[re.escape(m.group(0))],i)
    word_tokens = word_tokenize(str(i))
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    filtered_sentence=list(set(filtered_sentence))
    text=' '.join(filtered_sentence)
    topics.append(text)
    time.sleep(2)
print "Topics in List"
with open('Nepal-earthquake-tweets.jsonl', 'rb') as f:
    file= open('new.csv','wb')
    print "New File Created"
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    w = csv.writer(file)
    w.writerow(['Tweet_id','No of retweets','Query 1','Query 2','Query 3','Query 4','Query 5','Query 6','Query 7'])
    for item in json_lines.reader(f):
        text = str(item[u'text'].encode('utf-8'))
        removed = text.replace("@", "")
        remove = removed.replace("RT", "")
        remo = remove.replace(r'\n', ' ')
        s=str(item[u'id_str'])
        re=str(item[u'retweet_count'])
        remo=str(remo)
        nlist=[]
        remo2=text_to_vector(str(remo))
        for i in topics:
            i2=text_to_vector(str(i))
            nlist.append(get_cosine(i2,remo2))
        w.writerow([s,re,nlist[0],nlist[1],nlist[2],nlist[3],nlist[4],nlist[5],nlist[6]])
        print "Please Wait!!! Work in Progress"

