# TennaGraph

## Install & Setup
- create file with name `.env` in `app` directory (TennaGraph/app/) with such info:


GITHUB_USERNAME=Your username on github (disable 2FA)<br />
GITHUB_PASSWORD=Your password on github<br />
TWITTER_CONSUMER_KEY=See below<br />
TWITTER_CONSUMER_SECRET_KEY=See below<br />
TWITTER_ACCESS_TOKEN_KEY=See below<br />
TWITTER_ACCESS_TOKEN_SECRET_KEY=See below<br />

To get credentials for twitter, please, follow the instructions:<br />
https://python-twitter.readthedocs.io/en/latest/getting_started.html

- install Docker Engine
- open the project in terminal
- run command in the terminal `docker-compose up --build`
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
address: 0x342dF3b4190a6C6eBD0Dc69F4cC3f9deEE928c33

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
