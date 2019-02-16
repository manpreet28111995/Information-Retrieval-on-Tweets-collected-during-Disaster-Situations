import regex as re
import time
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
rep = {"A": "", "message": "","mention": "", "must": "","relevant": "", "However": "",".": "","(": "","/": " ",")": "",
       ",": "","Messages": "", "like": "","also": "", "informing": "","would": ""}
rep = dict((re.escape(k), v) for k, v in rep.iteritems())
pattern = re.compile("|".join(rep.keys()))
stop_words = set(stopwords.words('english'))
with open('Unclean Topics.txt', 'r') as myfile:
    data=myfile.read().replace('\n', ' ')
m = re.findall('Narrative:(.+?)</top>', data)
ctr=1
for i in m:
    i=i.rsplit('.',2)[0]
    i = pattern.sub(lambda m: rep[re.escape(m.group(0))], i)
    word_tokens = word_tokenize(str(i))
    filtered_sentence = [w for w in word_tokens if not w in stop_words] 
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    filtered_sentence=list(set(filtered_sentence))
    #print filtered_sentence
    text=' '.join(filtered_sentence)
    print "Query "+str(ctr)
    print text
    ctr=ctr+1
    time.sleep(2)
