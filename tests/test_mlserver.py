import unittest
import requests
import json


class TestMLServerAPI(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:8080/v2/models/classificador-produto/infer"
        self.headers = {"Content-Type": "application/json"}

    def test_infer_categoria(self):
        payload = {
            "inputs": [
                {
                    "name": "input-0",
                    "shape": [1],
                    "datatype": "BYTES",
                    "data": ["Calça jeans masculina"]
                }
            ]
        }
        response = requests.post(self.url, headers=self.headers, data=json.dumps(payload))
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('outputs', data)
        self.assertTrue(len(data['outputs']) > 0)


if __name__ == '__main__':
    unittest.main()
