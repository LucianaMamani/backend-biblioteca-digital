// ── SHARED UTILITIES ──

const Auth = {
  isLoggedIn: () => !!localStorage.getItem('bd_user'),
  getUser:    () => JSON.parse(localStorage.getItem('bd_user') || 'null'),
  isAdmin:    () => { const u = Auth.getUser(); return u && u.role === 'admin'; },
  login:      (user) => localStorage.setItem('bd_user', JSON.stringify(user)),
  logout:     () => { localStorage.removeItem('bd_user'); window.location.href = '../index.html'; }
};

function renderNav(activeLink = '') {
  const user  = Auth.getUser();
  const navEl = document.getElementById('main-nav');
  if (!navEl) return;

  const links = [
    { href: '../pages/catalogo.html', label: 'Catálogo', key: 'catalogo' },
    { href: '../pages/catalogo.html#generos', label: 'Géneros', key: 'generos' },
  ];

  const linksHTML = links.map(l =>
    `<li><a href="${l.href}" class="${activeLink === l.key ? 'active' : ''}">${l.label}</a></li>`
  ).join('');

  let actionsHTML = '';
  if (user) {
    const panelLink = user.role === 'admin' ? '../pages/panel-admin.html' : '../pages/panel-usuario.html';
    actionsHTML = `
      <a href="${panelLink}" class="btn btn-ghost btn-sm">Mi panel</a>
      <button onclick="Auth.logout()" class="btn btn-ghost btn-sm">Salir</button>`;
  } else {
    actionsHTML = `
      <a href="../pages/login.html"    class="btn btn-ghost btn-sm">Iniciar sesión</a>
      <a href="../pages/register.html" class="btn btn-primary btn-sm">Registrarse</a>`;
  }

  navEl.innerHTML = `
    <a href="../index.html" class="nav-logo">Biblio<span>Digital</span></a>
    <ul class="nav-links">${linksHTML}</ul>
    <div class="nav-actions">${actionsHTML}</div>`;
}

function showToast(msg, type = 'success') {
  const toast = document.createElement('div');
  toast.style.cssText = `
    position:fixed;bottom:2rem;right:2rem;z-index:9999;
    padding:.75rem 1.5rem;border-radius:3px;font-size:.85rem;
    background:${type === 'success' ? 'rgba(90,158,106,0.95)' : 'rgba(192,57,43,0.95)'};
    color:#fff;border:1px solid ${type === 'success' ? '#5a9e6a' : '#c0392b'};
    box-shadow:0 4px 20px rgba(0,0,0,.4);`;
  toast.textContent = msg;
  document.body.appendChild(toast);
  setTimeout(() => toast.remove(), 3000);
}

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleDateString('es-AR', { day: '2-digit', month: 'short', year: 'numeric' });
}

function debounce(fn, delay = 300) {
  let t;
  return (...args) => { clearTimeout(t); t = setTimeout(() => fn(...args), delay); };
}