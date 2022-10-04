#content.py models
from django.db import models
from user.models import UserModel

# Create your models here.
class ContentModel(models.Model):
    class Meta:
        db_table = 'content'

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    contents = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ContentComment(models.Model):
    class Meta:
        db_table = 'comment'

    contents = models.ForeignKey(ContentModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ContentModify(models.Model):
    class Meta:
        db_table = 'modify'

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    contents = models.CharField(max_length=256,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
