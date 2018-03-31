from wtforms import Form, StringField, TextAreaField, PasswordField, SelectField, FloatField, FormField, TextAreaField,  validators

#registration class that takes form data from html

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email= StringField('Email', [validators.Length(min=6, max=50)])
    password  =PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')

class MultiForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    description = TextAreaField('Description')

class LangForm(Form):
    lang = SelectField('Language', choices = [
        ('cpp','C'), 
        ('c','C++'), 
        ('py','Python'),
        ('java','Java'),
        ('js','JavaScript'),
        ('rb','Ruby'),
        ('go','Go'),
        ('s','Assemby'),
        ('mat','Matlab'),
        ('na','None')
        ])

    skill = SelectField('Skill Level', choices = [
        ('0', 'No Experience'),
        ('1', 'Beginner'),
        ('2', 'Advancing'),
        ('3', 'Intermediate'),
        ('4', 'Advanced'),
        ('5', 'Expert')
        ])
    

class EditProfile(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    degree = SelectField('Degree', choices = [('compe','Computer Engineering'), 
    ('softeng','Software Engineering'), 
    ('compsci','Computer Science')])

    year = SelectField('Year', choices = [('1st','First Year'), 
    ('2nd','Second Year'), 
    ('3rd','Third Year'), 
    ('4th','Fourth Year'), 
    ('5th','Fifth Year+'), 
    ('gd','Graduated')])

    gpa = FloatField('GPA', [validators.Length(min=2, max=2)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    github = StringField('GitHub Link', [validators.Length(min=6, max=50)])
    bio = TextAreaField('Bio (Less than 100 words)')

    #projects field
    First_Project = FormField(MultiForm)
    Second_Project = FormField(MultiForm)
    Third_Project = FormField(MultiForm)
    #work Experience field
    Work_Experience_One = FormField(MultiForm)
    Work_Experience_Two = FormField(MultiForm)
    Work_Experience_Three = FormField(MultiForm)
    #languages field
    Language_1 = FormField(LangForm)
    Language_2 = FormField(LangForm)
    Language_3 = FormField(LangForm)
    Language_4 = FormField(LangForm)
    Language_5 = FormField(LangForm)
    Language_6 = FormField(LangForm)
    Language_7 = FormField(LangForm)
    #skill tree