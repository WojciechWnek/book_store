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