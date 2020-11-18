import ifcopenshell
import argparse
from urllib.parse import quote
import IFC2BOT.classify
import IFC2BOT.zone_containment
import IFC2BOT.storey_element
import IFC2BOT.space_containment
import IFC2BOT.space_adjacency
import IFC2BOT.element_hosting
import os
import time
import multiprocessing as mp

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'Duplex_A_2019_L1.ifc')
output_file = os.path.join(dir_path, 'test.ttl')

def build_bot_triples(namespace):

    start_time = time.time()

    # Read arguments
    input_file_path = args.input_file
    output_file_path = args.output_file
    namespace = args.namespace

    # Read IFC file
    ifc_file = ifcopenshell.open(input_file_path)

    # Init log file
    wipe_file(output_file_path)
    log_file = open(output_file_path, "a")

    triples = "@prefix bot: <https://w3id.org/bot#> .\n"
    triples+= "@prefix inst: <%s> .\n" % namespace

    triples+= "\n##################\n"
    triples+= "# CLASSIFICATION #\n"
    triples+= "##################\n"

    triples+= IFC2BOT.classify.classify_buildings(ifc_file)
    triples+= IFC2BOT.classify.classify_storeys(ifc_file)
    triples+= IFC2BOT.classify.classify_spaces(ifc_file)
    triples+= IFC2BOT.classify.classify_elements(ifc_file)

    triples+= "\n#################\n"
    triples+= "# RELATIONSHIPS #\n"
    triples+= "#################\n"

    triples+= IFC2BOT.zone_containment.building_storey_rels(ifc_file)
    triples+= IFC2BOT.zone_containment.storey_space_rels(ifc_file)
    triples+= IFC2BOT.storey_element.storey_element_rels(ifc_file)
    triples+= IFC2BOT.space_containment.space_element_rels(ifc_file)
    triples+= IFC2BOT.space_adjacency.space_element_rels(ifc_file)
    triples+= IFC2BOT.element_hosting.wall_element_rels(ifc_file)

    log_file.write(triples)
    log_file.close()

    print("--- %s seconds ---" % (time.time() - start_time))

def wipe_file(fp):
    open(fp, 'w').close()

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input_file',
        help='Path to the input file',
        required=True
    )

    parser.add_argument('-o', '--output_file', 
        default='triples.ttl',
        help='Path to the output file'
    )

    parser.add_argument('-ns', '--namespace', 
        default='https://ex.com/',
        help='The namespace in which the triples should be described'
    )

    return parser.parse_args()

# main
args = get_arguments()
triples = build_bot_triples(args)