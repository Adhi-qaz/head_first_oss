// Toggles the mobile nav menu open/closed.
const navToggle = document.getElementById('nav-toggle');
const navLinks = document.getElementById('nav-links');

navToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
});

// TODO: close the mobile menu automatically when a nav link is clicked

// Highlight every 3rd chaya spot so it stands out on the page.
const spots = document.querySelectorAll('#spot-list li');
spots.forEach((spot, index) => {
  if (index % 3 === 1) {
    spot.classList.add('highlight');
  }
});
