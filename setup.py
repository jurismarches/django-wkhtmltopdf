import six
import wkhtmltopdf

from setuptools import setup, find_packages

requires = [
    'six>=1.5.2'
]

if six.PY3:
    requires.append('Django>=1.5')
else:
    requires.append('Django>=1.3')


setup(
    name='django-wkhtmltopdf',
    packages=find_packages(),
    include_package_data=True,
    version=wkhtmltopdf.__version__,
    description='Converts html to PDF using http://code.google.com/p/wkhtmltopdf/.',
    long_description=open('README.rst').read(),
    author=wkhtmltopdf.__author__,
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-wkhtmltopdf',
    install_requires=requires,
    zip_safe=False,
)
