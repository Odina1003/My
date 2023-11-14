from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post(request):
    # content = Post.objects.all
    content = [
        {'id':'1', 'title':'Blog', 'yaratilgan_sana':'12.11.2023', 'image':'images/blog.jpg'},
        {'id':'2', 'title':'My_Blog', 'yaratilgan_sana':'2.10.2023', 'image':'images/myblog.jpg'},
        {'id':'3', 'title':'News', 'yaratilgan_sana':'15.11.2023', 'image':'images/news.jpg'}
    ]
    return render(request=request, context={'content':content}, template_name='index.html')