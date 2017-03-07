# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from django.contrib import admin
from django import forms
from django.db import models
from mptt.admin import MPTTModelAdmin
from models import *

class InlineI18nAdmin(admin.TabularInline):
    extra = 1
    model = BlockI18N
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows':3,'cols':30})}
    }

class BlockMediaAdmin(admin.ModelAdmin):
    list_display = ('show_attachment', 'show_url')

class InlineBlockMediaAdmin(admin.TabularInline):
    extra = 1
    model = BlockMedia
    ordering = ('-created_on',)

class BlockAdmin(admin.ModelAdmin):
    list_display = ('page', 'name', 'slug', 'get_content')
    list_filter = ['page']
    inlines = [InlineBlockMediaAdmin, InlineI18nAdmin]
    class Media:
        js = ['/static/tinymce/js/tinymce/tinymce.min.js', '/static/tinymce/js/tinymce/jquery.tinymce.init.js']

    def get_content(self, obj):
        return mark_safe(obj.body)


class InlineBlockAdmin(admin.TabularInline):
    extra = 1
    model = Block
    ordering = ('-created_on',)
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows':3,'cols':30})}
    }

class PageAdmin(MPTTModelAdmin):
    change_list_template = 'pager/admin/change_list.html'
    inlines = [InlineBlockAdmin]
    ordering = ('title',)
    list_display = ('id', 'title', 'parent', 'url')
    list_editable = ('title', 'parent', 'url')
    list_filter = ['is_public']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug', 'description')

admin.site.register(Block, BlockAdmin)
admin.site.register(BlockMedia, BlockMediaAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(BlockI18N)
