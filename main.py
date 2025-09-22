from math import prod
from random import randint
from itertools import permutations

class Matrix:
    def __init__( self, matrix: list[int, ] ):
        self.matrix = matrix
        self.m, self.n = len( matrix ), len( matrix[0] )
        self.isSquare = self.m == self.n

    def __str__( self ) -> str:
        max_el_len = len( str( max( max(vec, key=lambda x: len(str(x))) for vec in self.matrix ) ) )

        result = "\n"
        for vec in self.matrix:
            result += " ".join( [ " " * ( max_el_len - len( str( el ) )) + str( el ) for el in vec ] ) + '\n'

        return result

    def __add__( self, other ):
        if isinstance( other, Matrix ):
            return Matrix( [ [ self.matrix[ i ][ j ] + other.matrix[ i ][ j ] for j in range( self.n ) ] for i in range( self.m ) ] )
        else:
            raise "Матрицы можно складывать только с матрицами"

    def __mul__( self, other ):
        if isinstance( other, Matrix ):
            if self.n == other.m:
                return Matrix( [ [ sum( self.matrix[ i ][ k ] * other.matrix[ k ][ j ] for k in range( self.n ) ) for j in range( other.n ) ] for i in range( self.m ) ] )
            else:
                raise "Для умножения матриц количество столбцов первой матрицы, должно быть равно количеству строк второй матрицы"
        elif isinstance( other, ( int, float ) ):
            return Matrix( [ [ self.matrix[ i ][ j ] * other for j in range( self.n ) ] for i in range( self.m ) ] )
        else:
            raise "Матрицы можно умножать только на матрицы, либо числа"

    def transposition( self ):
        return Matrix( [ [ self.matrix[ i ][ j ] for i in range( self.m ) ] for j in range( self.n ) ] )

    def minor( self, pos: list[ int, int ] ):
        result_matrix = [ [] for _ in range( self.m - 1 ) ]
        for i in range( self.m ):
            for j in range( self.n ):
                if i != pos[ 0 ] and j != pos[ 1 ]:
                    if i > pos[0]:
                        result_matrix[ i - 1 ].append( self.matrix[ i ][ j ] )
                    else:
                        result_matrix[ i ].append( self.matrix[ i ][ j ] )
        return Matrix( result_matrix )

    @staticmethod
    def sign_of_permutation( perm ):
        n = len( perm )
        inversions = 0
        for i in range( n ):
            for j in range( i+1, n ):
                if perm[ i ] > perm[ j ]:
                    inversions += 1
        return (-1) ** inversions

    def _det_formula( self ):
        if self.isSquare:
            if self.m == 1:
                return self.matrix[ 0 ][ 0 ]
            else:
                perms = list( permutations( range( self.n ) ) )
    
                det = 0
                for perm in perms:
                    product = 1
                    for i in range( self.n ):
                        product *= self.matrix[ i ][ perm[ i ] ]
                        
                    det += Matrix.sign_of_permutation( perm ) * product
                return det

    def _det_minors( self, k: int=0 ):
        if self.n == 1:
            return self.matrix[ 0 ][ 0 ]
        else:
            return sum( self.matrix[ i ][ 0 ] * ( -1 )**i * self.minor( [ i, 0 ] ).determinant() for i in range( self.m ) )

    def _get_vector( self, k: int ) -> list[int,]:
        return self.matrix[ k ]

    def _put_vector( self, k: int, vector: list ) -> None:
        self.matrix = [ self.matrix[i] if i != k else vector for i in range( self.m ) ] 

    def _change_vector( self, k1, k2 ):
        vector1 = self.matrix[ k1 ]
        vector2 = self.matrix[ k2 ]
        self.matrix[ k1 ], self.matrix[ k2 ] = vector2, vector1

    def _det_gaus( self ):
        if self.isSquare:
            if self.m == 1:
                return self.matrix[ 0 ][ 0 ]
            else:
                other = Matrix( self.matrix )
                for i in range( other.n - 1 ):
                    for j in range( 1, other.n - i ):
                        a = - other.matrix[ i + j ][ i ] / other.matrix[ i ][ i ]
                        other._put_vector( i + j, [ other._get_vector( i + j )[ n ] + other._get_vector( i )[ n ] * a for n in range( other.n ) ] )

        return prod( [ other.matrix[ i ][ i ] for i in range( other.m ) ] ) 

    def determinant( self, method: str="formula" ):
        if method == "formula": return self._det_formula()
        elif method == "minors":    return self._det_minors()
        elif method == "gaus":  return self._det_gaus()

    @staticmethod
    def unit( order: int ):
        return Matrix( [ [ int( i == j ) for j in range( order ) ] for i in range( order ) ] )
    