import graphene

from api.models import Book
from .book import BookType, CreateBookMutation, UpdateBookMutation


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType, title=graphene.String())

    def resolve_all_books(root, info, **kwargs):
        title = kwargs.get("title")
        queryset = Book.objects.all()
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    update_book = UpdateBookMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
