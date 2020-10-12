from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Article, Book, Links, Comment

import markdown

def home(request):
    ones = Article.published.order_by("-datetime")[:5]
    hots = Article.objects.order_by("-look")[:5]
    return render(request, 'myapp/home.html', locals())

def blog(request):
    ones = Article.published.order_by("-datetime")[:10]
    books = Book.objects.all()
    return render(request, 'myapp/blog.html', locals())

def links(request):
    ones = Links.objects.all()
    return render(request, 'myapp/links.html', locals())

def article(request, id):
    one = get_object_or_404(Article, pk=id)
    one.look += 1
    one.save()
    one.content = markdown.markdown(one.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    totals = one.book.article.filter(status='published')
    one_id = id
    comments = one.comment.filter(is_show=True)
    return render(request, "myapp/article.html", locals())

def page_not_found(request, exception):
    return render(request, "myapp/404.html")

def booklist(request, id):
    book = get_object_or_404(Book, pk=id)
    one = book.article.filter(status='published').first()
    if not one:
        raise Http404
    return redirect(one)

def comment(request):
    context = {}
    context['username'] = request.GET.get("username")
    context['QQ'] = request.GET.get("QQ")
    context['content'] = request.GET.get("comment")
    context['ip'] = request.META.get("REMOTE_ADDR")
    one_id = request.GET.get("from_url")
    context['blog'] = get_object_or_404(Article, id=one_id)
    Comment.objects.create(**context)
    return JsonResponse({"code":"success"})