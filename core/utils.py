
class Direction:
    """
    posicion x, y
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ml:

    @staticmethod
    def find_sequence(square, x, y, direction, word):
        """
        retorna una lista de posiciones
        :param x: fila
        :param y: columna
        :param direction:
        :param square: 
        :param word:  
        :return:
        """
        lista = []  # contiene una lista de posiciones
        word_index = 0

        while True:
            if x < 0 or x >= len(square[0]) or y < 0 or y >= len(square) or word_index >= len(word) or square[y][x] != word[word_index]:
                break

            # si cls.square[y][x] == cls.word[word_index] hago lo que sigue

            lista.append(Direction(x, y))  # agrego la posicion a la lista

            if word_index == len(word)-1:  # donde conviene poner esto?. antes del if, antes de agregar la posicion a la lista, aca o despues de incrementar word_index
                return lista  # si el indice word_index es igual al indice del ultimo elemento del string word retorno la lista. Ya termine de iterar sobre

            # le incremento los valores de la posicion actual a las variables x e y+
            x += direction.x
            y += direction.y
            word_index += 1  # incremento el indice porque
