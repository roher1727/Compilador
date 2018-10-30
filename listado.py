from compilador import compilador
from lector import lector


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


def adquirir_constantes_operador(texto):
    constantes = []
    for t in texto:
        t.append(' ')
        if t[1].lower() == 'equ':
            constantes.append([t[0].lower(), t[2]])

    return constantes

def checar_numero(operador, subrutinas_num):
    for c in subrutinas_num:    
        if(operador[2].lower() in c[0]):
            # print(c,operador)
        
            return True,c[1] 
    return False,None


def instrucciones_operando(texto):
    inst_operando = []
    for t in texto:
        t.append(' ')
        if '*' not in t[0]:
            if (t[1] != ' '):
                if(t[0] == ''):
                    inst_operando.append([t[1], t[2]])
    return inst_operando


def instrucciones_operando_num(texto, subrutinas_num):
    inst_operando = []
    numero = 0
    for t in texto:
        numero += 1
        t.append(' ')
        if '*' not in t[0]:
            if (t[1] != ' '):
                if(t[0] == ''):
                    booleano,num = checar_numero(t, subrutinas_num)
                    if booleano:
                        inst_operando.append([t[1], abs(numero - num)])
                    else: 
                        inst_operando.append([t[1],t[2]])
                        
    return inst_operando
            

def cambiar_constantes(instrucciones, constantes):
    constants = dict(constantes)
    for i in instrucciones:
        for c in constantes:
            if i[1].lower() in c:
                i[1] = constants[i[1].lower()]
                # print(i[1])
    # for t in instrucciones:
    #     print(t)
    return instrucciones


def cambiar_hexa(instrucciones, mnemonicos_opcode, subrutinas):
    for i in instrucciones:
        for m in mnemonicos_opcode:
            if i[0].lower() == m[0]:
                # print('{} \n'.format(i))
                if i[1] == ' ' or i[1].lower() in subrutinas:
                    if i[1].lower() in subrutinas:
                        if m[5] != '-- ':
                            i[0] = m[5]
                            # print(i, 'extendido')
                        elif m[7] == '-- ':
                            i[0] = m[6]
                            # print(i, 'inherente')
                        elif m[6] == '-- ':                   
                            i[0] = m[7]
                            # print(i, 'relativo')
                    elif m[7] == '-- ':
                        i[0] = m[6]
                        # print(i, 'inherente')
                    elif m[6] == '-- ':                   
                        i[0] = m[7]
                        # print(i, 'relativo')
                elif ',' in i[1]:
                    if 'x' in i[1] or 'X' in i[1]:
                        i[0] = m[3]
                        # print(i, 'indexado x')
                    if 'y' in i[1] or 'Y' in i[1]:
                        i[0] = m[4]
                        # print(i, 'indexado y')
                elif i[1][0] == '#':
                    i[0] = m[1]
                    # print(i, 'inmediado')
                elif len(i[1]) > 3:
                        i[0] = m[5]
                        # print(i, 'extendido')
                elif i[1][0] == '$':
                    i[0] = m[1]
                    # print(i, 'directo')
                else:
                    pass
                    # print(i, 'unknown')
    return instrucciones


def imprimir_chido(instrucciones):
    for it in instrucciones:
        if it[1] != ' ':
            if it[1][0] == '#':
                it[1] = it[1][1:]
            if it[1][0] == '$':
                it[1] = it[1][1:]
    return instrucciones
"""
    instrucciones1 = [j for i in instrucciones for j in i]
    print(instrucciones1)
"""

if __name__ == '__main__':
    compa = compilador()
    lector = lector()
    mnemonicos = compa.get_mnenomicos()
    text = procesar_texto(adquirir_texto())
    # obtener_operadores(text)
    constantes = adquirir_constantes_operador(text)
    subrutinas_num = lector.adquirir_subrutinas_numero(text)
    inst = lector.instrucciones_operando(text)
    subrutinas = lector.adquirir_subrutinas(text)
    hexa = cambiar_hexa(cambiar_constantes(inst, constantes), compa.get_mnenomicos_opcode(), subrutinas)
    inste = imprimir_chido(hexa)
    lol = instrucciones_operando_num(text, subrutinas_num)
    constantes_s = lector.adquirir_constantes(text)

    # Errores
    lector.error_identacion(text, subrutinas, constantes_s)
    lector.mnemonico_inexistente(text, compa.get_mnenomicos(), compa.get_directivas())
    lector.etiqueta_inexistente(text, subrutinas, constantes_s)
    lector.constante_inexistente(text, subrutinas, constantes_s)
    lector.no_tiene_end(text)
    lector.instruccion_c_operando(inst, compa.get_mnenomicos_opcode())
    lector.instruccion_n_operando(inst, compa.get_mnenomicos_opcode())
    
    directivas = compa.get_directivas()
    
    khe = []
    for l,i in zip(lol,inste) : 
        if i[1].lower() in subrutinas:
            i[1]=l[1]
        if 'X' in str(i[1]):
            a = list(i[1])
            a.remove('X')
            a.remove(',')
            a.remove('#')
            a.remove('$')

            a = "".join(a)
            i[1] = a
            # print(a)

        if 'Y' in str(i[1]):
            b = list(i[1])
            b.remove('Y')
            b.remove(',')
            
            b = "".join(b)
            i[1] = b
            # print(b)
        
        if '$' in str(i[1]):
            c = list(i[1])
            c.remove('$')

            c = "".join(c)
            i[1] = c
            # print(c)

        if ',' in str(i[1]):
            d = list(i[1])
            d.remove(',')

            d = "".join(d)
            i[1] = d
            # print(d)
        
        if ' \' ' in str(i[1]):
            
            d = list(i[1])
            print(d)
            d.remove('\'')

            d = "".join(d)
            i[1] = d
            print(d)

        if i[0].lower() in directivas:
            i[0] = ''
        khe.append(i)
    instrucciones1 = [str(j) for i in khe for j in i]
    # print(instrucciones1)
    texto = "".join(instrucciones1)
    # print(texto)
    with open('muestra.hex','w') as arc:
        for i in range(0,len(texto),2):
            if i%32 == 0:
                print('\n{}>'.format(8000+(i//2)),end=' ',file=arc)
            print("{}{}".format(texto[i],texto[i+1]),end=' ',file=arc)
        