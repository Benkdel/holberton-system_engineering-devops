Application Server


guide:

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

from this guide only do the following:
    - install gunicorn but globally, not in ve
    - set up a system to create a sock in working directory (modify paths to global, not env)
    - dont use a diferent file por WSGI, use same as flask app
    - modify the same nginx default file, adding a location with proxy red
