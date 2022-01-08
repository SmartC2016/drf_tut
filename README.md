# drf_tut
Django Rest Framework Tutorial

This is the tutorial on Youtube https://youtu.be/PqkvRz1sLF8

If you add 'rest_framework.authtoken' to local apps and
this configuration in settings.py

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}

"Token" will appear in the admin menue. You can now create a Token for a user
and then "export MY_TOKEN={the just created token withour curly braces}"

If you then do:

http POST localhost:8000/books/ title="Your title" num_pages=222 'Authorization: Token '$MY_TOKEN

the book will be created
