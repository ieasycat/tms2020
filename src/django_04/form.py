from django.forms import Form, CharField, IntegerField


class UserForm(Form):
    firstname = CharField(min_length=1, max_length=15)
    lastname = CharField(min_length=1, max_length=15)
    old = IntegerField(min_value=1, max_value=99)
