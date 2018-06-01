from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dna
import re
from .utils import Direction, Ml
from .exceptions import ContainsLetters, SquareMatrix


class Mutant(APIView):

    DIRECTIONS = [Direction(0, 1), Direction(0, -1), Direction(1, 0),
                  Direction(-1, 0), Direction(1, 1), Direction(1, -1),
                  Direction(-1, 1), Direction(-1, -1)]

    SEQUENCES = [
        ['A', 'A', 'A', 'A'],
        ['C', 'C', 'C', 'C'],
        ['G', 'G', 'G', 'G'],
        ['T', 'T', 'T', 'T'],
    ]

    def get(self, request):
        """
        curl -X GET http://localhost:8000/stats/
        :param request: 
        :return: 
        """
        all = Dna.objects.all().count()
        count_mutant_dna = Dna.objects.filter(is_mutant=True).count()
        count_human_dna = all - count_mutant_dna
        ratio = count_mutant_dna / count_human_dna

        return Response(
            {'count_mutant_dna': count_mutant_dna,
             'count_human_dna': count_human_dna,
             'ratio': ratio}
        )

    def post(self, request, format=None):
        """
        :param request: 
        :param format: 
        :return: 
        """
        dna = request.data['dna']

        try:
            matrix = self.validate_dna(dna)
        except(ContainsLetters, SquareMatrix) as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        dna, created = Dna.objects.get_or_create(
            dna='-'.join(dna),
        )

        if created:
            bool = self.is_mutant(matrix)
            if bool:
                dna.is_mutant = bool
                dna.save()
        else:
            bool = dna.is_mutant

        st = status.HTTP_200_OK if bool else status.HTTP_403_FORBIDDEN

        return Response({'is_mutant': bool}, status=st)

    def is_mutant(self, matrix):
        """ 
        determina si un dna pertenece a un humano o a un mutante
        :param matrix: 
        :return: boolean
        """

        lista_fuera = []
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                for sequence in Mutant.SEQUENCES:
                    for direction in Mutant.DIRECTIONS:
                        lista = Ml.find_sequence(matrix, x, y, direction, sequence)

                        if lista:
                            for i in lista:
                                if i not in lista_fuera:
                                    lista_fuera.append(i)
                            if len(lista_fuera) > 8: # lista_afuera tiene 8 posiciones. Hay dos secuencias en matrix.
                                return True
        return False

    def validate_dna(self, dna):
        """
        Valida si los string de la lista dna contiene solo los caracteres (A,T,G,C,a,t,g,c)
        :param dna: lista de string
        :return: one matrix NxN. One list of lists in python.
        """
        mat = []
        ant = len(dna[0])

        for string in dna:

            if ant != len(string):
                raise SquareMatrix('The matrix must be square')

            if not bool(re.match('^[ATGCatgc]+$', string)):
                raise ContainsLetters('the string should only have the '
                                      'characters: '
                                      'A, T, G, C, a, t, g, c')

            mat.append(list(string.upper()))

        return mat
