.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/collective/cs.ploneformdemo.svg?branch=master
    :target: https://travis-ci.org/collective/cs.ploneformdemo

.. image:: https://coveralls.io/repos/github/collective/cs.ploneformdemo/badge.svg?branch=master
    :target: https://coveralls.io/github/collective/cs.ploneformdemo?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/cs.ploneformdemo.svg
    :target: https://pypi.python.org/pypi/cs.ploneformdemo/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/cs.ploneformdemo.svg
    :target: https://pypi.python.org/pypi/cs.ploneformdemo
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/cs.ploneformdemo.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/cs.ploneformdemo.svg
    :target: https://pypi.python.org/pypi/cs.ploneformdemo/
    :alt: License


================
cs.ploneformdemo
================

This product is a demo product to check how a z3c.form based form is rendered in a Plone site. This is useful when designing the site, to check
all the special features that a form needs, such as required fields, error messages, etc.




Installation
------------

Install cs.ploneformdemo by adding it to your buildout::

    [buildout]

    ...

    eggs =
        cs.ploneformdemo


and then running ``bin/buildout``


After installing the addon using the Plone Control Panel, you can go to these URLs to check the forms:

- Full form: http://plonesite.com/test-form-view
- Full form with fieldsets: http://plonesite.com/test-form-fieldsets-view



Contribute
----------

- Issue Tracker: https://github.com/collective/cs.ploneformdemo/issues
- Source Code: https://github.com/collective/cs.ploneformdemo


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
