from django.contrib import admin

from .models import Coin, Post, Author, Comment


@admin.action(description="Обновить биографию")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(biography='Все об авторе. Интересно до ужаса')


class AdminAuthors(admin.ModelAdmin):
    list_display = ('name', 'surname', 'biography')
    list_filter = ('name', 'surname')
    search_fields = ['name']
    search_help_text = 'Поиск по имени автора (name)'
    actions = [reset_quantity]
    readonly_fields = ['email']
    fieldsets = [
        (
            'Данные',
            {
                'classes': ['wide'],
                'fields': ['name', 'surname', 'email'],
            },
        ),
        (
            'Биография',
            {
                'classes': ['wide'],
                'fields': ['biography'],
            },
        ),
        (
            'Дата',
            {
                'classes': ['wide'],
                'fields': ['birthday'],
            },
        ),

    ]


admin.site.register(Coin)
admin.site.register(Author, AdminAuthors)
admin.site.register(Post)
admin.site.register(Comment)
