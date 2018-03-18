from django.shortcuts import render

from .models import Comment
from article.models import ArticlePost
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    template_name = 'comment/comment_list.html'

@login_required(login_url="/account/login/")
def comment_reply(request,id):
    comment = Comment.objects.get(id = id)
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            new_comment = commentform.save(commit=False)
            new_comment.user = request.user
            new_comment.parent_comment = comment
            new_comment.article = comment.article
            new_comment.save()
            #return HttpResponse('your comment saved')
            return HttpResponseRedirect(comment.article.get_absolute_url())
        else:
            return HttpResponse('your comment is invalid')
    if request.method == 'GET':
        commentform = CommentForm()
        return render(request,'comment/comment_reply.html', {"form":commentform, "comment":comment})