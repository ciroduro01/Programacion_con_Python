# inventario_orm.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Configuración de la Base de Datos (SQLite)
# Esto crea el archivo inventario.db si no existe
DATABASE_URL = "sqlite:///inventario.db" 
engine = create_engine(DATABASE_URL)
Base = declarative_base() 


# 2. Creación del Modelo ORM (La tabla como una clase Python)
class Producto(Base):
    """Modelo ORM que representa la tabla 'productos'."""
    __tablename__ = 'productos'
    
    # Definición de columnas y tipos de datos SQL
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    def __repr__(self):
        """Representación legible del objeto Producto."""
        return f"Producto(ID={self.id}, Nombre='{self.nombre}', Precio={self.precio:.2f}, Stock={self.stock})"

# Crea la tabla en la base de datos (si no existe)
Base.metadata.create_all(engine)

# 3. Fábrica de Sesiones (Para gestionar transacciones)
Session = sessionmaker(bind=engine)


# 4. Clase de Lógica de Negocio (CRUD Manager)
class InventarioManager:
    def __init__(self):
        self.Session = Session

    # --- CRUD: CREATE ---
    def agregar_producto(self, nombre, precio, stock):
        """Crea y añade un nuevo producto (objeto Python) a la base de datos."""
        session = self.Session()
        try:
            nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
            session.add(nuevo_producto) # Añadir el objeto a la sesión
            session.commit()           # Ejecutar el INSERT en la DB
            print(f"Producto '{nombre}' añadido con éxito. ID: {nuevo_producto.id}")
        except Exception as e:
            session.rollback() 
            print(f"Error al añadir producto: {e}")
        finally:
            session.close()

    # --- CRUD: READ ---
    def obtener_todos(self):
        """Consulta todos los productos usando la sintaxis ORM."""
        session = self.Session()
        try:
            # Consulta todos los objetos Producto ordenados por ID
            productos = session.query(Producto).order_by(Producto.id).all()
            return productos
        except Exception as e:
            print(f"Error al obtener productos: {e}")
            return []
        finally:
            session.close()

    # --- CRUD: UPDATE ---
    def actualizar_stock(self, id_producto, nuevo_stock):
        """Busca un producto por ID y actualiza su stock."""
        session = self.Session()
        try:
            # Consultar el objeto
            producto = session.query(Producto).filter(Producto.id == id_producto).first()

            if producto:
                # Modifica el atributo del objeto Python
                stock_anterior = producto.stock
                producto.stock = nuevo_stock
                
                # Commit ejecuta el UPDATE
                session.commit()
                print(f"Stock de '{producto.nombre}' (ID {id_producto}) actualizado de {stock_anterior} a {nuevo_stock}.")
            else:
                print(f"Error: Producto con ID {id_producto} no encontrado.")
        except Exception as e:
            session.rollback()
            print(f"Error al actualizar stock: {e}")
        finally:
            session.close()

    # --- CRUD: DELETE ---
    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        session = self.Session()
        try:
            # Consultar el objeto
            producto = session.query(Producto).filter(Producto.id == id_producto).first()

            if producto:
                nombre = producto.nombre
                session.delete(producto) # Marca el objeto para eliminación
                session.commit()         # Ejecuta el DELETE
                print(f"Producto '{nombre}' (ID {id_producto}) eliminado correctamente.")
            else:
                print(f"Error: Producto con ID {id_producto} no encontrado.")
        except Exception as e:
            session.rollback()
            print(f"Error al eliminar producto: {e}")
        finally:
            session.close()


# 5. Funciones de Interfaz y Main
def mostrar_productos(productos):
    """Muestra la lista de productos en un formato legible."""
    if not productos:
        print("\n--- ¡Inventario vacío! ---\n")
        return

    print("\n-------------------------------------------------------------")
    print(" ID | Nombre                 | Precio | Stock")
    print("----|------------------------|--------|-------")
    for p in productos:
        print(f" {str(p.id).ljust(2)} | {p.nombre.ljust(22)} | {str(p.precio).rjust(6)} | {str(p.stock).rjust(5)}")
    print("-------------------------------------------------------------")


def main():
    manager = InventarioManager()
    
    print("\n Gestor de Inventario con SQLAlchemy (Proyecto N°9)")

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        try:
            if opcion == '1':
                nombre = input("Nombre: ").strip()
                precio = float(input("Precio: ").strip())
                stock = int(input("Stock inicial: ").strip())
                manager.agregar_producto(nombre, precio, stock)

            elif opcion == '2':
                productos = manager.obtener_todos()
                mostrar_productos(productos)

            elif opcion == '3':
                id_prod = int(input("ID del producto a actualizar: ").strip())
                nuevo_stock = int(input("Nuevo Stock: ").strip())
                manager.actualizar_stock(id_prod, nuevo_stock)

            elif opcion == '4':
                id_prod = int(input("ID del producto a eliminar: ").strip())
                manager.eliminar_producto(id_prod)

            elif opcion == '5':
                print("Cerrando la aplicación...")
                break

            else:
                print("Opción no válida. Intente de nuevo.")
        
        except ValueError:
            print("Entrada no válida. Asegúrese de ingresar números para ID, Precio y Stock.")


if __name__ == "__main__":
    main()