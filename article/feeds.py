from django.contrib.syndication.views import Feed

from .models import ArticlePost

class AllArticlesRssFeed(Feed):
    title = "陆文斌的博客"

    link='/'
    def items(self):
        return ArticlePost.objects.all()

    def item_title(self, item):
        return '[{0}] {1}'.format(item.category, item.title)

    def item_description(self, item):
        return item.content

































