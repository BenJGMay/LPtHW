try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'An example from LPTHW Exercise 47',
'author': 'Ben May',
'url': 'https://shop.learncodethehardway.org/paid/python3/ex47.html',
'download_url': 'https://shop.learncodethehardway.org/paid/python3/ex46.html',
'author_email': 'benjgmay@googlemail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['ex47'],
'scripts': [],
'name': 'ex47'
}

setup(**config)
