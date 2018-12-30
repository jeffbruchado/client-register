## Client-Register-Hash-Generator

This project is a based in a client register to generate a hash based on your CPF, bitcoin style;

This project consists of two applications, the Backend and the Frontend that consumes the Backend;

Backend is build using Python/Django REST Framework and the way development has been done is to extend django's user model authentication by adding the fields required for client registration;

To configure this project, follow the steps below:

### Installation

First of all you will have to download the project, run the following command:

```sh
$ git clone https://github.com/Jack3Dz/client-register.git
```

You will now need to have Python 3 installed on your machine, if you do not have it yet, you can download it at the following link:

I recommend you use the version that is most used by all users - https://www.python.org/

Once you have Python installed, you will need to access the application directory:

```sh
$ cd client-register\backend
```

After accessing the application directory, you will need to install the project dependencies by running the following command:

```sh
$ pip install -r requirements.txt
```

After that you will need to perform the application migrations by running the following commands:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

After that you'll be able to run the application:

```sh
$ python manage.py runserver
```

To run the tests run the following command:

```sh
$ python manage.py test
```
