from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title + ' - ' + self.author.name

    class Meta:
        db_table = 'book_authors'
        unique_together = ('book', 'author')
