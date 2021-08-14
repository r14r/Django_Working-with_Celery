# Example Django project using Celery

## Components

### RabbitMQ

localhost:15672

### Flower

localhost:15672

## Contents

``main/``
---------

This is a project in itself, created using
``django-admin.py startproject main``, and then the settings module
(``main/settings.py``) was modified to add ``app_celery`` to
``INSTALLED_APPS``

``main/celery.py``
----------

This module contains the Celery application instance for this project,
we take configuration from Django settings and use ``autodiscover_tasks`` to
find task modules inside all packages listed in ``INSTALLED_APPS``.

``app_celery/``
------------

Example generic app.  This is decoupled from the rest of the project by using
the ``@shared_task`` decorator.  This decorator returns a proxy that always
points to the currently active Celery instance.

Installing requirements
=======================

The settings file assumes that ``rabbitmq-server`` is running on ``localhost``
using the default ports. More information here:

http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html

In addition, some Python requirements must also be satisfied:

.. code-block:: console

    $ pip install -r requirements.txt

Starting the worker
===================

.. code-block:: console

    $ celery -A proj worker -l INFO

Running a task
===================

.. code-block:: console

    $ python ./manage.py shell
    >>> from app_celery.tasks import add, mul, xsum
    >>> res = add.delay(2,3)
    >>> res.get()
    5
