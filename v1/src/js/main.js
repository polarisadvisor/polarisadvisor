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
});
