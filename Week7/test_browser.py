import pytest
@pytest.fixture(params=["chrome", "firefox", "safari"])

def browser(request):
    browser_name = request.param
    print(f"\n [setup] launching {browser_name}")
    yield browser_name # provide the value to the test
    print(f" [teardown] closing {browser_name}")

def test_page_loads(browser):
    assert browser is not None

def test_button_clickable(browser):
    assert len(browser) > 0
