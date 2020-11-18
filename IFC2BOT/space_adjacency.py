from IFC2BOT.util import build_URI

# NB! This is only possible if the IFC file contains space boundaries

def space_element_rels(ifc_file):
    triples = "\n# SPACE/ELEMENT ADJACENCY\n"
    space_element_dict = _get_space_adjacent_elements(ifc_file)
    if not ifc_file.by_type("IfcRelSpaceBoundary"):
        triples+= "\n# IFC DIDN'T CONTAIN SPACE BOUNDARIES - NOT POSSIBLE TO DEDUCE SPACE/ELEMENT ADJACENCY\n"
    else:
        spaces = space_element_dict.keys()
        for space in spaces:
            for el in space_element_dict[space]:
                triples+= "%s bot:adjacentElement %s .\n" % (build_URI(space), build_URI(el))
    return triples

# private
def _get_space_adjacent_elements(ifc_file):
    space_el_dict = {}
    for b in ifc_file.by_type("IfcRelSpaceBoundary"):
        space = b.RelatingSpace
        element = b.RelatedBuildingElement
        if element:
            if not space.GlobalId in space_el_dict.keys():
                space_el_dict[space.GlobalId] = [element.GlobalId]
            else:
                space_el_dict[space.GlobalId].append(element.GlobalId)
    
    return space_el_dict