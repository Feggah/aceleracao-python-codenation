from main import get_temperature
import requests


class MockResponse:
    @staticmethod
    def json():
        return {'currently': {'temperature': 62}}


def test_get_temperature_by_lat_lng(monkeypatch):
    # Arrange
    def mock_get(self):
        return MockResponse()

    # Act
    monkeypatch.setattr(requests, "get", mock_get)
    result = get_temperature(-14.235004, -51.92528)

    # Assert
    assert result == 16
