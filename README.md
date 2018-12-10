# TennaGraph

## Install & Setup
- create file with name `.env` in `app` directory (TennaGraph/app/) with such info:


GITHUB_USERNAME=Your username on github<br />
GITHUB_PASSWORD=Your password on github<br />


- install Docker Engine
- open the project in terminal
- run command in the terminal `docker-compose up`
- wait several minutes
- in browser go to: http://localhost:8080 to see the user panel 
- in browser go to: http://localhost:8000/admin to see the django admin panel (login: admin, pass: 123456789)

## Trouble shootings
### if http://localhost:8080 doesn't work:
- stop containers (press ctrl+c)
- run `docker-compose run fe bash`
- run `npm install`
- open the project in a new terminal window
- run command in the terminal `docker-compose up`
- wait several minutes

###  if workers don't work, and you have the message in the terminal `ERROR: Pidfile (celerybeat.pid) already exists`:
- delete `celerybeat.pid` file in TennaGraph/app/ folder
- restart the project

## Run Django app tests
- open the project in terminal
- run `docker-compose run app python manage.py test`

## Smart Contract
### VotingManager (TestNet Rinkeby)
address: 0xc82d2f9b1e661d5238907e58bcaf6d8fe964fcc9

# Smart-Contracts Suite
Smart Contracts + Tests

To install all dependencies for smart contracts open TennaGraph/smart_contracts folder in your terminal and run:
``` bash
npm install
```

Then to run tests:
``` bash
npm run test
```

To run code-coverage:
``` bash
npm run cov
```