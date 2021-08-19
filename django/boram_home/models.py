from django.db import models

# Create your models here.

########################################
# 겸증요청과 결과를 저장하기 위한 모델 생성
########################################
class Response(models.Model):
    
    name = models.CharField(max_length=10) # 이름
    gubun = models.IntegerField()          # 연령
    question1 = models.IntegerField()      # 문항1번 답
    question2 = models.IntegerField()      # 문항2번 답
    question3 = models.IntegerField()      # 문항3번 답
    question4 = models.IntegerField()      # 문항4번 답
    question5 = models.IntegerField()      # 문항5번 답
    question6 = models.IntegerField()      # 문항6번 답
    question7 = models.IntegerField()      # 문항7번 답
    question8 = models.IntegerField()      # 문항8번 답
    question9 = models.IntegerField()      # 문항9번 답
    question10 = models.IntegerField()     # 문항10번 답
    kk1 = models.IntegerField()            # 검증결과
    reg_date = models.DateTimeField()      # 요청일시