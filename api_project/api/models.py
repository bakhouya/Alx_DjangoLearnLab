from django.db import models

# ===================================================
# model Book with title and author fields
# ===================================================
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
# ===================================================
