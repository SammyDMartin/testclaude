/* ═══════════════════════════════════════════════════════════════════════════
   Shared Navigation — injected into all pages
   ═══════════════════════════════════════════════════════════════════════════ */
(function() {
  const pages = [
    { href: 'index.html', label: 'HOME' },
    { sep: true },
    { href: 'stories.html', label: 'STORIES' },
    { href: 'drafts.html', label: 'DRAFTS' },
    { sep: true },
    { href: 'timeline.html', label: 'TIMELINE' },
    { href: 'codex.html', label: 'CODEX' },
    { href: 'worlds.html', label: 'WORLDS' },
    { href: 'threads.html', label: 'THREADS' },
    { href: 'science.html', label: 'SCIENCE' },
    { sep: true },
    { href: 'anthropic-trap.html', label: 'TRAP' },
    { href: 'facilitator.html', label: 'FACILITATOR' },
    { href: 'utilitaria.html', label: 'UTILITARIA' },
    { href: 'utilitaria-chat.html', label: 'EMISSARY' },
    { href: 'ai-analysis.html', label: 'AI ANALYSIS' },
    { href: 'reflections.html', label: 'REFLECTIONS' },
    { href: 'occupied-earth.html', label: 'OCCUPIED' },
    { sep: true },
    { href: 'battle.html', label: 'BATTLE' },
    { href: 'msd.html', label: 'MSD' },
    { href: 'diamond-duster.html', label: 'DUSTER' },
    { href: 'liberation.html', label: 'LIBERATION' },
    { href: 'orrery.html', label: 'ORRERY' },
    { href: 'interstice-map.html', label: 'NETWORK' },
    { href: 'ascensor.html', label: 'ASCENSOR' },
    { href: 'warseed.html', label: 'WARSEED' },
    { href: 'threshold-breach.html', label: 'THRESHOLD' },
    { href: 'asphere-combat.html', label: 'A-SPHERE' },
    { href: 'apathy-approach.html', label: 'APATHY' },
    { href: 'simulations.html', label: 'SIMS' },
    { href: 'interstice-transit.html', label: 'TRANSIT' },
    { href: 'isidore-charge.html', label: 'ISIDORE' },
    { href: 'wasteland-crawler.html', label: 'WASTELAND' },
    { href: 'utilitaria-escape.html', label: 'ESCAPE' },
    { href: 'bridge-tactical.html', label: 'BRIDGE' },
    { href: 'msd-dsphere.html', label: 'D-SPHERE' },
    { href: 'threshold-game.html', label: 'FIRST FLEET' },
    { href: 'apathy-game.html', label: 'WAR OF ALL WARS' },
  ];

  const current = location.pathname.split('/').pop() || 'index.html';
  const storyPages = ['reader.html','story.html','seeker-story.html','worlds-within-story.html','headhunted-story.html','inheritor-story.html','oblivion-story.html','sixty-percent-story.html','starwhisp-story.html','director-story.html','facilitator-story.html','bows-arrows-story.html','war-of-all-wars-story.html','other-moon-story.html','frameshift-story.html','utilitaria-story.html','last-duty-story.html'];

  const nav = document.createElement('nav');
  nav.id = 'site-nav';

  const brand = document.createElement('span');
  brand.className = 'nav-brand';
  brand.innerHTML = '<span class="diamond"></span>ASCENT UNIVERSE';
  nav.appendChild(brand);

  // Theme toggle
  const themeBtn = document.createElement('button');
  themeBtn.className = 'theme-toggle';
  themeBtn.setAttribute('aria-label', 'Toggle light/dark mode');
  const saved = localStorage.getItem('au-theme');
  if (saved === 'light') document.documentElement.setAttribute('data-theme', 'light');
  function updateThemeIcon() {
    themeBtn.textContent = document.documentElement.getAttribute('data-theme') === 'light' ? '◐' : '◑';
  }
  updateThemeIcon();
  themeBtn.addEventListener('click', () => {
    const isLight = document.documentElement.getAttribute('data-theme') === 'light';
    if (isLight) {
      document.documentElement.removeAttribute('data-theme');
      localStorage.setItem('au-theme', 'dark');
    } else {
      document.documentElement.setAttribute('data-theme', 'light');
      localStorage.setItem('au-theme', 'light');
    }
    updateThemeIcon();
  });
  nav.appendChild(themeBtn);

  const hamburger = document.createElement('button');
  hamburger.className = 'hamburger';
  hamburger.textContent = '≡';
  hamburger.setAttribute('aria-label', 'Menu');
  hamburger.addEventListener('click', () => {
    links.classList.toggle('open');
  });
  nav.appendChild(hamburger);

  const links = document.createElement('div');
  links.className = 'nav-links';
  pages.forEach(p => {
    if (p.sep) {
      const sep = document.createElement('span');
      sep.className = 'nav-sep';
      links.appendChild(sep);
      return;
    }
    const a = document.createElement('a');
    a.href = p.href;
    a.textContent = p.label;
    if (current === p.href || (current === '' && p.href === 'index.html') ||
        (p.href === 'stories.html' && storyPages.includes(current))) {
      a.className = 'active';
    }
    a.addEventListener('click', () => links.classList.remove('open'));
    links.appendChild(a);
  });
  nav.appendChild(links);

  // Inject scanlines
  const scan = document.createElement('div');
  scan.className = 'scanlines';

  // Inject status bar
  const bar = document.createElement('div');
  bar.className = 'status-bar';
  bar.innerHTML = '<span class="dim">ARCO INTERSTELLAR AGENCY</span><span class="bright" id="nav-clock"></span><span class="dim">CLEARANCE: DELTA</span>';

  // Back to top button
  const btt = document.createElement('button');
  btt.className = 'back-to-top';
  btt.setAttribute('aria-label', 'Back to top');
  btt.textContent = '▲';
  btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  document.addEventListener('DOMContentLoaded', () => {
    document.body.prepend(nav);
    document.body.appendChild(scan);
    document.body.appendChild(bar);
    document.body.appendChild(btt);

    // Show/hide back-to-top on scroll
    window.addEventListener('scroll', () => {
      btt.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    // Clock
    function tick() {
      const el = document.getElementById('nav-clock');
      if (!el) return;
      const now = new Date();
      const yr = now.getFullYear() + 750;
      const p = n => String(n).padStart(2, '0');
      el.textContent = `${yr}.${p(now.getMonth()+1)}.${p(now.getDate())} ${p(now.getHours())}:${p(now.getMinutes())}:${p(now.getSeconds())} UST`;
    }
    tick();
    setInterval(tick, 1000);
  });
})();
