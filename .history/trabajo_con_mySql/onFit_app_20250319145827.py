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
    
    if opcion == 1:  # listar clientes
        print('\n Listado de clientes')
        cliente_lista = ClienteDAO.seleccionar()
        for cliente in cliente_lista:
            print(cliente)
            
        print()
    
    elif opcion == 2:   # agregar cliente
        cliente_nombre   = input('Nombre del cliente  : ')
        cliente_apellido = input('Apellido del cliente: ')
        cliente_edad     = int(input('Edad del cliente: '))
        cliente_tel      = input('Teléfono del Cliente: ')
        
        cliente_insert = Cliente(cliente_nombre, cliente_apellido, cliente_edad, cliente_tel)
        cliente_a_insertar = ClienteDAO.insertar(cliente_insert)
        print(f'\nCliente {cliente_insert.nombre} insertado.\n')
        
    elif opcion == 3:   # modificar cliente
        cliente_id = int(input('Escribe el ID del Cliente a modificar'))
        cliente_nombre = input('Nombre del cliente  : ')
        cliente_apellido = input('Apellido del cliente: ')
        cliente_edad = int(input('Edad del cliente: '))
        cliente_tel = input('Teléfono del Cliente: ')
        
        cliente_update = Cliente(cliente_id, cliente_nombre, cliente_apellido, cliente_edad, cliente_tel)
        cliente_a_update = ClienteDAO.actualizar(cliente_update)
        print(f'\nCliente {cliente_update.nombre} actualizado.\n')
        
    elif opcion == 4:   # eliminar cliente
        cliente_id = int(input('Escribe el ID del Cliente a eliminar'))
        cliente_delete = Cliente(cliente_id)
        cliente_a_delete = ClienteDAO.eliminar(cliente_delete)
        print(f'\nCliente {cliente_delete.id} eliminado.\n')
        
        