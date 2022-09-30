from django.db import models
from user.models import UserModel

class ContentComment(models.Model):
    class Meta:
        db_table = "comment"

    content = models.ForeignKey(ContentModel, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
