import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


class TestJsonPlaceholderApi:
    def test_get_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post_by_id(self, post_id):
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == post_id

    @pytest.mark.parametrize("user_id", [1, 5, 10])
    def test_get_posts_by_user(self, user_id):
        response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id})
        assert response.status_code == 200
        for post in response.json():
            assert post["userId"] == user_id

    def test_create_post(self):
        response = requests.post(
            f"{BASE_URL}/posts", json={"title": "foo", "body": "bar", "userId": 1}
        )
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "foo"

    def test_get_comments_for_post(self):
        response = requests.get(f"{BASE_URL}/posts/1/comments")
        assert response.status_code == 200
        for comment in response.json():
            assert comment["postId"] == 1
