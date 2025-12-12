from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from django.db.models import Q


def index(request):
    """Главная страница с 5-ю последними опубликованными постами"""
    template = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        Q(pub_date__lte=timezone.now()) & Q(is_published=True)
        & Q(category__is_published=True)
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    """Страница отдельных постов"""
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('category', 'location', 'author'),
        Q(pk=id) & Q(is_published=True)
        & Q(category__is_published=True) & Q(pub_date__lte=timezone.now())
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категории"""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.select_related(
        'category', 'location', 'author'
    ).filter(
        Q(category=category) & Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
    ).order_by('-pub_date')
    context = {'category': category,
               'post_list': post_list}
    return render(request, template, context)
