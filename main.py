from random import randint

class Matrix:
    def __init__( self, matrix: list[list, ] ):
        self.matrix = matrix
        self.m, self.n = len( matrix ), len( matrix[0] )
        self.isSquare = self.m == self.n

    def __str__( self ) -> str:
        max_el_len = len( str( max( max(vec) for vec in self.matrix ) ) )

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

    def determinant( self ):
        if self.isSquare:
            if self.m == 1:
                return self.matrix[ 0 ][ 0 ]
            elif self.m == 2:
                return self.matrix[ 0 ][ 0 ] * self.matrix[ 1 ][ 1 ] - \
                       self.matrix[ 0 ][ 1 ] * self.matrix[ 1 ][ 0 ]
            elif self.m == 3:
                return self.matrix[ 0 ][ 0 ] * self.matrix[ 1 ][ 1 ] * self.matrix[ 2 ][ 2 ] + \
                       self.matrix[ 0 ][ 1 ] * self.matrix[ 1 ][ 2 ] * self.matrix[ 2 ][ 0 ] + \
                       self.matrix[ 0 ][ 2 ] * self.matrix[ 1 ][ 0 ] * self.matrix[ 2 ][ 1 ] - \
                       self.matrix[ 0 ][ 2 ] * self.matrix[ 1 ][ 1 ] * self.matrix[ 2 ][ 0 ] - \
                       self.matrix[ 0 ][ 1 ] * self.matrix[ 1 ][ 0 ] * self.matrix[ 2 ][ 2 ] - \
                       self.matrix[ 0 ][ 0 ] * self.matrix[ 1 ][ 2 ] * self.matrix[ 2 ][ 1 ]
            else:
                return sum( self.matrix[ i ][ 0 ] * ( -1 )**i * self.minor( [ i, 0 ] ).determinant() for i in range( self.m ) )
        else:
            raise "Определитель не определён для неквадратных матриц"

    @staticmethod
    def unit( order: int ):
        return Matrix( [ [ int( i == j ) for j in range( order ) ] for i in range( order ) ] )
    