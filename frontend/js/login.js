const emailInput = document.getElementById('email');
  const passwordInput = document.getElementById('password');
  const loginButton = document.getElementById('login-btn');
  const errorMsg = document.getElementById('error-msg');

  // Dữ liệu cố định cho kiểm thử
  const validCredentials = [
    { id: 1, name: 'Tester 1', email: 'test1@gmail.com', password: '123456' },
    { id: 2, name: 'Tester 2', email: 'test2@gmail.com', password: '123456' },
    { id: 3, name: 'Tester 3', email: 'test3@gmail.com', password: '123456' },
  ];

  // Bật/tắt nút đăng nhập dựa trên đầu vào
  function toggleLoginButton() {
    if (emailInput.value && passwordInput.value) {
      loginButton.disabled = false;
    } else {
      loginButton.disabled = true;
    }
  }

  emailInput.addEventListener('input', toggleLoginButton);
  passwordInput.addEventListener('input', toggleLoginButton);

  // Xử lý logic đăng nhập
  loginButton.addEventListener('click', () => {
    const email = emailInput.value;
    const password = passwordInput.value;

    errorMsg.innerText = '';
    errorMsg.style.display = 'none';

    // Kiểm tra email và mật khẩu có đúng định dạng không
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
      errorMsg.innerText = 'Email không hợp lệ';
      errorMsg.style.display = 'block';
      return;
    }
    if (password.length < 6) {
      errorMsg.innerText = 'Mật khẩu phải chứa ít nhất 6 ký tự';
      errorMsg.style.display = 'block';
      return;
    }

    const isValid = validCredentials.some(cred => cred.email === email && cred.password === password);

    if (isValid) {
      sessionStorage.setItem('user', JSON.stringify(validCredentials.find(cred => cred.email === email)));
      window.location.href = '/frontend/html/dashboard.html';
    } else {
      errorMsg.innerText = 'Email hoặc mật khẩu không chính xác';
      errorMsg.style.display = 'block';
    }
  });