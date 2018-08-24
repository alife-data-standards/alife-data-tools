
# ALife data standards tools

## Navigation

- [Overview](#overview)
  - [Tools](#tools)
  - [Converters](#converters)
- [Other tools and applications](#other-tools)
  - [Web apps](#web-apps)
  - [Third-party tools](#third-party-tools)

## Overview

This is a repository which will contain tools designed to work with the
[ALife community data standards](https://alife-data-standards.github.io/alife-data-standards/).

The tools here fall broadly into two categories, which define the organization of
this repository:

- (1) [converters](#converters)
- (2) everything else ([tools](#tools))

### Tools

The [tools directory](./tools/) contains tools that work with files in the standards
format. Tools are usually scripts or programs that perform analyses, visualizations,
or intermediate data processing.

Currently, each tool in the tools directory is contained within a folder with a
readme that describes the tool and the tool itself. This way of organizing tools
may, however, become unwieldy in the future and is thus subject to change ([suggestions](https://github.com/alife-data-standards/alife-data-tools/issues)
are welcome!).

### Converters

Data conversion tools translate data files from non-standard file formats to a
standards-compliant file format and vice versa. Data conversion tools can be found
in the [converters](./converters/) directory.

Within the converters directory, for each system that we have a conversion script/program
for, there is a directory associated with that particular system. Each system-specific
directory should contain a readme that gives a high-level description (at least
a sentence or two; e.g., system X does digital evolution) of the system and, if
possible, references to a publication that describes the system. Please create an
[issue](https://github.com/alife-data-standards/alife-data-tools/issues) for
inadequate readmes!

Conversion tools should follow the following naming scheme: `[standard data type]_[system]2std`
or `[standard data type]_std2[system]` (e.g., `genome_mabe2std.py`, `phylogeny_avida2std.py`).
Again, in the future we may find this naming scheme to be inadequate; [suggestions](https://github.com/alife-data-standards/alife-data-tools/issues)
for changes are welcome!

## Other tools

### Web apps

Tools in this category cannot be housed in this repository because they are set up as web applications. However, they have been tested on the latest version of the standards and found to work. If you run into issues using a web app with standard-compliant data (e.g.,
the tool is down or out of data), file an [issue](https://github.com/alife-data-standards/alife-data-tools/issues).

- [**Phylogeny visualizer**](https://emilydolson.github.io/lineage_viz_tool/standards_viz.html)
  - Description: Upload a standards-compliant phylogeny file and this website will draw a tree based on it. If you have additional fields in your data, you can color the nodes based on them.

### Third-party tools

This section contains links to tools that the standards maintainers have not yet vetted.
