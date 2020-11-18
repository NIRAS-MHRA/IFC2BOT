from IFC2BOT.util import build_URI
from IFC2BOT.util import get_rel

def space_element_rels(ifc_file):
    triples = "\n# SPACE/ELEMENT CONTAINMENT\n"
    space_element_dict = _get_space_contained_elements(ifc_file, "IfcSpace", "IfcElement")
    for space in space_element_dict.keys():
        for element in space_element_dict.get(space):
            triples+= "%s bot:containsElement %s .\n" % (build_URI(space), build_URI(element))
    return triples

# private
def _get_space_contained_elements(ifc_file, spatial_structure_type, related_element_type):
    return get_rel(ifc_file, "IfcRelContainedInSpatialStructure", "RelatingStructure", "RelatedElements", spatial_structure_type, related_element_type)