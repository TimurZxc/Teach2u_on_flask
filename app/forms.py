from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import Teacher, Educenter, Student, Parent


class TeacherRegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired(), Length(min=1, max=50)])
    last_name = StringField('Фамилия', validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    phone_number = StringField('Номер телефона', validators=[DataRequired(), Length(min=11, max=12)])
    password = PasswordField('Пароль', validators=[DataRequired(), Length(min=4, max=80)])
    direction = SelectField('Направление обучения', choices=[('Математическое'), ('Гуманитарное')])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')

    def validate_phone_number(self, phone_number):
        user = Educenter.query.filter(Educenter.phone_number==phone_number.data).first()
        user2 = Teacher.query.filter(Teacher.phone_number==phone_number.data).first()
        user3 = Student.query.filter(Student.phone==phone_number.data).first()
        user4 = Parent.query.filter(Parent.phone==phone_number.data).first()
        if user or user2 or user3 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')


    def validate_email(self, email):
        teacher = Teacher.query.filter_by(email=email.data).first()
        edu = Educenter.query.filter_by(email=email.data).first()
        if teacher or edu:
            raise ValidationError('Аккаунт с данной почтой уже существует')

        

class TeacherUpdateForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    phone_number = StringField('Номер телефона', validators=[DataRequired(), Length(min=11, max=12)])
    city = StringField('Город', validators=[Length(min=0, max=80)])
    format_ = SelectField('Формат обучения', choices=[('Онлайн'), ('Оффлайн'), ('Онлайн/Оффлайн')])
    languages = SelectField('Формат обучения', choices=[
                            ('Русский'), ('Английский'), ('Казахский')])    
    education = TextAreaField('Образование')
    experience = TextAreaField('Опыт')
    update = SubmitField('Обновить')

    def validate_phone_number(self, phone_number):
        user = Educenter.query.filter(Educenter.phone_number==phone_number.data).first()
        user3 = Student.query.filter(Student.phone==phone_number.data).first()
        user4 = Parent.query.filter(Parent.phone==phone_number.data).first()
        if user or user3 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')

    def validate_email(self, email):
        email1 = Educenter.query.filter_by(email=email.data).first()
        email3 = Student.query.filter_by(email=email.data).first()
        email4 = Parent.query.filter_by(email=email.data).first()
        if email1 or email3 or email4:
            raise ValidationError('Аккаунт с данной почтой уже существует')

        



class LoginForm(FlaskForm):
    email = StringField('Электронная почта', validators=[
                        DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[
                             DataRequired(), Length(min=4, max=80)])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class SubjectForm(FlaskForm):
    subject_name = StringField('Название', validators=[DataRequired()])
    subject_price = StringField(
        'Цена урока в час', validators=[DataRequired()])
    subject_description = TextAreaField(
        'Описание', validators=[DataRequired()])


class EduCenterRegistrationForm(FlaskForm):
    name = StringField('Название', validators=[
                       DataRequired(), Length(min=1, max=50)])
    email = StringField('Электронная почта', validators=[
                        DataRequired(), Email()])
    phone_number = StringField('Номер телефона', validators=[
                               DataRequired(), Length(min=11, max=12)])
    password = PasswordField('Пароль', validators=[
                             DataRequired(), Length(min=4, max=80)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Регистрация')
    address = StringField('Адрес', validators=[Length(min=0, max=80)])
    description = TextAreaField('Описание')

    def validate_phone_number(self, phone_number):
        user = Educenter.query.filter_by(
            phone_number=phone_number.data).first()
        user2 = Teacher.query.filter_by(phone_number=phone_number.data).first()
        user3 = Student.query.filter_by(phone=phone_number.data).first()
        user4 = Parent.query.filter_by(phone=phone_number.data).first()
        if user or user2 or user3 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')

    def validate_email(self, email):
        email1 = Educenter.query.filter_by(email=email.data).first()
        email2 = Teacher.query.filter_by(email=email.data).first()
        email3 = Student.query.filter_by(email=email.data).first()
        email4 = Parent.query.filter_by(email=email.data).first()
        if email1 or email2 or email3 or email4:
            raise ValidationError('Аккаунт с данной почтой уже существует')


        
class EduCenterUpdateForm(FlaskForm):
    email = StringField('Электронная почта', validators=[
                        DataRequired(), Email()])
    phone_number = StringField('Номер телефона', validators=[
                               DataRequired(), Length(min=11, max=12)])
    address = StringField('Адрес', validators=[Length(min=0, max=80)])
    description = TextAreaField('Описание')
    update = SubmitField('Обновить')

    def validate_phone_number(self, phone_number):
        user2 = Teacher.query.filter_by(phone_number=phone_number.data).first()
        user3 = Student.query.filter_by(phone=phone_number.data).first()
        user4 = Parent.query.filter_by(phone=phone_number.data).first()
        if user2 or user3 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')

    def validate_email(self, email):
        email2 = Teacher.query.filter_by(email=email.data).first()
        email3 = Student.query.filter_by(email=email.data).first()
        email4 = Parent.query.filter_by(email=email.data).first()
        if email2 or email3 or email4:
            raise ValidationError('Аккаунт с данной почтой уже существует')


class CourseForm(FlaskForm):
    course_name = StringField('Название', validators=[DataRequired()])
    course_price = StringField('Цена курса', validators=[DataRequired()])
    course_description = TextAreaField('Описание', validators=[DataRequired()])


class EduTeacher(FlaskForm):
    submit = SubmitField('Добавить учителя')
    update = SubmitField('Обновить')

    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамиллия', validators=[DataRequired()])
    info = TextAreaField('Информация', validators=[DataRequired()])
    languages = SelectField('Формат обучения', choices=[
                            ('Русский'), ('Английский'), ('Казахский')])


class ParentForm(FlaskForm):
    submit = SubmitField('Регистрация')
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамиллия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[
                               DataRequired(), Length(min=11, max=12)])
    password = PasswordField('Пароль', validators=[
                             DataRequired(), Length(min=4, max=80)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[
                                     DataRequired(), EqualTo('password')])

    def validate_phone(self, phone_number):
        user = Educenter.query.filter_by(phone_number=phone_number.data).first()
        user2 = Teacher.query.filter_by(phone_number=phone_number.data).first()
        user3 = Student.query.filter_by(phone=phone_number.data).first()
        user4 = Parent.query.filter_by(phone=phone_number.data).first()
        if user or user2 or user3 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')
        

    def validate_email(self, email):
        email1 = Educenter.query.filter_by(email=email.data).first()
        email2 = Teacher.query.filter_by(email=email.data).first()
        email3 = Student.query.filter_by(email=email.data).first()
        email4 = Parent.query.filter_by(email=email.data).first()
        if email1 or email2 or email3 or email4:
            raise ValidationError('Аккаунт с данной почтой уже существует')


        
class ParentUpdateForm(FlaskForm):
    update = SubmitField('Обновить')
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[
                               DataRequired(), Length(min=11, max=12)])
    def validate_phone(self, phone_number):
        user = Educenter.query.filter_by(phone_number=phone_number.data).first()
        user2 = Teacher.query.filter_by(phone_number=phone_number.data).first()
        user3 = Student.query.filter_by(phone=phone_number.data).first()
        if user or user2 or user3:
            raise ValidationError('Этот номер уже занят, попробуйте другой')
        

    def validate_email(self, email):
        email1 = Educenter.query.filter_by(email=email.data).first()
        email2 = Teacher.query.filter_by(email=email.data).first()
        email3 = Student.query.filter_by(email=email.data).first()
        if email1 or email2 or email3:
            
            raise ValidationError('Аккаунт с данной почтой уже существует')


class StudentForm(FlaskForm):
    submit = SubmitField('Регистрация')
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамиллия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[
                               DataRequired(), Length(min=11, max=12)])
    password = PasswordField('Пароль', validators=[
                             DataRequired(), Length(min=4, max=80)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[
                                     DataRequired(), EqualTo('password')])

    def validate_phone(self, phone_number):
        user = Educenter.query.filter_by(
            phone_number=phone_number.data).first()
        user2 = Teacher.query.filter_by(phone_number=phone_number.data).first()
        user3 = Student.query.filter_by(phone=phone_number.data).first()
        user4 = Parent.query.filter_by(phone=phone_number.data).first()
        if user or user2 or user3 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')
  
    def validate_email(self, email):
        email1= Educenter.query.filter_by(email=email.data).first()
        email2 = Teacher.query.filter_by(email=email.data).first()
        email3 = Student.query.filter_by(email=email.data).first()
        email4 = Parent.query.filter_by(email=email.data).first()
        if email1 or email2 or email3 or email4:
            raise ValidationError('Аккаунт с данной почтой уже существует')


        
class StudentUpdateForm(FlaskForm):
    update = SubmitField('Обновить')
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Номер телефона', validators=[
                               DataRequired(), Length(min=11, max=12)])

    def validate_phone(self, phone_number):
        user = Educenter.query.filter_by(
            phone_number=phone_number.data).first()
        user2 = Teacher.query.filter_by(phone_number=phone_number.data).first()
        user4 = Parent.query.filter_by(phone=phone_number.data).first()
        if user or user2 or user4:
            raise ValidationError('Этот номер уже занят, попробуйте другой')
  
    def validate_email(self, email):
        email1= Educenter.query.filter_by(email=email.data).first()
        email2 = Teacher.query.filter_by(email=email.data).first()
        email4 = Parent.query.filter_by(email=email.data).first()
        if email1 or email2 or email4:
            raise ValidationError('Аккаунт с данной почтой уже существует')

# class LoginForm(FlaskForm):
#    email = StringField('Электронная почта', validators=[DataRequired(),Email()])
#    password = PasswordField('Пароль', validators=[DataRequired(),Length(min= 4, max=80)])
#    remember = BooleanField('Запомнить меня')
#    submit = SubmitField('Войти')

# class UpdateForm(FlaskForm):
#    first_name = StringField('Имя',validators=[DataRequired(),Length(min= 1, max=50)])
#    last_name = StringField('Фамилия',validators=[DataRequired(),Length(min= 1, max=50)])
#    email = StringField('Электронная почта', validators=[DataRequired(),Email()])
#    submit = SubmitField('Загрузить')

#    def validate_username(self, username):
#       if username.data != current_user.username:
#          user = User.query.filter_by(username = username.data).first()
#          if user:
#             raise ValidationError('This username is already taked! Please choose another one.')

#    def validate_email(self, email):
#       if email.data != current_user.email:
#          email = User.query.filter_by(email = email.data).first()
#          if email:
#             raise ValidationError('This email is already taked! Please choose another one.')
