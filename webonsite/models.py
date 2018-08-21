from django.db import models

# Create your models here.
class OnSiteOrigin(models.Model):
    suburb=models.TextField(max_length=50,null=True)
    price=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    unit_price=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    unit_percentage=models.DecimalField(max_digits=3,decimal_places=2,null=True,default=0)
    income=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    remuneration=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    multiplier=models.DecimalField(max_digits=3,decimal_places=1,null=True,default=0)
    agreement_term=models.IntegerField(null=True,default=0)
    agreement_remain=models.IntegerField(null=True,default=0)
    agreement_age=models.IntegerField(null=True, default=0)
    total_unit=models.IntegerField(null=True,default=0)
    wage_per_unit=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    owner_occupy=models.IntegerField(null=True,default=0)
    letting=models.IntegerField(null=True,default=0)
    income_per_letting=models.DecimalField(max_digits=9,decimal_places=2,null=True,default=0)
    look_ups=models.IntegerField(null=True,default=0)
    outside_agents=models.IntegerField(null=True,default=0)
    manager_bed=models.IntegerField(null=True,default=0)
    manager_bathroom=models.IntegerField(null=True,default=0)
    manager_car=models.IntegerField(null=True,default=0)
    office=models.IntegerField(null=True,default=0)
    office_hour=models.IntegerField(null=True,default=0)
    agency=models.TextField(max_length=50,null=True)
    agent=models.TextField(max_length=50,null=True)
    complex_feature=models.TextField(max_length=500,null=True)
    url=models.TextField(max_length=100,null=True)
    title=models.TextField(max_length=200,null=True)
    description=models.TextField(null=True)
    unit_feature=models.TextField(max_length=500,null=True)
    pets=models.TextField(max_length=50,null=True)
    last_update=models.TextField(max_length=100,null=True)
    property_id=models.IntegerField()

    class Meta:
        verbose_name='Onsiteweb_Origin_info'
        ordering=('suburb',)

    def __str__(self):
        return '{0}-{1}-{2}-{3}-{4}'.format(self.property_id,self.suburb,self.title,self.price,self.income)




