from django.shortcuts import render, HttpResponse

# Create your views here.
import pymysql
import json




def sql():
    text = ''
    db = pymysql.connect('160.238.86.85', 'root', 'yscloud', 'zha')
    cursor = db.cursor()
    sql = 'select content from z_content'
    cursor.execute(sql)
    div = """<marquee  width="auto"  height="auto" direction="left"  behavior="slide"  scrollamount="15"  scrolldelay="30"  loop="1"  height="auto"  bgcolor="black" >
    	<font  face="隶书"  color="white"  size="4">"""
    for i in cursor.fetchall():
        text = div+ '<br>'+ str(i[0]) + "</font></marquee>"+r'</br>' + '\n'+ text
    db.close()
    #滚动样式
    
    #滚动框
    # div = """<DIV align=center
    # style='
    # color: #ffffff;
    # background-color: #000000;
    # border: solid 2px black;
    # width: 120px;
    # height: 200px;
    # overflow: scroll;
    # scrollbar-face-color: #889B9F;
    # scrollbar-shadow-color: #3D5054;
    # scrollbar-highlight-color: #C3D6DA;
    # scrollbar-3dlight-color: #3D5054;
    # scrollbar-darkshadow-color: #85989C;
    # scrollbar-track-color: #95A6AA;
    # scrollbar-arrow-color: #FFD6DA;
    # '>"""
    
    return text


def content(request):
    text = sql()
    return HttpResponse(text)


