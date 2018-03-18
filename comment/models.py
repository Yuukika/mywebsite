from django.db import models
from article.models import ArticlePost
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Comment(models.Model):
    article = models.ForeignKey(ArticlePost,related_name="comment")
    parent_comment = models.ForeignKey('self', blank=True, null=True, related_name="p_comment")
    user = models.ForeignKey(User)
    content = models.TextField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-date',)

    def get_absolute_url(self):
        return reverse("comment:comment_reply", args=[self.id])