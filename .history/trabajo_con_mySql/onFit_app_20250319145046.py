# Esto nos servirá para llamar a clienteDAO para realizar insert, update, delete, etc.
# Aquí se gestionan las rutas de la API
from clienteDAO import ClienteDAO
from cliente import Cliente

print('**** Clientes de On Fit *****')
opcion = None
while opcion != 5:
    print('''Menú:
          1. Listar Cliente
          2. Agregar cliente
          3. Modificar cliente
          4. Eliminar cliente
          5. Salir''')
    
    opcion = int(input('Escribe la opción (1 a 5): '))
    if opcion == 1:
        print('\n Listado de clientes')
        cliente_lista = ClienteDAO.seleccionar()
        for cliente in cliente_lista:
            print(cliente)
            
        print()
    
    elif opcion == 2:
        cliente_nombre   = input('Nombre del cliente  : ')
        cliente_apellido = input('Apellido del cliente: ')
        cliente_edad     = int(input('Edad del cliente: '))
        cliente_tel      = input('Teléfono del Cliente: ')
        
        cliente_insert = Cliente(cliente_nombre, cliente_apellido, cliente_edad, cliente_tel)
        cliente_a_insertar = ClienteDAO.insertar(cliente_insert)
        print(f'\nCliente {cliente_insert.nombre} insertado.\n')
        
    elif opcion == 3:
        