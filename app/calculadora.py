# app/calculadora.py

"""Operaciones aritméticas básicas de la calculadora."""

# IMPORTANTE: reemplaza ??? con los nombres completos de los 3 integrantes,
# separados por " | " y en el mismo orden de la sección Integrantes del README.
# Ejemplo: "Ana María Pérez | Luis Andrés Gómez | Sara Restrepo Ríos"
AUTOR = (
    "Jennifer Andrea Lopez Gomez | Santiago Alexander cardenas Laverde | "
    "Danna Salazar Cardenas | Samuel Cadavid Zapata"
)


def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta el segundo número del primero."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide el primer número entre el segundo."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """Eleva el primer número a la potencia del segundo."""
    return a**b


def modulo(a, b):
    """Calcula el residuo de la división entre el primer y el segundo número."""
    if b == 0:
        raise ZeroDivisionError("No se puede calcular el módulo con divisor cero")
    return a % b
