from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    sub_name = models.CharField(max_length=250, unique=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['sub_name']

    def __unicode__(self):
        return self.sub_name


class LastName(models.Model):
    page = models.ForeignKey(Page)
    last_name = models.CharField(max_length=200, unique=True)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['last_name']

    def __unicode__(self):
        return self.last_name


class Data(models.Model):
    strain = models.ForeignKey(LastName)
    min_range = models.IntegerField(blank=True)
    max_range = models.IntegerField(blank=True)
    size = models.IntegerField(blank=True)
    dr_up_down = models.CharField(max_length=300, blank=True)
    insertion_site = models.TextField(blank=True)
    integrase = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return self.strain











