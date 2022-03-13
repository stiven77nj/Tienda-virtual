
class Carro:

    # Constructor
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro: # Si no hay carro
            carro = self.session["carro"] = {}
        #else: # Si hay productos en el carro
        self.carro = self.session["carro"]
    
    # Agregar Productos
    def agregar(self, producto):
        # Si el carro no tiene un producto
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio), 
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        # Si el carro ya tiene el producto
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break

        self.guardar_carro() # Se actualiza el carro

    # Guardar carro
    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True
    
    # Eliminar productos
    def eliminar(self, producto):

        producto.id = str(producto.id)

        if producto.id in self.carro:
            del self.carro[producto.id] # Se elimina el producto
            self.guardar_carro() # Se actualiza el carro
    
    # Restar cantidad de un producto
    def restar_producto(self, producto):

        for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] - 1
                    value["precio"] = float(value["precio"]) - producto.precio
                    if value["cantidad"] < 1:
                        self.eliminar(producto)
                    break

        self.guardar_carro() # Se actualiza el carro
    
    # Limpirar el carro
    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True
        