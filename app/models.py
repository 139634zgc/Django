from __future__ import unicode_literals
from django.db import models

# Create your models here.

KIND_CHOICES = (
    ('PY技术', 'PY技术'),
    ('数据库', '数据库'),
    ('经济学', '经济学'),
    ('PY技术2', 'PY技术2'),
    ('数据库2', '数据库2'),
    ('经济学2', '经济学2'),
)


class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20, default='annoymous')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])