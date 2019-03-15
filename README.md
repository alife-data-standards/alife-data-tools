
# Software Resources for the Artificial Life Data Standards

**Navigation**

<!-- TOC -->

- [Overview](#overview)
- [Software Resource List](#software-resource-list)
  - [Developer Utilities/Libraries](#developer-utilitieslibraries)
    - [Python](#python)
  - [Data Converters](#data-converters)
  - [End-user Tools](#end-user-tools)
    - [Data processing](#data-processing)
    - [Visualizers](#visualizers)

<!-- /TOC -->

## Overview

This repository is a curated list of software resources related to the [ALife community data standards](https://alife-data-standards.github.io/alife-data-standards/).
We've modeled this repository after other GitHub-hosted resource curation efforts (e.g., [awesome lists](https://github.com/sindresorhus/awesome)).

We advocate the use of a number of software development best practices, including continuous integration testing, code coverage tracking, and static analysis. A general guide to our approach can be found [here](./good-practices.md).

## Software Resource List

### Developer Utilities/Libraries

Development utilities are provided for those who wish to create new tools that take
advantage of the ALife data standards. These utilities provide functionality such
as loading/saving standard-compliant data using various file formats, callable metric
and verification functions, _et cetera_.

#### Python

- [ALife Standards Development Package](https://github.com/alife-data-standards/alife-std-dev-python)
  - Currently has a variety of utility functions for working with phylogenies.

### Data Converters

Data converters translate data files from non-standard file formats to a
standards-compliant file format and vice versa.
Each converter should contain a readme that gives a high-level description (at least
a sentence or two) of the system (_e.g._, system X does digital evolution) and, if
possible, references to a publication that describes the system. Please create an
[issue](https://github.com/alife-data-standards/alife-data-tools/issues) for
inadequate readmes!

- [Avida to standards converters](https://github.com/alife-data-standards/converters-avida)
- [Modular Agent-based Evolver (MABE) to standards converters](https://github.com/alife-data-standards/converters-mabe)
- [Phylogeny standard to Visual Inspector for NeuroEvolution (VINE)](https://github.com/alife-data-standards/converters-vine)

### End-user Tools

#### Data processing

- [alife-data-standards general phylogeny tools pack](https://github.com/alife-data-standards/tools-pack-phylogeny)
  - This repository contains a set of commandline tools for analyzing phylogenies.

#### Visualizers

- [phylogeny visualizer](https://emilydolson.github.io/lineage_viz_tool/standards_viz.html)
  - Upload a standards-compliant csv formatted phylogeny file and this website will
    draw a tree based on it. If you have additional fields in your data, you can
    color the nodes based on them.
