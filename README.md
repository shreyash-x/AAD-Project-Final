# AAD Project

## AlgoBook

- This is a website developed as part of my AAD project which covers several algorithms in a beautiful manner.

## How to install

- Download and extract the zip file.
- Open a terminal in the downloaded folder.

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver # default port 8000
```

- Access the web app in browser on : http://127.0.0.1:8000/
