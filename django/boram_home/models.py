from django.db import models

# Create your models here.

########################################
# 겸증요청과 결과를 저장하기 위한 모델 생성
########################################
class Response(models.Model):
    
    name = models.CharField(max_length=10)          # 이름
    gubun = models.IntegerField()                   # 연령
    question1 = models.IntegerField()               # 문항1번 답
    question2 = models.IntegerField()               # 문항2번 답
    question3 = models.IntegerField()               # 문항3번 답
    question4 = models.IntegerField()               # 문항4번 답
    question5 = models.IntegerField()               # 문항5번 답
    question6 = models.IntegerField()               # 문항6번 답
    question7 = models.IntegerField()               # 문항7번 답
    question8 = models.IntegerField()               # 문항8번 답
    question9 = models.IntegerField()               # 문항9번 답
    question10 = models.IntegerField(null=True)     # 문항10번 답(9문항 설문이 존재하기 때문에 null 이 가능합니다.)
    kk1 = models.IntegerField()                     # 검증결과
    reg_date = models.DateTimeField()               # 요청일시


    ##################################
    # question 데이터 설정을 위한 메서드
    ##################################
    def setQuestionData(self, list):
        self.question1 = list[0]
        self.question2 = list[1]
        self.question3 = list[2]
        self.question4 = list[3]
        self.question5 = list[4]
        self.question6 = list[5]
        self.question7 = list[6]
        self.question8 = list[7]
        self.question9 = list[8]
        if len(list) == 10:
            self.question10 = list[9]