from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Optional, EqualTo

from .models import Category


def get_categories():
    categories = Category.query.all()
    return [(category.id, category.title) for category in categories]


class AddNewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired(message='Поле должно быть заполнено'),
                                                 Length(max=256, message='Заголовок не может превышать 256 символов')])
    text = TextAreaField('Новость', validators=[DataRequired(message='Поле должно быть заполнено')])
    category = SelectField('Категория', choices=get_categories())
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить меня")
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[DataRequired()])
    name = StringField("Имя", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='некорректный email')])
    password = PasswordField("Пароль", validators=[DataRequired()])
    password2 = PasswordField("Повторите пароль",
                              validators=[DataRequired(), EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')


class CategoryForm(FlaskForm):
    title = StringField("Название категории", validators=[DataRequired()])
    submit = SubmitField('Добавить')
