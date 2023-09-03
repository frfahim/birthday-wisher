# Birthday Wisher

Birthday wisher is a django based application, that wishes on customers birthday automatically.


### Tech
- Python
- Django
- Django Rest Framework
- Celery

### Installation

- Clone repo  `git clone git@github.com:frfahim/birthday-wisher.git`

- Goto project directory `cd birthday-wisher`

- Install requirement file `poetry install`

- Enter to virtual env created by Poetry `poetry shell`

- To run the projects

```
python manage.py migrate
python manage.py runserver
```

- Create a superuser `python manage.py createsuperuser`

- Or, Run project via bash command `./run_tapp.sh`


> If script file get permission error run `chmod +x run_tapp.sh` and hit `./run_tapp.sh` again
