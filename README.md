# LavishFrontend

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 15.2.8.

## Backend

### Development

1. You need Python 3.9
1. Clone the repository
1. `cd lavish-fe/backend/`
1. `pip install -r requirements/dev.txt`
1. `python manage.py migrate`
1. `python manage.py setup_superoot --commit`
1. `python manage.py runserver 0.0.0.0:8000`
1. Server is running on <http://localhost:8000>

### Helper Commands

Run them with `python manage.py <script>`

| Script | Description |
| ------------- | ------------- |
| `setup_superoot --commit` | Creates initial admin account. Default Username: _superoot_, Default Password: _lavishfilm!@#2023_ |
| `create_vehicle -n 1 --commit` | Creates sample vehicles. Pass in _n_ value to specify how many sample vehicles to be created, defaults to `1` if not specified |
| `create_salesorder --commit` | Creates a sample salesorder |
| `gimme_enum <enum_name>` | Prints the specified enum to console for frontend |


### Development with Docker

#### Setup

1. You need `docker` and `docker-compose`
    1. <https://docs.docker.com/get-docker/>
    1. <https://docs.docker.com/compose/install/>
1. Clone the repository
1. `cd lavish-fe/`
1. `docker-compose build`
1. `docker-compose up`

#### Connecting to containers

1. `docker exec -it lavish_django bash`
1. `docker exec -it lavish_pg_database bash`


## Frontend

### Development

1. You need Node 18
1. Clone the repository
1. `cd lavish-fe/frontend/`
1. `npm i`
1. `npm run start`
1. Open <http://localhost:4200>
