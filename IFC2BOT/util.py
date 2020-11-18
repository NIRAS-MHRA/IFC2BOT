from urllib.parse import quote

def build_URI(gid):
    gid = quote(gid)
    return "inst:%s" % (gid)

# rel_type is the type of relationship. Ex: IfcRelAggregates
# subject_ref is the relationship to the subject resource. Ex: RelatingObject
# target_ref is the relationship to the target resource. Ex: RelatedObjects
# subject_type is the class of the subject resource. Ex:IfcBuildingStorey
# target_type is the class of the target resource. Ex:IfcSpace
def get_rel(ifc_file, rel_type, subject_ref, target_ref, subject_type=None, target_type=None):

    obj_dict = {}

    # Get all rel aggregates relationships that is going out from the relatingObjectType
    if subject_type:
        rels = list(filter(lambda x: getattr(x, subject_ref).is_a(subject_type), ifc_file.by_type(rel_type)))
    else:
        rels = ifc_file.by_type(rel_type)
    
    for rel in rels:
        # Get all outgoing relationships that match the relatedObjectType
        if target_type:
            outgoing = list(filter(lambda x: x.is_a(target_type), getattr(rel, target_ref)))
        else:
            outgoing = getattr(rel, target_ref)

        # Get GlobalId
        if outgoing[0].GlobalId:
            outgoing = list(map(lambda x: x.GlobalId, outgoing))
        # Add to dictionary
        obj_dict[getattr(rel, subject_ref).GlobalId] = outgoing

    return obj_dict