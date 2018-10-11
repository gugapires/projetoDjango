from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# estou no livro pag. 46

#Django provides a comprehensive series of built-in field types. Some of the most commonly used
#are detailed below.
#• CharField , a field for storing character data (e.g. strings). Specify max_length to provide a
#maximum number o characters the field can store.
#• URLField , much like a CharField , but designed for storing resource URLs. You may also
#specify a max_length parameter.
#• IntegerField , which stores integers.
#• DateField , which stores a Python datetime.date object.