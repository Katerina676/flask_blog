from wtforms import Form, StringField, TextAreaField, FileField


class PostForm(Form):
    title = StringField('Title')
    text = TextAreaField('Text')