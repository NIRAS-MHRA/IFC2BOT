## IFC2BOT
Requires ifcopenshell

This is a simple Python 3.8 based CLI tool that extracts [BOT](https://w3id.org/bot#) triples from an IFC file using [ifcopenshell](http://ifcopenshell.org/python).

URLs are formulated simply as a concatenation of the provided namespace and a URL-encoded IFC GlobalId. For example: `https://niras.dk/projects/1234/0BTBFw6f90Nfh9rP1dlXr%24`

## Run
`python main.py -i my-file.ifc -o my-file.ttl -ns https://niras.dk/projects/1234/`

## Acknowledgements
The tool has been developed and made publicly available by [NIRAS](https://niras.com). It is our hope that it will benefit the construction industry as a whole by by taking us one step further towards a web-mediated BIM. Please contribute by forking this repository and sharing your improvements.