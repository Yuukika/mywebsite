from django import template
from django.utils.timezone import now, timedelta
import timeago
from django.db.models import Count
register = template.Library()

from article.models import ArticlePost,Category, Tag
from django.utils.safestring import mark_safe
import markdown

@register.filter(name="markdown")
def markdown_filter(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_comments(article):
    return article.comment.count()

@register.simple_tag
def all_category():
    return Category.objects.annotate(count=Count("article_category"))

@register.simple_tag
def all_tags():
    return Tag.objects.annotate(count=Count("article_tag"))

#@register.simple_tag
#def date_archives():
#    return ArticlePost.objects.dates('created', 'day', order="DESC")

@register.simple_tag
def all_articles():
    return ArticlePost.objects.all()


@register.inclusion_tag('article/latest_articles.html')
def latest_articles(n=5):
    latest_articles = ArticlePost.objects.order_by('-created')[:5]
    return {'latest_articles':latest_articles}


@register.filter("timeago")
def timeago_filter(value):
    now_ = now()
    return timeago.format(value, now_, 'zh_CN')



#@register.simple_tag
#def date_archives():
#    return ArticlePost.objects.dates('created', 'month', order="DESC")

@register.inclusion_tag('article/date_archives.html')
def date_archives():
    archives = ArticlePost.objects.dates('created', 'day', order="DESC")
    return {"date_archives": archives}





