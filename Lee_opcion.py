def lee_opcion():
    while True:
        opcion = input( "Ingrese A (altas) - B (bajas) - M (Modificaciones): ").upper()
        if opcion in ["A", "B", "C"]:
	    return opcion