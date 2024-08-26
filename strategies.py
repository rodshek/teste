# Mapeamento das relações entre números baseado no texto fornecido
number_relationships = {
    1: [2, 4, 11, 21, 31],
    2: [10, 22, 32, 33, 5, 25],
    3: [30],
    4: [14, 24, 34],
    5: [2, 15, 25, 35, 10],
    6: [7, 16, 26],
    7: [9, 30, 27, 24],
    8: [29, 19, 18],
    9: [28, 19, 18],
    10: [0, 20, 30, 27, 33],
    11: [1, 14],
    12: [6, 24, 22, 32],
    13: [31],
    14: [4, 24, 34, 11],
    15: [5],
    16: [28, 17, 18, 19],
    17: [20],
    18: [8, 9],
    19: [8, 9],
    20: [0, 10, 30],
    21: [1, 9, 12],
    22: [2, 5, 32, 33],
    23: [32],
    24: [4, 14, 34, 7],
    25: [5, 2, 35],
    26: [7, 36],
    27: [24, 28, 29],
    28: [9, 29, 27],
    29: [8, 9, 28, 27],
    30: [0, 10, 20, 33],
    31: [1, 13],
    32: [2, 22, 23, 30],
    33: [22, 11, 30],
    34: [24, 14, 4],
    35: [5, 2, 19, 21, 29],
    36: [0, 1, 2, 3]
}


def get_suggested_numbers(number):
    """
    Retorna a lista de números sugeridos para jogar com base no número inserido.
    Se não houver números relacionados, retorna uma lista vazia.
    """
    return number_relationships.get(number, [])
