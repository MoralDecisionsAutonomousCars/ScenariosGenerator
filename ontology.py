from owlready2 import *

print(Thing)

onto =  get_ontology("/mnt/c/Users/msavchen/Documents/NOjob/PP/ontology/pizza_rdf.owl").load()
print("HUJ2:", onto.Pizza)
onto_cl = list(onto.classes())
for cl in onto_cl:
    print(cl)
#print(onto.search(subclass_of = onto.Pizza))

print("HUJ:", onto["American"])
print("HUJ2:", onto.Pizza)
print(type(onto.ontology))
print(dir(onto))



print(list(onto.object_properties()))
print(onto["cliff.edge"])
print(onto.search(iri = "*izza"))
print(IRIS[("/mnt/c/Users/msavchen/Documents/NOjob/PP/ontology/pizza.owl#Pizza")])