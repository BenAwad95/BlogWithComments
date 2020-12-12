from django.urls import path
# * import views
from .views import PostView, post_detail

app_name = 'blogApp'
urlpatterns = [
    # ! the error that cause a big problem in my code is you forget put name 
    path('', PostView.as_view(), name = 'post_list'),
    path('post/<int:pk>/', post_detail, name = 'post_detail')
]
