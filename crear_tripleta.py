from rdflib import URIRef, BNode, Literal, Namespace, RDF, Graph
from rdflib.namespace import RDF, FOAF

g = Graph() #permite almacenar las definiciones y hechos q representan un dominio

#defino un espacio de nombres y creo nodos en ese espacio
mm = Namespace("http://localhost/mediawiki/index.php/persona")
jorge=mm.jorge
david=mm.david
    
#añado tripletas
g.add( (jorge, RDF.type, FOAF.persona) )
g.add( (david, RDF.type, FOAF.persona) )
g.add( (jorge, FOAF.name, Literal("Jorge")) )
g.add( (david, FOAF.name, Literal("David")) )
g.add( (david, FOAF.knows, jorge ) )
g.add( (jorge, FOAF.knows, david ) )
g.add( (david, FOAF.age, Literal("veinte")) )
g.add( (jorge, FOAF.age, Literal("23")) )
#g.serialize("test.rdf") #guardo el archivo en formato xml/rdf

#guardar el archivo en formato de tripleta
g.serialize("test1.nt", format='nt')


# pasar de formato nt a xml usando rdf2smw
# ./rdf2smw_v0.5_linux64 --in rdflib/test1.nt --out rdflib/test1.xml


#consultas sobre el grafo

#retorna los valores relacionados con maria

for  p, o in g[jorge]:
    print (p , o)
    
if (jorge, RDF.type, FOAF.persons):
    print("jorge es persona")
    
    


