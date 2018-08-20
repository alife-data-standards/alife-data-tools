
# ALife data standards tools

This is a repository which will contain tools designed to work with the
alife-data-standards.

The tools here fall broadly into two categories, converters and everything else.
The tools Tools folder contains tools which work with files in the standards
format. These tools may be analysis, visualization or helper tools. At the moment,
the tools directory contains a folder for each tool that has the code for that tool
and a readme. We may eventually find that the flat layout becomes unwieldy
 we will change 

## Converters

Within the converters folder, there is a folder for each system
(i.e. mabe, avida, aevol...). Conversion tools are named 
`[standard]_[system]2std` or `standard_std2[system]` (i.e. `genome_mabe2std.py`).

# Other tools

## Vetted web apps

Tools in this category cannot be housed in this repository because they are set up as web applications. However, they have been tested on the latest version of the standards and found to work.

- [**Phylogeny visualizer**](https://emilydolson.github.io/lineage_viz_tool/standards_viz.html): Upload a standards-compliant phylogeny file and this website will draw a tree based on it. If you have additional fields in your data you can color the nodes based on them.

## Other tools

This section includes links to tools that the standards maintainers have not yet vetted.
