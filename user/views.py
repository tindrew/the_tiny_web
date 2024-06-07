from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from . forms import ArticleForm, UpdateUserForm

from . models import Article

from account.models import CustomUser

from django.views.generic import DetailView

class MarkdownDetailView(DetailView):
    model = Article

@login_required
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'user/user-dashboard.html')
    else:
        return redirect('user-login')
    
@login_required(login_url='user-login')
def create_article(request):
    
    form = ArticleForm()
    
    if request.method == 'POST':
        
        form = ArticleForm(request.POST)
        
        if form.is_valid():
            
           article = form.save(commit=False)
           
           article.user = request.user #checking that the user is logged in
           
           article.save()
           
           return redirect('user-articles')
       
    context = {'CreateArticleForm': form}
    
    return render(request, 'user/create-article.html', context)


@login_required(login_url='user-login')
def user_articles(request):
    
    current_user = request.user.id
    
    # article = Article.objects.all().filter(user_id=current_user)
    articles = Article.objects.filter(user=request.user)

    context = {'AllArticles': articles}
    
    return render(request, 'user/user-articles.html', context)

@login_required(login_url='user-login')
def update_article(request, pk):
    
    try: 
        
        article = Article.objects.get(id=pk, user=request.user)
    
    except:
        
        return redirect('user-articles')
    
    
    form = ArticleForm(instance=article)
    # In a view or controller
    
    if request.method == 'POST':
        
        form = ArticleForm(request.POST, instance=article)
        
        if form.is_valid:
            
            form.save()
            
            return redirect('user-articles')
        
    context = {'UpdateArticleForm': form}
    
    return render(request, 'user/update-article.html', context)


@login_required(login_url='user-login')
def delete_article(request, pk):
    
    try:
        
        article = Article.objects.get(id=pk, user=request.user)
    
    except: 
        
        return redirect('user-articles')
    
    
    if request.method == 'POST':
        
        article.delete()
        
        return redirect('user-articles')
    
    return render(request, 'user/delete-article.html')

@login_required(login_url='user-login')
def account_management(request,):
    
    form = UpdateUserForm(instance=request.user)
    
    if request.method == 'POST':
        
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('user-Dashboard')
        
    context = {'UpdateUserForm': form}
    
    return render(request, 'user/account-management.html', context)
    
            
            
@login_required(login_url='user-login')
def delete_account(request,):
    
    if request.method == 'POST':
        
        delete_user = CustomUser.objects.get(email=request.user)
        
        delete_user.delete()
        
        return redirect('user-login')
    
    return render(request, 'user/delete-account.html')
        
    
    
            
