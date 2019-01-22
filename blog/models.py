import re
from django.forms import ValidationError
from django.db import models


def lnglat_validator(value):
    if not re.match('([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)',value):
        raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목',
                             help_text='포스팅 제목을 입력해주세요. 최대 100자 내외.')
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True,
                              validators=[lnglat_validator],
                              help_text='위도/경도 포맷으로 입력')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
