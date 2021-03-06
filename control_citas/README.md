# Control de citas médicas

## Run in production
`docker-compose -f docker-compose.prod.yml up -d --build`  

### Migrate tables

`docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`  

### Collecting static files

`docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`  

### Create superuser

`docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser`  
Output:  
 ```
Username (leave blank to use 'app'): admin
Email address:
Password:
Password (again):
The password is too similar to the username.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
 ```

## Run Developement
`docker-compose -f docker-compose.yml --build`  
`docker-compose -f docker-compose.yml up`
`docker-compose -f docker-compose.yml exec web python manage.py createsuperuser`  
Output:  
```
Username (leave blank to use 'app'): admin
Email address:
Password:
Password (again):
The password is too similar to the username.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Endpoints

#### Developement
- localhost:8000/pacientes/crear -> Creación de pacientes
- localhost:8000/pacientes/listar -> Listado de todos los pacientes
- localhost:8000/doctor/crear -> Creación de doctores
- localhost:8000/doctor/listar -> Listado de todos los doctores
- localhost:8000/cita/crear -> Creación de citas

#### Production
- localhost:1337/admin -> Sitio de administración
