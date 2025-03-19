# definición de la clase Cliente

class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, edad=None, telefono=None, dcreate=None, dupdate=None):  # Constructorde la clase Cliente
        self.id_cliente = id
        self.nombre     = nombre
        self.apellido   = apellido
        self.edad       = edad
        self.telefono   = telefono
        self.dcreate    = dcreate
        self.dupdate    = dupdate
        
    def __str__(self): # definición de la impresión de la clase Cliente
        return  (f'id_cliente: {self.id_cliente}, '
                f'Nombre: {self.nombre}, '
                f'Apellido: {self.apellido}, '
                f'Edad: {self.edad}, '
                f'Teléfono: {self.telefono}, '
                f'Fecha de creación: {self.dcreate}, '
                f'Fecha de actualización: {self.dupdate}'
                )