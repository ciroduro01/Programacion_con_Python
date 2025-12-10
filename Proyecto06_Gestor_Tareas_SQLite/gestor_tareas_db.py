# gestor_tareas_db.py
import sqlite3
from sqlite3 import Error
import sys

NOMBRE_DB = "tareas.db"

class DBManager:
    """Clase para encapsular toda la interacción con la base de datos SQLite."""
    def __init__(self):
        self.conn = None
        try:
            # 1. Conexión a la base de datos (se crea si no existe)
            self.conn = sqlite3.connect(NOMBRE_DB)
            print(f"Conexión a la base de datos '{NOMBRE_DB}' establecida.")
            self.crear_tabla()
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            
    def crear_tabla(self):
        """Crea la tabla 'tareas' si aún no existe."""
        sql_crear_tabla = """
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL,
            completada INTEGER NOT NULL
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_crear_tabla)
            self.conn.commit()
            print("Tabla 'tareas' verificada/creada.")
        except Error as e:
            print(f"Error al crear la tabla: {e}")

    def __del__(self):
        """Asegura que la conexión se cierre al destruir el objeto."""
        if self.conn:
            self.conn.close()
            
    # --- CRUD: CREATE (INSERT) ---
    def agregar_tarea(self, descripcion):
        """Inserta una nueva tarea en la base de datos."""
        # Usamos DATETIME('now', 'localtime') para registrar la hora actual
        sql_insert = """
        INSERT INTO tareas (descripcion, fecha_creacion, completada) 
        VALUES (?, DATETIME('now', 'localtime'), 0);
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_insert, (descripcion,)) 
            self.conn.commit() # ¡Crucial para guardar los cambios!
            print(f"Tarea '{descripcion}' añadida con éxito.")
            return cursor.lastrowid
        except Error as e:
            print(f"Error al añadir tarea: {e}")
            return None

    # --- CRUD: READ (SELECT) ---
    def obtener_todas_las_tareas(self):
        """Selecciona y retorna todas las tareas."""
        sql_select = "SELECT id, descripcion, completada, fecha_creacion FROM tareas ORDER BY id;"
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_select)
            filas = cursor.fetchall() 
            return filas
        except Error as e:
            print(f"Error al obtener tareas: {e}")
            return []

    # --- CRUD: UPDATE ---
    def marcar_como_completada(self, id_tarea):
        """Actualiza el estado de una tarea a completada (1)."""
        sql_update = """
        UPDATE tareas 
        SET completada = 1 
        WHERE id = ?;
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_update, (id_tarea,))
            self.conn.commit()
            if cursor.rowcount > 0:
                print(f"Tarea con ID {id_tarea} marcada como completada.")
                return True
            else:
                print(f"Error: Tarea con ID {id_tarea} no encontrada.")
                return False
        except Error as e:
            print(f"Error al actualizar tarea: {e}")
            return False

    # --- CRUD: DELETE ---
    def eliminar_tarea(self, id_tarea):
        """Elimina una tarea de la base de datos."""
        sql_delete = "DELETE FROM tareas WHERE id = ?;"
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_delete, (id_tarea,))
            self.conn.commit()
            if cursor.rowcount > 0:
                print(f"Tarea con ID {id_tarea} eliminada.")
                return True
            else:
                print(f"Error: Tarea con ID {id_tarea} no encontrada.")
                return False
        except Error as e:
            print(f"Error al eliminar tarea: {e}")
            return False

# --- Funciones de Interfaz ---

def mostrar_tareas(tareas):
    """Muestra la lista de tareas en un formato legible."""
    if not tareas:
        print("\n--- ¡No hay tareas pendientes! ---\n")
        return

    print("\n-------------------------------------------------------------")
    print(" ID | Estado | Fecha Creación      | Descripción")
    print("----|--------|---------------------|---------------------------")
    for tarea in tareas:
        id_t, desc, estado, fecha = tarea
        
        estado_simbolo = "✅" if estado == 1 else "⏳" 
        fecha_corta = fecha.split(' ')[0] 
        
        print(f" {str(id_t).ljust(2)} | {estado_simbolo.center(6)} | {fecha_corta.ljust(17)} | {desc}")
    print("-------------------------------------------------------------")

# --- FUNCIÓN PRINCIPAL (MAIN) ---

def main():
    # Instanciamos la clase que gestiona la DB
    db_manager = DBManager()
    
    if db_manager.conn is None:
        sys.exit(1)

    print("\n Gestor de Tareas con SQLite (Proyecto N°6)")

    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar nueva tarea")
        print("2. Ver todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la nueva tarea: ").strip()
            if descripcion:
                db_manager.agregar_tarea(descripcion)
            else:
                print("La descripción no puede estar vacía.")

        elif opcion == '2':
            tareas = db_manager.obtener_todas_las_tareas()
            mostrar_tareas(tareas)

        elif opcion == '3':
            try:
                id_t = int(input("Ingrese el ID de la tarea a completar: ").strip())
                db_manager.marcar_como_completada(id_t)
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == '4':
            try:
                id_t = int(input("Ingrese el ID de la tarea a eliminar: ").strip())
                db_manager.eliminar_tarea(id_t)
            except ValueError:
                print("El ID debe ser un número entero.")

        elif opcion == '5':
            print("Cerrando la aplicación...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()