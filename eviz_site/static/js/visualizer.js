const initialize = () => {
    methodDropdown = document.getElementById("method-dropdown");
    energyTypeDropdown = document.getElementById("energy_type-dropdown")
    lastStageDropdown = document.getElementById("last_stage-dropdown");
    ieamwDropdown = document.getElementById("ieamw-dropdown");
    includesNEUDropdown = document.getElementById("includes_neu-dropdown");
    yearDropdown = document.getElementById("year-dropdown");
    matnameDropdown = document.getElementById("matname-dropdown");
    const plotTypeSelector = document.getElementById('plot-type-dropdown');
    const toYearDropdown = document.getElementById('to-year-dropdown');
    const efficiencyDropdown = document.getElementById('efficiency-dropdown');

    plotTypeSelector.addEventListener('change', () => {
        if (plotTypeSelector.value === 'xy_plot') {
            toYearDropdown.style.display = 'inline';
            efficiencyDropdown.style.display = 'inline';
        } else {
            toYearDropdown.style.display = 'none';
            efficiencyDropdown.style.display = 'none';
        }
    });
};



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

    // set up the button to remove the new dropdown if need be
    const delButton = document.createElement('button');
    delButton.onclick = () => { newDropdown.remove(); delButton.remove(); };
    delButton.type = "button";
    delButton.textContent = "X";
    delButton.classList.add("remove-button");

    // add the dropdown and button to the dom
    desiredDropdown.before(newDropdown);
    newDropdown.after(delButton);
};



