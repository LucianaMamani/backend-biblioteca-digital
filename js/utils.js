// ── SHARED UTILITIES ──

const Auth = {
  isLoggedIn: () => !!localStorage.getItem('access'),
  logout:     () => { localStorage.clear(); window.location.href = '/'; }
};

async function renderNav(activeLink = '') {
  const navEl = document.getElementById('main-nav');
  if (!navEl) return;

  const links = [
    { href: '../pages/catalogo.html', label: 'Catálogo', key: 'catalogo' },
    { href: '../pages/catalogo.html#generos', label: 'Géneros', key: 'generos' },
  ];

  const linksHTML = links.map(l =>
    `<li><a href="${l.href}" class="${activeLink === l.key ? 'active' : ''}">${l.label}</a></li>`
  ).join('');

  const token = localStorage.getItem('access');
  let actionsHTML = `
    <a href="../pages/login.html"    class="btn btn-ghost btn-sm">Iniciar sesión</a>
    <a href="../pages/register.html" class="btn btn-primary btn-sm">Registrarse</a>`;

  if (token) {
    let panelLink = '../pages/panel-usuario.html';
    try {
      const res = await fetch('/api/perfil/me/', { headers: { 'Authorization': 'Bearer ' + token } });
      if (res.ok) {
        const user = await res.json();
        panelLink = user.is_staff ? '../pages/panel-admin.html' : '../pages/panel-usuario.html';
      }
    } catch (e) {}

    actionsHTML = `
      <a href="${panelLink}" class="btn btn-ghost btn-sm">Mi panel</a>
      <button onclick="Auth.logout()" class="btn btn-ghost btn-sm">Salir</button>`;
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

async function fetchConToken(url, options = {}) {
  let token = localStorage.getItem('access');
  options.headers = options.headers || {};
  options.headers['Authorization'] = 'Bearer ' + token;

  let res = await fetch(url, options);

  if (res.status === 401) {
    const refresh = localStorage.getItem('refresh');
    if (!refresh) { localStorage.clear(); window.location.href = '/pages/login.html'; return res; }

    const refreshRes = await fetch('/api/token/refresh/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh })
    });

    if (!refreshRes.ok) {
      localStorage.clear();
      window.location.href = '/pages/login.html';
      return res;
    }

    const data = await refreshRes.json();
    localStorage.setItem('access', data.access);

    options.headers['Authorization'] = 'Bearer ' + data.access;
    res = await fetch(url, options);
  }

  return res;
}