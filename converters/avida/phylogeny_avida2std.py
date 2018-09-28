"""
avida_to_standard_phylogeny.py

This script converts an avida .spop file into ALife standard-compliant phylogeny
file.

Currently outputs in format assumed by pandas.

Currently outputs each entry in output file in order they were read in from Avida
file.

Currently assumes Avida defaults in .spop fields.

"""

import argparse, os, copy
import pandas as pd

valid_out_formats = ["csv", "json"]

avida_set_fields = ["parents", "cells", "gest_offset", "lineage"]
avida_set_delim = ","

def main():
    # Setup command line arguments.
    parser = argparse.ArgumentParser(description="Avida .spop to ALife standard-compliant phylogeny converter.")
    parser.add_argument("input", type=str, help="Input avida .spop file.")
    parser.add_argument("-output", "-out", type=str, help="Name to assign to standard-compliant output file.")
    parser.add_argument("-format", type=str, default="csv", help="What standard file format should this script output? Valid options: 'JSON', 'CSV'")
    parser.add_argument("-minimal", action="store_true", help="Store minimal data in output file.")

    # Parse command line arguments.
    args = parser.parse_args()

    # Extract/validate arguments
    in_fp = args.input
    if (not os.path.isfile(in_fp)):
        exit("Failed to find provided input file ({})".format(in_fp))
    
    out_format = args.format.lower()
    if (not out_format in valid_out_formats):
        exit("Invalid output format provided ({}). Valid arguments include: {}".format(out_format, valid_out_formats))
    
    out_fp = args.output if (args.output != None) else args.input.replace(".spop", "_standard-phylogeny.{}".format(out_format))

    minimal_out = args.minimal

    # Open and parse input file into pandas data frame.
    # - Read in file, store as dict, use dict to make pandas dataframe object.
    with open(in_fp, "r") as fp:
        # Extract header information.
        header = None
        for line in fp:
            if line[:7] == "#format": 
                header = line.replace("#format", "").strip().split(" ")
                break
        if header == None:
            exit("Failed to find file format information in {}".format(in_fp))
        
        # Collect data from Avida file in format that will be easy to convert to
        # pandas dataframe object.
        avida_data = {field:[] for field in header}
        for line in fp:
            line = line.strip()
            # Consume all comment lines and blank lines.
            if line == "" or line[0] == "#": continue
            # If we're here, we're looking at data.
            # Note, Avida's output is pretty disgusting. We can't assume that all
            # trailing fields will exist on a line. :barf:
            line = line.split(" ")
            for i in range(0, len(header)):
                # If we don't have the value for a field, set to 'NONE'
                value = line[i] if i < len(line) else "NONE"
                # If the field is known to be a set, split on ','
                if header[i] in avida_set_fields: value = value.split(avida_set_delim)
                # Go ahead and add the value to the appropriate field.
                avida_data[header[i]].append(value)

    # Clean up avida data to play with standard.
    avida_data["ancestor_list"] = [list(map(int, [-1 if anc == "(none)" else anc for anc in anc_lst])) for anc_lst in avida_data.pop("parents")]
    avida_data["origin_time"] = copy.deepcopy(avida_data["update_born"])
    avida_data["id"] = list(map(int, avida_data["id"]))
           
    # Convert Avida data into pandas data frame.
    df = pd.DataFrame(data = avida_data)
    
    # Drop any fields we want to delete.
    del_fields = []
    if minimal_out:
        # What fields should we delete (if we're doing minimal output)?
        min_fields = ["id", "ancestor_list", "origin_time"]
        del_fields = [field for field in avida_data if not field in min_fields]
        df.drop(del_fields, axis=1, inplace=True)
    
    # Adjust the header so that standard fields are up front.
    stds_hd = ["id", "ancestor_list", "origin_time"]
    new_header = stds_hd + [field for field in avida_data if (not field in stds_hd) and (not field in del_fields)]
    # Write output in requested format.
    if (out_format == "csv"):
        with open(out_fp, "w"):
            df.to_csv(out_fp, sep=",", columns=new_header, index=False, index_label=False)
    elif (out_format == "json"):
        with open(out_fp, "w"):
            df.to_json(out_fp, orient="index")

if __name__ == "__main__":
    main()