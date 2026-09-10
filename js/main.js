// Nav shadow on scroll
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

// Mobile menu
const toggle = document.getElementById('navToggle');
const mobile = document.getElementById('navMobile');
toggle.addEventListener('click', () => {
  const open = mobile.classList.toggle('open');
  toggle.setAttribute('aria-expanded', open);
});
mobile.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  mobile.classList.remove('open');
  toggle.setAttribute('aria-expanded', 'false');
}));

// Scroll reveal
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach((el, i) => {
  el.style.transitionDelay = Math.min(i % 4 * 0.08, 0.24) + 's';
  io.observe(el);
});

// Lead form -> GHL inbound webhook
const GHL_WEBHOOK_URL = 'https://services.leadconnectorhq.com/hooks/XqfAPeJ461TBbejLBSKP/webhook-trigger/5SXxpPJwSxp4fWksH6r1';
const form = document.getElementById('leadForm');
if (form) {
  const status = document.getElementById('formStatus');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    status.className = 'form-status';
    if (!form.checkValidity()) { status.textContent = 'Please complete the required fields.'; form.reportValidity(); return; }
    const f = new FormData(form);
    // Keys must match the GHL mapping: inboundWebhookRequest.{full name, email, phone, message}
    const payload = {
      'full name': (f.get('full_name') || '').trim(),
      email: (f.get('email') || '').trim(),
      phone: (f.get('phone') || '').trim(),
      message: (f.get('message') || '').trim(),
      source: 'Website contact form',
      page: location.pathname
    };
    try {
      status.textContent = 'Sending…';
      const res = await fetch(GHL_WEBHOOK_URL, {
        method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
      });
      if (!res.ok) throw new Error();
      status.className = 'form-status ok';
      status.textContent = 'Thank you. We will be in touch shortly.';
      form.reset();
    } catch {
      status.textContent = 'Something went wrong. Please call (707) 343-0556.';
    }
  });
}
