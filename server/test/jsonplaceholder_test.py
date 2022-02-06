from server import init_api
import unittest

app_teste = init_api().app.test_client()


class testPlaceholder(unittest.TestCase):

    def test_get_desautorizado(self):
        response = app_teste.open('/jsonplaceholder', method="GET")
        self.assertEqual(401, response.status_code)


    def test_get_ok(self):
        response = app_teste.open('/jsonplaceholder', method="GET", auth=('usuario1', '123'))
        self.assertEqual(200, response.status_code)


if __name__ == "__main__":
    unittest.main()
