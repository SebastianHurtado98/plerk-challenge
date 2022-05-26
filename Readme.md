# PLERK CHALLENGE
Deployado en este [link](http://ec2-34-224-56-23.compute-1.amazonaws.com/) (solo http).
Documentación del api en este [link](http://ec2-34-224-56-23.compute-1.amazonaws.com/redoc/).

## CORRER EL PROYECTO:
- Clonar el repositorio
- Ir al repositorio
- docker compose build
- docker compose run django python3 manage.py migrate companies
- docker compose run django python3 manage.py migrate transactions
- docker compose run django python3 manage.py migrate
- docker compose run django python3 manage.py shell
- Dentro de shell usar las funciones para poblar la base de datos (también se podría crear un comando para ello).
    - from plerk.companies.dummy_data.import_csv import get_companies, get_transactions
    - get_companies()
    - get_transactions()
- docker compose up
- Ir a la [documentación](http://localhost/redoc/) y probar los endpoints (las vistas web de DRF están disponibles).

## CONSIDERACIONES:
Ambiente de desarrollo: He obviado algunas buenas prácticas de producción por comodidad:
- Debug=True para seguir debuggeando.
- Gunicorn no implementado.
- .env se encuentra en el repositorio por comodidad.

## ADICIONAL:
- Filtro para endpoint transactions: Filtrar por rango de precio, fecha, status puede ser importante para obtener insights de la data. 
- Documentación: Es vital para toda API. Usé el paquete redoc.
- Ambiente Docker: Importante para otros programadores que quieran usarlo.

## TEST API:
Puede descargar una colección de Postman de este [drive](https://drive.google.com/drive/u/1/folders/1y6QNKMc9VmQpM1qzis2pEMgHNM8j-Ou8).

## TODO:
- Price: Ver si es necesario modificar este requerimiento.

## NICE TO HAVE:
- Ambiente de deploy de producción.
- Implementación de cache para consultas pesadas.
