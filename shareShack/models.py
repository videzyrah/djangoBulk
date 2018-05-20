from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField(max_length=200, blank=True, null=True)
    contactPerson = models.TextField(max_length=200, blank=True, null=True, help_text="names,emails,phone,preference, etc.")

    def __str__(self):
        return self.name

class Staff(models.Model):
    staff = models.OneToOneField(User, on_delete = models.PROTECT)
    
class Borrower(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    cardnumber = models.IntegerField(unique=True)
    dateJoined = models.DateField()
    memberOf = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Item(models.Model):
    CATERING = 'CA'
    LANDSCAPING = 'LA'
    RECREATION = 'RE'
    MAINTENANCE = 'MA'
    FURNITURE = 'FU'
    DEPARTMENT_CHOICES = (
        (CATERING, 'Catering'),
        (LANDSCAPING, 'Landscaping'),
        (RECREATION, 'Recreation'),
        (MAINTENANCE, 'Maintenance'),
        (FURNITURE, 'Furniture'),
    )

    department = models.CharField(
        max_length=2,
        choices=DEPARTMENT_CHOICES,
        default=FURNITURE,
    )

    writtenId = models.CharField("Written ID", max_length=30, unique=True)
    name = models.CharField(max_length=30)
    donor = models.CharField(max_length=30)
    date_Added = models.DateField()
    condition = models.TextField(max_length=200, blank=True, null=True)
    in_Stock = models.BooleanField(default = True)
    checked_Out_To = models.ForeignKey(Borrower, models.SET_NULL, blank=True, null=True)
    due_Back = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.writtenId

class CheckOut(models.Model):
    id = models.AutoField(primary_key=True)
    dateIssued = models.DateField()
    borrower = models.ForeignKey(Borrower, models.SET_NULL, blank=True, null=True )
    staff = models.ForeignKey(User, on_delete = models.PROTECT)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return "%s item#" % self.id

class Return(models.Model):
    id = models.AutoField(primary_key=True)
    dateReturned = models.DateField()
    borrower = models.ForeignKey(Borrower, models.SET_NULL, blank=True, null=True)
    staff = models.ForeignKey(User, on_delete = models.PROTECT )
    items = models.ManyToManyField(Item)

    def __str__(self):
        return "%s item#" % self.id
