# dj-jwt

Dj-JWT is a JSON Web Token authentication plugin for vanilla django built on Simple JWT. This is a thin layer on Simple JWT, it should not need to be updated too regularly.

## Acknowledgments

[Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt) is a great jwt library, and is updated regulary. However, it is based soley for rest framework. This library is a thin layer on top of that which uses Simple JWT, but lets you use it with vanilla django.

## Getting Started

### Install

dj-jwt can be installed with pip:

```
pip install dj-jwt
```

Add 'djjwt' to your `INSTALLED_APPS` setting.

```
INSTALLED_APPS = [
    ...
    'djjwt',
]
```

If you are wanting to use the urls built in just add the following your projects `urls.py`

```python
path("token/", include(("djjwt.urls", "djjwt"), namespace="dj-jwt"))
```

Add the middleware to your middleware

```python
MIDDLEWARE = [
    ...
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "djjwt.middleware.DjangoJWTAuthentication",
]
```

### URL Usage

```
/token/authenticate/
/token/refresh/
/token/verify/
```

```python
from django.urls import reverse_lazy

reverse_lazy('jwt-token:authenticate')
reverse_lazy('jwt-token:refresh')
reverse_lazy('jwt-token:verify')
```

### Commands

You can create an access and refresh token on the command line to make testing easier.

```
./manage.py create_tokens --userid=2
./manage.py create_tokens --email=buddy@example.com
./manage.py create_tokens    # Grabs the first user in the system
```

Example output

```
Tokens for: Buddy Lindsey <buddy@example.com>
Access Token:  eyJ0...
Refresh Token: eyJ0...
```
