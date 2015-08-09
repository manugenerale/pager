# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.db import models
from mptt.admin import MPTTModelAdmin
from models import Page, Block

#class InlineI18nAdmin(admin.TabularInline):
#    extra = 1
#    model = BlockI18N
#    formfield_overrides = {
#        models.TextField: {'widget': forms.Textarea(attrs={'rows':3,'cols':30})}
#    }

class BlockAdmin(admin.ModelAdmin):
    list_display = ('page', 'name', 'slug', 'title', 'body')
    list_filter = ['page']
    #inlines = [InlineI18nAdmin]
    class Media:
        js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/grappelli/tinymce_setup/tinymce_setup.js',]

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
    list_display = ('title', 'is_public')
    list_editable = ('is_public',)
    list_filter = ['is_public']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug', 'description')

admin.site.register(Block, BlockAdmin)
admin.site.register(Page, PageAdmin)
#admin.site.register(BlockI18N)
