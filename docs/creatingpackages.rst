.. highlight:: shell

============
Using Twine to upload package to pypi or testpypi
============


Registering your account
---------
Because TestPyPI has a separate database from the live PyPI, you’ll need a separate user account for specifically for
TestPyPI. Go to testpyi_ to register your account.

Note: The database for TestPyPI may be periodically pruned, so it is not unusual for user accounts to be deleted.

.. _testpyi: https://test.pypi.org/account/register/


Using TestPyPI with Twine
--------
You can upload your distributions to TestPyPI using twine by passing in the --repository-url flag

    $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*


Using TestPyPI with pip
-------
You can tell pip to download packages from TestPyPI instead of PyPI by specifying the --index-url flag

    $ pip install --index-url https://test.pypi.org/simple/ your-package
