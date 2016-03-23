#coding:utf-8
from django.test import TestCase
import re
import sys
# -*- coding: gb18030 -*-   
import string  
import re  
from blog.models import Recommendlist,WeiboContent
import os
import jieba
from jieba import analyse
from Tkconstants import TOP
import numpy as np
from math import pow
import string


reload(sys)
sys.setdefaultencoding('utf-8') 

identify = string.maketrans('', '')
delEStr = string.punctuation + ' ' + string.digits + ' ' + string.letters  #ASCII 标点符号，空格和数字   
delCStr = '#《》（）&%￥#@！{}【】'

# uid="1043325954"
# time_choise="20151231"
# users_keys = {}
# for i in range(5):
#     all_weibo = ""
#     tm = int(time_choise)-i
#     contents = WeiboContent.objects.filter(userid=uid, date__contains=tm)
#     for d in contents:
#         all_weibo = all_weibo + ',' + d.content
#         userid = d.userid
#         date1 = d.date
#     if i==0:
#         users_keys.setdefault(userid, {}) #定义嵌套字典
#     print type(all_weibo.encode('utf-8'))
#     print type(all_weibo.strip().decode('utf-8'))
#     all_weibo = all_weibo.translate(identify, delEStr)
# #     all_weibo = all_weibo.translate(identify, delCStr)
#         
#     stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines()]
#         
#     segs = jieba.cut(all_weibo)
#     all_weibo = ','.join(list(set(segs)-set(stop)))
#     print all_weibo
#           
#     keywords = analyse.extract_tags(all_weibo,topK=3)
#     users_keys[userid][date1] = keywords
#     
# for k,v in users_keys.items():
#     for x,y in v.items():
#         print k,x,y,'\n'
#         for z in y:
#             print z

def key_wordsf(uid, time_choise):
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
    identify = string.maketrans('', '')
    delEStr = string.punctuation + ' ' + string.digits + ' ' + string.letters  #ASCII 标点符号，空格和数字   
    delCStr = '#《》（）&%￥#@！{}【】'
    a=[1,2,3]
    b=[2,3]
    set(a).difference(set(b))   #差集 1
    set(a).intersection(set(b)) #交集 2 3
    set(a).union(set(b))        #并集 1 2 3
    
    users_keys = {}
    
    for i in range(5):
        all_weibo = []
        tm = int(time_choise)-i
        contents=WeiboContent.objects.filter(date__contains=tm)
        for d in contents:
#             print type(d.content.encode('utf-8'))
            all_weibo.append(d.content)
            userid = d.userid
            date1 = d.date
        if i==0:
            users_keys.setdefault(userid, {}) #定义嵌套字典
                   
        stop = [line.strip().decode('utf-8') for line in open('stopword.txt').readlines()]
        all_weibo = [v for v in all_weibo if not str(v).isalpha()]
        all_weibo = ','.join(all_weibo)
        segs = jieba.cut(all_weibo)
        
        all_weibo = ','.join(list(set(segs)-set(stop)))
#         print type(str(all_weibo))
#         all_weibo = all_weibo.translate(identify, delEStr)
#         all_weibo = all_weibo.translate(identify, delCStr)
        
        keywords = analyse.extract_tags(all_weibo,topK=3)
        users_keys[userid][tm] = ','.join(keywords)
    
    for k,v in users_keys.items():
        for x,y in v.items():
            print ("uid:%s,datetime:%s,keyword:%s") % (k,x,y)
    
    
         
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
    return lastresult
        
if __name__=='__main__':
#     d= AHP()
#     print d
    uid1="1043325954"
    time_choise1="20151231"
    key_wordsf(uid1, time_choise1)
























# identify = string.maketrans('', '')   
#   
# delEStr = string.punctuation + ' ' + string.digits +string.letters  #ASCII 标点符号，空格和数字   
# delCStr = '《》（）&%￥#@！{}【】'   
#   
# s = "aaa中华人架共和国   【】abcd1231" 
#   
# s = s.translate(identify, delEStr) #去掉ASCII 标点符号和空格   
# 
# print type(s)
# 
# print s
# if re.findall('[\x80-\xff].', s):    #s为中文   
#    s = s.translate(identify, delCStr)   
#    print s   
# else: #s为英文   
#     print s  