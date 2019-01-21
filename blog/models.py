from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100,
                             # choices = (
                             #     ('제목1', '제목1 레이블'),
                             #     ('제목2', '제목2 레이블'),
                             #     ('제목3', '제목3 레이블'),
                             # )
                             verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
