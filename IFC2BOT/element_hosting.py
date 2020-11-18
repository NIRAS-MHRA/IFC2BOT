from IFC2BOT.util import build_URI
from IFC2BOT.util import get_rel

def wall_element_rels(ifc_file):
    triples = "\n# ELEMENT/ELEMENT HOSTING\n"
    sub_element_dict = _get_sub_elements(ifc_file)
    for element in sub_element_dict.keys():
        for hel in sub_element_dict.get(element):
            triples+= "%s bot:hasSubElement %s .\n" % (build_URI(element), build_URI(hel))
    return triples

# private
def _get_sub_elements(ifc_file):
    el_el_dict = {}
    for b in ifc_file.by_type("IfcRelVoidsElement"):
        parent = b.RelatingBuildingElement
        child = b.RelatedOpeningElement
        if child:
            if not parent.GlobalId in el_el_dict.keys():
                el_el_dict[parent.GlobalId] = [child.GlobalId]
            else:
                el_el_dict[parent.GlobalId].append(child.GlobalId)
    return el_el_dict