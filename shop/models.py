from django.db import models
from django.contrib.auth.models import User


SIZE = (
    ( "M" , "M"),
    ( "L" , "L"),
    ( "XL" , "XL"),
    ( "XXL" , "XXL"),
    ( "XXXL" , "XXXL"),
        )
    
STAR_CHOICE = [
       ("1" , '★☆☆☆☆'),
       ('2' , '★★☆☆☆'),
       ('3' , '★★★☆☆'),
       ('4' , '★★★★☆'),
       ('5' , '★★★★★'),
     ]     

    
class Product(models.Model):
    name  =  models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url= models.CharField(max_length=255,default='' )     
    size = models.CharField(max_length=20, choices= SIZE)
    color = models.CharField(max_length=30)
    rating = models.CharField(max_length=30 , choices=STAR_CHOICE)
  
    
    
    def __str__(self):
        return self.name
    

          

class Review(models.Model):
    user = models.ForeignKey(User , related_name='reviews' , on_delete=models.CASCADE)
    image_url= models.CharField(max_length=255,default='' )  
    product = models.ForeignKey(Product , related_name='product' , on_delete=models.CASCADE)
    comment = models.TextField(default="Classy")
    rating = models.CharField(max_length=30 , choices=STAR_CHOICE)
    
    
    def __str__(self):
        return f'Review for {self.product.name} by {self.user.username}'


class Wishlist(models.Model):
    user = models.ForeignKey(User , related_name='wishlist', on_delete=models.CASCADE)
   
    products = models.ManyToManyField(Product)
    
    
    
    def __str__(self):
        return f'Wishlist of {self.user.username}'
    
Rating = [
       ("1" , '1'),
       ('2' , '2'),
       ('3' , '3'),
       ('4' , '4'),
   
     ]     
      
    
class UserReview(models.Model):
    name = models.CharField(max_length=255)
    star_rating = models.CharField(max_length=6, choices=Rating)
    comment = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.star_rating} stars'