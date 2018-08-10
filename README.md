# Fuzzy Grassmann Numbers

A `Python` library for the mathematics of Fuzzy Grassmann Numbers.


## Concept

### Grassmann Numbers

A Grassmann number is a generalized dual number.

A dual number is an extension of the real numbers, and has the form

    z = a + b⋅ε

where

    a, b are real numbers and
    ε^2 = 0

Therefore, a Grassmann number will have the form

    g = a + b⋅ε_1 + c⋅ε_2 + ...

where

    ε_1^2 = 0
    ε_2^2 = 0
    ε_3^2 = 0

and so forth, but their multiplication will be

    ε_1 ⋅ e_2 = - ε_2 ⋅ e_1
    ε_2 ⋅ e_3 = - ε_3 ⋅ e_2

and so forth.


### Fuzzy Numbers

A fuzzy number describes the degree of belonging to a certain set with the use of a membership function.

Given an interval `[x_1, x_2]`, with `x_1` and `x_2` being real numbers, we map each number in the interval to a number in the real segment [0, 1]. This mapping characterizes the belonging, the membership of the entity to the set.

Addition would take then the form:

    [x_1, x_2] + [y_1, y_2] = [x_1 + y_1, x_2 + y_2]

Subtraction:

    [x_1, x_2] - [y_1, y_2] = [x_1 - y_1, x_2 - y_2]

Multiplication:

    [x_1, x_2] ⋅ [y_1, y_2] = [min(x_1⋅y_1, x_1⋅y_2, x_2⋅y_1, x_2⋅y_2), max(x_1⋅y_1, x_1⋅y_2, x_2⋅y_1, x_2⋅y_2)]

Division:

    [x_1, x_2] / [y_1, y_2] = [min(x_1/y_1, x_1/y_2, x_2/y_1, x_2/y_2), max(x_1/y_1, x_1/y_2, x_2/y_1, x_2/y_2)]


### Fuzzy Grassmann Numbers

Considering the Grassmann number

    g = a + b⋅ε_1 + c⋅ε_2 + ...

A Fuzzy Grassmann number is one where the coefficients `a`, `b`, `c`, and so forth are fuzzy numbers, arriving at

    fg = [a_1, a_2] + [b_1, b_2]⋅ε_1 + [c_1, c_2]⋅ε_2 + ...



## Inspiration

This idea of a Fuzzy Grassmann Number arrived while glancing over `2017, Felix Mora-Camino, Carlos Alberto Nunes Cosenza, Fuzzy Dual Numbers. Theory and Applications, Springer`.
