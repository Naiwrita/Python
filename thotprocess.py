import nltk
import sys
import string
import re
import nltk.corpus
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import state_union
from nltk.corpus import stopwords
from nltk.text import Text
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from collections import Counter

with open('C:\Program Files (x86)\Python36-32\setnepal.txt','r') as f:
    f1 = f.read()

list = open("C:\Program Files (x86)\Python36-32\setnepal.txt").readlines()
f2=open('C:\Program Files (x86)\Python36-32\pnepalset.txt','w+') 
    
list1 = []

def extract_words(s):
    return [re.sub('^@[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in s.split()]

for i in list:
    counter = 0
    st = str(i)
    #print(i)
    list1 = extract_words(st)
    for j in list1:
        st = str(j)
        #print(j)
        if (counter ==0):
            if (st.startswith('@')):
                counter = counter +1
                continue
            elif(st.startswith('#')):
                for c in st:
                    if (c == '#'):
                        st1=st.lstrip(c)
                        f2.write(st1)
                        f2.write(' ')
                        counter=counter+1
            else:
                f2.write(st)
                f2.write(' ')
                counter = counter +1
        else:
            if(st.startswith('@') | st.startswith('#') | st.startswith('+') | st.startswith('(')):
                for c in st:
                    if ((c == '#') | (c == '@') | (c == '+') | (c == '(')):
                        st1=st.lstrip(c)
                        f2.write(st1)
                        f2.write(' ')
                        break

            elif (st.startswith('http:') |st.startswith('https:')):
                continue
            else:
                f2.write(st)
                f2.write(' ')
    f2.write('\n')
f2.close()

#POS TAG 
datadic = dict()
conjdic = dict()

with open('C:\Program Files (x86)\Python36-32\Test.txt','r') as f:
    f1 = f.read()

list = open("C:\Program Files (x86)\Python36-32\Test.txt").readlines()

list1=[]
listtag = []

counter = 0
c = 0

f3=open('C:\Program Files (x86)\Python36-32\dictionary.txt','a+') 

for i in list:                                          
    list1 = extract_words(i)                
    for j in list1:                                                                  
        del listtag[:]
        if (j.lower() not in datadic):
            for k in list:                                  
                token = word_tokenize(k)
                T = nltk.pos_tag(token)
                for a,b in T:                               
                    if (a.lower() == j.lower()):
                        listtag.append(b)
                tag = Counter(listtag).most_common(1)
                for w in tag:
                   datadic.update({j.lower():w[0]})
    
        print(datadic)
        if ((len(datadic) == 1) & (c == 0)):
            f3=open('C:\Program Files (x86)\Python36-32\dictionary.txt','w+')
            
            for k, v in datadic.items():
                    f3.write(k + '  ' + v)
                    f3.write('\n')
            datadic.clear()
            f3.close()
            c = 1

        elif(len(datadic) == 100):
            f3=open('C:\Program Files (x86)\Python36-32\dictionary.txt','a+')
            for k, v in datadic.items():
                f3.write(k + '  ' + v)
                f3.write('\n')
            datadic.clear()
            f3.close()
        
 
with open('C:\Program Files (x86)\Python36-32\dabi.txt','r') as f3:
    f12 = f3.read()

list = open("C:\Program Files (x86)\Python36-32\dabi.txt").readlines()

with open('C:\Program Files (x86)\Python36-32\dictionary.txt','r') as f:
    f1 = f.read()

list1 = open("C:\Program Files (x86)\Python36-32\dictionary.txt").readlines()
fpos = open('C:\Program Files (x86)\Python36-32\inputpos.txt', 'a+' )

listpos = []
c =0
v = 0
for i in list:
    st = str(i)
    j = re.sub('[^A-Za-z]+', '  ', i)
    k = extract_words(j)
    for q in k:
        qstr = str(q)
        for w in list1:
            st = str(w)
            k1 = extract_words(w)
            k1str = str(k1[0])
            if(qstr.lower() == k1str):
                c = 1
                t = k1[1]
        if(c == 1):
            listpos.append((qstr,t))
            c = 0
        if (v ==0):
            v = 1
            fpos = open('C:\Program Files (x86)\Python36-32\inputpos.txt', 'w+' )
            fpos.write(listpos)
            fpos.write('\n')
    else:
        fpos = open('C:\Program Files (x86)\Python36-32\inputpos.txt', 'a+' )
        fpos.write(listpos)
        fpos.write('\n')
        
    listpos.clear()
fpos.close()            



  
    
