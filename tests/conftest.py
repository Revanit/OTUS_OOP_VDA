import pytest


@pytest.fixture(scope="function", autouse=True)
def db():
    print("\nStart DB")
    yield
    print("\nEnd DB")


@pytest.fixture
def api_server(request):
    print("\nStart API")

    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3, 5, 15
        if type_of_number == "float":
            return 3.5, 5.5, 19.25

    yield _wrapper
    print("\nEnd API")
