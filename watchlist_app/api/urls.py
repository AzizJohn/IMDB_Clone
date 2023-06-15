from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import StreamPlatformListAV, StreamPlatformDetailAV, WatchListListAV, \
    WatchListDetailDetailAV, ReviewList, ReviewDetail, ReviewCreate

urlpatterns = [
    path('stream/list/', StreamPlatformListAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),
    path('list/', WatchListListAV.as_view(), name='watchlist'),
    path('<int:pk>/', WatchListDetailDetailAV.as_view(), name='watchlist-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

]
