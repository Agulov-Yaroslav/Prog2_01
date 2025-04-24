"""
!/usr/bin/env python3
-*- coding: utf-8 -*-
"""


#Aufgabe1
def slice_string(input: str = "Programmieren") -> str:
    #nemgP
    return input[::-3]

'''
s = "Programmieren"
print(s[len(s)])

Wir kriegen ein Fehlermeldung
IndexError: string index out of range
Weil Indexierung in Python mit 0 beginnt und die Länge des Strings deswegen größer um eins
als das Index des letztes Char

>>> s = "Programmieren\n2"
>>> s_raw = r"Programmieren\n2"
>>> print(len(s))
15
>>> print(len(s_raw))
16
>>> print(s)
Programmieren
2
>>> print(s_raw)
Programmieren\n2
>>> 
In Variable s_rawwird ein Raw-Sring gespeichert, wo die Escape-Sequenzen nicht ausgewertet werden.
Dacher jeder Symbol so ausgedruckt wird wie er steht, und die länge des Sequenzes 16 Symbole ist.
In Variable s wird '\n' als Zeilenbruch interpretiert, was ein Symbol ist.
'''

#Aufgabe2

# def read_file(file: str) -> str:
#     raise NotImplementedError("Implement me!")
#
# def compute_ttr(corpus: str) -> float:
#     raise NotImplementedError("Implement me!")
#
#
# def get_unigrams(corpus: str) -> dict:
#     raise NotImplementedError("Implement me!")
#
# def invert_dict(d: dict) -> dict:
#     raise NotImplementedError("Implement me!")
#
# class Type:
#     def __init__(self, type: str, freq: int) -> None:
#         raise NotImplementedError("Implement me!")
#
#
# def dict_to_type_list(d: dict) -> list:
#     raise NotImplementedError("Implement me!")
#
#
# def scale_matrix(scalar: int, matrix: list) -> list:
#     raise NotImplementedError("Implement me!")
#
#
# def sum_matrices(matrix1: list, matrix2: list) -> list:
#     raise NotImplementedError("Implement me!")
#
#
# def transpose_matrix(matrix: list) -> list:
#     raise NotImplementedError("Implement me!")


if __name__ == "__main__":
    # Indexing
    assert slice_string() == "nemgP"

    ##########################################

    # Corpus Analysis

    # corpus = read_file("grail.txt")
    # ttr = compute_ttr(corpus)
    # print(f"The type token ratio is {ttr:.2f}.")
    #
    # unigram_dict = get_unigrams(corpus)
    #
    # print(sorted(unigram_dict.items(), reverse=True, key=lambda x: x[1])[:10])
    # print(
    #     sorted(invert_dict(unigram_dict).items(), reverse=True, key=lambda x: x[0])[:10]
    # )
    # print(sorted(invert_dict(unigram_dict).items(), key=lambda x: x[0])[8])
    # print(
    #     sorted(dict_to_type_list(unigram_dict), key=lambda x: x.freq, reverse=True)[:10]
    # )
    #
    # ##########################################
    #
    # # Matrices
    #
    # a = [[1, 2, 3], [4, 5, 6]]
    # b = [[5, 3, 1], [-1, -3, -5]]
    # c = [[6, 5, 4], [3, 2, 1], [1, 0, -1], [-3, -4, -5]]
    #
    # assert scale_matrix(5, a) == [[5, 10, 15], [20, 25, 30]]
    # assert scale_matrix(-1, c) == [[-6, -5, -4], [-3, -2, -1], [-1, 0, 1], [3, 4, 5]]
    #
    # assert sum_matrices(a, b) == [[6, 5, 4], [3, 2, 1]]
    #
    # assert transpose_matrix(a) == [[1, 4], [2, 5], [3, 6]]
    # assert transpose_matrix(c) == [[6, 3, 1, -3], [5, 2, 0, -4], [4, 1, -1, -5]]
