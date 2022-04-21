from app import db, Publisher, Book, Genre, Author


publisher1 = Publisher('Baltos Lankos')
publisher2 = Publisher('Nieko rimto')
publisher3 = Publisher('Alma Litera')
publisher4 = Publisher('Vilniaus Dailės akademijos leidykla')
publisher5 = Publisher('Versus aureus')



db.session.add_all([publisher1, publisher2, publisher3, publisher4, publisher5])
db.session.commit()



publishers = Publisher.query.all()
print(publishers)

genre1 = Genre('Action and Adventure')
genre2 = Genre('Classics')
genre3 = Genre('Fantasy')
genre4 = Genre('Detective ')
db.session.add_all([genre1, genre2, genre3, genre4])
db.session.commit()

genres = Genre.query.all()
print(genres)


author1 = Author('Jonas', '', 'Jonaitis')
author2 = Author('Petras', '', 'Petraitis')
author3 = Author('Antanas', '', 'Antanaitis')
db.session.add_all([author1, author2, author3])
db.session.commit()

authors = Author.query.all()
print(authors)

book1 = Book('Book 1', 355, 7, '9783161484100', '2000-12-12')
book1.publisher_id = 1
db.session.add(book1)
db.session.commit()


author = Author.query.get(1)
genre = Genre.query.get(1)
book = Book.query.get(1)

book.authors.append(author)
book.genres.append(genre)

print(book, book.authors, book.genres)