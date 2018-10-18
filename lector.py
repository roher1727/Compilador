from compilador import compilador


def adquirir_texto():
    texto = []

    with open('MONITOs.ASC', 'r') as archivo:
        for fila in archivo:
            texto.append("A"+fila)
    return texto


def procesar_texto(texto):

    text = []

    for t in texto:
        t = t.split()
        tmp = list(t[0])
        tmp[0] = " "
        t[0] = "".join(tmp)[1:]
        text.append(t)
        # print(t)

    return text


def adquirir_subrutinas(texto):
    compal = compilador()
    subrutinas = []
    for t in texto:
        t.append(' ')
        if t[0] != '' and t[0][0] != '*' and t[0].lower() not in compal.mnemonicos and t[0].lower() not in compal.directivas:
            try:
                if t[1].lower() != 'equ':
                    subrutinas.append(t[0])
            except(IndexError):
                pass
    return subrutinas


def adquirir_constantes(texto):
    constantes = []
    for t in texto:
        t.append(' ')
        if t[1].lower() == 'equ':
            constantes.append(t[0])

    return constantes


def error_identacion(texto, subrutinas, constantes):
    cont = 0
    for t in texto:
        cont += 1
        t.append(' ')
        if t[0] != '' and t[0][0] != '*':
            if (t[0] not in constantes):
                if t[0] not in subrutinas:
                    print('{} Error en linea {}'.format(t[0], cont))


if __name__ == '__main__':
    compa = compilador()
    texto_crudo = adquirir_texto()
    texto_proc = procesar_texto(texto_crudo)
    subrutinas = adquirir_subrutinas(texto_proc)
    constantes = adquirir_constantes(texto_proc)

    error_identacion(texto_proc, subrutinas, constantes)
    print(subrutinas)
