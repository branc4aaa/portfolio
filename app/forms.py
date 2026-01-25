from django.forms import Form, CharField, EmailField, Textarea

class ContactForm(Form):
    name = CharField(max_length=100, label='Your Name')
    email = EmailField(label='Your Email')
    message = CharField(widget=Textarea, label='Your Message')