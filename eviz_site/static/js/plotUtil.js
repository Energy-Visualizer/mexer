var plotSection;

const init = () => {
    plotSection = document.getElementById("plot-div");
}

// zooming variables
var plotZoom = 1;

// panning variables
var plotPanX = 0;
var plotPanY = 0;
var dragging = false;
var originX, originY;

const updatePlot = () => {
    // devide by plotZoom so that the image doesn't move relatively faster the more zoomed a user is
    plotSection.style.transform = "scale(" + plotZoom + ") translate(" + plotPanX  / plotZoom + "px," + plotPanY  / plotZoom + "px)";
}

const resetPlot = () => {
    plotSection.style.transform = "scale(1) translate(0px,0px)";
    plotZoom = 1;
    plotPanX = plotPanY = 0;
    dragging = false;
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

    // TODO: zoom into where the user's mouse points
    // plotSection.style.transformOrigin = event.clientX / plotZoom + "px " + event.clientY / plotZoom + "px";
    updatePlot();
}

// panning

// get mouse down to start panning
plotSection.onmousedown = (event) => {

    // if middle mouse button was clicked
    if (event.which == 2 || event.button == 4) {
        event.preventDefault()
        dragging = true;
        originX = event.clientX - plotPanX;
        originY = event.clientY - plotPanY;
    }
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