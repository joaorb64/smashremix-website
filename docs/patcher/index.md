---
title: Patcher
ssb_crc: eb97929e
---

<div class="patch-tabs">
  <button class="md-button md-button--primary" onclick="switchCategory('releases', this)">Smash Remix Releases</button>
  <button class="md-button md-button--primary" onclick="switchCategory('other', this)">Other / Misc</button>
</div>

<div class="patch-controls">
  <select id="patch-selector" onchange="updatePatcher()"></select>
  <button class="md-button md-button--primary" id="openPatchModal" style="flex-shrink: 0;">
    Patch Notes
  </button>
</div>

<div id="region-container" style="margin-bottom: 1rem; margin-left: 1rem;">
  <label style="margin-right:15px;">
    <input type="radio" name="region" value="ntsc" checked onchange="updatePatcher()">
    <span>NTSC</span>
  </label>

  <label id="pal-radio-label">
    <input id="pal-radio" type="radio" name="region" value="pal" onchange="updatePatcher()">
    <span>PAL60</span>
  </label>
</div>

<div id="patchModal" class="material-modal" data-search-exclude>
  <div class="material-modal-dialog">

    <div class="material-modal-header">
      <h3 id="patchModalTitle">Patch Notes</h3>
      <button class="material-modal-close" id="closePatchModal">✕</button>
    </div>

    <div class="material-modal-body" id="patchModalBody">
    </div>

  </div>
</div>

<!-- Modal -->
 <div class="modal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Modal body text goes here.</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
<div class="modal fade material-modal" id="patchModal" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-wide">
    <div class="modal-content">
      <div class="modal-header">
        <h2 class="modal-title">Patch Notes</h2>
        <button type="button"
                class="modal-close"
                data-bs-dismiss="modal">
          ✕
        </button>
      </div>
    </div>
  </div>
</div>

<div id="rom-patcher-container" data-search-exclude>
  <div class="rom-patcher-row margin-bottom" id="rom-patcher-row-file-rom">
    <div class="text-right"><label for="rom-patcher-input-file-rom" data-localize="yes">ROM file:</label></div>
    <div class="rom-patcher-container-input">
      <input type="file" id="rom-patcher-input-file-rom" class="empty" disabled />
    </div>
  </div>
  <div class="margin-bottom text-selectable text-mono text-muted" id="rom-patcher-rom-info">
    <div class="rom-patcher-row">
      <div class="text-right">CRC32:</div>
      <div class="text-truncate"><span id="rom-patcher-span-crc32"></span></div>
    </div>
    <div class="rom-patcher-row">
      <div class="text-right">MD5:</div>
      <div class="text-truncate"><span id="rom-patcher-span-md5"></span></div>
    </div>
    <div class="rom-patcher-row">
      <div class="text-right">SHA-1:</div>
      <div class="text-truncate"><span id="rom-patcher-span-sha1"></span></div>
    </div>
    <div class="rom-patcher-row" id="rom-patcher-row-info-rom">
      <div class="text-right">ROM:</div>
      <div class="text-truncate"><span id="rom-patcher-span-rom-info"></span></div>
    </div>
  </div>

  <div class="rom-patcher-row margin-bottom" id="rom-patcher-row-file-patch">
    <div class="text-right"><label for="rom-patcher-input-file-patch" data-localize="yes">Patch file:</label>
    </div>
    <div class="rom-patcher-container-input">
      <select id="rom-patcher-select-patch"></select>
    </div>
  </div>
  <div class="rom-patcher-row margin-bottom" id="rom-patcher-row-patch-description">
    <div class="text-right text-mono text-muted" data-localize="yes">Description:</div>
    <div class="text-truncate" id="rom-patcher-patch-description"></div>
  </div>
  <div class="rom-patcher-row margin-bottom text-selectable text-mono text-muted"
    id="rom-patcher-row-patch-requirements">
    <div class="text-right text-mono" id="rom-patcher-patch-requirements-type">ROM requirements:</div>
    <div class="text-truncate" id="rom-patcher-patch-requirements-value"></div>
  </div>

  <div class="text-center" id="rom-patcher-row-apply">
    <div id="rom-patcher-row-error-message" class="margin-bottom"><span id="rom-patcher-error-message"></span>
    </div>
    <button id="rom-patcher-button-apply" data-localize="yes" disabled>Apply patch</button>
  </div>
</div>

<div id="rom-patcher-powered" class="text-center">
  <a href="https://github.com/marcrobledo/RomPatcher.js" target="_blank"><img
      src="rom-patcher-js/assets/powered_by_rom_patcher_js.png" loading="lazy" />Powered by Rom Patcher JS</a>
</div>

<link type="text/css" rel="stylesheet" href="rom-patcher-js/style.css" media="all" />
<script type="text/javascript" src="rom-patcher-js/RomPatcher.webapp.js"></script>
<script type="text/javascript" src="showdownjs/showdown.min.js"></script>

<script>
const myPatcherSettings = {
  language: 'en',
  requireValidation: true,
  allowDropFiles: false,
};

let releases = [];
let others = [];
let currentNoteVersion = '';
let currentNoteBody = '';

async function loadAllPatches() {
  try {
    const [relResp, otherResp] = await Promise.all([
      fetch('patches/releases.json'),
      fetch('patches/other.json')
    ]);

    if (relResp.ok) releases = await relResp.json();
    if (otherResp.ok) others = await otherResp.json();

    populateAllOptions();
    switchCategory('releases', );
  } catch (err) {
    console.warn('Failed loading patch data', err);
  }
}

function populateAllOptions() {
  const select = document.getElementById('patch-selector');
  select.innerHTML = '';

  // Releases
  releases.forEach(entry => {
    const opt = document.createElement('option');
    opt.value = entry.version;
    opt.textContent = entry.name;
    opt.dataset.category = 'releases';
    opt.dataset.files = JSON.stringify(entry.files);
    opt.dataset.notes = entry.patch_notes || '';
    opt.dataset.version = entry.name || '';
    select.appendChild(opt);
  });

  // Other patches
  others.forEach(entry => {
    const opt = document.createElement('option');
    opt.value = entry.name;
    opt.textContent = entry.name;
    opt.dataset.category = 'other';
    opt.dataset.file = entry.file;
    opt.dataset.description = entry.description || '';
    select.appendChild(opt);
  });
}

function updatePatcher() {
  const selector = document.getElementById('patch-selector');
  const selected = selector.options[selector.selectedIndex];
  if (!selected) return;

  const ntscRadio = document.querySelector('input[name="region"][value="ntsc"]');
  const palRadio = document.getElementById('pal-radio');

  let patchFile = null;

  if (selected.dataset.category === 'releases') {
    const files = JSON.parse(selected.dataset.files);

    if (files.pal) {
      palRadio.disabled = false;
    } else {
      palRadio.disabled = true;
      ntscRadio.checked = true;
    }

    const region = document.querySelector('input[name="region"]:checked').value;
    patchFile = files[region] || files.ntsc;

    currentNoteBody = selected.dataset.notes || '';
    currentNoteVersion = selected.dataset.version || '';
  }

  if (selected.dataset.category === 'other') {
    palRadio.disabled = true;
    ntscRadio.checked = true;
    patchFile = selected.dataset.file;
    currentNoteBody = '';
    currentNoteVersion = '';
  }

  if (!patchFile) return;

  const patcherConfig = {
    file: `patches/${selected.dataset.category}/${patchFile}`,
    name: patchFile,
    inputCrc32: 'eb97929e',
    description: selected.dataset.description || null,
    outputName: `${selected.textContent} (Patched)`
  };

  if (RomPatcherWeb.isInitialized() === false) {
    RomPatcherWeb.initialize(myPatcherSettings, patcherConfig);
  } else {
    RomPatcherWeb.setEmbededPatches(patcherConfig);
  }

  // Notes button logic
  const notesBtn = document.getElementById('openPatchModal');
  if (currentNoteBody) {
    notesBtn.style.display = '';
  } else {
    notesBtn.style.display = 'none';
  }
}

function switchCategory(category, button) {
  const selector = document.getElementById('patch-selector');
  const options = selector.querySelectorAll('option[data-category]');
  const tabButtons = document.querySelectorAll('.patch-tabs .md-button');

  // Atualiza botão ativo
  tabButtons.forEach(btn => btn.classList.remove('active'));
  if (button) button.classList.add('active');
  else tabButtons[0].classList.add('active');

  let firstMatch = null;

  options.forEach(opt => {
    if (opt.dataset.category === category) {
      opt.style.display = '';
      if (!firstMatch) firstMatch = opt;
    } else {
      opt.style.display = 'none';
    }
  });

  if (firstMatch) {
    selector.value = firstMatch.value;
  }

  // Sempre volta para NTSC ao trocar categoria
  const ntscRadio = document.querySelector('input[name="region"][value="ntsc"]');
  ntscRadio.checked = true;

  updatePatcher();
}

window.addEventListener('load', function(){

  loadAllPatches().then(() => {
    updatePatcher();
  });

  document.getElementById('patch-selector')
    .addEventListener('change', updatePatcher);
});

const modal = document.getElementById('patchModal');
const openBtn = document.getElementById('openPatchModal');
const closeBtn = document.getElementById('closePatchModal');
const modalBody = document.getElementById('patchModalBody');
const modalTitle = document.getElementById('patchModalTitle');

const converter = new showdown.Converter({
  tables: true,
  strikethrough: true,
  simpleLineBreaks: true
});

openBtn.addEventListener('click', () => {
  modalTitle.textContent = currentNoteVersion ? `${currentNoteVersion}` : 'Patch Notes';
  const html = converter.makeHtml(currentNoteBody || 'No notes.');
  modalBody.innerHTML = html;
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden'; // lock page scroll
});

function closeModal() {
  modal.style.display = 'none';
  document.body.style.overflow = '';
}

// Modal close button
closeBtn.addEventListener('click', closeModal);

// Clicking outside of modal closes it
modal.addEventListener('click', (e) => {
  if (e.target === modal) closeModal();
});

// ESC closes modal
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modal.style.display === 'flex') {
    closeModal();
  }
});
</script>
