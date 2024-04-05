from models import User
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    EmailField,
    TextAreaField,
    IntegerField,
    FloatField,
)
from wtforms.validators import (
    InputRequired,
    Length,
    ValidationError,
    NumberRange,
    DataRequired,
    Optional,
)


class RegisterForm(FlaskForm):
    """Form for registering a new user."""

    name = StringField(
        "Name",
        validators=[InputRequired(), Length(max=80)],
        render_kw={"placeholder": "Name"},
    )
    email = EmailField(
        "Email",
        validators=[InputRequired(), Length(max=120)],
        render_kw={"placeholder": "Email"},
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8)],
        render_kw={"placeholder": "Password"},
    )
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already in use.")
        return True


class LoginForm(FlaskForm):
    """Form for logging in a user."""

    email = EmailField(
        "Email",
        validators=[InputRequired(), Length(max=120)],
        render_kw={"placeholder": "Email Address"},
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=8)],
        render_kw={"placeholder": "Password"},
    )
    submit = SubmitField("Login")

    def validate_email(self, field):
        if not User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is not registered.")
        return True


class BookForm(FlaskForm):
    """Form for adding a new book."""

    title = StringField(
        "Title",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Title"},
    )
    author = StringField(
        "Author (s)",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Author (s)"},
    )
    genre = StringField(
        "Genre",
        validators=[Optional(), Length(max=100)],
        render_kw={"placeholder": "Genre"},
    )
    year = IntegerField(
        "Year",
        validators=[Optional(), NumberRange(min=0, max=9999)],
        render_kw={"placeholder": "Year"},
    )
    rating = FloatField(
        "Rating",
        validators=[Optional(), NumberRange(min=0.0, max=5.0)],
        render_kw={"placeholder": "Rating out of 5"},
    )
    review = TextAreaField(
        "Review", validators=[Optional()], render_kw={"placeholder": "Review"}
    )
    summary = TextAreaField(
        "Summary", validators=[Optional()], render_kw={"placeholder": "Summary"}
    )
    submit = SubmitField("Submit")
