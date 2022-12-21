from django.db import models


class productColour(models.Model):
    j=(
        ("red","red"),
        ("blue","blue"),
        ("green","green"),
        ("black","black")
    )
    colour=models.CharField(max_length=5,choices=j,default="red")
class productImage(models.Model):
     Image = models.ImageField( blank=True)

class productMainModel(models.Model):
    l=(
        (10,10),
        (20,20),
        (30,30)
    )
    k=(
        ("high","high"),
        ("low","low"),
        ("medium","medium")
    )
    Title=models.CharField(max_length=20)
    Description=models.CharField(max_length=100)
    Price=models.DecimalField(decimal_places=2,max_digits=10)
    Size=models.IntegerField(choices=l,default=10)
    Quality=models.CharField(max_length=10,choices=k)
    productcolour=models.ForeignKey(productColour,on_delete=models.CASCADE,null=True)
    productimage=models.ForeignKey(productImage,on_delete=models.CASCADE,null=True)

   
