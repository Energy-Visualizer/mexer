---
title: "Mexer: An Open-Source Energy and Exergy Data Visualization Platform"
tags:
  - Python
  - Django
  - Energy
  - Exergy
  - Data Visualization
  - Docker
authors:
  - name: Adam Byle
    orcid: https://orcid.org/0009-0000-2983-1906
    affiliation: 1
  - name: Edom Maru
    orcid: https://orcid.org/0009-0006-9527-9615
    affiliation: 1
  - name: Kenneth Howes
    affiliation: 1
  - name: Matthew Heun
    orcid: https://orcid.org/0000-0002-7438-214X
    affiliation: 1
  - name: Randall Pruim
    orcid: https://orcid.org/0000-0002-0817-2371
    affiliation: 1
affiliations:
  - name: Calvin University
    index: 1
date: 03 April 2025
bibliography: paper.bib
---

# Summary

Mexer is an open-source, web-based platform designed for the interactive visualization of energy and exergy data. It enables users to explore and analyze energy conversion chains (ECCs) which offers valuable understanding of energy systems and their efficiencies. Mexer provides a user-friendly interface that makes complex datasets on energy production, transformation, and consumption accessible and engaging. By translating raw data into meaningful visualization, Mexer bridges the gap between raw energy data and practical understanding which supports informed decision-making in energy management, sustainability planning, and policy development.[@brockway2024clpfu] [@pinto2023electricity] [@WPFUDatabase2024] [@Heun2024].

# Statement of need

Energy and exergy analysis are essential for evaluating the efficiency of energy systems and guiding sustainable energy policy [@brockway2024clpfu]. Understanding the dynamic nature of energy conversion and utilization is critical for addressing global energy challenges. However, many existing platforms lack the flexibility and interactivity needed by energy researchers, policymakers, and educators[@tostes2024rail] [@CLPFUDatabase2024]. Mexer addresses these limitations by providing an open-source, web-based solution that enables users to generate interactive visualizations of energy and exergy flows across different sectors and regions, without the need for coding expertise.

# Functionality

Mexer integrtes energy data from the World Physical-Final-Useful (WPFU) database, which is pre-processed and stored in a PostgreSQL database. This data is structured into transformation matrices representing energy and exergy flows across different sectors and regions. Users interact with the front-end interface to select their desired parameters such as countries, energy types, and time periods. This input triggers real-time queries to the Django backend, which processes the data, applies necessary computations, and formats it for visualization.

Once processed, the data is passed to visualization libraries like Plotly and VegaLite, enabling users to explore dynamic visualizations such as Sankey diagrams, XY plots, or matrix views. These visualizations allow users to investigate energy flows, identify inefficiencies, and compare different regions or timeframes. Additionally, users have options to download images, raw data, or copy plots for external use. The platform is built with scalability in mind, utilizing a containerized architecture with Docker, which ensures easy deployment and easy hosting on local servers or the cloud. The system also includes a history feature, allowing users to track and revisit their past queries and visualizations for ongoing analysis or comparison. This setup allows Mexer to provide an efficient and accessible tool for energy researchers, policymakers, and educators to analyze and present energy system data[@pinto2023electricity] [@brockway2024clpfu].

## Key features

- **Data visualization**: Mexer supports multiple visualization types, including Sankey diagrams, XY plots, and matrices, allowing users to explore energy data from different perspectives.
- **Customization**: Users can customize visualizations based on specific needs, such as selecting data ranges, applying filters, and modifying visualization parameters, without writing any query code.
- **Historical query tracking**: Mexer allows users to revisit past visualizations for comparative analysis.
- **No coding required**: All functionalities are accessible via the graphical interface, removing the barrier for non-technical users.
- **Data-download capabilities**: Users can download filtered datasets and visual representations for offline analysis, presentation, or policy documentation.
- **Containerized deployment**: Mexer uses a Docker-based deployment to ensure ease of installation and compatibility across different environments [@docker].

# Example usage

Mexer is designed to be a versatile tool that can be used across various sectors of energy research and policy-making. Potential use cases include:

- **Identifying energy efficiency opportunities**: By visualizing energy usage over time, users can pinpoint areas where behavioral or infrastructural changes could optimize energy consumption.

- **Informing policy decisions**: Mexer can provide policymakers with visual evidence of how different energy policies impact consumption patterns, supporting informed decision-making.

- **Analyzing long-term energy transitions**: Mexer can be used to study historical energy data and assess changes in energy efficiency over decades, offering valuable insights into long-term sustainability efforts.

# Acknowledgements

The development of Mexer was supported by the Energy Economics Team. We appreciate the contributions of Tânia Sousa, Paul Brockway, and all collaborators whose input has been invaluable in shaping the tool's functionality and user experience. Mexer was developed at Calvin University as part of the STEM department's summer research program. Initial development was made possible with a grant from Instituto Superior Técnico, Lisbon, Portugal.

# References
