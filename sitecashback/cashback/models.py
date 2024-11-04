from django.db import models


class Article(models.Model):
    STATUS = [
        (False, "Draft"),
        (True, "Published"),
    ]
    title = models.CharField(max_length=255, verbose_name="Name")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=STATUS, default=True)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="posts"
    )
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags')

    def __str__(self):
        return self.title

    class Meta:
        # db_table = 'Article'
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        indexes = [models.Index(fields=["created_at"])]


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    tag = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)

    def __str__(self) -> str:
        return self.tag
