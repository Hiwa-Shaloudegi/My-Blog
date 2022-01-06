from .models import Post

def add_variable_to_base(request):
    posts = Post.objects.all().order_by("-views")[:5]
    return {
        'posts': posts
    }