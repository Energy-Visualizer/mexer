const HISTORY_STORAGE_KEY = "mexer_history_v1";

const HISTORY_DATA_FIELDS = [
  "dataset",
  "version",
  "country",
  "method",
  "energy_type",
  "last_stage",
  "product_aggregation",
  "industry_aggregation",
  "plot_type",
  "gross_net",
  "matname",
  "year",
  "to_year",
];

const loadHistoryStore = () => {
  try {
    const raw = localStorage.getItem(HISTORY_STORAGE_KEY);
    if (!raw) return { entries: [], groups: [] };
    const parsed = JSON.parse(raw);
    return {
      entries: Array.isArray(parsed.entries) ? parsed.entries : [],
      groups: Array.isArray(parsed.groups) ? parsed.groups : [],
    };
  } catch (e) {
    console.error("Failed to read history from localStorage", e);
    return { entries: [], groups: [] };
  }
};

const saveHistoryStore = (store) => {
  try {
    localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(store));
  } catch (e) {
    console.error("Failed to save history to localStorage", e);
  }
};

const generateId = () => {
  if (window.crypto?.randomUUID) return window.crypto.randomUUID();
  return "id-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
};

const plotTypeLabel = (plotType) => {
  switch (plotType) {
    case "sankey":
      return "Sankey";
    case "xy_plot":
      return "X-Y Plot";
    case "matrices":
      return "Matrices";
    default:
      return plotType || "Plot";
  }
};

const countryLabel = (countryField) => {
  if (!countryField) return "No region";
  const countries = Array.isArray(countryField) ? countryField : [countryField];
  if (countries.length === 1) return countries[0];
  return `${countries[0]} +${countries.length - 1}`;
};

const formatRelativeTime = (isoString) => {
  const then = new Date(isoString).getTime();
  const diffSeconds = Math.round((Date.now() - then) / 1000);

  if (diffSeconds < 5) return "Just now";
  if (diffSeconds < 60) return `${diffSeconds}s ago`;

  const diffMinutes = Math.round(diffSeconds / 60);
  if (diffMinutes < 60) return `${diffMinutes}m ago`;

  const diffHours = Math.round(diffMinutes / 60);
  if (diffHours < 24) return `${diffHours}h ago`;

  const diffDays = Math.round(diffHours / 24);
  if (diffDays < 7) return `${diffDays}d ago`;

  return new Date(isoString).toLocaleDateString(undefined, {
    month: "short",
    day: "numeric",
  });
};

const generateEntryName = (plotType, fields) => {
  const parts = [
    countryLabel(fields.country),
    fields.dataset || "Unknown dataset",
  ];
  if (plotType === "matrices" && fields.matname) {
    parts.push(fields.matname);
  }
  return parts.join(" > ");
};

const escapeHtml = (str) => {
  const div = document.createElement("div");
  div.textContent = String(str ?? "");
  return div.innerHTML;
};

const captureHistoryFields = (form) => {
  const formData = new FormData(form);
  const fields = {};

  for (const name of HISTORY_DATA_FIELDS) {
    const values = formData.getAll(name);
    if (values.length === 0) continue;
    fields[name] = values.length === 1 ? values[0] : values;
  }

  fields.includes_neu = formData.has("includes_neu");
  return fields;
};

const setSelectValue = (select, value) => {
  if (!select || value === undefined) return;
  select.value = value;
  select.dispatchEvent(new Event("change", { bubbles: true }));
};

const setRadioValue = (form, name, value) => {
  if (value === undefined) return;
  const radios = form.querySelectorAll(`input[type="radio"][name="${name}"]`);
  radios.forEach((radio) => {
    radio.checked = radio.value === value;
  });
  const checked = form.querySelector(
    `input[type="radio"][name="${name}"]:checked`,
  );
  if (checked) checked.dispatchEvent(new Event("change", { bubbles: true }));
};

const setCheckboxGroup = (form, name, values) => {
  if (values === undefined) return;
  const wanted = Array.isArray(values) ? values : [values];
  const boxes = form.querySelectorAll(`input[type="checkbox"][name="${name}"]`);
  boxes.forEach((box) => {
    box.checked = wanted.includes(box.value);
  });
};

const setAllNamed = (form, name, value) => {
  if (value === undefined) return;
  form.querySelectorAll(`[name="${name}"]`).forEach((el) => {
    el.value = value;
  });
};

const restoreHistoryEntry = (id) => {
  const store = loadHistoryStore();
  const entry = store.entries.find((e) => e.id === id);
  if (!entry) return;

  const form = document.getElementById("query-form");
  if (!form) return;

  const fields = entry.fields;

  // Plot type first, determines which fields are even visible/enabled.
  setRadioValue(form, "plot_type", entry.plotType);

  // Dataset next, changing it can reset dependent fields (matrix options,
  // sandbox version visibility), so anything dependent must be set after.
  if (fields.dataset) {
    setSelectValue(document.getElementById("dataset-dropdown"), fields.dataset);
  }

  if (fields.version) {
    const isSandbox = String(fields.dataset || "").startsWith("sDB:");
    const versionSelect = document.getElementById(
      isSandbox ? "sandbox-version-dropdown" : "version-dropdown",
    );
    setSelectValue(versionSelect, fields.version);
  }

  setCheckboxGroup(form, "country", fields.country);
  setCheckboxGroup(form, "method", fields.method);
  setCheckboxGroup(form, "energy_type", fields.energy_type);
  setCheckboxGroup(form, "product_aggregation", fields.product_aggregation);
  setCheckboxGroup(form, "industry_aggregation", fields.industry_aggregation);

  if (fields.last_stage) setRadioValue(form, "last_stage", fields.last_stage);
  if (fields.gross_net) setRadioValue(form, "gross_net", fields.gross_net);

  const includesNeu = form.querySelector('[name="includes_neu"]');
  if (includesNeu) includesNeu.checked = Boolean(fields.includes_neu);

  // Matrix must be set after dataset settles, since dataset change
  // auto-selects a default matrix.
  if (fields.matname) {
    setSelectValue(document.getElementById("matname-dropdown"), fields.matname);
  }

  setAllNamed(form, "year", fields.year);
  setAllNamed(form, "to_year", fields.to_year);

  if (sidebar?.dataset.open === "true") {
    closeSidebar(sidebar, toggleBtn);
  }
};

const addHistoryEntry = (plotType, fields) => {
  const store = loadHistoryStore();
  const now = new Date().toISOString();

  // If this exact query is already in history, bump it to the top and
  // refresh its timestamp instead of creating a duplicate. Preserves
  // any rename/pin/group the user has already set on it.
  const existingIndex = store.entries.findIndex(
    (e) =>
      e.plotType === plotType &&
      JSON.stringify(e.fields) === JSON.stringify(fields),
  );

  if (existingIndex !== -1) {
    const [existing] = store.entries.splice(existingIndex, 1);
    existing.createdAt = now;
    store.entries.unshift(existing);
  } else {
    store.entries.unshift({
      id: generateId(),
      name: generateEntryName(plotType, fields),
      pinned: false,
      groupId: null,
      createdAt: now,
      plotType,
      fields,
    });
  }

  saveHistoryStore(store);
  renderHistory();
};

const deleteHistoryEntry = (id) => {
  const store = loadHistoryStore();
  store.entries = store.entries.filter((e) => e.id !== id);
  saveHistoryStore(store);
  renderHistory();
};

const renameHistoryEntry = (id, newName) => {
  if (!newName || !newName.trim()) return;
  const store = loadHistoryStore();
  const entry = store.entries.find((e) => e.id === id);
  if (entry) entry.name = newName.trim();
  saveHistoryStore(store);
  renderHistory();
};

const toggleHistoryPin = (id) => {
  const store = loadHistoryStore();
  const entry = store.entries.find((e) => e.id === id);
  if (entry) entry.pinned = !entry.pinned;
  saveHistoryStore(store);
  renderHistory();
};

const assignHistoryGroup = (id, groupId) => {
  const store = loadHistoryStore();
  const entry = store.entries.find((e) => e.id === id);
  if (entry) entry.groupId = groupId || null;
  saveHistoryStore(store);
  renderHistory();
};

const createHistoryGroup = (name) => {
  if (!name || !name.trim()) return;
  const store = loadHistoryStore();
  store.groups.push({
    id: generateId(),
    name: name.trim(),
    createdAt: new Date().toISOString(),
  });
  saveHistoryStore(store);
  renderHistory();
};

const renameHistoryGroup = (id, newName) => {
  if (!newName || !newName.trim()) return;
  const store = loadHistoryStore();
  const group = store.groups.find((g) => g.id === id);
  if (group) group.name = newName.trim();
  saveHistoryStore(store);
  renderHistory();
};

const deleteHistoryGroup = (id) => {
  const store = loadHistoryStore();
  store.groups = store.groups.filter((g) => g.id !== id);
  store.entries.forEach((e) => {
    if (e.groupId === id) e.groupId = null;
  });
  saveHistoryStore(store);
  renderHistory();
};

const clearHistory = () => {
  const confirmed = confirm(
    "Clear all history? This will permanently delete every history entry and group. This cannot be undone.",
  );
  if (!confirmed) return;

  saveHistoryStore({ entries: [], groups: [] });
  renderHistory();
};

const promptRenameEntry = (id) => {
  const entry = loadHistoryStore().entries.find((e) => e.id === id);
  if (!entry) return;
  const name = prompt("Rename history entry:", entry.name);
  if (name !== null) renameHistoryEntry(id, name);
};

const promptRenameGroup = (id) => {
  const group = loadHistoryStore().groups.find((g) => g.id === id);
  if (!group) return;
  const name = prompt("Rename group:", group.name);
  if (name !== null) renameHistoryGroup(id, name);
};

const promptNewGroup = () => {
  const name = prompt("New group name:");
  if (name) createHistoryGroup(name);
};

const renderEntry = (entry, groups) => {
  const groupOptions = groups
    .map(
      (g) =>
        `<option value="${g.id}" ${entry.groupId === g.id ? "selected" : ""}>${escapeHtml(g.name)}</option>`,
    )
    .join("");

  return `
    <div class="bg-gray-800 rounded-md p-2 mb-2 text-left">
      <div class="flex items-start gap-2">
        <button type="button"
          class="flex-1 min-w-0 text-left bg-transparent hover:bg-gray-700 rounded-md p-1 transition-colors"
          onclick="restoreHistoryEntry('${entry.id}')">
          <span class="block font-semibold text-sm break-words">${escapeHtml(entry.name)}</span>
          <span class="block text-xs text-gray-400">${escapeHtml(plotTypeLabel(entry.plotType))} - ${escapeHtml(formatRelativeTime(entry.createdAt))}</span>
        </button>
        <div class="flex flex-col gap-1 items-center pt-1 flex-shrink-0">
          <button type="button" title="${entry.pinned ? "Unpin" : "Pin"}"
            class="${entry.pinned ? "text-yellow-400" : "text-gray-400"} hover:text-yellow-300 text-xs w-4"
            onclick="toggleHistoryPin('${entry.id}')">
            <i class="fas fa-thumbtack"></i>
          </button>
          <button type="button" title="Rename"
            class="text-gray-400 hover:text-blue-400 text-xs w-4"
            onclick="promptRenameEntry('${entry.id}')">
            <i class="fas fa-pen"></i>
          </button>
          <button type="button" title="Delete"
            class="text-gray-400 hover:text-red-400 text-xs w-4"
            onclick="deleteHistoryEntry('${entry.id}')">
            <i class="fas fa-trash-alt"></i>
          </button>
        </div>
      </div>
      ${
        groups.length > 0
          ? `<select class="w-full max-w-full text-xs bg-gray-700 text-white rounded-md mt-2 px-1 py-1"
               onchange="assignHistoryGroup('${entry.id}', this.value)">
               <option value="">No group</option>
               ${groupOptions}
             </select>`
          : ""
      }
    </div>
  `;
};

const renderSection = (title, entries, groups) => `
  <div class="mt-4">
    ${title ? `<span class="text-sm font-bold text-cyan-400 px-1">${escapeHtml(title)}</span>` : ""}
    <div class="mt-2">
      ${entries.map((e) => renderEntry(e, groups)).join("")}
    </div>
  </div>
`;

const renderGroupSection = (group, groupEntries, allGroups) => `
  <div class="mt-4">
    <div class="flex items-center justify-between px-1">
      <span class="text-sm font-bold text-cyan-400 truncate">${escapeHtml(group.name)}</span>
      <div class="flex gap-2 flex-shrink-0">
        <button type="button" title="Rename group" class="text-gray-400 hover:text-blue-400 text-xs"
          onclick="promptRenameGroup('${group.id}')"><i class="fas fa-pen"></i></button>
        <button type="button" title="Delete group" class="text-gray-400 hover:text-red-400 text-xs"
          onclick="deleteHistoryGroup('${group.id}')"><i class="fas fa-trash-alt"></i></button>
      </div>
    </div>
    <div class="mt-2">
      ${
        groupEntries.length > 0
          ? groupEntries.map((e) => renderEntry(e, allGroups)).join("")
          : '<p class="text-xs text-gray-500 px-1">No entries in this group.</p>'
      }
    </div>
  </div>
`;

const renderHistory = () => {
  const container = document.getElementById("history-list");
  if (!container) return;

  const { entries, groups } = loadHistoryStore();

  if (entries.length === 0) {
    container.innerHTML =
      '<p class="text-sm text-gray-400 mt-2">No history yet.</p>';
    return;
  }

  const pinned = entries.filter((e) => e.pinned);
  const byGroup = new Map(groups.map((g) => [g.id, []]));
  const ungrouped = [];

  entries.forEach((e) => {
    if (e.pinned) return;
    if (e.groupId && byGroup.has(e.groupId)) {
      byGroup.get(e.groupId).push(e);
    } else {
      ungrouped.push(e);
    }
  });

  let html = "";

  if (pinned.length > 0) html += renderSection("Pinned", pinned, groups);
  groups.forEach((group) => {
    html += renderGroupSection(group, byGroup.get(group.id) || [], groups);
  });
  if (ungrouped.length > 0)
    html += renderSection(
      groups.length > 0 ? "Ungrouped" : "",
      ungrouped,
      groups,
    );

  html += `
    <div class="mt-4 flex flex-col gap-2">
      <button type="button" onclick="promptNewGroup()"
        class="w-full text-sm bg-gray-800 hover:bg-gray-700 text-white rounded-md py-2 px-3">
        + New Group
      </button>
      <button type="button" onclick="clearHistory()"
        class="w-full text-sm bg-red-900 hover:bg-red-800 text-white rounded-md py-2 px-3">
        Clear History
      </button>
    </div>
  `;

  container.innerHTML = html;
};
