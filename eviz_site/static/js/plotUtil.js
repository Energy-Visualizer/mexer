var plotSection = document.getElementById("plot-div")

// zooming variables
var plotZoom = 1;

// panning variables
var plotPanX = 0;
var plotPanY = 0;
var dragging = false;
var originX, originY;

const updatePlot = () => {
    plotSection.style.transform = "scale(" + plotZoom + ") translate(" + plotPanX + "px," + plotPanY + "px)";
    console.log("scale(" + plotZoom + ") translate(" + plotPanX + "px," + plotPanY + "px)");
    // plotSection.style.transformOrigin = "0 0";
}

// zooming
plotSection.onwheel = (event) => {
    event.preventDefault();

    // if scrolling wheel up, increase zoom
    if (event.deltaY < 0)
        plotZoom *= 1.1;

    // if scrolling wheel down, decrease zoom
    else
        plotZoom /= 1.1;

    updatePlot();
}

// panning

// get mouse down to start panning
plotSection.onmousedown = (event) => {
    dragging = true;
    originX = event.clientX - plotPanX;
    originY = event.clientY - plotPanY;
}

// get mouse up to stop panning
plotSection.onmouseup = () => {
    dragging = false;
}

// get mouse movement to pan
plotSection.onmousemove = (event) => {
    // only pan if holding mouse button down
    if (dragging) {
        plotPanX = event.clientX - originX;
        plotPanY = event.clientY - originY;
        updatePlot();
    }
}