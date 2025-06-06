from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.http import HttpResponseNotFound
from django.template.loader import render_to_string

def index(request):
    """
    Mostra la pàgina principal amb els últims 3 posts ordenats per data.
    """
    posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/index.html', {'posts': posts})

def posts_list(request):
    """
    Mostra un llistat de tots els posts ordenats per data.
    """
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    """
    Mostra el detall d'un post donat el seu slug.
    """
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def authors_list(request):
    """
    Mostra un llistat de tots els autors.
    """
    authors = Author.objects.all()
    return render(request, 'blog/authors_list.html', {'authors': authors})

def author_detail(request, author_id):
    """
    Mostra el detall d'un autor i els seus posts associats.
    """
    author = get_object_or_404(Author, id=author_id)
    posts = author.posts.all()
    tags = Tag.objects.filter(posts__author=author).distinct()
    return render(request, 'blog/author_detail.html', {
        'author': author,
        'posts': posts,
        'tags': tags,
    })

def tags_list(request):
    """
    Mostra un llistat de totes les etiquetes (tags).
    """
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})

def tag_posts(request, tag):
    """
    Mostra tots els posts associats a una etiqueta específica.
    """
    tag = get_object_or_404(Tag, name=tag)
    posts = tag.posts.order_by('-date')
    return render(request, 'blog/tag_post.html', {'tag': tag, 'posts': posts})

def error_404_view(request, exception):
    """
    Mostra una pàgina d'error 404 personalitzada.
    """
    html = render_to_string('blog/404.html', request=request)
    return HttpResponseNotFound(html)
