import pytest
import requests

BASE_URL = "https://dog.ceo/api"


class TestDogApi:
    def test_get_all_breeds(self):
        response = requests.get(f"{BASE_URL}/breeds/list/all")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "message" in data

    @pytest.mark.parametrize("breed", ["hound", "bulldog", "pug"])
    def test_get_images_by_breed(self, breed):
        response = requests.get(f"{BASE_URL}/breed/{breed}/images")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert isinstance(data["message"], list)

    @pytest.mark.parametrize("sub_breed", ["afghan", "basset"])
    def test_get_images_by_sub_breed(self, sub_breed):
        response = requests.get(f"{BASE_URL}/breed/hound/{sub_breed}/images")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"

    def test_random_image(self):
        response = requests.get(f"{BASE_URL}/breeds/image/random")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["message"].startswith("https://")

    def test_random_image_by_breed(self):
        response = requests.get(f"{BASE_URL}/breed/hound/images/random")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
