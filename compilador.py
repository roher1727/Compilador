# -*- coding: utf-8 -*-
import codecs
import numpy as np


class compilador:
    archivo = []
    with codecs.open('68HC11.csv', "r", encoding='utf-8', errors='ignore') as fdata:
        for row in fdata:
                cortada = row.split(',')
                archivo.append(cortada)

    mnemonicos = [filita[1] for filita in archivo]
    mnemonicos = mnemonicos[1:]
    # print(mnemonicos)
    arreglo_mne = np.array(archivo)

    mnemonicos_opcode = []

    for filita in archivo:
        mnemonicos_opcode.append([filita[1],filita[2], filita[5], filita[8], filita[11], filita[14], filita[17], filita[20]])

    mnemonicos_opcode = mnemonicos_opcode[1:]

    direccionamientos = {'inmediato': [filita[2:5] for filita in archivo], 'directo': [filita[5:8] for filita in archivo], 'indexadox': [filita[8:11] for filita in archivo], 'indexadoy': [filita[11:14] for filita in archivo], 'extendido': [filita[14:17] for filita in archivo], 'inherente': [filita[17:20] for filita in archivo], 'relativo': [filita[20:23] for filita in archivo]}

    directivas = ['org', 'equ', 'fcb', 'end']

    """
    for i in range(0,len(mnemonicos)):
        print('\n'+mnemonicos[i]+'\n')
    for k in direccionamientos.keys():
        print(k, end= ' ')
        print(direccionamientos[k][i], end=' ')
    """

    def __init__(self):
        pass

    def indice_mnemonico(self, mnemonico):
        try:
            return self.mnemonicos.index(mnemonico)
        except(ValueError):
            print('No es un mnemonico')

    def tipo_direccionamiento(self, tipo):
        try:
            for k in self.direccionamientos.keys():
                if self.direccionamientos[k][tipo][0] != '-- ':
                    print(k)
        except(TypeError):
            pass

    def get_mnenomicos(self):
        return self.mnemonicos

    def get_directivas(self):
        return self.directivas

    def get_mnenomicos_opcode(self):
        return self.mnemonicos_opcode


if __name__ == '__main__':
    compa = compilador()
    # print(compa.mnemonicos)
    # compa.tipo_direccionamiento(4)
    mnemos = print(compa.get_mnenomicos_opcode())
