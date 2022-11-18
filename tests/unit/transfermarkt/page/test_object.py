"""
This module tests the page object module.
"""

import pytest
import requests_mock

from transfermarkt.page.object import PageObject


@pytest.fixture
def obj():
    return PageObject()


class MockResponse:
    """
    This class mocks a response object.
    """
    def __init__(self, **kwargs):
        self.status_code = kwargs.get("status_code")

    @property
    def status_code(self):
        """
        Returns the status code of the response.
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int):
        """
        Sets the status code of the response.
        """
        self._status_code = status_code


class TestStatusCodeGetter:
    def test_with_undefined_response(self, obj):
        obj.response = None

        assert obj.status_code is None

    def test_with_defined_response_200(self, obj):
        obj.response = MockResponse(status_code=200)

        assert obj.status_code == 200

    def test_with_defined_response_404(self, obj):
        obj.response = MockResponse(status_code=404)

        assert obj.status_code == 404


class TestLoad:
    def test_with_unset_instance_and_missing_param(self, obj):
        with pytest.raises(ValueError, match="The url parameter is required!"):
            obj.load()

    def test_without_headers(self, obj):
        with requests_mock.Mocker() as m:
            m.get("http://test.com", text="Hello World!")

            # Act
            obj.load(url="http://test.com")

        # Assert
        assert obj.status_code == 200
        assert obj.response is not None
        assert obj.soup is not None

    def test_with_headers(self, obj):
        # Arrange
        obj.headers = {"User-Agent": "Mozilla/5.0"}

        with requests_mock.Mocker() as m:
            m.get("http://test.com", text="Hello World!")

            # Act
            obj.load(url="http://test.com")

        # Assert
        assert obj.status_code == 200
        assert obj.response is not None
        assert obj.soup is not None


def test_erase(obj):
    obj.url = "http://test.com"
    obj.headers = {}
    obj.soup = {}
    obj.response = MockResponse(status_code=200)

    obj.erase()

    assert obj.url is None
    assert obj.headers is None
    assert obj.soup is None
    assert obj.response is None


def test_repr(obj):
    obj.url = "http://test.com"
    obj.headers = {}
    obj.soup = {}
    obj.response = MockResponse(status_code=200)

    assert repr(obj) == "PageObject(url='http://test.com')"
