=============
Documentation
=============
This readme is a work in progress.

============
Installation
============
Install Python
--------------
`Download Python here.<https://www.python.org/downloads/>`_
If you are on windows, I suggest making an installation path that has no spaces, for example:
C:\Python\Python35
This is due to tox/virtualenv breaking with spaces in the install path.
Also, make sure to add Python35 to your system path.

Install pytest-selenium via pip
-------------------------------
pip is a package installation tool for python. To install pytest-selenium all you have to do is type into command line:
pip install pytest-selenium -U

Install PyPOM via pip
---------------------
PyPOM is currently still in active development.

===================
Framework Breakdown
===================
Selenium
--------

Pytest
------

Pytest-Selenium
---------------
Including pytest-variables and pytest-html

PyPOM
-----

============
Test Writing
============


===================
Jenkins Integration
===================


====================
Test Runs and Triage
====================


===============
Further Reading
===============
`History of Pytest-Selenium from Dave Hunt <https://air.mozilla.org/mozilla-web-qa-re-volution-of-our-webdriver-based-python-testing-framework/>`_
`Pytest-Selenium Read The Docs <http://pytest-selenium.readthedocs.org/en/latest/>`_

==========
CODE TODO:
==========
- key press test suite development
- framework test suite development
- .loc file extension support for pytest-variables
  (would allow for a SPoM for locator values)
