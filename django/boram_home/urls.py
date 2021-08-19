# boram_home > urls.py

from django.urls import path
from . import views

urlpatterns = [
    #########
    # 메인화면
    #########
    path('', views.index),

    #####################################
    # 제출된 설문결과를 학습된 검증기에 검증
    #####################################
    path('submit', views.submit)
]
