class Empresa():
    def __init__(self):
        self.id_empresa=0
        self.rsoc=""
        self.RFC=""
        self.DomFis={
            'calle':"",
            'noExt':0,
            'noInt':0,
            'col':"",
            'CP':"",
            'estado':"",
            'municipio':"",
            'pais':"México"
        }
        self.NomProp=""
        self.TelCont=""
        self.productos=[]
        self.clientes=[]
        self.empleados=[]
        self.ventas=[]
        self.folios=[]
        
    def genDomFis(self):
        pass
    def prntDatos(self):
        pass
    def editDatos(self):
        pass
    def reg_empleado(self):
        pass
    def deshab_empleado(self):
        pass
    def hab_empleado(self):
        pass
    def genVenta(self):
        pass
    def genProducto(self):
        pass

class Empleado():
    def __init__(self, id, id_empresa):
        self.id=0
        self.Nombre=""
        self.Puesto=""
        self.clientes_cargo=[]
    def reg_producto():
        pass
    def reg_venta():
        pass
    def reg_cliente():
        pass
    def ver_clientes():
        pass
    def ver_productos():
        pass
    
class Cliente():
    def __init__(self):
        self.id=0
        self.EsMoral=True
        self.nombre_registro=""
        self.RFC=""
        self.self.DomFis={
            'calle':"",
            'noExt':0,
            'noInt':0,
            'col':"",
            'CP':"",
            'estado':"",
            'municipio':"",
            'pais':"México"
        }
        self.Tel_contacto=""
        self.nombre_responsable=""
    