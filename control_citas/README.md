# Control de citas médicas

## Run in production
`docker-compose -f docker-compose.prod.yml up -d --build`
Migrate tables
`docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`
Collecting static files
`docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`

## Run Developement
`docker-compose -f docker-compose.yml --build`
`docker-compose -f docker-compose.yml up`

## Endpoints

#### Developement
- localhost:8000/pacientes/crear -> Creación de pacientes
- localhost:8000/pacientes/listar -> Listado de todos los pacientes
- localhost:8000/doctor/crear -> Creación de doctores
- localhost:8000/doctor/listar -> Listado de todos los doctores
- localhost:8000/cita/crear -> Creación de citas

#### Production
- localhost:1337/admin -> Sitio de administración
