from django.shortcuts import render
from user.models import Article
from django.db.models import Q

def discover_articles(request):
    article = Article.objects.all()
    
    
    context = {'AllArticles': article, }
    return render(request, 'discover/discover-articles.html', context)

def discover_article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'discover/discover-article-detail.html', context)
    
    
def discover_articles(request):
    query = request.GET.get('search_query')
    if query:
        article = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) 
        ).distinct()
    else:
        article = Article.objects.all()
        
    context = {'AllArticles': article}
    return render(request, 'discover/discover-articles.html', context)