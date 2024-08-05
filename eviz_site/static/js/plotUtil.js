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
    plotTitle.setAttribute("y", 16); // top left
    plotTitle.setAttribute("x", 4);
    plotTitle.textContent = title;
    sankeySvg.appendChild(plotTitle);

    // get all the nodes ('g' tags) and put the proper labels on them
    for (const node of sankeySvg.getElementsByTagNameNS("http://www.w3.org/2000/svg", "g")) {

        let node_info = node.children[0]; // get the rect child element, which contains all the info about the node

        // only apply the label if the passes a certain size threshold
        if (node_info.getAttribute("height") < plotSection.clientHeight * 0.05)
            continue;

        // with the "nodes" json argument to this function, get the label for the node in question
        // nodes labels are kept column by row (aka position). which column and which row to use
        // is kept as html attributes in the "node_info" element
        let label = document.createElementNS("http://www.w3.org/2000/svg","text"); // text element to represent label
        label.textContent = nodes[node_info.getAttribute("column")][node_info.getAttribute("position")]["label"];
        node.appendChild(label)
    }

    updateSankeyDownload(sankeySvg);
}

let sankeyDownloadURL;
const updateSankeyDownload = (sankeySVG) => {
    // turn the inner html of the container into a data blob
    // with mime set up for svg. This will let the textual svg in the html
    // be used by image processors to display an actual image
    const downloadBlob = new Blob([sankeySVG.outerHTML], {type: "image/svg"});

    // if the link was already populated, revoke it
    // as a new link is going to be used
    if (sankeyDownloadURL != null)
        revokeObjectURL(sankeyDownloadURL);

    // set up the link with the plot data
    sankeyDownloadURL = URL.createObjectURL(downloadBlob);
}

const downloadSankey = () => {
    const a = document.createElement("a");
    a.href = sankeyDownloadURL;
    a.download = "sankey.svg";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

export {downloadSankey, createSankey};