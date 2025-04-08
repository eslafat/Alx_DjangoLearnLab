from relationship_app.models import Author, Book
from relationship_app.models import Library
from relationship_app.models import Library, Librarian

author_name = "eslam"

author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books:
    print(f"- {book.title}")
    
    

library = Library.objects.get(name=library_name)
books = library.books.all()
print(f"Books in {library.name}:")
for book in books:
    print(f"- {book.title}")
    
library_name = "lib5"
librarian = Librarian.objects.get(library = library)
print(f"{librarian} who is working in {library_name}")
