from distutils.core import setup

setup(name='recepies',
    version='1.0',
    description='Book recepie web app',
    author='Gabriel Fr. Borges de Carvalho',
    author_email='gabrielfr.borges@gmail.com',
    python_requires='>=3.8.6',
    install_requires=[
        'flask',
        'gunicorn',
        'pytest',
        'coverage',
        'blinker',
        'flask-injector',
    ])
