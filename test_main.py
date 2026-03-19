import unittest
from unittest.mock import MagicMock
from main import process_metadata

class TestCloudFunction(unittest.TestCase):
    def test_flujo_exitoso(self):
        # Se simula la recepción de un pdf
        mock_event = MagicMock()
        mock_event.data = {
            "name": "documento_turing.pdf",
            "size": "5000",
            "contentType": "application/pdf",
            "bucket": "mi-bucket-turing"
        }
        # Ejecutamos la función y verificamos que no truene
        try:
            process_metadata(mock_event)
            print("\nPrueba de flujo exitoso: PASADA")
        except Exception as e:
            self.fail(f"La función falló con datos válidos: {e}")

    def test_manejo_errores(self):
        # Simulamos que manda un evento vacío (error)
        mock_event = MagicMock()
        mock_event.data = {} 
        try:
            process_metadata(mock_event)
            print("Prueba de manejo de errores: PASADA")
        except Exception:
            self.fail("La función debería manejar el error internamente.")

if __name__ == '__main__':
    unittest.main()
