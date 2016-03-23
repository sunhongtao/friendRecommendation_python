#coding:utf-8
'''
Created on 2016年3月10日

@author: 1811
'''
from blog.models import Recommendlist,WeiboContent
import os
import jieba
from jieba import analyse
from Tkconstants import TOP
import numpy as np
from math import pow
import string
import re
import sys

identify = string.maketrans('', '')
delEStr = string.punctuation + ' ' + string.digits + ' ' + string.letters  #ASCII 标点符号，空格和数字   
delCStr = '#《》（）&%￥#@！{}【】'   


def key_words(uid, time_choise):  
    '''
    根据用户uid和选定的时间，可以求出临近时间的微博
    dict = {user1:[date:"",date:"",date:"",date:"",date:""],
            user2:[key1,key2,key3,key4,key5],
            user3:[key1,key2,key3,key4,key5],
            user4:[key1,key2,key3,key4,key5],
            user5:[key1,key2,key3,key4,key5],
            ...
            }
    '''
    a=[1,2,3]
    b=[2,3]
    set(a).difference(set(b))   #差集 1
    set(a).intersection(set(b)) #交集 2 3
    set(a).union(set(b))        #并集 1 2 3
    
    users_keys = {}
    
    for i in range(5):
        all_weibo = ""
        tm = int(time_choise)-i
        contents=WeiboContent.objects.filter(userid=uid, date__contains=tm)
        for d in contents:
            print type(d.content.encode('utf-8'))
            all_weibo = all_weibo +','+ d.content
            userid = d.userid
            date1 = d.date
        if i==0:
            users_keys.setdefault(userid, {}) #定义嵌套字典
                
        all_weibo = all_weibo.translate(identify, delEStr)
        all_weibo = all_weibo.translate(identify, delCStr) 
        
        stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines()]
        
        segs = jieba.cut(all_weibo)
        all_weibo = ','.join(list(set(segs)-set(stop)))
        print all_weibo
          
        keywords = analyse.extract_tags(all_weibo,topK=3)
        users_keys[userid][date1] = keywords
    
    for k,v in users_keys.items():
        for x,y in v.items():
            print k,x,y,'\n'
            for z in y:
                print z
             
def AHP():
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
        
if __name__=='__main__':
#     AHP()
    uid="1043325954"
    time_choise="20151231"
    key_words(uid, time_choise)
