const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "student" && password === "studentpass") {
        location.replace("https://mohanv2030.github.io/dms/student.html");
        alert("You have successfully logged in.");
    }
    else if (username === "teacher" && password === "teacherpass") {
        alert("You have successfully logged in.");
        location.replace("https://mohanv2030.github.io/dms/teacher.html");
    }
    else {
        alert("Invalid username and/or password");
    }
})
