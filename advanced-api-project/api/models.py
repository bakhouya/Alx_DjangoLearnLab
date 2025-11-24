
from django.db import models





# =====================================================================================
# Author Model
# =====================================================================================
class Author(models.Model):
    # Name of the author
    name = models.CharField(max_length=100, verbose_name="Name Author")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
# =====================================================================================




# =====================================================================================
# Book Model
# =====================================================================================
class Book(models.Model):
    # Title of the book 
    title = models.CharField(max_length=200, verbose_name="Ritle Book")
    # Year Of Publication 
    publication_year = models.IntegerField(verbose_name="Year Publication")
    # Author of the book user ralationship with Author model type one to many
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Author Book")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
# =====================================================================================
