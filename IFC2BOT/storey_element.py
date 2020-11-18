from IFC2BOT.util import build_URI
from IFC2BOT.util import get_rel

def storey_element_rels(ifc_file):
    triples = "\n# STOREY/ELEMENT\n"
    building_storey_dict = _get_storey_element_rels(ifc_file)
    for building in building_storey_dict.keys():
        for storey in building_storey_dict.get(building):
            triples+= "%s bot:hasElement %s .\n" % (build_URI(building), build_URI(storey))
    return triples

# Private
def _get_storey_element_rels(ifc_file):
    return get_rel(ifc_file, 'IfcRelContainedInSpatialStructure', 'RelatingStructure', 'RelatedElements')