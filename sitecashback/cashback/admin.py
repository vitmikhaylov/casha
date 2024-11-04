from django.contrib import admin

from .models import Article, Category, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "slug", "content", "is_published", "category"]
    list_display = (
        "id",
        "title",
        "slug",
        # "post_photo",
        "created_at",
        "updated_at",
        "is_published",
    )
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)
    list_display_links = (
        "id",
        "title",
    )
    ordering = (
        "id",
        "title",
        "-created_at",
        "updated_at",
    )
    list_editable = ("is_published",)
    list_per_page = 5
    search_fields = (
        "id",
        "title",
    )
    list_filter = ("is_published",)
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "tag"]
    list_display_links = ["id", "tag"]
    prepopulated_fields = {"slug": ("tag",)}
