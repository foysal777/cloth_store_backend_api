from django.contrib import admin
from .models import Review, Product , Wishlist ,UserReview

# Register your models here.
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(UserReview)