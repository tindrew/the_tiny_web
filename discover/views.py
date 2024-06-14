from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.models import Article

def discover_articles(request):
    article = Article.objects.all()
    
    
    context = {'AllArticles': article, }
    return render(request, 'discover/discover-articles.html', context)

def discover_article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'discover/discover-article-detail.html', context)
    