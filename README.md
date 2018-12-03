# TennaGraph

## Install & Setup
- create file with name `.env` in `app` directory (TennaGraph/app/) with such info:

`
GITHUB_USERNAME=Your username on github
GITHUB_PASSWORD=Your password on github
SECRET_KEY=IPUWEpSFrXd-nzs4HKENG8G6-sHA9WqPStZpNw97tpY=
`

- install Docker Engine
- open the project in terminal
- run command in the terminal `docker-compose up`
- wait several minutes
- in browser go to: http://localhost:8080 to see the user panel 
- in browser go to: http://localhost:8000/admin to see the django admin panel (login: admin, pass: 123456789)


## Run Django app tests
- open the project in terminal
- run `docker-compose run app python manage.py test`
