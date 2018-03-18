from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import ArticlePost,Category,Tag
from comment.models import Comment
from comment.forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
def home(request):
    articles = ArticlePost.objects.all()
    paginator = Paginator(articles,2)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request, 'home.html', {'articles':articles, 'page': current_page})


def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    article.increase_views()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            #return HttpResponse('successful')
            return HttpResponseRedirect(article.get_absolute_url())
    else:
        comment_form = CommentForm()
        return render(request, 'article/article_detail.html', {'article':article,'comment_form':comment_form})

def date_archives(request,year,month):
    articles = ArticlePost.objects.filter(created__year=year,created__month=month).order_by('-created')
    return render(request, 'article/article_archives.html', {'articles':articles})

def category_archives(request,category):
    category = get_object_or_404(Category, name= category)
    articles = ArticlePost.objects.filter(category=category).order_by('-created')
    return render(request, 'article/article_archives.html', {'articles':articles})

def tag_archives(requeset, tag):
    tag = get_object_or_404(Tag, name = tag)
    articles = ArticlePost.objects.filter(tag=tag).order_by('-created')
    return render(request, 'article/article_archives.html', {'articles':articles})


