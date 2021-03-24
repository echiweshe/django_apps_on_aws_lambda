from django.db import models

# Create your models here.
# Here, each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.
# Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.

# The name of each Field instance in your Python code will be used in your  database as the column name.

# You can use an optional first positional argument to a Field to designate a human-readable name. e,g, pub_date = models.DateTimeField('date published'). 
# Some Field classes have required arguments. For example, CharField requires a max_length. That’s used not only in the database schema, but in validation.
# A Field can also have various optional arguments; e.g. set the default numerical value to 0, or a text field withplace holder text.

# Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

# The follwoing commands tell Django is able to:
# Create a database schema (CREATE TABLE statements) for this app.
# Create a Python database-access API for accessing Question and Choice objects.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# By running makemigrations, (with the cli command $ python manage.py makemigrations stats) you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

# Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file stats/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.

# There’s a command that will run the migrations for you and manage your database schema automatically - that’s called migrate, and we’ll come to it in a moment - but first, let’s see what SQL that migration would run. The sqlmigrate command takes migration names and returns their SQL: $ python manage.py sqlmigrate polls 0001