[![Codacy Badge](https://api.codacy.com/project/badge/Grade/67645d217d094e27b72c90cc0656fafc)](https://app.codacy.com/app/dev-jey/Store-Manager-v1?utm_source=github.com&utm_medium=referral&utm_content=codeMarble254/Store-Manager-v1&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/dev-jey/Store-Manager-v1.svg?branch=develop)](https://travis-ci.org/dev-jey/Store-Manager-v1)
[![Maintainability](https://api.codeclimate.com/v1/badges/844b5306d2d6cae17f34/maintainability)](https://codeclimate.com/github/dev-jey/Store-Manager-v1/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/dev-jey/Store-Manager-v1/badge.svg?branch=develop)](https://coveralls.io/github/dev-jey/Store-Manager-v1?branch=develop)

# Store-Manager
## This is a simple store management application

### To run this project you should follow the following steps

**Find the app on heroku**  

<https://jemo-store-manager.herokuapp.com/> 

    1. Create a virual enviroment with the command

```
    $ virtualenv -p python3 env
```

    2. Activate the env with the command

```
    $ source env/bin/activate
```

    3. Install git
```
    sudo apt install git

```

    4. clone this repo
```
    $ git clone https://github.com/codeMarble254/Store-Manager-v1.git
```
    5. cd into the folder 
```
    Store-Manager-v1
```

    6. export environment variables 
```
    $ export DB_URL="storemanager"
    $ export TEST_DB_URL="test_db"
    $ export APP_SETTINGS="development"
    $ export SECRET_KEY="{your key}"
    $ export FLASK_APP=run.py
    $ export EMAIL="email"
    $ export PASSWORD="password"
```

    7. create the development database
```
    createdb storemanager
```

    8. create the testing database
```
    $ createdb test_db
```

    9. Switch to `develop` branch
```
    $ git checkout develop
```

    10. install requirements
```
    $ pip install -r requirements.txt
```

### Now we are ready to run

    11. for tests run
```
    pytest -v --cov=app
```

    12. for the application run  
```
    $ flask run
```
### If you run the aplication, you can test the various api endpoints using postman

The api endpoints are

| Endpoint                   | Description                   |
| ---                        | ---                           |
| GET /products              | Fetch all products            |
| GET /products/productId    | Fetch a single product record |
| GET /sales                 | Fetch all sale records        |
| GET /sales/saleId          | Fetch a single sale record    |
| POST /products             | Create a product              |
| POST /sales                | Create a sale order           |
| POST /auth/signup          | Signup a user                 |
| POST /auth/login           | Login a user                  |
| PUT /users/userId          | Update a user                 |
| POST /auth/logout          | Logout a user                 |
| PUT /products/productId    | Update a product              |
| DELETE /products/productId | Delete a product              |

## **Resources used** 

<https://travis-ci.org/> \
<https://apiary.io/> \
<https://codeclimate.com/> \
<https://coveralls.io/> \
Python \
Flask \
Postgres SQL

