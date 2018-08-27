#-*- coding:utf-8 -*-
from django.contrib import admin
from mainapp.models import *

# Register your models here.


class IndexPhotoLbumAdmin(admin.ModelAdmin):
    list_display = ['pl_id','pl_name','pl_title','pl_images']
    list_filter = ['pl_id']
    search_fields = ['pl_id']
    list_per_page = 4
    fieldsets = [
        ('头条名称', {'fields' : ['pl_id', 'pl_name']}),
        ('内容图片', {'fields' : ['pl_title','pl_images']}),
    ]

class IndexMarketingAdmin(admin.ModelAdmin):
    list_display = ['mt_id', 'mt_name', 'mt_title', 'mt_content','mt_icon','mt_images']
    list_filter = ['mt_id']
    search_fields = ['mt_name']
    list_per_page = 10
    fieldsets = [
        ('头条名称', {'fields': ['mt_id', 'mt_name']}),
        ('标题图标', {'fields': ['mt_title', 'mt_icon']}),
        ('内容图片', {'fields': ['mt_content', 'mt_images']}),
    ]

class IndexFeaturetteAdmin(admin.ModelAdmin):
    list_display = ['ft_id', 'ft_name', 'ft_title', 'ft_content', 'ft_images']
    list_filter = ['ft_id']
    search_fields = ['ft_name']
    list_per_page = 10
    fieldsets = [
        ('头条名称', {'fields': ['ft_id', 'ft_name']}),
        ('标题内容', {'fields': ['ft_title', 'ft_content']}),
        ('图片', {'fields': ['ft_images']}),
    ]
admin.site.register(PhotoLbum, IndexPhotoLbumAdmin)
admin.site.register(Marketing, IndexMarketingAdmin)
admin.site.register(Featurette, IndexFeaturetteAdmin)


class CultureTimelineAdmin(admin.ModelAdmin):
    list_display = ['tl_id', 'tl_name', 'tl_headertitle', 'tl_releasetime', 'tl_content']
    list_filter = ['tl_id']
    search_fields = ['tl_name']
    list_per_page = 10
    fieldsets = [
        ('头条名称', {'fields': ['tl_id', 'tl_name']}),
        ('标题时间', {'fields': ['tl_headertitle', 'tl_releasetime']}),
        ('内容', {'fields': ['tl_content']}),
    ]
admin.site.register(Timeline, CultureTimelineAdmin)



class Joinus_headleJoinusDataAdmin(admin.ModelAdmin):
    list_display = ['jd_name', 'jd_phone', 'jd_professional', 'jd_interest']
    list_filter = ['jd_name']
    search_fields = ['jd_phone']
    list_per_page = 10
    fieldsets = [
        ('姓名', {'fields': ['jd_name']}),
        ('电话', {'fields': ['jd_phone',]}),
        ('专业', {'fields': ['jd_professional']}),
        ('兴趣', {'fields': ['jd_interest']}),
    ]
admin.site.register(JoinusData, Joinus_headleJoinusDataAdmin)



admin.site.register(HomePageContent)
admin.site.register(GlobalTitle)
admin.site.register(GlobalAdvert)
