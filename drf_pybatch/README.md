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
    - Claass Based Views ==> Generics

```