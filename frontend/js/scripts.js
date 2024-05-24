document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting immediately
    console.log('Form submission prevented');

    var form = this;
    console.log('Form element:', form);

    form.classList.add('fade-out'); // Add the fade-out animation class
    console.log('Fade-out class added');

    setTimeout(function() {
        console.log('Timeout reached, submitting form');
        form.submit(); // Submit the form after the animation completes
    }, 500); // Delay in milliseconds matching the CSS animation
});
