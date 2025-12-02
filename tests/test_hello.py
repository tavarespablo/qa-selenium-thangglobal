from selenium import webdriver

def test_open_site():
    driver = webdriver.Chrome()
    driver.get("https://thangglobal.com")
    assert "Thang Global" in driver.title
    driver.quit