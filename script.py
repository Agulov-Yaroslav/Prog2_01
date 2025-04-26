"""
!/usr/bin/env python3
-*- coding: utf-8 -*-
"""
import copy


# Aufgabe1
def slice_string(input: str = "Programmieren") -> str:
    # nemgP
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
Dacher jeder Symbol so ausgedruckt wird wie er steht, und die länge des Sequences 16 Symbole ist.
In Variable s wird '\n' als Zeilenbruch interpretiert, was ein Symbol ist.
'''


# Aufgabe2

def read_file(file: str) -> str:
    f = open(file, "r")
    corpus = f.read()
    f.close()
    return corpus


def wort_to_tok(corpus: str) -> list:
    # Um wörter korrect zu spliten, werden wir alle Zeichen durch Leerzeichen ersetzen
    zeichen = (',', '.', '!', '?', ':', '[', ']', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ';')
    c_ohne_zeich = corpus.lower()
    for z in zeichen:
        c_ohne_zeich = c_ohne_zeich.replace(z, ' ')
    return c_ohne_zeich.split()


def compute_ttr(corpus: str) -> float:
    tokens = wort_to_tok(corpus)
    types = set(tokens)
    return len(types) / len(tokens)


def get_unigrams(corpus: str) -> dict:
    """
    ein Dictionary, das für jedes Wort zählt, wie häufig es im Korpus vorkommt.
    :param corpus:
    :return:
    """
    tokens = wort_to_tok(corpus)
    unigrams = dict()

    for token in tokens:
        unigrams[token] = unigrams.get(token, 0) + 1

    return unigrams


def invert_dict(d: dict) -> dict:
    invert_d = {v: k for k, v in d.items()}
    return invert_d


'''
    Welches Problem gibt es?
    Wie lässt sich dieses für unseren Anwendungsfall lösen?

    Das Problem ist:
    Mehrere Wörter können die gleiche Häufigkeit haben und
    Dictionary-Keys dürfen sich aber nicht doppeln.
    Nur das letzte Wort pro Häufigkeit wird behalten.
    
    Die Werte im invertierten Dictionary müssen Listen sein,
    um mehrere Wörter pro Häufigkeit zu speichern
    '''


class Type:
    def __init__(self, type: str, freq: int) -> None:
        """
        Type soll dieselben Informationen speichern wie ein Key-Value-Paar aus get unigrams.
        :param type:
        :param freq:
        """
        self.type = type
        self.freq = freq


def dict_to_type_list(d: dict) -> list:
    """
    Konvertieren des Dictionary aus get unigrams
    in eine Liste aus Type-Instanzen

    :param d:
    :return:
    """
    return [Type(k, v) for k, v in d.items()]


def scale_matrix(scalar: int, matrix: list) -> list:
    """
    Funktion nimmt ein Skalar und eine beliebige Matrix
    und jeden Wert in der Matrix mit dem Skalar multipliziert

    :param scalar:
    :param matrix:
    :return:
    """
    result = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(i * scalar)
        result.append(new_row)
    return result


def sum_matrices(matrix1: list, matrix2: list) -> list:
    #result = matrix1.copy()
    """
    Die Zeile macht nur eine flache Kopie von matrix1. Das heißt:
    result ist eine neue Liste, aber die die Zeilen sind dieselben
    Objekte wie in matrix1.

    Deswegen importiere ich 'copy'
    """
    result = copy.deepcopy(matrix1)

    for row in range(len(matrix1)):
        for i in range(len(matrix1[0])):
            result[row][i] = matrix1[row][i] + matrix2[row][i]

    return result


def transpose_matrix(matrix: list) -> list:
    """
    eine Funktion, die eine beliebige Matrix
    nimmt und die zugehörige transponierte Matrix zurückgibt.

    :param matrix:
    :return:
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


if __name__ == "__main__":
    # Indexing
    assert slice_string() == "nemgP"

    ##########################################

    # Corpus Analysis

    corpus = read_file("grail.txt")
    unigrams = get_unigrams(corpus)
    invert_dict(unigrams)
    ttr = compute_ttr(corpus)
    print(f"The type token ratio is {ttr:.2f}.")

    unigram_dict = get_unigrams(corpus)

    print(sorted(unigram_dict.items(), reverse=True, key=lambda x: x[1])[:10])
    print(
        sorted(invert_dict(unigram_dict).items(), reverse=True, key=lambda x: x[0])[:10]
    )
    print(sorted(invert_dict(unigram_dict).items(), key=lambda x: x[0])[8])
    print(
        sorted(dict_to_type_list(unigram_dict), key=lambda x: x.freq, reverse=True)[:10]
    )

    ##########################################

    # Matrices

    a = [[1, 2, 3], [4, 5, 6]]
    b = [[5, 3, 1], [-1, -3, -5]]
    c = [[6, 5, 4], [3, 2, 1], [1, 0, -1], [-3, -4, -5]]

    assert scale_matrix(5, a) == [[5, 10, 15], [20, 25, 30]]
    assert scale_matrix(-1, c) == [[-6, -5, -4], [-3, -2, -1], [-1, 0, 1], [3, 4, 5]]


    assert sum_matrices(a, b) == [[6, 5, 4], [3, 2, 1]]

    assert transpose_matrix(a) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix(c) == [[6, 3, 1, -3], [5, 2, 0, -4], [4, 1, -1, -5]]



