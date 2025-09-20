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

    @staticmethod
    def unit( order: int ):
        return Matrix( [ [ int( i == j ) for j in range( order ) ] for i in range( order ) ] )
    