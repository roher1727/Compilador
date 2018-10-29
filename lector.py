from compilador import compilador


class lector:

    def __init__(self):
        pass

    def adquirir_texto(self):
        texto = []

        with open('MONITOs.ASC', 'r') as archivo:
            for fila in archivo:
                texto.append("A"+fila)
        return texto

    def procesar_texto(self, texto):

        text = []

        for t in texto:
            t = t.split()
            tmp = list(t[0])
            tmp[0] = " "
            t[0] = "".join(tmp)[1:]
            text.append(t)
            # print(t)

        return text

    def adquirir_subrutinas(self, texto):
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

    def adquirir_subrutinas_numero(self, texto):
        compal = compilador()
        subrutinas = []
        numero = 0
        for t in texto:
            numero += 1
            t.append(' ')
            if t[0] != '' and t[0][0] != '*' and t[0].lower() not in compal.mnemonicos and t[0].lower() not in compal.directivas:
                try:
                    if t[1].lower() != 'equ':
                        subrutinas.append([t[0].lower(),numero])
                except(IndexError):
                    pass
        return subrutinas

    def adquirir_constantes(self, texto):
        constantes = []
        for t in texto:
            t.append(' ')
            if t[1].lower() == 'equ':
                constantes.append(t[0].lower())

        return constantes

    def instrucciones_operando(self, texto):
        inst_operando = []
        for t in texto:
            t.append(' ')
            if '*' not in t[0]:
                if (t[1] != ' '):
                    if(t[0] == ''):
                        inst_operando.append([t[1], t[2]])
        return inst_operando

    def error_identacion(self, texto, subrutinas, constantes):
        cont = 0
        for t in texto:
            cont += 1
            t.append(' ')
            if t[0] != '' and t[0][0] != '*':
                if (t[0].lower() not in constantes):
                    if t[0].lower() not in subrutinas:
                        print('{} Error en linea {}'.format(t[0], cont))

    def checar_mnemonico(self, fila, mnemonicos, directivas):
        for m in mnemonicos:
            if fila[1].lower() == m or fila[1].lower() in directivas:
                return True
        return False

    def checar_subrutinas(self, fila, subrutinas, constantes):
        for s in subrutinas:
            if fila[2].lower() == s or fila[2].lower() in constantes or fila[2].lower() == ' ':
                return True
        return False

    def checar_constantes(self, fila, subrutinas, constantes):
        for c in constantes:
            if fila[2].lower() == c or fila[2].lower() in subrutinas or fila[2].lower() == ' ':
                return True
        return False

    def mnemonico_inexistente(self, texto, mnemonicos, directivas):
        conta = 0
        for t in texto:
            conta += 1
            t.append(' ')
            if t[0] == '' and t[1] != ' ':
                if not self.checar_mnemonico(t, mnemonicos, directivas):
                    print('Error en linea {} mnemonico inexistente {}'.format(conta, t))

    def etiqueta_inexistente(self, texto, subrutinas, constantes):
        conta = 0
        for t in texto:
            conta += 1
            if t[0] == '' and t[1] != ' ':
                if t[2][0] != '$':
                    if t[2][0] != '#':
                        if not self.checar_subrutinas(t, subrutinas, constantes):
                            print('Error en linea {} etiqueta inexistente {}'.format(conta, t))

    def constante_inexistente(self, texto, subrutinas, constantes):
        conta = 0
        for t in texto:
            conta += 1
            if t[0] == '' and t[1] != ' ':
                if t[2][0] != '$':
                    if t[2][0] != '#':
                        if not self.checar_constantes(t, subrutinas, constantes):
                            print('Error en linea {} constante inexistente {}'.format(conta, t))


    # def variable_inexistente():
    #    pass

    def instruccion_c_operando(self, instrucciones_operando, mnemonicos_opcode):
        conta = 0
        for i in instrucciones_operando:
            conta += 1
            if i[1] != ' ':
                for m in mnemonicos_opcode:
                    # print(m, i)
                    if i[0].lower() in m:
                        if m[6] != '-- ':
                            print('Error', i, conta)


    def instruccion_n_operando(self, instrucciones_operando, mnemonicos_opcode):
        conta = 0
        for i in instrucciones_operando:
            conta += 1
            if i[1] == ' ':
                for m in mnemonicos_opcode:
                    # print(m, i)
                    if i[0].lower() in m:
                        if m[6] == '-- ':
                            print('Error', i, conta)



    def no_tiene_end(self, texto):
        for t in texto:
            for m in t:
                if m.lower() == 'end':
                    # print(' si tiene equisde')
                    return True
        return False


if __name__ == '__main__':
    compa = compilador()
    lector = lector()
    texto_crudo = lector.adquirir_texto()
    texto_proc = lector.procesar_texto(texto_crudo)
    subrutinas = lector.adquirir_subrutinas(texto_proc)
    subrutinas_num = lector.adquirir_subrutinas_numero(texto_proc)
    constantes = lector.adquirir_constantes(texto_proc)
    lector.error_identacion(texto_proc, subrutinas, constantes)
    lector.mnemonico_inexistente(texto_proc, compa.get_mnenomicos(), compa.get_directivas())
    lector.etiqueta_inexistente(texto_proc, subrutinas, constantes)
    lector.constante_inexistente(texto_proc, subrutinas, constantes)
    lector.no_tiene_end(texto_proc)
    inst_op = lector.instrucciones_operando(texto_proc)
    lector.instruccion_c_operando(inst_op, compa.get_mnenomicos_opcode())
    lector.instruccion_n_operando(inst_op, compa.get_mnenomicos_opcode())
    print(subrutinas_num)
