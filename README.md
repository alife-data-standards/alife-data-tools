
This is a repository which will contain tools designed to work with the
alife-data-standards.

The tools here fall broadly into two categories, converters and everything else.
The tools Tools folder contains tools which work with files in the standards
format. These tools may be analysis, visualization or helper tools. At the moment,
the tools directory contains a folder for each tool that has the code for that tool
and a readme. We may eventually find that the flat layout becomes unwieldy
 we will change 

Within the converters folder, there is a folder for each system
(i.e. mabe, avida, aevol...). Conversion tools are named 
`[standard]_[system]2std` or `standard_std2[system]` (i.e. `genome_mabe2std.py`).
