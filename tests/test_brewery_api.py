import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1"


class TestBreweryApi:
    def test_get_breweries_list(self):
        response = requests.get(f"{BASE_URL}/breweries")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.parametrize("by_city", ["San Diego", "Portland"])
    def test_get_breweries_by_city(self, by_city):
        response = requests.get(f"{BASE_URL}/breweries", params={"by_city": by_city})
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.parametrize("per_page", [5, 10])
    def test_breweries_pagination(self, per_page):
        response = requests.get(f"{BASE_URL}/breweries", params={"per_page": per_page})
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= per_page

    def test_get_single_brewery(self):
        response = requests.get(
            f"{BASE_URL}/breweries/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"

    def test_search_brewery(self):
        response = requests.get(f"{BASE_URL}/breweries/search", params={"query": "dog"})
        assert response.status_code == 200
        assert isinstance(response.json(), list)
