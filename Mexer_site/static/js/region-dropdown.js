/**
 * Region checkbox-dropdown controller.
 * Replaces the old setRegionMode / handleRegionMode / showDropdown trio.
 *
 * Expects markup like:
 * <div id="region-dropdown-root">
 *   <button id="dropdown-trigger">...</button>
 *   <div id="dropdown-panel">
 *     <button id="select-all-btn">Select all</button>
 *     <button id="deselect-all-btn">Deselect all</button>
 *     <span id="selected-count"></span>
 *     <input id="country-search" />
 *     <div id="country-options">
 *       <label><input type="checkbox" name="country" value="..."></label>
 *       ...
 *     </div>
 *   </div>
 * </div>
 */
const initRegionDropdown = () => {
  const root = document.getElementById("region-dropdown-root");
  if (!root) return; // page doesn't have the region picker; nothing to do

  const trigger = document.getElementById("dropdown-trigger");
  const triggerLabel = document.getElementById("trigger-label");
  const chevron = document.getElementById("trigger-chevron");
  const panel = document.getElementById("dropdown-panel");
  const optionsContainer = document.getElementById("country-options");
  const searchInput = document.getElementById("country-search");
  const selectAllBtn = document.getElementById("select-all-btn");
  const deselectAllBtn = document.getElementById("deselect-all-btn");
  const selectedCountEl = document.getElementById("selected-count");

  const menu_input_assert = (el, name) =>
    console.assert(el, name + " -- ensure this failed input has its id field set properly");
  menu_input_assert(trigger, "dropdown-trigger");
  menu_input_assert(panel, "dropdown-panel");
  menu_input_assert(optionsContainer, "country-options");

  // Checkboxes are server-rendered ({% for country in countries %}), so we
  // read them directly instead of holding a separate array of names.
  const getCheckboxes = () => [...optionsContainer.querySelectorAll('input[type="checkbox"]')];

  const getSelectedValues = () =>
    getCheckboxes()
      .filter((cb) => cb.checked)
      .map((cb) => cb.value);

  const syncTriggerLabel = () => {
    const all = getCheckboxes();
    const selected = getSelectedValues();

    if (selected.length === 0) {
      triggerLabel.textContent = "Select regions…";
      triggerLabel.classList.add("text-gray-400");
    } else if (selected.length === all.length) {
      triggerLabel.textContent = "All regions";
      triggerLabel.classList.remove("text-gray-400");
    } else if (selected.length <= 2) {
      triggerLabel.textContent = selected.join(", ");
      triggerLabel.classList.remove("text-gray-400");
    } else {
      triggerLabel.textContent = `${selected.length} regions selected`;
      triggerLabel.classList.remove("text-gray-400");
    }

    if (selectedCountEl) selectedCountEl.textContent = `${selected.length} selected`;
  };

  const openPanel = () => {
    panel.classList.remove("hidden");
    chevron?.classList.add("rotate-180");
    trigger.setAttribute("aria-expanded", "true");
    if (searchInput) {
      searchInput.value = "";
      filterOptions("");
      searchInput.focus();
    }
  };

  const closePanel = () => {
    panel.classList.add("hidden");
    chevron?.classList.remove("rotate-180");
    trigger.setAttribute("aria-expanded", "false");
  };

  const filterOptions = (query) => {
    const q = query.trim().toLowerCase();
    getCheckboxes().forEach((cb) => {
      const row = cb.closest("label");
      const match = cb.value.toLowerCase().includes(q);
      row.style.display = match ? "" : "none";
    });
  };

  // -- wire up events --

  trigger.addEventListener("click", () => {
    panel.classList.contains("hidden") ? openPanel() : closePanel();
  });

  document.addEventListener("click", (e) => {
    if (!root.contains(e.target)) closePanel();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closePanel();
  });

  searchInput?.addEventListener("input", (e) => filterOptions(e.target.value));

  selectAllBtn?.addEventListener("click", () => {
    getCheckboxes().forEach((cb) => (cb.checked = true));
    syncTriggerLabel();
  });

  deselectAllBtn?.addEventListener("click", () => {
    getCheckboxes().forEach((cb) => (cb.checked = false));
    syncTriggerLabel();
  });

  optionsContainer.addEventListener("change", (e) => {
    if (e.target.matches('input[type="checkbox"]')) syncTriggerLabel();
  });

  // Initial state on load (reflects whatever the server rendered as checked)
  syncTriggerLabel();
};
