protocolo = input("¿QUÉ PROTOCOLO OCUPAREMOS? ")
if protocolo == "OSPF":
    print("DISTANCIA ADMINISTRATIVA DE 110")
elif protocolo == "RIP":
    print("DISTANCIA ADMINISTRATIVA DE 120")
elif protocolo == "EIGRP":
    print("DISTANCIA ADMINISTRATIVA DE 90")
elif protocolo == "BGP":
    print("DISTANCIA ADMINISTRATIVA DE 20")
else:
    print("Protocolo no reconocido o no se encuentra en la lista.")