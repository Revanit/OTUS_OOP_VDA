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
        data = response.json()
        assert isinstance(data, list)
        for brewery in data:
            assert by_city.lower() in brewery["city"].lower()

    @pytest.mark.parametrize("per_page", [5, 10])
    def test_breweries_pagination(self, per_page):
        response = requests.get(f"{BASE_URL}/breweries", params={"per_page": per_page})
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= per_page

    @pytest.mark.parametrize("brewery_id", ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"])
    def test_get_single_brewery(self, brewery_id):
        response = requests.get(f"{BASE_URL}/breweries/{brewery_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == brewery_id
        assert data["name"] == "MadTree Brewing 2.0"

    @pytest.mark.parametrize("query", ["dog", "brew"])
    def test_search_brewery(self, query):
        response = requests.get(f"{BASE_URL}/breweries/search", params={"query": query})
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0
