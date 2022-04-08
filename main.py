import os
import sys
import string
import random
import multiprocessing


def get_dominio_aleatorio():
    tamanho_string = 15
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=tamanho_string))


def consulta_dominio(dominio_principal, servidor_dns):
    string_aleatoria = get_dominio_aleatorio()
    os.system('host -t A {}.{} {}'.format(string_aleatoria, dominio_principal, servidor_dns))


def get_multiplas_consultas(dominio_principal, servidor_dns, iteracoes):
    processes = []
    for _ in range(iteracoes):
        process = multiprocessing.Process(target=consulta_dominio(dominio_principal, servidor_dns))
        processes.append(process)

    for i in range(len(processes)):
        processes[i].start()


if __name__ == '__main__':
    dominio_principal = sys.argv[1]
    servidor_dns = sys.argv[2]
    iteracoes = int(sys.argv[3])
    get_multiplas_consultas(dominio_principal, servidor_dns, iteracoes)
