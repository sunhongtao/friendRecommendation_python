#encoding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.context_processors import request
from blog.models import WeiboContent, NineMonthkeys
from django.template.context import RequestContext
import jieba
import jieba.posseg
from operator import itemgetter
import numpy as np
from blog.tests import weight
from audioop import reverse

try:
    from .analyzer import ChineseAnalyzer
except ImportError:
    pass



# Create your views here.

def show(request):
    return HttpResponse("Hello world!")

def login(req):
    if req.method == 'POST':
        name = req.POST.get('uname', '')
        passwd = req.POST.get('upasswd', '')
#         nm = WeiboContent.objects.filter(userid_exact='%s' %name)
        if passwd=='2':
            return render_to_response('MyFrame.html', {'name':name})
    return render_to_response('login.html', {'document_root':'~/sun/django/mac/blog/templates/images'})

def top(req):
    name = req.GET['id']
    return render_to_response('top.html',{'name':name})

def showContent(request):
    uid = request.GET['id']
    user_con = WeiboContent.objects.filter(userid=uid)
    return render_to_response('showContent.html', {'uid': id, 'userinfo':user_con},context_instance=RequestContext(request))
    
def test(req):
    uid = req.GET['id']
    time_get = req.POST.get('date1')
    recommendlist = {}
    if req.method=='POST':
        print uid,time_get
        recommendlist = recomendfriend(uid,time_get)
        
        recommendlist = sorted(recommendlist.iteritems(), key=lambda d:d[1], reverse=True)

        return render_to_response('test.html',{'id':uid,'date1':time_get,'recommendlist':recommendlist[0:5]})
    return render_to_response('test.html',{'id':uid})

  

def recomendfriend(uid, time_get):
    '''
            进行好友推荐
    '''
    targetUserinfo =getTargetUserInfo(uid, time_get)
    Candidateinfo = GetCandidateUserInfo(time_get)
    weight = GetWeight()
    dict1={}
    d = targetUserinfo
    a = Candidateinfo
    for k,v in a.items():
        result = 0.0
        for i in range(5):
            for j in range(5):
                jiaoji = set(d[i].split("#")).intersection(set(v[j].split("#")))
                bingji = set(d[i].split("#")).union(set(v[j].split("#")))
                result += round(weight[i]*weight[j]*(1.0*len(jiaoji)/len(bingji)), 4)
        dict1[k]=result + 0.5
    return dict1


def getTargetUserInfo(uid, time_get):
    userid = uid
    pt = time_get
    tm = pt
    targetUser = {}
    x = int(pt)
    targetkey=[]
    for k in range(5):
        con1 = NineMonthkeys.objects.filter(posttime=str(x), uid=userid)
        x = x-1
        if not con1:
            targetkey.append(" ")
        for d in con1:
            targetkey.append(d.keywords)
            print con1
    targetUser[userid]=targetkey
    print len(targetkey)
    return targetkey
    
def GetCandidateUserInfo(pt):
    '''
            根据时间信息，获取候选集中的好友信息
    '''
    index = int(pt)
    Candidateset = {}
    candidate_uid = NineMonthkeys.objects.values('uid').distinct()
    for info in candidate_uid:
        id = info.values()[0]
        li1=[]
        Candidateset[id]=li1
    print len(Candidateset.keys())  
    for man in Candidateset.keys():
        for k in range(5):
            candidate_info = NineMonthkeys.objects.filter(posttime=str(index),uid=man)
            index = index - 1
            if candidate_info.count()==0:
                Candidateset[man].append(man)
            else:
                for info in candidate_info:
                    Candidateset[man].append(info.keywords)
    print len(Candidateset.keys())
    return Candidateset

def GetWeight():
    '''
            层次分析法：计算权重
    '''
    last=[]
    lastresult=[]
    mat = np.array([[1,3,5,7,9],
                    [round(1.0*1/3,2),1,3,5,7],
                    [round(1.0*1/5,2),round(1.0*1/3,2),1,3,5],
                    [round(1.0*1/7,2),round(1.0*1/5,2),round(1.0*1/3,2),1,3],
                    [round(1.0*1/9,2),round(1.0*1/7,2),round(1.0*1/5,2),round(1.0*1/3,2),1]
                    ])
    a,b = mat.shape
    for i in range(a):
        result = 1.0
        for j in range(b):
            result = result*mat[i][j]
        d = round(pow(result,1.0*1/5), 2)
        last.append(d)
    for i in range(5):
        lastresult.append(round(1.0*last[i]/sum(last), 2))
    for i in lastresult:
        print "lastresult:", i
    return lastresult

def Semantic(userkey=None):
    '''
    对用户的微博特征词进行语义分析
    '''
    pass

def Emotion(req):
    '''
    对用户进行情感分析
    '''
    pass




