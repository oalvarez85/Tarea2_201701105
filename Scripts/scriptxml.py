from xml.dom import minidom

def leerXml():
    doc = minidom.parse("./Data/data.xml")
    nombre = doc.getElementsByTagName("producto")[0]
    print("** Se obtuvo una estructura XML del archivo data.xml **")
    print("")
    tienda = doc.getElementsByTagName("producto")
    for producto in tienda:
        nid = producto.getAttribute("id")
        nombre = producto.getElementsByTagName("nombre")[0]
        precio = producto.getElementsByTagName("precio")[0]
        exitencia = producto.getElementsByTagName("existencia")[0]
        descuento = producto.getElementsByTagName("descuento")[0]
        print("Nombre: %s " % nombre.firstChild.data)    
        print("Precio: Q.%s" % precio.firstChild.data)
        print("Existencias: %s" % exitencia.firstChild.data)
        print("Descuento: %s" % descuento.firstChild.data)
        print('')
    print("**La estructura utilizada es:")    
    print(type(tienda))