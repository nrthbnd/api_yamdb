from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (
    CategoryViewSet, GenreViewSet, TitleViewSet, CommentViewSet, ReviewViewSet,
    ConfirmationView
)

app_name = 'api'

router = SimpleRouter()

router.register('titles', TitleViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register(
    r'titles/(?P<titles_id>\d+)/reviews',
    CommentViewSet,
    basename='reviews',
)
router.register(
    r'titles/(?P<titles_id>\d+)/reviews/(?P<review_id>\d+)/comments/',
    ReviewViewSet,
    basename='reviews',
)

urlpatterns = [
    path('', include(router.urls)),
    path('auth', include('djoser.urls')),
    path('auth', include('djoser.urls.jwt')),
    path('auth/signup/', ConfirmationView.as_view()),
]
