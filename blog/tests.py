#coding:utf-8
from django.test import TestCase
from blog.models import WeiboContent,NineMonthkeys
from numpy.ma.core import ids

# Create your tests here.

# for i in range(5):
#     T = NineMonthkeys.objects.filter(uid=userid,posttime=pt)
# #     tm = int(tm)-1
#     print T
# D = NineMonthkeys.objects.filter(uid=userid)
# for t in D:
#     print t.uid,
# con = NineMonthkeys.objects.filter(posttime=pt).filter(uid=userid)
'''
根据userid 和时间进行好友推荐时，需要处理目标用户的文本信息
'''
userid = '1043325954'
pt = '20150930'
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

'''
对备选集合进行处理 整合成字典形式
Candidateset = {user1:[key1,key2,key3,key4,key5],user2:[key1,key2,key3,key4,key5],...,}
'''
index = int(pt)
Candidateset = {}
candidate_uid = NineMonthkeys.objects.values('uid').distinct()
for info in candidate_uid:
    id = info.values()[0]
    li1=[]
#     print type(id)
    Candidateset[id]=li1
print len(Candidateset.keys())  
# for k,v in Candidateset.items():
#     print k,v

for man in Candidateset.keys():
    for k in range(5):
        candidate_info = NineMonthkeys.objects.filter(posttime=str(index),uid=man)
        index = index - 1
        
        if candidate_info.count()==0:
            Candidateset[man].append(man)
        else:
            for info in candidate_info:
                Candidateset[man].append(info.keywords)
#         for info in candidate_info:
#             if info.keywords:
#                 Candidateset[info.uid].append(info.keywords)
#             else:
#                 Candidateset[info.uid].append(man)

print len(Candidateset.keys())

# for k in Candidateset.values():
#     for w in k:
#         print w
#     print '\n'           
# print Candidateset        
# for k, v in Candidateset.items():
#     print k,
#     for i in v:
#         i,
#     print '\n'

# setuser={uid1:[],uid2:[],uid3:[]}
# for k, v in setuser.items():
#     for keyword in v:
#         for 
print "\n"
'''
计算相似度例子
'''
# result = 0.0
dict1={}
weight = [0.51,0.2638,0.1296,0.0636,0.0329]
# d = ["1#2","2#4","3#5"] 
# a = {2:["1#2#3","2#4#6","3#4"],1:["1#2","2#4",""],3:["1#2#3#4","3#5","3#4"]}
d = targetkey
a = Candidateset
for k,v in a.items(): #k=1,2,3  v=[] v[]  v[]
    result = 0.0
#     print k,v[0]
    for i in range(5):
        for j in range(5):
#             print d[i],v[j]
            jiaoji = set(d[i].split("#")).intersection(set(v[j].split("#")))
            bingji = set(d[i].split("#")).union(set(v[j].split("#")))
#             print len(jiaoji),len(bingji)
            result += weight[i]*weight[j]*(1.0*len(jiaoji)/len(bingji))
#         print "result =",result
    dict1[k]=result
print dict1
