"""
This is for pytest to find and stop being upset not finding any tests.

>>> 'Happy?'[:-1]
'Happy'
"""
from cps import version


def test_version_is_set():
    assert version.__version__
