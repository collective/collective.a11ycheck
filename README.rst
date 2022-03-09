.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/collective/collective.a11ycheck.svg?branch=master
    :target: https://travis-ci.org/collective/collective.a11ycheck

.. image:: https://coveralls.io/repos/github/collective/collective.a11ycheck/badge.svg?branch=master
    :target: https://coveralls.io/github/collective/collective.a11ycheck?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/collective.a11ycheck.svg
    :target: https://pypi.python.org/pypi/collective.a11ycheck/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/collective.a11ycheck.svg
    :target: https://pypi.python.org/pypi/collective.a11ycheck
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/collective.a11ycheck.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/collective.a11ycheck.svg
    :target: https://pypi.python.org/pypi/collective.a11ycheck/
    :alt: License


====================
collective.a11ycheck
====================

Reports accessibility issues to your site editors when a page is saved.

When an editor saves a page (any content) in Plone, a11ycheck runs a subscriber that checks the full HTML of the page, and will display an alert to the editor if the page fails any of the set accessibility checks.

Initially, a11ycheck only checks against two issues. These are configurable through a control panel for whether or not your site will report these issues to the editors:

* Each page should have exactly 1 <h1>
* Each image should have alt text

Since the entire page's HTML is checked, issues that exist in the templates will also be reported. Works with regular Plone types and Mosaic pages.

The control panel includes the following configuration:

* Which issues will be reported (all enabled by default)
* Which content types will report issues on add (all enabled by default)
* Which content types will report issues on edit (all enabled by default)

The subscriber runs against all Dexterity types on add and on edit. If you have content types that open the Mosaic editor as soon as the page is added, you will want to disable the subscriber on add for that type.


Installation
------------

Install collective.a11ycheck by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.a11ycheck


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.a11ycheck/issues
- Source Code: https://github.com/collective/collective.a11ycheck


License
-------

The project is licensed under the GPLv2.
