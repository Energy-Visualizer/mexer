const plotSection = document.getElementById("plot-section");

import {PlotCreator} from './SanKEY_script.js'

const createSankey = (nodes, links, options, title) => {
    // plotSection.innerHTML = ""; // clear the plot section first
    let sankeyPlot = new PlotCreator(
        plotSection, // container in the dom
        nodes,
        links,
        plotSection.clientWidth, // plot width
        plotSection.clientHeight, // plot height
        0, // first column to show
        5, // last column to show (e.g. 0, 4 shows columns 0-3)

        // further options
        // combination of "options" param and options defined here
        Object.assign(options, {
            on_link_hover_function: (link_info,link_data_reference,link_element,event) => {
                return `${link_info["from_label"]}<br>${Math.round(link_info["value"])} TJ<br>${link_info["to_label"]}`
            },
            on_node_hover_function: (node_info,node_data_reference,node_element,event) => {
                return `${node_info["label"]}<br>${Math.round(node_info["value"])} TJ`
            }
        })
    )

    /* Generating the labels and title for the sankey diagram
    The above code will generate an svg in the dom to 
    represent the sankey diagram. It is always given the ID
    "sankey_field". Getting into that svg allows for the addition
    of various HTML elements that will be our nodes labels and plot title */
    const sankeySvg = document.getElementById("sankey_field");
    
    // text elements must be created under the svg namespace to work
    const plotTitle = document.createElementNS("http://www.w3.org/2000/svg","text");
    plotTitle.setAttribute("y", 16);
    plotTitle.setAttribute("x", 4);
    plotTitle.textContent = title;
    sankeySvg.appendChild(plotTitle);

    // get all the nodes ('g' tags)
    // and all the proper labels
    for (const node of sankeySvg.getElementsByTagNameNS("http://www.w3.org/2000/svg", "g")) {
        let node_info = node.children[0];
        let label = document.createElementNS("http://www.w3.org/2000/svg","text");
        label.textContent = nodes[node_info.getAttribute("column")][node_info.getAttribute("position")]["label"];
        if (node_info.getAttribute("height") > plotSection.clientHeight * 0.05) {
            node.appendChild(label)
        }
    }
}

// to let us use the function outside of this module
window.createSankey = createSankey;

/* OLD Code

// to hold the div in which is the plot
var plotSection;

// zooming variables
var plotZoom;

// panning variables
var plotPanX, plotPanY, dragging, originX, originY;

const updatePlot = () => {
    // devide by plotZoom so that the image doesn't move relatively faster the more zoomed a user is
    plotSection.style.transform = "scale(" + plotZoom + ") translate(" + plotPanX / plotZoom + "px," + plotPanY / plotZoom + "px)";
}

const resetPlot = () => {
    plotSection.style.transform = "scale(1) translate(0px,0px)";
    plotZoom = 1;
    plotPanX = plotPanY = 0;
    dragging = false;
}

const initPlotUtils = () => {
    plotSection = document.querySelector("div div.plotly-graph-div");
    resetPlot();

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

}

// listener to initialize this script when htmx loads in a new plot
// htmx.on("htmx:afterSwap", (event) => {
//     if (event.detail.target.id == "plot-section")
//          initPlotUtils();
// });

end OLD Code */