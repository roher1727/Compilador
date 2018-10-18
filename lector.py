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
                    subrutinas.append(t[0].lower())
            except(IndexError):
                pass
    return subrutinas


def adquirir_constantes(texto):
    constantes = []
    for t in texto:
        t.append(' ')
        if t[1].lower() == 'equ':
            constantes.append(t[0].lower())

    return constantes


def error_identacion(texto, subrutinas, constantes):
    cont = 0
    for t in texto:
        cont += 1
        t.append(' ')
        if t[0] != '' and t[0][0] != '*':
            if (t[0].lower() not in constantes):
                if t[0].lower() not in subrutinas:
                    print('{} Error en linea {}'.format(t[0], cont))


def checar_mnemonico(fila, mnemonicos, directivas):
    for m in mnemonicos:
        if fila[1].lower() == m or fila[1].lower() in directivas:
            return True
    return False


def checar_subrutinas(fila, subrutinas, constantes):
    for s in subrutinas:
        if fila[2].lower() == s or fila[2].lower() in constantes or fila[2].lower() == ' ':
            return True
    return False


def checar_constantes(fila, subrutinas, constantes):
    for c in constantes:
        if fila[2].lower() == c or fila[2].lower() in subrutinas or fila[2].lower() == ' ':
            return True
    return False


def mnemonico_inexistente(texto, mnemonicos, directivas):
    conta = 0
    for t in texto:
        conta += 1
        t.append(' ')
        if t[0] == '' and t[1] != ' ':
            if not checar_mnemonico(t, mnemonicos, directivas):
                print('Error en linea {} mnemonico inexistente {}'.format(conta, t))


def etiqueta_inexistente(texto, subrutinas, constantes):
    conta = 0
    for t in texto:
        conta += 1
        if t[0] == '' and t[1] != ' ':
            if t[2][0] != '$':
                if t[2][0] != '#':
                    if not checar_subrutinas(t, subrutinas, constantes):
                        print('Error en linea {} etiqueta inexistente {}'.format(conta, t))


def constante_inexistente(texto, subrutinas , constantes):
    conta = 0
    for t in texto:
        conta += 1
        if t[0] == '' and t[1] != ' ':
            if t[2][0] != '$':
                if t[2][0] != '#':
                    if not checar_constantes(t, subrutinas, constantes):
                        print('Error en linea {} constante inexistente {}'.format(conta, t))


def variable_inexistente():
    pass


def instruccion_c_operando():
    pass


def instruccion_n_operando():
    pass


def no_tiene_end(texto):
    for t in texto:
        for m in t:
            if m.lower() == 'end':
                print(' si tiene equisde')
                return True


if __name__ == '__main__':
    compa = compilador()
    texto_crudo = adquirir_texto()
    texto_proc = procesar_texto(texto_crudo)
    subrutinas = adquirir_subrutinas(texto_proc)
    constantes = adquirir_constantes(texto_proc)
    error_identacion(texto_proc, subrutinas, constantes)
    mnemonico_inexistente(texto_proc, compa.get_mnenomicos(), compa.get_directivas())
    etiqueta_inexistente(texto_proc, subrutinas, constantes)
    constante_inexistente(texto_proc, subrutinas, constantes)
    no_tiene_end(texto_proc)
