from IFC2BOT.util import build_URI
from IFC2BOT.util import get_rel

def building_storey_rels(ifc_file):
    triples = "\n# BUILDING/STOREY\n"
    building_storey_dict = _get_rel_aggregates(ifc_file, "IfcBuilding", "IfcBuildingStorey")
    for building in building_storey_dict.keys():
        for storey in building_storey_dict.get(building):
            triples+= "%s bot:hasStorey %s .\n" % (build_URI(building), build_URI(storey))
    return triples

def storey_space_rels(ifc_file):
    triples = "\n# STOREY/SPACE\n"
    storey_building_dict = _get_rel_aggregates(ifc_file, "IfcBuildingStorey", "IfcSpace")
    for building in storey_building_dict.keys():
        for storey in storey_building_dict.get(building):
            triples+= "%s bot:hasSpace %s .\n" % (build_URI(building), build_URI(storey))
    return triples

# PRIVATE
def _get_rel_aggregates(ifc_file, relating_object_type, related_object_type):
    return get_rel(ifc_file, "IfcRelAggregates", "RelatingObject", "RelatedObjects", relating_object_type, related_object_type)