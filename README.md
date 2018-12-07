# TennaGraph

## Install & Setup
- create file with name `.env` in `app` directory (TennaGraph/app/) with such info:


GITHUB_USERNAME=Your username on github <br />
GITHUB_PASSWORD=Your password on github <br />
SECRET_KEY=IPUWEpSFrXd-nzs4HKENG8G6-sHA9WqPStZpNw97tpY= <br />


- install Docker Engine
- open the project in terminal
- run command in the terminal `docker-compose up`
- wait several minutes
- in browser go to: http://localhost:8080 to see the user panel 
- in browser go to: http://localhost:8000/admin to see the django admin panel (login: admin, pass: 123456789)

## Trouble shootings
if http://localhost:8080 doesn't work:
- stop containers (press ctrl+c)
- run `docker-compose run fe bash`
- run `npm install`
- open the project in a new terminal window
- run command in the terminal `docker-compose up`
- wait several minutes
 

## Run Django app tests
- open the project in terminal
- run `docker-compose run app python manage.py test`

## Smart Contract
### VotingManager (TestNet Rinkeby)
address: 0xb662f0418fb5c501d9fbe437640c3856acc14f56
