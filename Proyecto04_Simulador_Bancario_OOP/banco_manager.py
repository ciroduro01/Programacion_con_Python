# banco_manager.py

BASE_CLIENTES = {} # Estructura global para almacenar instancias de Cliente

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial=0.0):
        #Encapsulamiento: El saldo solo se puede modificar por métodos
        self.__numero_cuenta = numero_cuenta
        self.__saldo = saldo_inicial
        print(f"Cuenta {self.__numero_cuenta} creada con saldo: ${self.__saldo:.2f}")

    # --- Métodos de Comportamiento ---

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito de ${monto:.2f} realizado.")
        else:
            print("Error: El monto del depósito debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print("Error: El monto del retiro debe ser positivo.")
            return False
        
        #Manejo de Error/Excepción de negocio
        if self.__saldo >= monto:
            self.__saldo -= monto
            print(f"Retiro de ${monto:.2f} exitoso.")
            return True
        else:
            print("Error: Saldo insuficiente.")
            return False

    # --- Métodos de Acceso (Getters) ---
    
    def consultar_saldo(self):
        return self.__saldo

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta

class Cliente:
    def __init__(self, id_cliente, nombre, saldo_inicial):
        self.id = id_cliente
        self.nombre = nombre
        # Composición: Cada cliente tiene un objeto CuentaBancaria
        self.cuenta = CuentaBancaria(id_cliente, saldo_inicial)
    
    def mostrar_perfil(self):
        """Muestra la información del cliente y el saldo de su cuenta."""
        saldo_actual = self.cuenta.consultar_saldo()
        print("\n--- PERFIL DEL CLIENTE ---")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Saldo Actual: ${saldo_actual:.2f}")
        print("--------------------------")

# --- Funciones de Gestión Global ---

def crear_cliente(id_cliente, nombre, saldo_inicial):
    """Crea una instancia de Cliente y la añade a la base de datos."""
    if id_cliente in BASE_CLIENTES:
        print(f"Error: El cliente con ID {id_cliente} ya existe.")
        return
    
    try:
        nuevo_cliente = Cliente(id_cliente, nombre, float(saldo_inicial))
        BASE_CLIENTES[id_cliente] = nuevo_cliente
        print(f"Cliente '{nombre}' añadido al sistema.")
    except ValueError:
        print("Error: El saldo inicial debe ser un número válido.")

def encontrar_cliente(id_cliente):
    """Busca y retorna el objeto Cliente si existe."""
    return BASE_CLIENTES.get(id_cliente.strip())

def manejar_operacion(cliente_obj, tipo_op):
    """Función genérica para manejar Depósito o Retiro."""
    try:
        monto = float(input(f"Ingrese el monto a {tipo_op}: "))
    except ValueError:
        print("Error: El monto debe ser un número válido.")
        return

    if tipo_op == 'depositar':
        cliente_obj.cuenta.depositar(monto)
    elif tipo_op == 'retirar':
        cliente_obj.cuenta.retirar(monto)

# --- FUNCIÓN PRINCIPAL (MAIN) ---

def main():
    # Inicialización de Objetos para Prueba (Ejemplo de creación de instancias)
    crear_cliente("101", "Ana Gómez", 500.00)
    crear_cliente("102", "Juan Pérez", 1200.50)

    print("\n\n*** Bienvenido al Simulador Bancario (OOP) ***")

    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Crear Nuevo Cliente/Cuenta")
        print("2. Depositar Fondos")
        print("3. Retirar Fondos")
        print("4. Consultar Saldo y Perfil")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            id_cliente = input("ID de Nuevo Cliente: ").strip()
            nombre = input("Nombre: ").strip()
            saldo = input("Saldo Inicial: ").strip()
            crear_cliente(id_cliente, nombre, saldo)

        elif opcion in ('2', '3', '4'):
            id_cliente = input("Ingrese su ID de Cliente: ").strip()
            cliente_actual = encontrar_cliente(id_cliente)
            
            if cliente_actual is None:
                print(f"Error: Cliente con ID {id_cliente} no encontrado.")
                continue

            if opcion == '2':
                manejar_operacion(cliente_actual, 'depositar')
            
            elif opcion == '3':
                manejar_operacion(cliente_actual, 'retirar')
                
            elif opcion == '4':
                cliente_actual.mostrar_perfil()

        elif opcion == '5':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()