try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'An erxample from LPTHW Exercise 46',
'author': 'Ben May',
'url': 'https://shop.learncodethehardway.org/paid/python3/ex46.html',
'download_url': 'https://shop.learncodethehardway.org/paid/python3/ex46.html',
'author_email': 'benjgmay@googlemail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['ex46'],
'scripts': [],
'name': 'ex46'
}

setup(**config)
