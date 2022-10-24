from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect

from articles.forms import ArticleForm
from articles.models import Article
from decorators.decorators import ajax_login_required, ajax_permission_required


def article_home_view(request):
    if request.user.groups.filter(name="Moderator").exists() or request.user.is_superuser:
        articles = Article.objects.all().order_by('-creation_date')
    else:
        articles = Article.objects.filter(status=1).order_by('-publish_date')
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles_home.html', {'page_obj': page_obj})


def article_detail_view(request, slug):
    context = {'article': Article.objects.get(slug=slug)}
    return render(request, 'article.html', context)


@ajax_login_required
def article_like_view(request, slug):
    if request.method == 'POST':
        article_likes = Article.objects.get(slug=slug).likes
        if request.user in article_likes.all():
            article_likes.remove(request.user)
            return JsonResponse({'liked': False, 'counter': article_likes.count()}, status=200)
        else:
            article_likes.add(request.user)
            return JsonResponse({'liked': True, 'counter': article_likes.count()}, status=200)


@ajax_permission_required('articles.publish_article')
def article_publish_view(request, slug):
    if request.method == 'POST':
        article = Article.objects.get(slug=slug)
        article.publish()
        return JsonResponse({'detail': "Article published"}, status=200)


@permission_required('articles.add_article')
def article_add_view(request):
    form = ArticleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('article_home')
    return render(request, 'article_form.html', {'form': form})


@permission_required('articles.change_article')
def article_edit_view(request, slug):
    form = ArticleForm(request.POST or None, instance=Article.objects.get(slug=slug))
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('..')
    context = {'form': form}
    return render(request, 'article_form.html', context)
