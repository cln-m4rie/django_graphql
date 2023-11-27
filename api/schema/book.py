from graphene_django import DjangoObjectType
import graphene

from api.models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "genre", "year")

class CreateBookMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        genre = graphene.String(required=True)
        year = graphene.Int(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, title, genre, year):
        book = Book.objects.create(title=title, genre=genre, year=year)
        return CreateBookMutation(book=book)


class UpdateBookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        genre = graphene.String()
        year = graphene.Int()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, id, title=None, genre=None, year=None):
        book = Book.objects.get(id=id)
        if title:
            book.title = title
        if genre:
            book.genre = genre
        if year:
            book.year = year
        book.save()
        return UpdateBookMutation(book=book)
