from IFC2BOT.util import build_URI

def classify_buildings(ifc_file):
    triples = "\n# BUILDINGS\n"
    for item in ifc_file.by_type('IfcBuilding'):
        triples+= "%s a bot:Building .\n" % (build_URI(item.GlobalId))
    return triples

def classify_storeys(ifc_file):
    triples = "\n# STOREYS\n"
    for item in ifc_file.by_type('IfcBuildingStorey'):
        triples+= "%s a bot:Storey .\n" % (build_URI(item.GlobalId))
    return triples

def classify_spaces(ifc_file):
    triples = "\n# SPACES\n"
    for item in ifc_file.by_type('IfcSpace'):
        triples+= "%s a bot:Space .\n" % (build_URI(item.GlobalId))
    return triples

def classify_elements(ifc_file):
    triples = "\n# ELEMENTS\n"
    for item in ifc_file.by_type('IfcElement'):
        triples+= "%s a bot:Element .\n" % (build_URI(item.GlobalId))
    return triples