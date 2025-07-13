import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="URL to check"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        type=int,
        help="Expected status code",
    )


@pytest.fixture
def url(request):
    return request.config.getoption("url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("status_code")


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
