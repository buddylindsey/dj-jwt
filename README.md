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

Include Urls

```python
path("token/", include(("djjwt.urls", "djjwt"), namespace="dj-jwt"))
```

Creates

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
