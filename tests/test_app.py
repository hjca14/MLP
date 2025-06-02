import unittest
from app import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_predizer_categoria(self):
        response = self.app.post('/predizer_categoria', json={'descricao': 'Calça jeans'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('categoria', data)
        self.assertEqual(data['categoria'], 'Roupas')


if __name__ == '__main__':
    unittest.main()
