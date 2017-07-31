Simple Python Module Template
=============================

This simple python module template repo.

While the repo is public it is mostly intended for personal use,
and to have quick access to a template for my own work.

**Note:** I primarily write in Python 3 but have included *__future__* imports
and *__metaclass__* in *initmod/__init__.py* for basic backwards compatibility.

If Python 2.7 compatibility is a critical requirement the six module is advised.

If not I say **Fail Forward**

Basic tasks for new Module
--------------------------

- Move initmod directory to new name::

    $ mv initmod newname

- Edit setup.py to reflect the new project

  Find *nose* tests to change with the following::

    $ grep -ir "initmod" tests

  or use sed::

    $ sed -i 's/initmod/newname/g' tests/*

  where *newname* is the name of the project

- Code

- Profit

Setup docs Directory with Sphinx
--------------------------------

Run quickstart to configure Sphinx for project::

    $ cd docs
    $ sphinx-quickstart
