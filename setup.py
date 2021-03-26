from distutils.core import setup

setup(name='recepies',
      version='1.0',
      description='Book recepie web app',
      author='Gabriel Fr. Borges de Carvalho',
      author_email='gabrielfr.borges@gmail.com',
      python_requires='>=3.8.6',
      install_requires=[
          'Flask==1.1.2',
          'gunicorn==20.0.4',
          'pytest==6.2.2',
          'coverage==5.5',
          'blinker==1.4',
          'Flask-Injector==0.12.3',
      ])
