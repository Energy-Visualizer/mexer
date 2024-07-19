/**
 * Initializes the application UI and sets up event listeners.
 * This function is called when the page loads.
 */
const initialize = () => {
    // main metadata
    countryDropdown = document.getElementById("country-dropdown");

    menuInputs = []; // collection to keep track of all the items that can be toggled in the menus

    // specific metadata
    singleYearInput = document.getElementById("single-year-input");
    menuInputs.push(singleYearInput);
    fromYearInput = document.getElementById("from-year-input");
    menuInputs.push(fromYearInput);
    toYearInput = document.getElementById("to-year-input");
    menuInputs.push(toYearInput);
    efficiencyDropdown = document.getElementById('efficiency-dropdown');
    menuInputs.push(efficiencyDropdown);
    matnameDropdown = document.getElementById("matname-dropdown");
    menuInputs.push(matnameDropdown);

    colorBy = document.getElementById("color-by");
    menuInputs.push(colorBy);
    lineBy = document.getElementById("line-by");
    menuInputs.push(lineBy);
    facetColBy = document.getElementById("facet-col-by");
    menuInputs.push(facetColBy);
    facetRowBy = document.getElementById("facet-row-by");
    menuInputs.push(facetRowBy);
    grossNet = document.getElementById("grossnet_radio");

    colorScale = document.getElementById("color-scale");
    menuInputs.push(colorScale);
    
    // download button (only for matrix menu)
    downloadButton = document.getElementById("download")

    // menu setups
    sankeyMenuInputs = [singleYearInput];
    xyMenuInputs = [fromYearInput, toYearInput, efficiencyDropdown, colorBy, lineBy, facetColBy, facetRowBy];
    matrixMenuInputs = [fromYearInput, toYearInput, matnameDropdown, colorScale];

    // have specifics show differently for different plots
    let selectedValue = null; // to be filled in the following loop
    const plotTypeButtons = document.querySelectorAll('#plot-type-input');
    plotTypeButtons.forEach( (plotTypeButton) => {

        // Add approptiate event listener based on plot type
        if (plotTypeButton.checked)
            selectedValue = plotTypeButton.value; // if a button is already selected, remember its value
        
        if (plotTypeButton.value === 'xy_plot')
            plotTypeButton.addEventListener('change', handleXYPlot);

        else if (plotTypeButton.value === "sankey")
            plotTypeButton.addEventListener('change', handleSankey);

        else if (plotTypeButton.value === "matrices")
            plotTypeButton.addEventListener('change', handleMatrices);
    });

    // if there is an already selected plot, set up the query section accordingly
    if (selectedValue === "xy_plot")
        handleXYPlot();

    else if (selectedValue === "sankey")
        handleSankey();

    else if (selectedValue === "matrices")
        handleMatrices();

    // if not, hide all specifics
    else {
        startMenuSwitch();
    }
}

/** Enables an input element and displays its container. */
const inputOn = (element) => {
    element.disabled = false;
    element.closest('.query-choice').style.display = "block"; // the closest ancestor has the associated text and input itself
}

/** Disables an input element and hides its container. */
const inputOff = (element) => {
    element.disabled = true;
    element.closest('.query-choice').style.display = "none"; // the closest ancestor has the associated text and input itself
}

/** Enables all radio buttons within an element and displays the container */
const inputRadioOn = (element) => {
    const radioButtons = element.querySelectorAll('input[type="radio"]');
    radioButtons.forEach(radio => {
        radio.disabled = false;
    });
    element.closest('.query-choice').style.display = "block";
}

/** Disables all radio buttons within an element and displays the container */
const inputRadioOff = (element) => {
    const radioButtons = element.querySelectorAll('input[type="radio"]');
    radioButtons.forEach(radio => {
        radio.disabled = true;
    });
    element.closest('.query-choice').style.display = "none";
}

const startMenuSwitch = () => {
    for (let item of menuInputs)
        inputOff(item);
    downloadButton.style.display = "none";
    inputRadioOff(grossNet);
}

const handleXYPlot = () => {
    startMenuSwitch();
    for (let item of xyMenuInputs)
        inputOn(item);
    inputRadioOn(grossNet);
}

// Configure UI for Sankey Diagram
const handleSankey = () => {
    startMenuSwitch();
    for (let item of sankeyMenuInputs)
        inputOn(item);
}

// Configure UI for matrices
const handleMatrices = () => {
    startMenuSwitch();
    for (let item of matrixMenuInputs)
        inputOn(item);
    downloadButton.style.display = "block";
}

/** Add a new dropdown for a specified category */
const showDropdown = (name) => {

    // figure out which dropdown we want to add
    let desiredDropdown;
    switch (name) {
        case ("country"):
            desiredDropdown = countryDropdown;
            break;
        // case ("method"):
        //     desiredDropdown = methodDropdown;
        //     break;
    }

    // set up the new dropdown
    // needs to be constant or the remove buttons will get confused on which to delete
    const newDropdown = desiredDropdown.cloneNode(deep = true);
    newDropdown.required = "required";
    newDropdown.disabled = false;

    // set up the button to remove the new dropdown if need be
    const delButton = document.createElement('button');
    delButton.onclick = () => { newDropdown.remove(); delButton.remove(); };
    delButton.type = "button";
    delButton.textContent = "\u2717";
    delButton.classList.add("remove-button");

    // put the dropdown and button together so they act as one block
    const wholeDropdown = document.createElement("div");
    wholeDropdown.classList.add("space-info-text")
    wholeDropdown.appendChild(newDropdown);
    wholeDropdown.appendChild(delButton);

    // add the dropdown and button to the dom
    desiredDropdown.after(wholeDropdown);
};

//Refreshes the history list using HTMX
function refreshHistory() {
    htmx.ajax("GET", "/history", {target:"#history-list", swap:"innerHTML"});
}

