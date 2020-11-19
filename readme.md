## IFC2BOT
Requires ifcopenshell

This is a simple Python 3.8 based CLI tool that extracts [BOT](https://w3id.org/bot#) triples from an IFC file using [ifcopenshell](http://ifcopenshell.org/python).

URLs are formulated simply as a concatenation of the provided namespace and a URL-encoded IFC GlobalId. For example: `https://niras.dk/projects/1234/0BTBFw6f90Nfh9rP1dlXr%24`

This parser only converts BOT classification and relationships. This includes:
```turtle
# CLASSIFICATION
<building> a bot:Building .
<storey> a bot:Storey .
<space> a bot:Space .
<element> a bot:Element .

# RELATINSHIPS
<building> bot:hasStorey <storey> .
<storey> bot:hasSpace <space> .
<storey> bot:hasElement <element> .
<space> bot:containsElement <element> .
<space> bot:adjacentElement <element> .
<wall> bot:hasSubElement <window> .
<wall> bot:hasSubElement <door> .
```

## Install
* Install Python 3.8
* Download [ifcopenshell](http://ifcopenshell.org/python) and unzip in this dir
* You are good to go!

## Run
`python main.py -i my-file.ifc -o my-file.ttl -ns https://niras.dk/projects/1234/`

## Limitations
Deriving adjacency between spaces and adjacent elements requires that the IFC is exported with space boundaries.

## Performance
The current version of the exporter has the following conversion times when executed on a Lenovo P50 laptop with Intel Core i7-6820HQ 2.70 GHz CPU and 32 GB 2133 MHz DDR ram:

| Model                     | IFC size | BOT size | Triple count | Conversion time |
|---------------------------|----------|:--------:|--------------|-----------------|
| Duplex with L1 boundaries | 1.37 MB  |   56 KB  | 823          | 0.28s           |
| Water park                | 112 MB   |  745 KB  | 12,676       | 15.4s           |
| Large office building (AP) | 163 MB  |  2.93 MB | 44,421       | 17.4s           |


## Acknowledgements
The tool has been developed and made publicly available by [NIRAS](https://niras.com). It is our hope that it will benefit the construction industry as a whole by by taking us one step further towards a web-mediated BIM. Please contribute by forking this repository and sharing your improvements.