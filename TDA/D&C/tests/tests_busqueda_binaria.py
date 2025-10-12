import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from  busqueda_binaria import busqueda_binaria as  bb


def test_busqueda_binaria_existe():
  S = [1, 2, 3]
  assert bb(S, 3) == 2
  assert bb(S, 1) == 0
  assert bb(S, 2) == 1

def test_busqueda_binaria_no_existe():
  S = [1, 2, 3]
  assert bb(S, 4) is None
  assert bb(S, 0) is None
  
if __name__ == "__main__":
    print("Ejecutando pruebas simples:")
    try:
        test_busqueda_binaria_existe()
        test_busqueda_binaria_no_existe()
        print("Todas las pruebas pasaron exitosamente.")
    except AssertionError as e:
        print(f"Error en la prueba: {e}")