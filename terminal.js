(() => {
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (motion.matches) return;

  const lines = [...document.querySelectorAll('[data-typewriter]')].map((element) => {
    const text = element.textContent;
    const source = document.createElement('span');
    source.className = 'typewriter-source';
    source.textContent = text;

    // Screen readers keep the complete original sentence, without character updates.
    const visual = document.createElement('span');
    visual.className = 'typewriter-visual';
    visual.setAttribute('aria-hidden', 'true');

    element.replaceChildren(source, visual);
    element.classList.add('typewriter');
    return { element, visual, text, characters: [...text], speed: Number(element.dataset.typewriter) };
  });
  if (!lines.length) return;

  let index = 0;
  let startsAt = performance.now() + 180;
  let frame;

  const reveal = (line) => {
    line.element.replaceChildren(document.createTextNode(line.text));
    line.element.classList.remove('typewriter', 'is-typing');
  };

  const finish = () => {
    cancelAnimationFrame(frame);
    lines.forEach(reveal);
    motion.removeEventListener('change', onMotionChange);
  };

  function onMotionChange(event) {
    if (event.matches) finish();
  }

  function type(now) {
    if (now < startsAt) {
      frame = requestAnimationFrame(type);
      return;
    }

    const line = lines[index];
    line.element.classList.add('is-typing');
    const count = Math.min(line.characters.length, Math.floor((now - startsAt) / line.speed));
    line.visual.textContent = line.characters.slice(0, count).join('');

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
  frame = requestAnimationFrame(type);
})();
