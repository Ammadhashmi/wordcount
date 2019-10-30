from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
     return render(request,'home.html',{'hithere':'this is me!'})

def count(request):
    fulltext=request.GET['fulltext']
    textcount=fulltext.split()
    worddict={}
    for word in textcount:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sortedwords=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{"textcount":len(textcount),"fulltext":fulltext,"worddict":sortedwords})

def about(request):
    return render(request,'about.html',{})