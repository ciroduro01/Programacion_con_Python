# app_inventario.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# 1. Inicialización de Flask y Configuración de DB
app = Flask(__name__)

# Configuración de la base de datos (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario_api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 2. Modelo ORM (usando db.Model de Flask-SQLAlchemy)
class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False, unique=True) # Nombre único para evitar duplicados
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    # Método clave para serialización: convierte el objeto ORM a un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock
        }

# Crear las tablas de la DB si no existen al iniciar la aplicación
with app.app_context():
    db.create_all()

# 3. Rutas de la API (Endpoints CRUD)

@app.route('/productos', methods=['GET', 'POST'])
def manejar_productos():
    if request.method == 'GET':
        # READ ALL: Obtener todos los productos
        productos = Producto.query.all()
        lista_productos = [p.to_dict() for p in productos]
        return jsonify(lista_productos)

    elif request.method == 'POST':
        # CREATE: Añadir un nuevo producto
        data = request.get_json()
        
        # Validación de datos requeridos
        if not data or 'nombre' not in data or 'precio' not in data:
            return jsonify({'error': 'Faltan datos requeridos (nombre, precio) en el JSON.'}), 400

        try:
            nuevo_producto = Producto(
                nombre=data['nombre'],
                precio=float(data['precio']),
                stock=int(data.get('stock', 0)) # Usa 0 si no se provee stock
            )

            db.session.add(nuevo_producto)
            db.session.commit()
            
            # Retornar el objeto creado con código 201 (Created)
            return jsonify(nuevo_producto.to_dict()), 201 
        
        except ValueError:
             return jsonify({'error': 'Precio o stock deben ser números válidos.'}), 400
        except IntegrityError:
             db.session.rollback()
             return jsonify({'error': 'El nombre del producto ya existe (Nombre único).'}), 409 # Conflict
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': f'Error interno del servidor: {str(e)}'}), 500


@app.route('/productos/<int:producto_id>', methods=['GET', 'PUT', 'DELETE'])
def manejar_producto_id(producto_id):
    # Buscar el producto. get_or_404 maneja el error si no se encuentra el ID
    producto = Producto.query.get_or_404(producto_id)
    
    if request.method == 'GET':
        # READ ONE: Obtener un producto específico
        return jsonify(producto.to_dict())

    elif request.method == 'PUT':
        # UPDATE: Modificar producto existente
        data = request.get_json()
        
        try:
            if 'nombre' in data:
                producto.nombre = data['nombre']
            if 'precio' in data:
                producto.precio = float(data['precio'])
            if 'stock' in data:
                producto.stock = int(data['stock'])

            db.session.commit()
            return jsonify(producto.to_dict())
        
        except ValueError:
            db.session.rollback()
            return jsonify({'error': 'Datos de actualización no válidos (precio/stock).'}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'El nombre de producto ya existe.'}), 409

    elif request.method == 'DELETE':
        # DELETE: Eliminar producto
        db.session.delete(producto)
        db.session.commit()
        # Retornar 204 No Content (eliminación exitosa sin cuerpo de respuesta)
        return '', 204

# 4. Ejecución del Servidor
if __name__ == '__main__':
    print("Servidor Flask inicializado. Ejecutándose en http://127.0.0.1:5000/")
    print("Endpoints: /productos (GET/POST) y /productos/<id> (GET/PUT/DELETE)")
    # El modo debug=True es útil para desarrollo
    app.run(debug=True)