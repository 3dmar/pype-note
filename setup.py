import setuptools
from distutils.core import setup


setup(name = "pypenote",
    author = "Adinan Paiva",
    author_email = "paiva.adinan@gmail.com",
    version = "1.0",
    packages = setuptools.find_packages('lib'),
    package_dir = {"" : "lib"},
    install_requires = ['evernote', 'html2text'],
    data_files = [('/etc/pypenote', ['etc/config.ini'])],
    entry_points = {"console_scripts": ["pypenote = pypenote.pypenote:main"]}
    )
