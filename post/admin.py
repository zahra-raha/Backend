from django.contrib import admin
from .models import Post, PostsCategory, PostComment, Inbox

# Inline admin
class PostCommentInline(admin.TabularInline):
    model = PostComment
    min_num = 0
    extra = 0
    

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostCommentInline]
    list_display = "title", "description",
    search_fields = "title", "price",
    list_filter = "category", "price"
    

@admin.register(PostsCategory)
class PostsCategoryAdmin(admin.ModelAdmin):
    list_display = "name", "icon"
    search_fields = "name",
    

@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display =  "name", "phone_number", "email", "timestamp"
    search_fields = "name", "phone_number", "email"
    