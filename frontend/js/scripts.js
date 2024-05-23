document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting normally
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    console.log('Login attempt with username:', username, 'and password:', password);
    // Here you would typically handle the login logic or call a backend service
});
