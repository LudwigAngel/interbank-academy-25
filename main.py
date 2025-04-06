import csv

def read_transactions(file_path):
    """
    Lee el archivo CSV y devuelve una lista de transacciones.
    Cada transacción es un diccionario con las claves 'id', 'tipo' y 'monto'.
    """
    transactions = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = {
                    'id': int(row['id']),
                    'tipo': row['tipo'],
                    'monto': float(row['monto'])
                }
                transactions.append(transaction)
    except FileNotFoundError:
        print(f"Error: El archivo '{file_path}' no fue encontrado.")
        exit(1)
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        exit(1)
    return transactions

def calculate_balance(transactions):
    """
    Calcula el balance final sumando los créditos y restando los débitos.
    """
    credit_total = sum(t['monto'] for t in transactions if t['tipo'] == 'Crédito')
    debit_total = sum(t['monto'] for t in transactions if t['tipo'] == 'Débito')
    return credit_total - debit_total

def find_highest_transaction(transactions):
    """
    Encuentra la transacción con el monto más alto.
    Devuelve una tupla con el ID y el monto.
    """
    highest = max(transactions, key=lambda t: t['monto'])
    return highest['id'], highest['monto']

def count_transaction_types(transactions):
    """
    Cuenta el número de transacciones por tipo ('Crédito' y 'Débito').
    """
    credit_count = sum(1 for t in transactions if t['tipo'] == 'Crédito')
    debit_count = sum(1 for t in transactions if t['tipo'] == 'Débito')
    return credit_count, debit_count

def generate_report(transactions):
    """
    Genera el reporte final basado en las transacciones.
    """
    balance_final = calculate_balance(transactions)
    highest_id, highest_amount = find_highest_transaction(transactions)
    credit_count, debit_count = count_transaction_types(transactions)

    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_final:.2f}")
    print(f"Transacción de Mayor Monto: ID {highest_id} - {highest_amount:.2f}")
    print(f"Conteo de Transacciones: Crédito: {credit_count} Débito: {debit_count}")

if __name__ == "__main__":
    # Ruta al archivo CSV
    file_path = 'data.csv'

    # Leer y procesar las transacciones
    transactions = read_transactions(file_path)

    # Generar el reporte
    generate_report(transactions)