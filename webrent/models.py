from django.db import models

# Create your models here.
class RentOrigin(models.Model):
    property_id=models.IntegerField()
    crawl_date=models.DateField()
    street_address=models.TextField(max_length=100,null=True)
    suburb=models.TextField(max_length=50,null=True)
    post_code=models.TextField(max_length=50,null=True)
    bed=models.IntegerField(null=True,default=0)
    bathroom=models.IntegerField(null=True,default=0)
    car=models.IntegerField(null=True,default=0)
    property_type=models.TextField(max_length=50,null=True)
    price=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    price_des=models.TextField(max_length=50,null=True)
    date_available=models.TextField(max_length=50,null=True)
    title = models.TextField(max_length=500, null=True)
    description=models.TextField(null=True)
    bond=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    allowance = models.TextField(max_length=100, null=True)
    indoor_feature = models.TextField(max_length=500, null=True)
    outdoor_feature = models.TextField(max_length=500, null=True)
    other_feature = models.TextField(max_length=500, null=True)
    floorplan = models.TextField(max_length=500, null=True)
    school = models.TextField( null=True)
    median_rent=models.TextField(max_length=200,null=True)
    rental_yield=models.TextField(max_length=200,null=True)
    agency=models.TextField(max_length=200,null=True)
    agent=models.TextField(max_length=200,null=True)
    url=models.TextField(max_length=100,null=True)


    class Meta:
        unique_together = ("property_id", "crawl_date")
        verbose_name='Realestate_Rent_Origin_info'
        ordering=('suburb',)

    def __str__(self):
        return '{0}-{1}-{2}-{3}-{4}'.format(self.property_id,self.suburb,self.street_address,self.price,self.agency)
