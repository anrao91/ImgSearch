
# ImgSearch

ImgSearch is a Tag based search engine. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* accounts (User registration, Login, Profile management)
* santa_search (Load images from [Pixabay][2], Store it in redis, facilitate search)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ virtualenv ImgSearch`
    2. `$ . ImgSearch/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Dependancies 
* redis-server

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://pixabay.com