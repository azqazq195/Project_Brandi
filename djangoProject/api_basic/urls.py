from django.urls import path, include
# from .views import article_list, article_details
from .views import ArticleAPIView, ArticleDetailsAPIView, GenericAPIView

urlpatterns = [
    # path('article/', article_list),
    # path('article/details/<int:pk>', article_details),
    path('article/', ArticleAPIView.as_view()),
    path('article/details/<int:id>', ArticleDetailsAPIView.as_view()),
    path('article/generic/<int:id>', GenericAPIView.as_view()),
]

