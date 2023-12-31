# ORM
## The Commands
- **migrate**, which is responsible for applying and unapplying migrations.
- **makemigrations**, which is responsible for creating new migrations based on the changes you have made to your models.
- **sqlmigrate**, which displays the SQL statements for a migration.
- **showmigrations**, which lists a project’s migrations and their status.

## Filters - fields lookups
https://docs.djangoproject.com/en/4.2/topics/db/queries/#field-lookups

## ORM conditions

AND  - 

OR - |

```
from django.db.models import Q

Book.objects.filter(Q(rating__lt=3) | Q(is-bestselling=True), Q(author="J.K Rowling"))

```



# Admin

```
python manage.py createsuperuser
```

## Add Book model to admin
```
from .models import Book

admin.site.register(Book)
```

## Admin configuration

https://docs.djangoproject.com/en/4.2/ref/contrib/admin/



# Relationships

Relations on a books Table

One to many (one author can have many books)
```
class Book(models.Model):
    [...]
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
```

One to one (one author can have one address)
```
class Author(models.Model):
    [...]
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
```

Many to many (one book can be publushed in many countries)
```
class Book(models.Model):
    [...]
    published_countries = models.ManyToManyField(Country, null=False)
```