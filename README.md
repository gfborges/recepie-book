# RECEPIES BOOK
This is a Recepie book web app project made in Flask.

### Install 
Install required python libraries for the setup.
```
$ python3 -m pip install virtualenv setuptools 
```
Create a virtual enviroment (windows users should use `./env/Scripts/activate.bat`)
```
$ python3 -m virtualenv env
$ source env/bin/activate
```
Install the dependencies with the following command:
```
(env)$ pip install -e .
```
Using this instead of `pip install -r requirements.txt` allows the project to ensure python version and use absolute imports.
To turn off the virtual enviroment run `deactivate`
### Aplication
The aplication runs by defult in the localhost:5000. To run the aplication execute the shell script or copy the commando to the terminal
```
$ ./serve
```
The scipt above does not support windows, use `(env)$ python recepie/main.py` to run without with guinicorn. 
### Database
To config the persistence, run the `config.sql` and `schema.sql` scripts.

### Test
The tests run with the command `pytest`, for coverage details run `coverage report` or `coverage` 

### Presentations
 * [Prototype](https://youtu.be/2MtCiCcfWuE)
 * [Persistence](https://youtu.be/rZ5X5Vafx8M)
### Author
[Gabriel Fr. Borges](https://github.com/gfborges)
