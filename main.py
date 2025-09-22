from math import prod
from random import randint
from itertools import permutations

class Matrix:
    class Vector:
        def __init__( self, vec: list[int, ] ):
            self.vec = vec
            self.n = len( vec )

        def __add__( self, other ):
            if isinstance( other, Matrix.Vector ):
                return Matrix.Vector( [ self.vec[ i ] + other.vec[ i ] for i in range( self.n ) ] )
            
        def __mul__( self, other ):
            if isinstance( other, (int, float) ):
                return Matrix.Vector( [ other * self.vec[ i ] for i in range( self.n )] )
        
    def __init__( self, matr: list[Vector, ] ):
        if isinstance( matr[ 0 ], Matrix.Vector ):
            self.m, self.n = len( matr ), matr[0].n
            self.matr = matr
        else:
            self.m, self.n = len( matr ), len( matr[ 0 ] )
            self.matr = [ Matrix.Vector( vec ) for vec in matr ]
        self.isSquare = self.m == self.n
        if self.isSquare:
            self.order = self.n

    def __str__( self ) -> str:
        MAX_LEN_EL = len( str( max( max( vec.vec, key=lambda x: len( str( x ) ) ) for vec in self.matr ) ) )
        result = "\n"
        for vec in self.matr:
            result += " ".join( [ " " * ( MAX_LEN_EL - len( str( el ) )) + str( el ) for el in vec.vec ] ) + '\n'
        return result
    
    def __add__( self, other ):
        if isinstance( other, Matrix ):
            return Matrix( [ self.matr[ i ] + other.matr[ i ] for i in range( self.m ) ] )

    def __mul__( self, other ):
        if isinstance( other, ( int, float ) ):
            return Matrix( [ vec * other for vec in range( self.m ) ] )
        elif isinstance( other, Matrix ):
            return Matrix( [ [ sum( self.matr[ i ].vec[ k ] * other.matr[ k ].vec[ j ] for k in range( self.n ) ) for j in range( other.n ) ] for i in range( self.m ) ] )

    def _transposition( self ):
        return Matrix( [ [ self.matr[ i ].vec[ j ] for i in range( self.m ) ] for j in range( self.n ) ] )

    def _minor( self, pos: list[ int, int ] ):
        result_matrix = []
        for i in range( self.m ):
            if i != pos[ 0 ]:
                result_matrix.append( [] )
                for j in range( self.n ):
                    if j != pos[ 1 ]:
                        result_matrix[ -1 ].append( self.matr[ i ].vec[ j ] )
        return Matrix( result_matrix )
    
    def determinant( self, methods: str="formula" ) -> int | float:
        if methods == "formula":
            return Matrix._det_formula( self.matr )
        elif methods == "minors":
            return Matrix._det_minors( self.matr )
        elif methods == "gaus":
            return Matrix._det_gaus( self.matr )

    @staticmethod
    def _det_formula( matrix: list=[ list, ] ) -> int | float:
        obj = Matrix( matrix )
        if obj.isSquare:
            if obj.order == 1:
                return obj.matr[ 0 ].vec[ 0 ]
            else:
                perms = list( permutations( range( obj.order ) ) )
                det = 0
                for J in range( len( perms ) ):
                    det += ( -1 )**Matrix._invers( perms[ J ] ) * prod( [ obj.matr[ i ].vec[ perms[ J ][ i ] ] for i in range( obj.order ) ] )
                return det

    @staticmethod
    def _det_minors( matrix: list=[ list, ] ) -> int | float:
        obj = Matrix( matrix )
        if obj.isSquare:
            if obj.order == 1:
                return obj.matr[ 0 ].vec[ 0 ]
            else:
                return sum( ( -1 )**i * obj.matr[ i ].vec[ 0 ] * obj._minor( [ i, 0 ] ).determinant( "minors" ) for i in range( obj.order ) )

    @staticmethod
    def _det_gaus( matrix: list=[ list, ] ) -> int | float:
        obj = Matrix( matrix )
        if obj.isSquare:
            if obj.order == 1:
                return obj.matr[ 0 ].vec[ 0 ]
            else:
                for i in range( obj.order - 1 ):
                    for j in range( 1, obj.order - i ):
                        a = - obj.matr[ i + j ].vec[ i ] / obj.matr[ i ].vec[ i ]
                        obj.matr[ i + j ] += obj.matr[ i ] * a

                return prod( [ obj.matr[ i ].vec[ i ] for i in range( obj.order ) ] ) 

    @staticmethod
    def _invers( perm: list[ int, ] ):
        n = len( perm )
        inversions = 0
        for i in range( n ):
            for j in range( i+1, n ):
                if perm[ i ] > perm[ j ]:
                    inversions += 1
        return inversions

    @staticmethod
    def unit( order: int ):
        return Matrix( [ [ int( i == j ) for j in range( order ) ] for i in range( order ) ] )

    @staticmethod
    def random( m: int, n: int, diap: list[ int, int ]=[ -10, 10 ]):
        return Matrix( [ [ randint( *diap ) for j in range( n ) ] for i in range( m ) ] )
    