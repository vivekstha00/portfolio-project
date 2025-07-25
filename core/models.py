from django.db import models

class Bio(models.Model):
    name = models.CharField(max_length= 50)
    titles = models.CharField(max_length = 150)
    email = models.EmailField()
    phone_number = models.CharField(max_length =15, blank=True, null=True)
    address = models.CharField(max_length=200)
    age = models.IntegerField()
    gogle_map_link = models.URLField()
    freelance = models.BooleanField(default=True)
    degree = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Socials(models.Model):
    name = models.CharField(max_length = 20)
    icon = models.ImageField()
    url = models.URLField()

    def __str__(self):
        return self.name
    
class Statistics(models.Model):
    name = models.CharField(max_length = 20)
    number = models.CharField(max_length = 15)
    icon = models.ImageField()

    def __str__(self):
        return self.name
    
class Skills(models.Model):
    name = models.CharField(max_length = 20)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    # class Meta:
    #     verbose_plural ="Skills"


class Service(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    description = models.TextField()

    def __str__(self):
        return self.name

class EnquiryForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f"Enquiry from {self.name}"