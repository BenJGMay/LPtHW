try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
'description': 'My Project',
'author': 'Ben May',
'url': 'URL to get it at.',
'download_url': 'Where to downliad it.',
'author_email': 'benjgmay@googlemail.com',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['NAME'],
'scripts': [],
'name': 'projectname'
}

setup(**config)
