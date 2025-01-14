from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Thiết lập trình duyệt
def setup_browser():
    driver = webdriver.Firefox()  # webdriver.Chrome()
    driver.implicitly_wait(5)  # Đợi các thành phần tải
    return driver

# Kiểm thử đăng nhập thành công
def test_login_success():
    driver = setup_browser()
    driver.get("http://127.0.0.1:5500/frontend/html/login.html")

    # Nhập thông tin đăng nhập hợp lệ
    driver.find_element(By.ID, "email").send_keys("test1@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-btn").click()

    # Xác minh kết quả
    time.sleep(2)
    assert "/dashboard.html" in driver.current_url, "Không chuyển đến trang dashboard"

    driver.quit()

# Kiểm thử đăng nhập sai định dạng email
def test_login_invalid_email():
    driver = setup_browser()
    driver.get("http://127.0.0.1:5500/frontend/html/login.html")

    # Nhập thông tin đăng nhập không hợp lệ
    driver.find_element(By.ID, "email").send_keys("wrongexample")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-btn").click()

    # Xác minh thông báo lỗi
    error_msg = driver.find_element(By.ID, "error-msg").text
    assert error_msg == "Email không hợp lệ", "Thông báo lỗi email không hợp lệ không chính xác"

    driver.quit()

# Kiểm thử đăng nhập sai định dạng mật khẩu (ít hơn 6 ký tự)
def test_login_invalid_password():
    driver = setup_browser()
    driver.get("http://127.0.0.1:5500/frontend/html/login.html")

    # Nhập thông tin đăng nhập không hợp lệ
    driver.find_element(By.ID, "email").send_keys("test1@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.ID, "login-btn").click()

    # Xác minh thông báo lỗi
    error_msg = driver.find_element(By.ID, "error-msg").text
    assert error_msg == "Mật khẩu phải chứa ít nhất 6 ký tự", "Thông báo lỗi mật khẩu không hợp lệ không chính xác"

    driver.quit()

# Kiểm thử đăng nhập thất bại sai email
def test_login_failure_wrong_email():
    driver = setup_browser()
    driver.get("http://127.0.0.1:5500/frontend/html/login.html")

    # Nhập thông tin đăng nhập không hợp lệ
    driver.find_element(By.ID, "email").send_keys("wrong1@gmail.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "login-btn").click()

    # Xác minh thông báo lỗi
    error_msg = driver.find_element(By.ID, "error-msg").text
    assert error_msg == "Email hoặc mật khẩu không chính xác", "Thông báo sai thông tin đăng nhập khi sai email không chính xác"

    driver.quit()

# Kiểm thử đăng nhập thất bại sai mật khẩu
def test_login_failure_wrong_password():
    driver = setup_browser()
    driver.get("http://127.0.0.1:5500/frontend/html/login.html")

    # Nhập thông tin đăng nhập không hợp lệ
    driver.find_element(By.ID, "email").send_keys("test1@gmail.com")
    driver.find_element(By.ID, "password").send_keys("654321")
    driver.find_element(By.ID, "login-btn").click()

    # Xác minh thông báo lỗi
    error_msg = driver.find_element(By.ID, "error-msg").text
    assert error_msg == "Email hoặc mật khẩu không chính xác", "Thông báo sai thông tin đăng nhập khi sai email không chính xác"

    driver.quit()

# Kiểm thử nút đăng nhập bị vô hiệu hóa
def test_login_button_disabled():
    driver = setup_browser()
    driver.get("http://127.0.0.1:5500/frontend/html/login.html")

    # Để trống các trường thông tin
    login_btn = driver.find_element(By.ID, "login-btn")
    assert not login_btn.is_enabled(), "Nút đăng nhập không bị vô hiệu hóa"

    driver.quit()

# Chạy các kịch bản
# if __name__ == "__main__":
#     test_login_success()
#     test_login_invalid_email()
#     test_login_invalid_password()
#     test_login_failure_wrong_email()
#     test_login_failure_wrong_password()
#     test_login_button_disabled()
if __name__ == "__main__":
    all_tests = [
        test_login_success,
        test_login_invalid_email,
        test_login_invalid_password,
        test_login_failure_wrong_email,
        test_login_failure_wrong_password,
        test_login_button_disabled,
    ]

    passed_tests = 0
    total_tests = len(all_tests)

    for test in all_tests:
        try:
            test()
            passed_tests += 1
            print(f"{test.__name__}: Passed")
        except AssertionError as e:
            print(f"{test.__name__}: Failed - {e}")

    if passed_tests == total_tests:
        print("🎉 Tất cả các bài kiểm thử đều thành công! 🎉")
    else:
        print(f"✅ {passed_tests}/{total_tests} bài kiểm thử thành công.")
        