const plotSection = document.getElementById("plot-section");

// Requires Plotly to be loaded globally, e.g. via:
//   <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
// If you'd rather bundle it, `npm install plotly.js-dist-min` and
// `import Plotly from "plotly.js-dist-min";` instead of relying on the global.

// keep a handle to the current plot div so download/threshold logic can reach it
let currentGraphDiv = null;
let currentNodes = null; // flat {label, color, x} from the backend, kept for label-threshold recompute

const createSankey = (nodes, links, options, title, num_columns) => {
  currentNodes = nodes;

  const data = [
    {
      type: "sankey",
      orientation: "h",
      arrangement: options.arrangement || "snap",
      node: {
        label: nodes.label,
        color: nodes.color,
        x: nodes.x,
        pad: 15,
        thickness: 20,
        line: { color: "black", width: 0.5 },
      },
      link: {
        source: links.source,
        target: links.target,
        value: links.value,
        color: links.color,
        // stash the readable from/to labels so the hovertemplate below can use them
        customdata: links.from_label.map((from_label, idx) => [
          from_label,
          links.to_label[idx],
        ]),
        hovertemplate:
          "%{customdata[0]}<br>%{value:.0f} TJ<br>%{customdata[1]}<extra></extra>",
      },
    },
  ];

  const layout = {
    title: { text: title, font: { size: 16 } },
    font: { size: 12 },
    paper_bgcolor: options.plot_background_color || "#f4edf7",
    plot_bgcolor: options.plot_background_color || "#f4edf7",
    width: plotSection.clientWidth,
    height: plotSection.clientHeight,
    margin: { l: 4, r: 4, t: 32, b: 4 },
  };

  Plotly.newPlot(plotSection, data, layout, {
    responsive: true,
    displaylogo: false,
  }).then((graphDiv) => {
    currentGraphDiv = graphDiv;
    applyLabelThreshold();
  });
};

// The old SanKEY.js renderer measured each node's rendered pixel height and
// hid the label if the node was too small. Plotly doesn't expose that hook
// directly, so we approximate "size" using each node's flow value relative
// to the largest node in the diagram, which is what actually drives a
// sankey node's rendered height.
const applyLabelThreshold = () => {
  if (!currentGraphDiv || !currentNodes) return;

  const thresholdInput = document.getElementById("label-threshold");
  if (!thresholdInput) return;

  // same "flip" as before: small slider values -> low threshold -> most labels show
  const labelThreshold = Math.pow(1 - thresholdInput.value, 5);

  const trace = currentGraphDiv.data[0];
  const nodeValues = computeNodeValues(trace.link, currentNodes.label.length);
  const maxValue = Math.max(...nodeValues, 0);

  const displayLabels = currentNodes.label.map((label, idx) => {
    const relativeSize = maxValue > 0 ? nodeValues[idx] / maxValue : 0;
    return relativeSize >= labelThreshold ? label : "";
  });

  Plotly.restyle(currentGraphDiv, { "node.label": [displayLabels] }).then(() =>
    updateSankeyDownload(),
  );
};

// a node's rendered size is proportional to max(sum of incoming, sum of outgoing)
const computeNodeValues = (link, nodeCount) => {
  const incoming = new Array(nodeCount).fill(0);
  const outgoing = new Array(nodeCount).fill(0);

  link.source.forEach((sourceIdx, i) => {
    outgoing[sourceIdx] += link.value[i];
  });
  link.target.forEach((targetIdx, i) => {
    incoming[targetIdx] += link.value[i];
  });

  return incoming.map((val, idx) => Math.max(val, outgoing[idx]));
};

let sankeyDownloadURL;
const updateSankeyDownload = () => {
  if (!currentGraphDiv) return;

  Plotly.toImage(currentGraphDiv, {
    format: "svg",
    width: plotSection.clientWidth,
    height: plotSection.clientHeight,
  }).then((dataUrl) => {
    // Plotly.toImage returns a data: URL directly, not an object URL,
    // so there's nothing to revoke here (unlike the old Blob-based approach)
    sankeyDownloadURL = dataUrl;
  });
};

const downloadSankey = () => {
  if (!sankeyDownloadURL) return;

  const a = document.createElement("a");
  a.href = sankeyDownloadURL;
  a.download = "sankey.svg";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
};

export { downloadSankey, createSankey };
