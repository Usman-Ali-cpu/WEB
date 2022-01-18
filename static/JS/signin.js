document.body.onload = displayData();
var rememberbox = document.getElementById('remember-me');
var yourname = document.getElementById("your_name");
var yourpass = document.getElementById('your_pass');
var submitBtn = document.getElementById('signin');
submitBtn.addEventListener('click', function () {
    if (rememberbox.checked == true) {
        localStorage.setItem('sign_name', yourname.value);
        localStorage.setItem('sign_password', yourpass.value);
    }
    else {
        localStorage.removeItem('sign_name');
        localStorage.removeItem('sign_password');
    }
});
function displayData() {
    var innname = document.getElementById('your_name');
    var innpass = document.getElementById('your_pass');
    if (localStorage.getItem('sign_name')) {
        let name = localStorage.getItem('sign_name');
        let password = localStorage.getItem('sign_password');
        innname.value = name;
        innpass.value = password;
    } else {
        innname.value = '';
        innpass.value = '';
    }
}