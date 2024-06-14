const initialize = () => {
    // main metadata
    methodDropdown = document.getElementById("method-dropdown");
    energyTypeDropdown = document.getElementById("energy_type-dropdown")
    lastStageDropdown = document.getElementById("last_stage-dropdown");
    ieamwDropdown = document.getElementById("ieamw-dropdown");
    includesNEUDropdown = document.getElementById("includes_neu-dropdown");

    // specific metadata
    singleYearInput = document.getElementById("single-year-input");
    fromYearInput = document.getElementById("from-year-input");
    toYearInput = document.getElementById("to-year-input");
    efficiencyDropdown = document.getElementById('efficiency-dropdown');
    matnameDropdown = document.getElementById("matname-dropdown");

    // have specifics show differently for different plots
    const plotTypeSelector = document.getElementById('plot-type-dropdown');
    plotTypeSelector.addEventListener('change', () => {

        if (plotTypeSelector.value === 'xy_plot')
            handleXYPlot();

        else if (plotTypeSelector.value === "sankey")
            handleSankey();

        else if (plotTypeSelector.value === "matrices")
            handleMatrices();
    });

    // have whatever the plot selection is currently set to show up at start
    // TODO: make this better
    if (plotTypeSelector.value === 'xy_plot')
        handleXYPlot();

    else if (plotTypeSelector.value === "sankey")
        handleSankey();

    else if (plotTypeSelector.value === "matrices")
        handleMatrices();
};

const inputOn = (element) => {
    element.disabled = false;
    element.parentElement.style.display = "block";
}

const inputOff = (element) => {
    element.disabled = true;
    element.parentElement.style.display = "none";
}

const handleXYPlot = () => {
    inputOff(singleYearInput);
    inputOff(matnameDropdown);

    inputOn(fromYearInput);
    inputOn(toYearInput);
    inputOn(efficiencyDropdown);
}

const handleSankey = () => {
    inputOff(fromYearInput);
    inputOff(toYearInput);
    inputOff(efficiencyDropdown);
    inputOff(matnameDropdown);

    inputOn(singleYearInput);
}

const handleMatrices = () => {
    inputOff(fromYearInput);
    inputOff(toYearInput);
    inputOff(efficiencyDropdown);
    
    inputOn(matnameDropdown);
    inputOn(singleYearInput);
}

const showDropdown = (name) => {

    // figure out which dropdown we want to add
    let desiredDropdown;
    switch (name) {
        case ("method"):
            desiredDropdown = methodDropdown;
            break;
        case ("energy_type"):
            desiredDropdown = energyTypeDropdown;
            break;
        case ("last_stage"):
            desiredDropdown = lastStageDropdown;
            break;
        case ("ieamw"):
            desiredDropdown = ieamwDropdown;
            break;
        case ("includes_neu"):
            desiredDropdown = includesNEUDropdown;
            break;
        case ("year"):
            desiredDropdown = yearDropdown;
            break;
        case ("matname"):
            desiredDropdown = matnameDropdown;
            break;
    }

    // set up the new dropdown
    // needs to be constant or the remove buttons will get confused on which to delete
    const newDropdown = desiredDropdown.cloneNode(deep = true);
    newDropdown.style.display = "inline";
    newDropdown.required = "required";
    newDropdown.disabled = false;

    // set up the button to remove the new dropdown if need be
    const delButton = document.createElement('button');
    delButton.onclick = () => { newDropdown.remove(); delButton.remove(); };
    delButton.type = "button";
    delButton.textContent = "\u2717";
    delButton.classList.add("remove-button");

    // add the dropdown and button to the dom
    desiredDropdown.before(newDropdown);
    newDropdown.after(delButton);
};



