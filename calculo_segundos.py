def calc_asegundos (horas, minutos, segundos):
    """ Transforma en segundos una medida de tiempo expresada en horas, minutos y segundos """
    segsal = 3600 * horas + 60 * minutos + segundos # regla de transformacion
    return segsal