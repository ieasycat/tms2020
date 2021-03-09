from django.forms import Form, CharField, IntegerField


class UserForm(Form):
    firstname = CharField(min_length=1, max_length=15, label='First name')
    lastname = CharField(min_length=1, max_length=15, label='Last name')
    old = IntegerField(min_value=1, max_value=99)
