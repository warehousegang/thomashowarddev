/* Interface-only fixture. Never use this example as a published model forecast. */
(() => {
  'use strict';
  const button = document.getElementById('run-forecast');
  const label = document.getElementById('run-label');
  const result = document.getElementById('forecast-result');
  const status = document.getElementById('forecast-status');
  if (!button || !label || !result || !status) return;

  let running = false;
  button.disabled = false;

  function reveal() {
    result.hidden = false;
    button.setAttribute('aria-expanded', 'true');
    label.textContent = 'Reset demo';
    button.disabled = false;
    running = false;
    status.textContent = 'Example revealed: Lions 62%, Packers 38%. Sample values only; no trained model was run.';
  }

  button.addEventListener('click', () => {
    if (running) return;
    if (!result.hidden) {
      result.hidden = true;
      button.setAttribute('aria-expanded', 'false');
      label.textContent = 'Run demo forecast';
      status.textContent = 'Demo reset. The public record is unchanged.';
      return;
    }
    running = true;
    button.disabled = true;
    label.textContent = 'Opening example…';
    status.textContent = 'Revealing sample probabilities…';
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) reveal();
    else window.setTimeout(reveal, 650);
  });
})();
