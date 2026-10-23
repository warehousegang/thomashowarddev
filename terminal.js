(() => {
  const root = document.documentElement;
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');

  // The head script hides the original text before the first paint. If it has
  // already fallen back to static content, or this script runs twice, leave it alone.
  if (root.dataset.terminalState !== 'pending') return;
  if (motion.matches) {
    delete root.dataset.terminalState;
    return;
  }

  const lines = [...document.querySelectorAll('[data-typewriter]')].map((element) => ({
    element,
    text: element.textContent,
    height: element.getBoundingClientRect().height,
    originalMinHeight: element.style.minHeight,
    speed: Number(element.dataset.typewriter),
  }));

  if (!lines.length) {
    delete root.dataset.terminalState;
    return;
  }

  // Keep exactly one text node per line. No hidden copy or overlapping layer.
  for (const line of lines) {
    line.characters = [...line.text];
    line.node = document.createTextNode('');
    line.element.style.minHeight = `${line.height}px`;
    line.element.classList.add('typewriter-waiting');
    line.element.replaceChildren(line.node);
  }
  root.dataset.terminalState = 'running';

  let index = 0;
  let startsAt = performance.now() + 180;
  let frame;

  function reveal(line) {
    line.node.data = line.text;
    line.element.style.minHeight = line.originalMinHeight;
    line.element.classList.remove('typewriter-waiting', 'is-typing');
  }

  function finish() {
    cancelAnimationFrame(frame);
    lines.forEach(reveal);
    root.dataset.terminalState = 'complete';
    motion.removeEventListener('change', onMotionChange);
    window.removeEventListener('resize', finish);
  }

  function onMotionChange(event) {
    if (event.matches) finish();
  }

  function type(now) {
    if (now < startsAt) {
      frame = requestAnimationFrame(type);
      return;
    }

    const line = lines[index];
    line.element.classList.remove('typewriter-waiting');
    line.element.classList.add('is-typing');
    const count = Math.min(line.characters.length, Math.floor((now - startsAt) / line.speed));
    line.node.data = line.characters.slice(0, count).join('');

    if (count === line.characters.length) {
      reveal(line);
      index += 1;
      if (index === lines.length) {
        finish();
        return;
      }
      startsAt = now + 220;
    }

    frame = requestAnimationFrame(type);
  }

  motion.addEventListener('change', onMotionChange);
  window.addEventListener('resize', finish);
  frame = requestAnimationFrame(type);
})();
