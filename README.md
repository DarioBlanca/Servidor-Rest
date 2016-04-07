# Servidor-Rest
Servidor para alta de conexiónes, de tipo restfull y con mucha onda. La finalidad de dicho servidor es devolver al cliente un listado clientes conectados en el mismo momento. Salud!

Ejemplo de uso:

pip install httpie

$ http POST http://127.0.0.1:8000/api/servicio-a-consumir usuario="" password="" ippublica="" ipprivada=""

el methodo del pedido varia en base a lo que se quiera hacer con el usuario
Metodos: POST - PUT - DELETE

Para mas info ver /servidor/api/views.py (se re entiende)
