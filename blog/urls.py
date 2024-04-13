from django.urls import path
from . import views


urlpatterns = [
    # READ
    path('', views.home, name='home'),#뒤의 home은 url의 별칭
    # DETAIL READ
    path('blog/<int:blog_id>', views.detail, name='detail'),#detail의 요리행위에게도 가야함
    # CREATE
    path('blog/new', views.new, name='new'),
    path('blog/create', views.create, name='create'),
    # UPDATE
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name='update'),
    # DELETE
    path('blog/delete/<int:blog_id>', views.delete, name='delete'),

    
] 

