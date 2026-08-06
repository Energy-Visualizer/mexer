const openFieldTooltip = (button, tip) => {
  if (!tip._homeParent) {
    tip._homeParent = tip.parentElement;
    tip._homeNext = tip.nextSibling;
  }
  document.body.appendChild(tip);
  tip.classList.remove("hidden");

  const btnRect = button.getBoundingClientRect();
  tip.style.left = btnRect.left + "px";
  tip.style.width = "16rem";
  const spaceAbove = btnRect.top;
  if (spaceAbove > 100) {
    tip.style.top = "";
    tip.style.bottom = window.innerHeight - btnRect.top + 4 + "px";
  } else {
    tip.style.bottom = "";
    tip.style.top = btnRect.bottom + 4 + "px";
  }
};

/** Hides a field-info tooltip and returns it to its original spot in the DOM. */
const closeFieldTooltip = (tip) => {
  tip.classList.add("hidden");
  if (tip._homeParent) tip._homeParent.insertBefore(tip, tip._homeNext);
};

/** Toggles a field-info tooltip open/closed. Bound to the (i) button's onclick. */
const toggleFieldTooltip = (button) => {
  const wrapper = button.parentElement;
  const tip =
    wrapper._tip || (wrapper._tip = wrapper.querySelector(".field-tooltip"));

  if (tip.classList.contains("hidden")) openFieldTooltip(button, tip);
  else closeFieldTooltip(tip);
};

const closeAllFieldTooltips = () => {
  document
    .querySelectorAll(".field-tooltip:not(.hidden)")
    .forEach(closeFieldTooltip);
};

let currentActionTab = "plot";

const switchActionTab = (tab) => {
  currentActionTab = tab;

  const plotBtn = document.getElementById("plot-tab-btn");
  const downloadBtn = document.getElementById("download-tab-btn");
  const plotPanel = document.getElementById("plot-tab-panel");
  const downloadPanel = document.getElementById("download-tab-panel");

  const activate = (btn) => {
    btn.classList.add("border-blue-500", "text-blue-500");
    btn.classList.remove("border-transparent", "text-gray-500");
  };
  const deactivate = (btn) => {
    btn.classList.remove("border-blue-500", "text-blue-500");
    btn.classList.add("border-transparent", "text-gray-500");
  };

  const showPlot = tab === "plot";
  plotPanel.classList.toggle("hidden", !showPlot);
  downloadPanel.classList.toggle("hidden", showPlot);
  showPlot ? activate(plotBtn) : activate(downloadBtn);
  showPlot ? deactivate(downloadBtn) : deactivate(plotBtn);

  // "Visualization" / "X-Y plot" read oddly when nothing is being plotted.
  const vizLabel = document.querySelector(
    "#viz-type-label-wrapper .font-semibold",
  );
  const xyLabel = document.getElementById("xy-plot-type-label");
  if (vizLabel) vizLabel.textContent = showPlot ? "Visualization" : "Data Type";
  if (xyLabel) xyLabel.textContent = showPlot ? "X-Y plot" : "X-Y data";

  applyPlotTypeVisibility();
};

const findMissingRequiredFields = (form) => {
  const missingNames = new Set();
  form.querySelectorAll("[required]").forEach((field) => {
    if (field.disabled) return;
    const container = field.closest(".query-choice") || field;
    if (container.offsetParent === null) return; // not visible

    if (field.type === "radio") {
      const group = form.querySelectorAll(
        `input[type="radio"][name="${field.name}"]`,
      );
      const anyChecked = [...group].some((radio) => radio.checked);
      if (!anyChecked) missingNames.add(field.name);
    } else if (!field.value) {
      missingNames.add(field.name);
    }
  });
  return [...missingNames];
};

/** Blocks submission with a clear message if a visible required field is unfilled. */
const guardFormSubmit = (form) => {
  const missing = findMissingRequiredFields(form);
  if (missing.length > 0) {
    alert(
      "Please fill in the following before continuing: " + missing.join(", "),
    );
    return false;
  }
  return true;
};

/**
 * Initializes the application UI and sets up event listeners.
 * This function is called when the page loads.
 */
const initialize = () => {
  initRegionDropdown();

  // let htmx give a general error response when something goes wrong with
  // some data
  document.body.addEventListener("htmx:responseError", (error) => {
    error.detail.target.innerHTML = `Error creating plot! Status code ${error.detail.xhr.status}.\nPlease try again later. Contact information on the about page.`;
  });

  document.body.addEventListener("htmx:sendError", (error) => {
    error.detail.target.innerHTML = `Error creating plot! Status code ${error.detail.xhr.status}.\nPlease try again later. Contact information on the about page.`;
  });

  const datasetDropdown = document.getElementById("dataset-dropdown");

  document.addEventListener("DOMContentLoaded", function () {
    document
      .getElementById("matname-dropdown")
      .addEventListener("change", function () {});
  });

  const setMatrixOptions = () => {
    const datasetOption = datasetDropdown.selectedOptions[0];
    const datasetTables = JSON.parse(datasetOption.getAttribute("data-table"));

    // Adjust visibility of matrix list items based on target dataset.
    const matrixOptions = [...matnameDropdown.children];
    let found = false;
    for (let i = 0; i < matrixOptions.length; i++) {
      const option = matrixOptions[i];
      const matrixTables = JSON.parse(option.getAttribute("data-table"));
      const overlap = matrixTables.some((t) => datasetTables.includes(t));

      if (overlap) {
        option.classList.remove("hidden");
        if (!found) {
          found = true;
          matnameDropdown.selectedIndex = i;
        }
      } else option.classList.add("hidden");
    }

    showColors();
  };

  datasetDropdown.addEventListener("change", () => {
    setMatrixOptions();

    // Version dropdown depends on whether we're targeting a sandbox or
    // non-sandbox dataset.
    if (document.getElementById("dataset-dropdown").value.startsWith("sDB:")) {
      document.getElementById("sandbox-version-dropdown").hidden = false;
      document.getElementById("sandbox-version-dropdown").disabled = false;
      document.getElementById("version-dropdown").hidden = true;
      document.getElementById("version-dropdown").disabled = true;
    } else {
      document.getElementById("sandbox-version-dropdown").hidden = true;
      document.getElementById("sandbox-version-dropdown").disabled = true;
      document.getElementById("version-dropdown").hidden = false;
      document.getElementById("version-dropdown").disabled = false;
    }
  });

  assertion_message_instruction =
    " -- ensure this failed input has its id field set properly";
  const menu_input_assert = (input_element, input_name) =>
    console.assert(input_element, input_name + assertion_message_instruction);

  menuInputs = []; // collection to keep track of all the items that can be toggled in the menus

  // specific metadata
  const singleYearInput = document.getElementById("single-year-input");
  menu_input_assert(singleYearInput, "singleYearInput");
  menuInputs.push(singleYearInput);
  const fromYearInput = document.getElementById("from-year-input");
  menu_input_assert(fromYearInput, "fromYearInput");
  menuInputs.push(fromYearInput);
  const toYearInput = document.getElementById("to-year-input");
  menu_input_assert(toYearInput, "toYearInput");
  menuInputs.push(toYearInput);
  const efficiencyDropdown = document.getElementById("efficiency-dropdown");
  menu_input_assert(efficiencyDropdown, "efficiencyDropdown");
  menuInputs.push(efficiencyDropdown);
  const matnameDropdown = document.getElementById("matname-dropdown");
  menu_input_assert(matnameDropdown, "matnameDropdown");
  menuInputs.push(matnameDropdown);

  colorBy = document.getElementById("color-by");
  menu_input_assert(colorBy, "colorBy");
  menuInputs.push(colorBy);
  lineBy = document.getElementById("line-by");
  menu_input_assert(lineBy, "lineBy");
  menuInputs.push(lineBy);
  facetColBy = document.getElementById("facet-col-by");
  menu_input_assert(facetColBy, "facetColBy");
  menuInputs.push(facetColBy);
  facetRowBy = document.getElementById("facet-row-by");
  menu_input_assert(facetRowBy, "facetRowBy");
  menuInputs.push(facetRowBy);

  grossNet = document.getElementById("gross_net_radio");
  menu_input_assert(grossNet, "grossNet");

  coloringMethod = document.getElementById("coloring-options");
  menu_input_assert(coloringMethod, "coloringMethod");

  colorScale = document.getElementById("color-scale");
  menu_input_assert(colorScale, "colorScale");
  menuInputs.push(colorScale);

  labelThreshold = document.getElementById("label-threshold");
  menu_input_assert(labelThreshold, "labelThreshold");
  menuInputs.push(labelThreshold);

  // menu setups
  sankeyMenuInputs = [singleYearInput, labelThreshold];
  xyMenuInputs = [
    fromYearInput,
    toYearInput,
    efficiencyDropdown,
    colorBy,
    lineBy,
    facetColBy,
    facetRowBy,
  ];
  matrixMenuInputs = [fromYearInput, toYearInput, matnameDropdown, colorScale];

  plotOnlyInputs = [
    efficiencyDropdown,
    colorBy,
    lineBy,
    facetColBy,
    facetRowBy,
    colorScale,
    labelThreshold,
  ];

  // have specifics show differently for different plots
  const plotTypeButtons = document.querySelectorAll(".plot-type-input");
  plotTypeButtons.forEach((plotTypeButton) => {
    plotTypeButton.addEventListener("change", applyPlotTypeVisibility);
  });

  // set up the query section for whichever plot type (and tab) is active
  applyPlotTypeVisibility();

  // Let users select what form of data they would like to download
  // No download options present in HTML
  // document.getElementById('download-options-button').addEventListener('click', function () {
  //     var downloadOptions = document.getElementById('download-options');
  //     downloadOptions.classList.toggle('hidden');
  // });

  // Auto-close settings when plot is generated.
  const makePlotButton = document.getElementById("get");
  const plotSection = document.getElementById("plot-section");

  makePlotButton.addEventListener("click", () => {
    plotSection.scrollIntoView();
    closePlotMenu(plotParamsMenu, ppTglButton);
  });

  const showColors = () => {
    // Coloring Method is plot-only, so it never applies on the Download tab
    // regardless of which matrix is selected.
    if (matnameDropdown.value === "RUVY" && currentActionTab === "plot") {
      inputRadioOn(coloringMethod);
    } else {
      inputRadioOff(coloringMethod);
    }
  };

  matnameDropdown.onchange = showColors;
  showColors();

  setMatrixOptions();
};

/** Enables an input element and displays its container. */
const inputOn = (element) => {
  if (element === null) return;

  element.disabled = false;
  element.closest(".query-choice").style.display = "block"; // the closest ancestor has the associated text and input itself
};

/** Disables an input element and hides its container. */
const inputOff = (element) => {
  if (element === null) return;

  element.disabled = true;
  console.log("Hide", element);
  element.closest(".query-choice").style.display = "none"; // the closest ancestor has the associated text and input itself
};

/** Enables all radio buttons within an element and displays the container */
const inputRadioOn = (element) => {
  if (element === null) return;

  const radioButtons = element.querySelectorAll('input[type="radio"]');
  radioButtons.forEach((radio) => {
    radio.disabled = false;
  });
  element.closest(".query-choice").style.display = "block";
};

/** Disables all radio buttons within an element and displays the container */
const inputRadioOff = (element) => {
  if (element === null) return;

  const radioButtons = element.querySelectorAll('input[type="radio"]');
  radioButtons.forEach((radio) => {
    radio.disabled = true;
  });
  console.log("Hide", element);
  element.closest(".query-choice").style.display = "none";
};

const startMenuSwitch = () => {
  for (let item of menuInputs) inputOff(item);
  inputRadioOff(grossNet);
  inputRadioOff(coloringMethod);
};

const handleXYPlot = () => {
  startMenuSwitch();
  for (let item of xyMenuInputs) inputOn(item);
  inputRadioOn(grossNet);
  inputRadioOff(coloringMethod);
};

// Configure UI for Sankey Diagram
const handleSankey = () => {
  startMenuSwitch();
  for (let item of sankeyMenuInputs) inputOn(item);
  inputRadioOff(coloringMethod);
};

// Configure UI for matrices
const handleMatrices = () => {
  startMenuSwitch();
  for (let item of matrixMenuInputs) inputOn(item);
  inputRadioOn(coloringMethod);
};

const applyPlotTypeVisibility = () => {
  const selected = document.querySelector(".plot-type-input:checked")?.value;
  if (selected === "xy_plot") handleXYPlot();
  else if (selected === "sankey") handleSankey();
  else if (selected === "matrices") handleMatrices();
  else startMenuSwitch();

  if (currentActionTab === "download") {
    for (let item of plotOnlyInputs) inputOff(item);
    inputRadioOff(coloringMethod);
  }
};

const setRegionMode = (isAll) => {
  let countryDropdownsContainer = document.getElementById("country-dropdowns");
  let addCountryBtn = document.getElementById("add-country-btn");
  countryDropdownsContainer
    .querySelectorAll("select")
    .forEach((sel) => (sel.disabled = isAll));
  countryDropdownsContainer.style.opacity = isAll ? "0.4" : "";
  countryDropdownsContainer.style.pointerEvents = isAll ? "none" : "";
  addCountryBtn.disabled = isAll;
};

const handleRegionMode = (radio) => setRegionMode(radio.value === "all");

const showDropdown = (name) => {
  let countryDropdown = document.getElementById("country-dropdown");
  let countryDropdownsContainer = document.getElementById("country-dropdowns");
  let templateDropdown;
  switch (name) {
    case "country":
      templateDropdown = countryDropdown;
      break;
  }

  const newSelect = templateDropdown.cloneNode(true);
  newSelect.id = "";
  newSelect.required = true;
  newSelect.disabled = false;
  newSelect.name = templateDropdown.name;

  const removeBtn = document.createElement("button");
  removeBtn.type = "button";
  removeBtn.textContent = "Remove";
  removeBtn.className =
    "px-3 py-1.5 text-sm font-medium border border-gray-300 rounded-md bg-white text-red-600 hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-400 flex-shrink-0";

  const row = document.createElement("div");
  row.className = "flex items-center gap-2 mt-2";
  row.appendChild(newSelect);
  row.appendChild(removeBtn);

  removeBtn.addEventListener("click", () => row.remove());

  countryDropdownsContainer.appendChild(row);
};

document.addEventListener("DOMContentLoaded", () => {
  const initialMode = document.querySelector(
    'input[name="region-mode"]:checked',
  );
  if (initialMode) setRegionMode(initialMode.value === "all");
});

let plotWindow = null;
let plotWindowLoaded = false;
const plotInNewWindow = () => {
  // get the plot html to insert into the plot window
  const plotHTML = document.getElementById("plot-section").outerHTML;

  // if the plot was closed, set it to null to reopen
  if (plotWindow?.closed) {
    plotWindow = null;
    plotWindowLoaded = false;
  }

  // make a new plot window if need be and give it the plotHtml content
  plotWindow ??= window.open(
    "/plot-stage",
    "_blank",
    "location=yes,height=600,width=600,scrollbars=yes,status=yes",
  );
  // use insertAdjacentHTML() to parse the plotHTML and insert the proper
  // nodes into the new window DOM
  plotWindow.onload = (e) => {
    plotWindow.document.body.insertAdjacentHTML("afterbegin", plotHTML);
    plotWindowLoaded = true;
  };

  if (plotWindowLoaded) plotWindow.document.body.innerHTML = plotHTML;
};
