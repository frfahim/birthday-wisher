# Birthday Wisher

Birthday wisher is a django based application, that wishes on customers birthday automatically.


### Tech
- Python
- Django
- Django Rest Framework
- Celery
- Redis

### Installation

- Clone the repo  `git clone git@github.com:frfahim/birthday-wisher.git`

- Goto project directory `cd birthday-wisher`

- Used poetry here, To Install necessary packages `poetry install`

- If you are not using poetry then create an virtual enviornment and install pakages `pip install -r requirements.txt`

- Copy `.env.sample` file then create a file `.env` (make sure you have changed env value with your data) without env file project wont run
`cp .env.sample .env`

- Enter to virtual env created by Poetry `poetry shell`

- To run the projects

```
python manage.py migrate
python manage.py runserver
```

- Create a superuser `python manage.py createsuperuser`

- Or, Run project via bash command `./run_app.sh`

> If the script file get permission error run `chmod +x run_app.sh` and hit `./run_app.sh` again

We need to install redis as a message broker, install from here, [installation](https://redis.io/docs/getting-started/installation/)

Run redis server

```
redis-server
```

Now run the celery

```
celery -A conf worker -l info --beat
```


### API's

We have api's to create or update customer and get a list of customers or retrieve a single customer

<details>
<summary> Customer Create API </summary>


POST API URL
```
localhost:8000/api/v1/customers/
```

payload
```
{
  "name": "Fahim 1",
  "email": "user.email+1@gmail.com",
  "birthdate": "2023-09-04"
}
```
Response
```
{
  "id": 1,
  "name": "Fahim 1",
  "birthdate": "2023-09-04",
  "email": "user.email+1@gmail.com"
}
```
</details>


<details>
<summary> Customer List </summary>


GET API URL
```
localhost:8000/api/v1/customers/
```

Response
```
[
  {
    "id": 1,
    "name": "Fahim 1",
    "birthdate": "2023-09-04",
    "email": "user.email+1@gmail.com"
  },
  {
    "id": 2,
    "name": "Fahim 2",
    "birthdate": "2023-08-04",
    "email": "user.email+2@gmail.com"
  }
]
```
</details>


<details>
<summary> Customer Update API </summary>


PUT API URL
```
localhost:8000/api/v1/customers/<id>/
```

PUT payload
```
{
  "name": "Fahim 1",
  "birthdate": "2023-09-05"
}
```
Response
```
{
  "id": 1,
  "name": "Fahim 1",
  "birthdate": "2023-09-05",
  "email": "user.email+1@gmail.com"
}
```
</details>


<details>
<summary> Customer Get API </summary>


GET API URL
```
localhost:8000/api/v1/customers/<id>/
```

Response
```
{
  "id": 1,
  "name": "Fahim 1",
  "birthdate": "2023-09-05",
  "email": "user.email+1@gmail.com"
}
```
</details>


#### TODO:
 - Docker support and docker-compose
 - Add ruff, mypy for better coding style
 - Integrate pre-commit to automate code checking
