# matrix
Пробую реализовать класс для работы с матрицами из линейной алгебры. Основные операции с матрицами, а также нахождение определителя.

# Реализованные методы:
## 1.1. Сумма матриц:
A = (a<sub>ij</sub>)

B = (b<sub>ij</sub>)

C = A + B = (a<sub>ij</sub> + b<sub>ij</sub>)

## 1.2. Произведение матрицы на число:
A = (a<sub>ij</sub>)

λ * A = (λ * a<sub>ij</sub>)

## 1.3. Произведение матрицы на матрицу:
A = (a<sub>ij</sub>)

B = (b<sub>jk</sub>)

C = A * B = (c<sub>ik</sub>)

c<sub>ik</sub> = a<sub>i1</sub> * b<sub>1k</sub> + aa<sub>i2</sub> * b<sub>2k</sub> + ... + aa<sub>ij</sub> * b<sub>jk</sub>

## 1.4. Транспонирование:
A = (a<sub>ij</sub>)

A<sup>T</sup> = (a<sub>ji</sub>)



# Пример использования:
A = Matrix( [ 1, 2 ],
            [ 3, 4 ] )
            
B = Matrix( [ 1, 2, 3 ], 
            [ 4, 5, 6 ] )
            

C = A * B


print( C )
