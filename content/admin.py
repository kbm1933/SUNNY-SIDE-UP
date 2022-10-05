from django.contrib import admin
from .models import ContentModel
# Register your models here.

#photo라는 테이블이 갭ㄹ로 존재하는 것으로 나타내지 말고,
#content테이블의 각 레코드 안에 해당하는 것으로 나타내주어야함

# #photo 클래스를 inline으로 나타낸다.
# class PhotoInline(admin.TabularInline):
#     model = Photo

# #content클래스는 해당하는 photo 객체를 리스트로 관리
# class ContentAdmin(admin.ModelAdmin):
#     inlines = [PhotoInline, ]

# admin.site.register(ContentModel, ContentAdmin)
admin.site.register(ContentModel)