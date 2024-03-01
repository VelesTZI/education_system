from django.contrib import admin

from .models import Product, Lesson, Group, AcessProduct

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author_creathor',
        'name_product',
        'start_date_time_product',
        'price_product'
    )

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'lesson_product',
        'neme_lesson',
        'video_link',
    )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'get_category',
        'min_count_users',
        'max_count_users',
        'group_product',
    )

@admin.register(AcessProduct)
class AcessProductAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        # 'produkt'
    )