from xml.etree.ElementTree import Element, ElementTree

root = Element("Acordeon")
todeschini = Element("Todeschini")
scandalli = Element("Scandalli", cor="preta", modelo="120 Baixos")
maestrina = Element("Maestrina")

root.append(todeschini)
root.append(scandalli)
root.append(maestrina)

ElementTree(root).write("xml_manipulando/xml/acordeon.xml")
