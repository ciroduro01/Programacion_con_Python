# Proyecto N°4: Simulador de Cuenta Bancaria

## Fundamentos de Programación Orientada a Objetos (OOP)

## 1\. Objetivo y Resumen

El objetivo principal de este proyecto es simular un sistema bancario básico para clientes, demostrando los principios fundamentales de la **Programación Orientada a Objetos (OOP)** en Python, específicamente: **Clases**, **Objetos**, **Encapsulación** y **Composición**.

La aplicación permite la creación de clientes y cuentas, y la realización de operaciones transaccionales básicas (depósito, retiro y consulta de saldo) a través de una interfaz de línea de comandos (CLI).

**Valor Clave:** Implementación de la **integridad de los datos** (no permitir retiros con saldo insuficiente) usando métodos de clase controlados.

-----

## 2\. Tecnologías y Herramientas Utilizadas

Este proyecto se enfoca en la implementación del paradigma de programación, utilizando las características nativas del lenguaje Python.

  * **Lenguaje:** Python 3.x
  * **Paradigma:** Programación Orientada a Objetos (OOP)
  * **Conceptos Centrales:**
      * **Encapsulación:** Uso de atributos privados (ej. `__saldo`) en la clase `CuentaBancaria`.
      * **Composición:** La clase `Cliente` **"tiene un"** objeto `CuentaBancaria`.
      * **Clases y Objetos:** Definición de `CuentaBancaria` y `Cliente`.

-----

## 3\. Resultados Clave

El programa proporciona una interfaz interactiva de menú que permite gestionar las cuentas de manera robusta y segura.

### Integridad Transaccional

El resultado clave es la aplicación exitosa de la **lógica de negocio** en los métodos, garantizando la consistencia de los datos:

  * **Restricción de Retiro:** El método `retirar(monto)` verifica el saldo antes de realizar cualquier operación. Si `saldo < monto`, la transacción es rechazada, evitando que el saldo se vuelva negativo.
  * **Control de Acceso:** El saldo de la cuenta no puede ser modificado directamente desde fuera de la clase, sino únicamente a través de los métodos `depositar` y `retirar`, lo que asegura la **Encapsulación**.

-----

## 4\. Desarrollo del Proyecto (Procedimiento)

El diseño del proyecto se basa en dos clases principales con responsabilidades bien definidas:

1.  **Clase `CuentaBancaria`:**
      * Responsable exclusiva de la lógica financiera (depósito, retiro) y del estado del dinero (`__saldo`).
      * El saldo se marca como privado (`__saldo`) para forzar la interacción a través de los métodos de la clase, cumpliendo la **Encapsulación**.
2.  **Clase `Cliente`:**
      * Responsable de la identidad del usuario (`id_cliente`, `nombre`).
      * Utiliza **Composición** al inicializar un objeto `CuentaBancaria` dentro de sí misma (`self.cuenta`).
3.  **Estructura Global:** Se utiliza un diccionario global (`BASE_CLIENTES`) para almacenar instancias de los objetos `Cliente`, indexadas por su ID, simulando la base de datos de clientes en memoria.

-----

## 5\. Estructura del Repositorio y Archivos

El proyecto se encuentra en un único archivo de código, lo que facilita su ejecución.

```
Programacion_con_Python/
└── Proyecto04_Simulador_Bancario_OOP/
    ├── banco_manager.py        # Contiene las clases Cliente, CuentaBancaria y la lógica del menú.
    └── README.md               # Documentación del proyecto.
```

-----

## 6\. Conclusiones

Este proyecto demuestra un dominio funcional de:

  * **Diseño de Clases:** Habilidad para modelar entidades del mundo real (Cliente, Cuenta) como clases de Python.
  * **Encapsulación:** Control riguroso sobre los atributos internos (saldo) de una clase para proteger la integridad de los datos.
  * **Composición de Objetos:** Uso de una clase dentro de otra para delegar responsabilidades (el cliente delega la gestión del saldo a la cuenta).
  * **Lógica de Negocio:** Implementación de reglas transaccionales clave (ej. verificación de saldo insuficiente).

-----

# Project N°4: Bank Account Simulator (Object-Oriented Programming (OOP) Fundamentals)

## 1. Objective and Summary

The main objective of this project is to simulate a basic banking system for clients, demonstrating the fundamental principles of Object-Oriented Programming (OOP) in Python, specifically: Classes, Objects, Encapsulation, and Composition.

The application allows the creation of clients and accounts, and the execution of basic transactional operations (deposit, withdrawal, and balance inquiry) through a command-line interface (CLI).

**Key Value**: Implementation of data integrity (preventing withdrawals with insufficient funds) using controlled class methods.

---

## 2. Technologies and Tools Used

This project focuses on implementing the programming paradigm, using the native features of the Python language.

* **Language**: Python 3.x
* **Paradigm**: Object-Oriented Programming (OOP)
* **Core Concepts**:
* **Encapsulation**: Use of private attributes (e.g., `__saldo`) in the `CuentaBancaria` class.
* **Composition**: The `Cliente` class "has" a `CuentaBancaria` object.
* **Classes and Objects**: Definition of `CuentaBancaria` and `Cliente`.

---

## 3. Key Results

The program provides an interactive menu interface that allows for robust and secure account management.

### Transactional Integrity

The key result is the successful application of business logic in the methods, guaranteeing data consistency:

* **Withdrawal Restriction**: The `retirar(monto)` method checks the balance before performing any operation. If `saldo < monto`, the transaction is rejected, preventing the balance from becoming negative.
* **Access Control**: The account balance cannot be modified directly from outside the class, but only through the `depositar` and `retirar` methods, thus ensuring encapsulation.

---

## 4. Project Development (Procedure)

The project design is based on two main classes with well-defined responsibilities:

1. `CuentaBancaria` Class:
* Exclusively responsible for financial logic (deposits, withdrawals) and the account balance (`__saldo`).
* The balance is marked as private (`__saldo`) to force interaction through the class's methods, thus adhering to encapsulation.
2. `Cliente` Class:
* Responsible for the user's identity (`id_cliente`, `nombre`).
* It uses composition when initializing a `CuentaBancaria` object within itself (`self.cuenta`).
3. **Global Structure**: A global dictionary (`BASE_CLIENTES`) is used to store instances of `Cliente` objects, indexed by their ID, simulating the in-memory customer database.

---

## 5. Repository and File Structure

The project is contained in a single code file, which facilitates its execution.

```bash
Programacion_con_Python/
└── Proyecto04_Simulador_Bancario_OOP/
    ├── banco_manager.py       # Contains the Client, BankAccount classes and the menu logic.
    └── README.md     # Project documentation.
```

---

## 6. Conclusions

This project demonstrates a functional mastery of:

* **Class Design**: Ability to model real-world entities (Client, *Cliente*, Account, *Cuenta*) as Python classes.
* **Encapsulation**: Rigorous control over the internal attributes (balance, *saldo*) of a class to protect data integrity.
* **Object Composition**: Use of one class within another to delegate responsibilities (the client delegates balance management to the account).
* **Business Logic**: Implementation of key transactional rules (e.g., insufficient balance check).
