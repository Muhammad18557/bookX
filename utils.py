"""This module contains helper functions that are used in the main application."""

from models import *


def is_book_liked_by_user(book_id, user_id):
    """Helper function to check if a book is liked by a user."""
    return bool(Like.query.filter_by(book_id=book_id, user_id=user_id).first())


def get_pending_likes(user_id):
    """ "This function returns the books that the user has liked, but the owner of the book has not liked any of the user's books."""
    liked_books = Like.query.filter_by(user_id=user_id).all()

    pending_likes = []
    for like in liked_books:
        book = Book.query.get(like.book_id)
        # Check if the owner of the liked book has not liked any of the user's books
        reciprocal_like = (
            Like.query.join(Book, Like.book_id == Book.id)
            .filter(Book.user_id == book.user_id, Like.user_id != user_id)
            .first()
        )
        if not reciprocal_like:
            pending_likes.append(book)
    return pending_likes


def get_book_exchange_matches_with_objects(user_id):
    """This function returns the books that the user has liked and the owner of the book has liked one of the user's books."""
    exchange_matches = set()

    user_likes = Like.query.filter_by(user_id=user_id).all()

    for user_like in user_likes:
        liked_book = Book.query.get(user_like.book_id)
        book_owner_id = liked_book.user_id

        if (
            book_owner_id != user_id
        ):  # Making sure the current user is not liking their own book
            owner_likes = Like.query.filter_by(user_id=book_owner_id).all()

            owner_liked_book_ids = [
                like.book_id for like in owner_likes if like.user_id == book_owner_id
            ]

            mutual_likes = Book.query.filter(
                Book.id.in_(owner_liked_book_ids), Book.user_id == user_id
            ).all()

            for mutual_like in mutual_likes:
                exchange_matches.add((liked_book, mutual_like))

    exchange_matches_list = list(exchange_matches)

    print(f"Exchange matches ({len(exchange_matches_list)} pairs):")
    for pair in exchange_matches_list:
        print(
            f"- {pair[0].title} liked by {user_id} <-> {pair[1].title} liked by {pair[1].user_id}"
        )

    return exchange_matches_list


def get_user_exchanges(user_id):
    """This function returns the exchanges that the user has participated in."""
    exchanges = Exchange.query.filter(
        (Exchange.user_id_a == user_id) | (Exchange.user_id_b == user_id)
    ).all()

    book_ids = [exchange.book_id_a for exchange in exchanges] + [
        exchange.book_id_b for exchange in exchanges
    ]

    books = Book.query.filter(Book.id.in_(book_ids)).all()
    book_titles = {book.id: book.title for book in books}

    for exchange in exchanges:
        exchange.book_a_title = book_titles.get(exchange.book_id_a)
        exchange.book_b_title = book_titles.get(exchange.book_id_b)

    return exchanges
