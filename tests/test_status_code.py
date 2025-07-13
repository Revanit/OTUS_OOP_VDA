import requests


def test_check_status_code(url, status_code):
    response = requests.get(url)
    assert (
        response.status_code == status_code
    ), f"Expected {status_code}, got {response.status_code}"
