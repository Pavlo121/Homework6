import requests


class WebService:
    def get_data(self, url: str) -> dict:
        response = requests.get(url)
        response.raise_for_status()  # Піднімемо виключення для статусів 4xx та 5xx
        return response.json()


# Тестування класу WebService
import unittest
from unittest.mock import patch, Mock


class TestWebService(unittest.TestCase):

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        # Створюємо фейкову відповідь
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        service = WebService()
        result = service.get_data("https://www.youtube.com/")

        # Перевіряємо, що результат правильний
        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with("https://www.youtube.com/")

    @patch('requests.get')
    def test_get_data_not_found(self, mock_get):
        # Створюємо фейкову відповідь для помилки 404
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        service = WebService()

        # Перевіряємо, що виклик методу підніме виключення
        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_data("http://fakeurl.com")

    @patch('requests.get')
    def test_get_data_server_error(self, mock_get):
        # Створюємо фейкову відповідь для помилки 500
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500 Internal Server Error")
        mock_get.return_value = mock_response

        service = WebService()

        # Перевіряємо, що виклик методу підніме виключення
        with self.assertRaises(requests.exceptions.HTTPError):
            service.get_data("http://fakeurl.com")


if __name__ == '__main__':
    unittest.main()
