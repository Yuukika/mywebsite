from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from slugify import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class ArticlePost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name = "article")
    content = models.TextField()
    category = models.ForeignKey(Category,related_name="article_category")
    tag = models.ManyToManyField(Tag,blank=True, related_name="article_tag")
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=500)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("title",)
        index_together = (('id', 'slug'),)
        # 对数据库中这个两个字段建立索引，提高读取文章对象的速度
    def __str__(self):
        return self.title
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse("article:article_detail", args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        # 调用父类的 save 方法将数据保存到数据库中
        super(ArticlePost, self).save(*args, **kwargs)

