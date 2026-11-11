/*
  Masthead link collapsing. Replaces the theme's GreedyNav, which caches link widths
  measured at DOM-ready (wrong if the stylesheet hasn't applied yet) and doesn't know
  about the theme toggle button. This version re-measures the real layout every time.
*/
(function () {
  var nav = document.getElementById('site-nav');
  if (!nav) return;
  var visible = nav.querySelector('.visible-links');
  var hidden = nav.querySelector('.hidden-links');
  var btn = nav.querySelector('.greedy-nav__toggle');
  var timer;

  function outer(el) {
    if (!el || el.offsetParent === null) return 0;
    var cs = getComputedStyle(el);
    return el.getBoundingClientRect().width + parseFloat(cs.marginLeft) + parseFloat(cs.marginRight);
  }

  function fits() {
    var used = 0;
    for (var c = nav.firstElementChild; c; c = c.nextElementSibling) {
      if (c !== visible && c !== hidden) used += outer(c);
    }
    var need = 0;
    for (var i = 0; i < visible.children.length; i++) need += outer(visible.children[i]);
    return need <= nav.clientWidth - used - 10;
  }

  function layout() {
    // start from everything visible, then move links into the menu until the rest fit
    while (hidden.firstElementChild) visible.appendChild(hidden.firstElementChild);
    btn.classList.add('hidden');
    if (fits()) return finish();
    btn.classList.remove('hidden');
    while (visible.lastElementChild && !fits()) {
      hidden.insertBefore(visible.lastElementChild, hidden.firstElementChild);
    }
    finish();
  }

  function finish() {
    btn.setAttribute('count', hidden.children.length);
    if (!hidden.children.length) {
      hidden.classList.add('hidden');
      btn.classList.remove('close');
    }
  }

  var pending = false;
  function schedule() {
    if (pending) return;
    pending = true;
    requestAnimationFrame(function () { pending = false; layout(); });
  }

  btn.addEventListener('click', function () {
    hidden.classList.toggle('hidden');
    btn.classList.toggle('close');
    clearTimeout(timer);
  });
  hidden.addEventListener('click', function () {
    hidden.classList.add('hidden');
    btn.classList.remove('close');
  });
  hidden.addEventListener('mouseleave', function () {
    timer = setTimeout(function () {
      hidden.classList.add('hidden');
      btn.classList.remove('close');
    }, 1000);
  });
  hidden.addEventListener('mouseenter', function () { clearTimeout(timer); });

  window.addEventListener('resize', schedule);
  window.addEventListener('load', schedule);          // after stylesheets/images
  document.addEventListener('cava:themechange', schedule);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(schedule);
  if (window.ResizeObserver) new ResizeObserver(schedule).observe(nav);
  layout();
})();
