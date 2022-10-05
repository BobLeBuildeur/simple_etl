# Simple ETL

A quick domain specific language for ETL transformations

Uses Pandas on the background for a very powerful suite of extractors, transformations and loaders.

QT-based interface to simplify life a bit.


## For user interface

`python3 ./etl.py`


## For cli

`python3 ./cli.py your_file_with_commands.txt`


# Language

Base usage:

```
extract {adapter} from {source}

transform {source} by {transformer} {[params]}

load {source} as {adapter} into {output}
```

There can be one or more extractors, transformers and loaders.

**Example**

```
extract csv from input.csv
extract excel from definitions.xslx

transform input.csv by matching definitions.xslx by color
transform input.csv by formatting active with checkbox

load input.csv as excel into output.xlsx
```

> Note: sources path's are relative

## Extraction adapters

**csv**

Extracts csv into source

`extract csv from {source}`


**excel**

Extracts excel into source

`extract excel from {source}`


## Transfomers

**Dropping**

Removes columns from source

`transform {source} by dropping {column, [column..]}`


**Filtering**

Removes rows based on comparison

`transform {source} by filtering {label} {comparison} {value}`

Can compare through:

- `=` - Equals to
- `!=` - Not equals to 
- `>` - Greater than 
- `>=` - Greater than or equal to 
- `<` - Lesser than 
- `<=` - Lesser than or equal to 


**Formatting**

Formats cells values for given column

`transform {source} by formatting {column} with {formatter} {[args]}`

Formatters:

- `checkbox` - Normalizes common boolean values (yes, no, y, x, TRUE, FALSE) 
- `trim` - Removes characters from begging or end of text. Args: beggining, end
- `slice` - Gets text from middle of text. Args: from, to
- `upper` - Changes text to uppercase
- `lower` - Changes text to lowercase


**Matching**

Joins sources A and B into A, matching values and copying other columns. 

`transform {sourceA} by matching {sourceB} by {column}`


**Renaming**

Renames a column

`transform {source} by renaming {column} to {name}`


## Loader adapters

**csv**

Saves source into file, formatted as CSV

`load {source} as csv into {file}`


**excel**

Saves source into file, formatted as Excel

File needs to have `xslx` extension, otherwise error is thrown

`load {source} as excel into {file}.xlsx`

# Building

**For your target system**

For your target system, simply run pyinstaller pointing to the specfile

`pyinstaller etl.spec`

**Linux and Windows**

> This is broken! Somehow it only works half the time...

You can build binaries for Windows and Linux distributions using pyinstaller

It runs on a virtual machine (using Wine to target Windows).

With docker installed, simply run the build shell script.

`./build.sh`