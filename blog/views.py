from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator

# READ
def home(request):
    blogs = Blog.objects.all()
    paginator= Paginator(blogs, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})#보라 블로그를 초록 블로그로 home.html에 담을거야
#response 형태로 다시 줄거야
# DETAIL READ
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    print(blog.image)
    return render(request, 'detail.html', {'blog': blog})


# CREATE
def new(request):
    return render(request, 'new.html')#작성하기에서 


def create(request):
    new_blog = Blog()
    # new_blog.title = request.POST['title']
    # new_blog.content = request.POST['content']#post요청이 들어왔는데 title로 뽑아서 가져올 거야     
    new_blog.title = request.POST.get('title')
    new_blog.content = request.POST.get('content')
    new_blog.image = request.FILES.get('image')#get으로 받음 이미지 없을떄 키에러방지
    print(new_blog.title)
    print(request.FILES.get('image'))
    new_blog.save()#매니저님을 통해 저장
    return redirect('detail', new_blog.id) #url detail, 같이 id를 들고 가라 
    # return render(request, 'detail.html', {'blog': new_blog})
#render 나한테 post 사용 렉 걸려서 새로고침 그러면 명령 계속
#redirect post가 get으로 변경되어 안전

# UPDATE
def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)#Blog 내에 pk를 통해 보낸다
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    old_blog.title = request.POST.get('title')
    old_blog.content = request.POST.get('content')
    old_blog.image = request.FILES.get('image')
    print(old_blog.image)
    print(request.FILES.get('image'))
    old_blog.save()
    return redirect('detail', old_blog.id)
    # return render(request, 'detail.html', {'blog': old_blog})



# DELETE
def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')