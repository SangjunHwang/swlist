from django.db import models
from datetime import datetime

class Board(models.Model):
    idx=models.AutoField(primary_key=True) #게시물 번호
    writer=models.CharField(null=False,max_length=50) #이름
    title=models.CharField(null=False,max_length=120) #제목
    hit=models.IntegerField(default=0) #조회수
    content=models.TextField(null=False) #본문
    post_date=models.DateTimeField(default=datetime.now, blank=True) #날짜
    filename=models.CharField(null=True, blank=True, default='', max_length=500) #첨부파일 이름
    filesize=models.IntegerField(default=0) #첨부파일 크기
    down=models.IntegerField(default=0) #다운로드 횟수

    def hit_up(self):
        self.hit +=1 #조회수 증가 처리
    def down_up(self):
        self.down +=1 #다운로드 횟수 증가 처리리

class Comment(models.Model):
    idx=models.AutoField(primary_key=True)
    board_idx=models.IntegerField(null=False)
    writer=models.CharField(null=False, max_length=50)
    content=models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now, blank=True)