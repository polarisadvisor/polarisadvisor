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
          // Success - hide form and show calendar
          form.style.display = 'none';
          showCalendarEmbed();
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
        message.innerHTML = text;
        form.appendChild(message);

        // Scroll message into view
        message.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      function showCalendarEmbed() {
        // Create success message container
        const successContainer = document.createElement('div');
        successContainer.className = 'calendar-embed-container';

        // Add thank you message
        const thankYouMessage = document.createElement('div');
        thankYouMessage.className = 'calendar-thank-you';
        thankYouMessage.innerHTML = '<h3>Thank you for reaching out</h3><p>If you would like to schedule a call with me now, please use the calendar below. Otherwise, I will get back to you in 1-2 business days and we can find a time that works for both of us.</p>';
        successContainer.appendChild(thankYouMessage);

        // Add embedded calendar iframe
        const calendarFrame = document.createElement('iframe');
        calendarFrame.src = 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ37Q-W5sjj16iHZnwzHISzm7i53ccSEnbGpQ_tQjsQMnh3gES04INpZyMrzWloM5G_KFHAOFkus?gv=true';
        calendarFrame.className = 'calendar-iframe';
        calendarFrame.setAttribute('frameborder', '0');
        calendarFrame.setAttribute('scrolling', 'yes');
        successContainer.appendChild(calendarFrame);

        // Insert after the form
        form.parentNode.insertBefore(successContainer, form.nextSibling);

        // Scroll to the calendar
        successContainer.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }
});
