# Reto Técnico: Procesamiento de Transacciones Bancarias (CLI)

## **Introducción**

Este proyecto implementa una aplicación de línea de comandos (CLI) que procesa un archivo CSV con transacciones bancarias y genera un reporte que incluye:

- **Balance Final**: Suma de los montos de las transacciones de tipo "Crédito" menos las de tipo "Débito".
- **Transacción de Mayor Monto**: Identifica el ID y el monto de la transacción con el valor más alto.
- **Conteo de Transacciones**: Número total de transacciones para cada tipo ("Crédito" y "Débito").

El propósito de este reto es demostrar habilidades en el procesamiento de datos, lógica algorítmica y desarrollo de aplicaciones CLI utilizando buenas prácticas de programación.

---

## **Instrucciones de Ejecución**

### **Requisitos**
- Python 3.6 o superior instalado en tu sistema.
- Acceso a un terminal o línea de comandos.

### **Pasos para Ejecutar la Aplicación**

1. **Clonar el Repositorio**  
   Clona este repositorio en tu máquina local usando el siguiente comando:
   ```bash
   git clone https://github.com/codeableorg/interbank-academy-25.git

2. **Navegar al Directorio del Proyecto** 
Ingresa al directorio del proyecto:
   cd interbank-academy-25

3. **Instalar Dependencias (si las hay)** 
Este proyecto no requiere dependencias externas adicionales, ya que utiliza la biblioteca estándar de Python. Si se agregan dependencias en el futuro, se pueden instalar con:
   pip install -r requirements.txt
4. **Ejecutar la Aplicación** 
Asegúrate de que el archivo data.csv esté presente en la raíz del proyecto. Luego, ejecuta el programa con el siguiente comando:
   python main.py
5. **Ver el Reporte** 
El reporte se mostrará directamente en la terminal. Por ejemplo:
Reporte de Transacciones
Balance Final: 10985.85
Transacción de Mayor Monto: ID 222 - 499.69
Conteo de Transacciones: Crédito: 508 Débito: 492

### **Enfoque y Solución**
El proyecto sigue un enfoque modular y legible:

   - Lectura del CSV: Se usa la biblioteca csv para convertir cada fila en un diccionario.

   - Balance Final: Se suman créditos y se restan débitos.

   - Mayor Monto: Se identifica con max().

   - Conteo por Tipo: Uso de comprensiones de listas.

- Decisiones de Diseño:

   - Modularidad para facilitar mantenimiento

   - Manejo de errores para mayor robustez

   - Escalabilidad para futuras mejoras

### **Estructura del Proyecto**

interbank-academy-25/
│
├── main.py          # Código principal
├── data.csv         # Archivo con transacciones de ejemplo
├── README.md        # Documentación del proyecto
└── requirements.txt # Dependencias (actualmente vacío)
