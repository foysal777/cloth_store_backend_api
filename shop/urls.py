from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  ProductViewset , UsermyProfileView,ReviewViewset ,UserProfileView, WishListViewset , UserReviewViewSet  , AverageRatingView
from . import views

router = DefaultRouter()
router.register('product' , ProductViewset)
router.register('Review' , ReviewViewset)
router.register('wishlist' , WishListViewset)
router.register('userreviews', UserReviewViewSet , basename='reuser')





urlpatterns = [
    path('' , include(router.urls)),     
    path('myprofile/', UsermyProfileView.as_view(), name='userprofile'),
    path('api/user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('register/' , views.userRegistration.as_view() , name= 'register'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('average_rating/', AverageRatingView.as_view(), name='average-rating'),
    
   
   
  
]