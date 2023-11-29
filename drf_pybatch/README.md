```Virtual Machine
# Create a virtual environment to isolate our package dependencies locally
    python3 -m venv env or virtualenv venv
    source env/bin/activate  # On Windows use `env\Scripts\activate`
```

```DJango and drf install
# Install Django and Django REST framework into the virtual environment
    - pip install django
    - pip install djangorestframework
    - configure rest_framework in installed apps
```
```serializers.py
    - create serializer.py file in app
    - you can use any of these
        - class SnippetSerializer(serializers.Serializer):
        - class SnippetSerializer(serializers.ModelSerializer):
        - class SnippetSerializer(serializers.HyperLinkedSerializer):
```

```Views
- you can create views using following ways
    - Class Based Views ==>API View
    - Function Based Views ==> @api_view
    - Class Based Views ==> Mixins
    - Claass Based Views ==> Generics ==> simple

```

```HTTP Protocol: Hyper text transfer protocal
Rest Methods:
------------
GET:To read the datafrom database
POST: To create the data in database
PUT: To update the data in database ==> All payload ==> update
DELETE: To delete the data from database 
PATCH:  specifc field we should pass, no need to pass all data 
```
```HTTP Status
1xx informational response – the request was received, continuing process
2xx successful – the request was successfully received, understood, and accepted
3xx redirection – further action needs to be taken in order to complete the request
4xx client error – the request contains bad syntax or cannot be fulfilled
5xx server error – the server failed to fulfil an apparently valid request

1*
------------
100

2 *
----------
200 ok ==> success
201 ==> Data inserted to database or created
202 Accepted

3*
-------------
redirect

4*
---------
400 ==>Bad Request
401 ==> unauthorized access
403 ==> Forbidden
404 ==> url not found
405 Method Not Allowed

5 *
---------------
500 ==> internal server error
502 Bad Gateway
```

```DRF: Django Rest Framework

Django Application or jave application ==> API(payload)==>Postman ==> CRUD

```