"""This is the main file for the Book Exchange web application."""

from database import db
from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask import flash
import time
from utils import (
    get_pending_likes,
    get_book_exchange_matches_with_objects,
    get_user_exchanges,
    is_book_liked_by_user,
)
from flask_login import (
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user,
)
from forms import RegisterForm, LoginForm, BookForm

app = Flask(__name__, template_folder="templates")
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book_exchange.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "notverysecretive"

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from models import User, Book, Like, Exchange  # comes later to avoid circular imports


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/", methods=["GET"])
def index():
    """This function is the main page of the application. It displays the featured books and allows users to search for books by title, author, genre, and year."""
    query = request.args.get("query", "")
    author = request.args.get("author", "")
    genre = request.args.get("genre", "")
    year = request.args.get("year", "")

    books_query = Book.query

    if query:
        books_query = books_query.filter(
            Book.title.contains(query)
            | Book.summary.contains(query)
            | Book.review.contains(query)
        )
    if author:
        books_query = books_query.filter(Book.author.contains(author))
    if genre:
        books_query = books_query.filter(Book.genre.contains(genre))
    if year and year.isdigit():
        books_query = books_query.filter(Book.year == int(year))

    books = books_query.all()
    if current_user.is_authenticated:
        for book in books:
            book.is_liked = is_book_liked_by_user(book.id, current_user.id)

    return render_template("index.html", featured_books=books, query=query)


@app.route("/login", methods=["GET", "POST"])
def login():
    """ "This function handles the login page of the application. It validates the user's credentials and logs them in if they are correct."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully", "success")
            time.sleep(1)
            return redirect(url_for("index"))
        # flash(form.errors if form.errors else "", "error")
    return render_template("login.html", form=form)


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """This function logs the user out of the application. Only if the user is logged in."""
    print("logout is called")
    logout_user()
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """This function handles the registration page of the application. It validates the user's input and creates a new user if the input is valid."""
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            email=form.email.data, password=hashed_password, name=form.name.data
        )
        db.session.add(new_user)
        db.session.commit()
        print("User created")
        return redirect(url_for("login"))
    print("error", form.errors)
    return render_template("register.html", form=form)


@app.route("/profile/<int:user_id>", methods=["GET", "POST"])
@login_required
def profile(user_id):
    """This function displays the profile page of a user. It shows the user's information and the books they have added to the application."""
    user = User.query.get_or_404(user_id)
    books = Book.query.filter_by(user_id=user_id).all()
    for book in books:
        book.is_liked = is_book_liked_by_user(book.id, current_user.id)
    return render_template("profile.html", user=user, books=books)


@app.route("/edit_profile", methods=["POST"])
@login_required
def edit_profile():
    """This function allows the user to edit their profile. It updates the user's information in the database."""
    user_id = request.form.get("user_id")
    user = User.query.get_or_404(user_id)
    if user.id != current_user.id:
        flash("You are not allowed to edit this profile.", "error")
        return redirect(url_for("profile", user_id=user.id))

    user.location = request.form["location"]
    user.bio = request.form["bio"]
    db.session.commit()
    flash("Profile updated successfully!", "success")
    return redirect(url_for("profile", user_id=user.id))


@app.route("/add_book", methods=["POST", "GET"])
def add_book():
    """This function allows the user to add a new book to the application. It validates the user's input and adds the book to the database."""
    form = BookForm()
    if form.validate_on_submit():
        book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            year=form.year.data,
            rating=form.rating.data,
            review=form.review.data,
            summary=form.summary.data,
            user_id=current_user.id,
        )
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully!", "success")
        return redirect(url_for("profile", user_id=current_user.id))
    return render_template("add_book.html", form=form)


@app.route("/view_book/<int:book_id>")
@login_required
def view_book(book_id):
    """This function displays the details of a book. It shows the book's information and allows the user to like the book."""
    book = Book.query.get_or_404(book_id)
    return render_template("view_book.html", book=book)


@app.route("/like_book/<int:book_id>", methods=["POST"])
@login_required
def like_book(book_id):
    """This function allows the user to like a book. It adds the like to the database."""
    print("like_book is called once")
    existing_like = Like.query.filter_by(
        user_id=current_user.id, book_id=book_id
    ).first()
    print("existing_like", existing_like)
    if not existing_like and current_user.id != Book.query.get(book_id).user_id:
        like = Like(user_id=current_user.id, book_id=book_id)
        db.session.add(like)
        db.session.commit()
        return {"success": True}
    return {"success": False}


@app.route("/unlike_book/<int:book_id>", methods=["POST"])
@login_required
def unlike_book(book_id):
    """This function allows the user to unlike a book. It removes the like from the database."""
    like = Like.query.filter_by(user_id=current_user.id, book_id=book_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        return {"success": True}
    return {"success": False}


@app.route("/dashboard")
@login_required
def dashboard():
    """This function displays the user's dashboard. It shows the user's pending likes, book exchange matches, and book exchanges."""
    user_id = current_user.id
    pending_likes = get_pending_likes(user_id)
    matches = get_book_exchange_matches_with_objects(user_id)
    exchanges = get_user_exchanges(user_id)

    for book in pending_likes:
        book.is_liked = is_book_liked_by_user(book.id, current_user.id)

    for book1, book2 in matches:
        print("book1", book1)
        print("book2", book2)
        book1.is_liked = is_book_liked_by_user(book1.id, current_user.id)
        book2.is_liked = is_book_liked_by_user(book2.id, current_user.id)

    return render_template(
        "dashboard.html",
        pending_likes=pending_likes,
        matches=matches,
        exchanges=exchanges,
    )


@app.route("/exchange/<int:book1_id>/<int:book2_id>", methods=["GET", "POST"])
@login_required
def exchange(book1_id, book2_id):
    """This function allows the user to exchange two books. It updates the database to reflect the exchange."""
    print("exchange is called")
    book1 = Book.query.get_or_404(book1_id)
    book2 = Book.query.get_or_404(book2_id)

    if book1.user_id != current_user.id and book2.user_id != current_user.id:
        print("You can't exchange books you don't own.", "error")
        return redirect(url_for("dashboard"))

    mutual_like = Like.query.filter_by(user_id=book2.user_id, book_id=book1_id).first()
    if not mutual_like:
        flash(
            "The exchange cannot be completed as the interest is not mutual.", "error"
        )
        print("The exchange cannot be completed as the interest is not mutual.")
        return redirect(url_for("dashboard"))

    book1.user_id, book2.user_id = book2.user_id, book1.user_id

    new_exchange = Exchange(
        book_id_a=book1_id,
        book_id_b=book2_id,
        user_id_a=current_user.id,
        user_id_b=book2.user_id,
        status="accepted",
    )
    db.session.add(new_exchange)

    # Commit the changes to the database
    db.session.commit()

    print("Exchange completed successfully!", "success")
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)
