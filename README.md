# Wagtail Quick Tutorial

## Overview

These are instructions to get a simple project started. This repo is up to date with the last step of the tutorial.

## Setup Project Folder with virtualenv

```
virtualenv -p python3 wagtail-demo
cd wagtail-demo
mkdir app
cd app
code .
```

## Install Wagtail

```
source ../bin/activate
pip install wagtail
wagtail start project
```

### Install Wagtail Dependencies

```
cd project
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Check to see if it worked

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Let's create an app

```
python manage.py startapp astronauts
```

project/astronauts/models.py

```python
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class AstronautsIndexPage(Page):
  intro_text = RichTextField(blank=True)
  intro_image = models.ForeignKey(
    'wagtailimages.Image',
    on_delete=models.SET_NULL,
    related_name='+',
    null=True,
    blank=True
  )

  content_panels = Page.content_panels + [
    FieldPanel('intro_text', classname="full"),
    ImageChooserPanel('intro_image'),
  ]

```

project/settings/base.py

```python
# add the app to your installed apps

INSTALLED_APPS = [
    'home',
    'search',
    'astronauts',

    'wagtail.contrib.forms',
    # ...
]


```

## Make & Run Migration

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Check to see if it worked

[http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

- Login with username/password (created during `createsuperuser`)
- Click Pages > Home > Add Child Page
- Choose "Astronauts Index Page"
- Fill out the details
- Click PUblish
- Click "View Live" (under the newly created page)
- Oh no, an error!

## Create Template File

```
mkdir astronauts/templates
mkdir astronauts/templates/astronauts
touch astronauts/templates/astronauts/astronauts_index_page.html
python manage.py runserver
```

- No error, but blank page

astronauts/templates/astronauts/astronauts_index_page.html

```jinja
{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}
{% block body_class %}template-astronauts-index-page{% endblock %}
{% block content %}

<h1>{{ page.title }}</h1>
<p>{{ page.intro_text|richtext }}</p>
{% image page.intro_image fill-1080x720 %}

{% endblock %}
```

- Refresh the page and check it out!
