#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# def test():
#     from api_basic.models import Article
#     from api_basic.serializers import ArticleSerializer
#     from rest_framework.renderers import JSONRenderer
#     from rest_framework.parsers import JSONParser
#
#     a = Article(title='Article Title', author='Moseoh', email='azqazq195@gmail.com')
#     a.save()
#     a = Article(title='New Article', author='John', email='John@gmail.com')
#     a.save()
#
#     serializer = ArticleSerializer(a)
#     print(serializer.data)
#
#     content = JSONRenderer().render(serializer.data)
#     print(content)
#
#     serializer = ArticleSerializer(Article.objects.all(), many=True)
#     print(serializer.data)

def test():
    print("TEST")
    import jwt
    from djangoProject.settings import SECRET_KEY
    encoded = jwt.encode({"name": "문성하"}, SECRET_KEY, algorithm='HS256')
    print({"token": encoded})
    decoded = jwt.decode(encoded, SECRET_KEY, algorithms='HS256')
    print(decoded)
    decoded = jwt.decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6Mn0._5lRKHUSXDGVxhickAlllZEf5yBET3QrqgdRr8ZdJGE", SECRET_KEY, algorithms='HS256')
    print(decoded)
    print(decoded.get('token'))


if __name__ == '__main__':
    main()
    # test()
