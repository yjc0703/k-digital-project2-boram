from boram.db import DATABASES
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LogisticRegression
import pymysql
import pandas as pd
from .models import *
import datetime

DB = DATABASES['default']

def getLogisticRegression(dm1):

    # DB 에서 데이터 읽어오기
    # db 접속
    conn = pymysql.connect(host = DB['HOST'], port = DB['PORT'], user = DB['USER'], passwd = DB['PASSWORD'], db = DB['NAME'], cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()

    sql = """
    SELECT b.* 
      FROM respondent a
     INNER JOIN response_fit b on a.ID = b.ID 
     WHERE a.DM1 = {}
    """.format(dm1)
    cur.execute(sql)

    result = cur.fetchall()
    df = pd.DataFrame(result)

    # db 연결 종료
    conn.commit()    
    conn.close()

    # feature 와 label 분리
    df_y = df['KK1']
    df_X = df.drop(['ID', 'KK1'], axis=1)

    # 1그룹의 경우 문항이 9개밖에 없으므로 Q3_10 컬럼 제거해주어야 함
    df_X = df_X.drop(['Q3_10'], axis=1)

    # 모델 학습
    lr = LogisticRegression(max_iter=4000)
    lr.fit(df_X.values, df_y.values)

    # 모델 리턴
    return lr

# 구분값(dm1) 기준으로 4개의 모델을 서버 기동과 동시에 생성
lr_1 = getLogisticRegression(1)
lr_2 = getLogisticRegression(2)
lr_3 = getLogisticRegression(3)
lr_4 = getLogisticRegression(4)


# Create your views here.
def index(request):
    return render(request, 'index.html')  


def submit(request):

    gubun = request.POST['gubun']

    # 알고리즘 테스트
    fieldCount = 10
    if gubun == '1':
        lr = lr_1
        fieldCount = 9
    elif gubun == '2':
        lr = lr_2
    elif gubun == '3':
        lr = lr_3
    elif gubun == '4':
        lr = lr_4  

    X = []
    for i in range(1, fieldCount + 1):
        value = request.POST['question' + str(i)]
        X.append(value)
        
    result = lr.predict([X])


    # DB 에 저장
    res = Response()
    res.gubun = gubun
    res.question1 = request.POST['question1']
    res.question2 = request.POST['question2']
    res.question3 = request.POST['question3']
    res.question4 = request.POST['question4']
    res.question5 = request.POST['question5']
    res.question6 = request.POST['question6']
    res.question7 = request.POST['question7']
    res.question8 = request.POST['question8']
    res.question9 = request.POST['question9']
    res.question10 = request.POST['question10']
    res.name = request.POST['name']
    res.reg_date = datetime.datetime.now()
    res.kk1 = result

    res.save()


    # 화면에 과의존 유형을 노출
    return HttpResponse(result)