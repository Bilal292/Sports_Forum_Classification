
from django.urls import path
from .views import HomeView,PostDetailView,AddPostView,MyPostView, DeletePostView, AddCommentView, CricketView,FootballView,VolleyballView,RugbyView,HockeyView,TabletennisView,TennisView,BaseballView,BasketballView,BadmintonView
urlpatterns = [
    path('', HomeView.as_view()  ,name='home'),
    path('post/<int:pk>', PostDetailView.as_view()  ,name='post-details'),
    path('addpost/', AddPostView.as_view()  ,name='add_post'),
    path('myposts/', MyPostView.as_view()  ,name='my_posts'),
    path('post/<int:pk>/delete', DeletePostView.as_view()  ,name='post-delete'),
    path('post/<int:pk>/comment/', AddCommentView.as_view(),name='add_comment'),
    path('cricket/', CricketView.as_view(), name='cricket'),
    path('baseball/', BaseballView.as_view(), name='baseball'),
    path('volleyball/', VolleyballView.as_view(), name='volleyball'),
    path('rugby/', RugbyView.as_view(), name='rugby'),
    path('hockey/', HockeyView.as_view(), name='hockey'),
    path('tabletennis/', TabletennisView.as_view(), name='tabletennis'),
    path('tennis/', TennisView.as_view(), name='tennis'),
    path('football/', FootballView.as_view(), name='football'),
    path('basketball/', BasketballView.as_view(), name='basketball'),
    path('badminton/', BadmintonView.as_view(), name='badminton'),

]
