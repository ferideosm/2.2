from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    articles = Article.objects.all()
    print('articles ==', articles)
    for a in articles:
        print('a ==', a)
        for scope in a.scopes.all():
            print('scope ==', scope)
            print('scope.id ==', scope.id)
            print('scope.is_main ==', scope.is_main)
            print('scope .tags==', scope.tag)

    context = {'object_list': articles}
    return render(request, template, context)
