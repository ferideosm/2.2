from django.contrib import admin
from .models import Article, ArticleScope, Tag
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

class ArticleScopeInlineFormset(BaseInlineFormSet):

    def clean(self):

        count_main = 0
        len_ = 0

        for form in self.forms:

            if not form.cleaned_data.get('DELETE'):

                if not form.cleaned_data.get('is_main') and len_ == 0:
                    raise ValidationError('Выберите основной раздел. Он должен быть первым')

                if form.cleaned_data.get('is_main'):
                    count_main += 1
                    
                len_ += 1

        if count_main > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean() 

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 0
    formset = ArticleScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    inlines = [ArticleScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    list_filter = ('name', )