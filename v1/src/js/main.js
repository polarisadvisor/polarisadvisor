// Mobile navigation toggle
document.addEventListener('DOMContentLoaded', function() {

  const navToggle = document.querySelector('.nav-toggle');
  const navFull = document.querySelector('.site-nav-full');
  const overlay = document.querySelector('.nav-overlay');
  const body = document.body;

  if (!navToggle || !navFull || !overlay) {
    return;
  }

  function toggleMenu() {
    const isActive = navToggle.classList.contains('active');

    navToggle.classList.toggle('active');
    navToggle.setAttribute('aria-expanded', !isActive);
    navFull.classList.toggle('active');
    overlay.classList.toggle('active');

    // Prevent body scroll when menu is open
    body.style.overflow = !isActive ? 'hidden' : '';

  }

  function closeMenu() {
    navToggle.classList.remove('active');
    navToggle.setAttribute('aria-expanded', 'false');
    navFull.classList.remove('active');
    overlay.classList.remove('active');
    body.style.overflow = '';
  }

  // Toggle menu - simple click handling works on all platforms
  navToggle.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    toggleMenu();
  });

  // Close menu when clicking overlay
  overlay.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    closeMenu();
  });

  // Close menu when clicking any nav link
  navFull.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', closeMenu);
  });

  // Close menu on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && navFull.classList.contains('active')) {
      closeMenu();
    }
  });

  // Contact form AJAX submission
  const contactForm = document.querySelector('.contact-form');
  console.log('Contact form found:', contactForm);

  if (contactForm) {
    console.log('Adding submit event listener to contact form');

    contactForm.addEventListener('submit', function(e) {
      console.log('=== FORM SUBMIT EVENT FIRED ===');
      console.log('Event preventDefault called');
      e.preventDefault();

      const form = e.target;
      const formData = new FormData(form);
      const submitButton = form.querySelector('button[type="submit"]');
      const originalButtonText = submitButton.textContent;

      console.log('Form action URL:', form.action);
      console.log('Form data:', Array.from(formData.entries()));

      // Disable button and show loading state
      submitButton.disabled = true;
      submitButton.textContent = 'Sending...';

      // Remove any existing messages
      const existingMessage = form.querySelector('.form-message');
      if (existingMessage) {
        existingMessage.remove();
      }

      // Submit to Formspree
      console.log('Starting AJAX fetch to Formspree...');
      fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      })
      .then(response => {
        console.log('Response received:', response.status, response.statusText);
        if (response.ok) {
          console.log('SUCCESS: Form submitted successfully');
          // Success - show message and reset form
          form.reset();
          showMessage('success', 'Thank you. I\'ll be in touch within 2-3 business days.');
          submitButton.textContent = originalButtonText;
          submitButton.disabled = false;

          // Redirect to home after 3 seconds
          setTimeout(function() {
            window.location.href = '/';
          }, 3000);
        } else {
          console.log('ERROR: Response not OK');
          // Error from Formspree
          return response.json().then(data => {
            console.log('Error data:', data);
            throw new Error(data.error || 'Form submission failed');
          });
        }
      })
      .catch(error => {
        console.log('CATCH: Error occurred:', error);
        // Network error or other failure
        showMessage('error', 'Something went wrong. Please try again or email directly.');
        submitButton.textContent = originalButtonText;
        submitButton.disabled = false;
      });

      function showMessage(type, text) {
        const message = document.createElement('div');
        message.className = `form-message form-message-${type}`;
        message.textContent = text;
        form.appendChild(message);

        // Scroll message into view
        message.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    });
  }
});
