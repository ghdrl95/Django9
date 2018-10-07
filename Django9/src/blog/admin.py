from django.contrib import admin
from .models import Post,PostFile,PostImage,PostType
# Register your models here.

admin.site.register(Post)
admin.site.register(PostFile)
admin.site.register(PostImage)
admin.site.register(PostType)