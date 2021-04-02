from django.urls import path,include
from . import views
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router =  DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')

urlpatterns = [
    path('',views.index,name ='index'),
    path('register/', views.registerPage,name ='register'),
    path('login/', views.loginPage,name ='login'),
    path('logout/', views.logoutUser,name ='logout'),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>', ArticleDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

]
