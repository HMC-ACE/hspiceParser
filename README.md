# hspiceParser

Welcome to the hspiceParser GitHub page. hspiceParser aims to be the final word in parsing hSpice output files, building on a long legacy of programs built by other circuit designers.

The main goals of hspiceParser are:

1. **Very simple installation** - Easy to set up and use
2. **Support for a wide variety of output formats** - Compatible with multiple hSpice formats
3. **Thorough documentation** - Clear explanations of what the parser is doing

If you've ever Googled "hSpice output format" and been frustrated at the result, then we're hoping this project helps.

## Installation

### Using pixi package manager

Run the following command in your terminal:

```bash
pixi add hspice_parser --git https://github.com/HMC-ACE/hspiceParser --branch main

pixi add hspice_parser --git https://github.com/HMC-ACE/hspiceParser --tag latest
```

### Using pip
You can also install hspiceParser using pip:

```bash
pip install git+https://github.com/HMC-ACE/hspiceParser.git@main
```

### Quick Download

You can download hspiceParser directly from [here](https://github.com/HMC-ACE/hspiceParser/blob/main/src/hspice_parser/hspiceParser.py), or run the following terminal command:

```bash
wget https://raw.githubusercontent.com/HMC-ACE/hspiceParser/main/src/hspice_parser/hspiceParser.py
```

### Requirements

The instruction above enable most of hSpiceParser’s functionality, but some output formats require additional Python libraries.  The Parser file only relies on built-in Python 3.4+ functions to produce .m, .csv and Pickle files. The parser can also produce Matlab .mat files, but it requires that you have Scipy and Numpy installed on your machine to do so.

## Documentation

- **Usage Guide**: See [Usage.md](Usage.md) for examples and detailed usage instructions
- **Output Formats**: See [hSpice_output.md](hSpice_output.md) for documentation on supported hSpice output file formats (9601, 2001, and ASCII)

## Contributing

We hope you download and use this parser, and we are also eager to integrate features from the community. Send us some pull requests!
