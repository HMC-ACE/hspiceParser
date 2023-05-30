# Usage

`hSpiceParser <filename> <output format>`
* Converts an hSpice output file in 9601, 2001 or ASCII format specified by <filename> to an output format specified by <output format>.

# Overview

The hspiceParser is made to convert hSpice DC, AC and transient simulation output files (*.swX, *.acX, *.trX) to file types that are readable by common mathematical software. It is capable of reading the 9601 and 2001 binary formats, the ASCII file format, and the measure file format. The parser can generate CSV files, matlab files containing ASCII strings in arrays, which are given the suffix “.m”, and Python Pickle files. Downloading Scipy and Numpy allows it to produce Matlab binary files in 
the .mat format.

hSpice simulations report arrays of values of electrical variables that correspond to an independent variable specified by the simulation command (.dc, .ac or .tr).  It is possible to write simulation commands that repeat the simulation with slight variations, referred to as an inner sweep, and the repeated copies of the electrical variables that result are called sweeps. It is also possible to repeat the simulation command using a different syntax called an ‘alter’.  Each alteration created by an alter will produce a separate output file: eg: a transient simulation might produce a tr0 file on its first alter and a tr1 file on its second alter. Details of these commands can be found in the hSpice command reference.

If there are multiple sweeps in the input file and the CSV option is selected, the parser will create a folder of CSV files named according to the value of the swept variable. The use of both the “.m” and pickle option will result in a single file that contains all of the sweeps. The pickle option saves a python dictionary with the variable names from the hSpice file as the keys, and the corresponding values for each variable stored in a two dimensional list with the first dimension corresponding to the sweep index and the second corresponding to the values of the variable throughout the simulation. The “.m” and “.mat” is organized in the same way as the pickle output but in the appropriate object

# Installation

The parser is a single python file that is run from the terminal. To use it you must have Python 3.5+ which does require installation from [here](https://www.python.org/downloads/). Download the file here [raw link] or navigate to the appropriate directory on your computer and do the following:

`wget https://github.com/HMC-ACE/hspiceParser/blob/main/hspiceParser.py`

This download enables most of hSpiceParser’s functionality, but some output formats require additional Python libraries.  The Parser file only relies on built-in Python 3.4+ functions to produce .m, .csv and Pickle files. The parser can also produce Matlab .mat files, but it requires that you have Scipy and Numpy installed on your machine to do so.

# Usage Examples

To use the parser do:

`python hSpice_parser.py <hspice file path> <parser output format>`

For example if the file is in the same directory as the parser, named test.tr0, and I want the CSV option. Then I would do:

`python hSpice_parser.py test.tr0 csv`

This will produce a file named `test_tr0.csv` in the same directory as the `test.tr0` file. If test.tr0 has sweeps in it, then a folder called `test_tr0_csv` containing a csv for each sweep will appear in the same directory as `test.tr0`.

For help do:

`python hSpice_parser.py -h` or `python hSpice_parser.py --help`

The hSpiceParser function can be imported into your own Python scripts. If there were multiple hSpice files in a folder that you wanted to parse all at once, you could use the script below:

```python
from os import path, listdir
from hspiceParser import import_export

directory = 'path/to/files'  # this code assumes that this directory only contains compatible files.
output_ext = 'pickle'

for filename in listdir(directory):
    full_path = path.join(directory, filename)
    _, ext = path.splitext(full_path)
    if ext[:2] in ['tr', 'sw', 'ac']: 
        import_export(full_path, output_ext)
```
