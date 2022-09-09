# SimpleVectorLibrary
A vector library for an environment which does not allow importing modules (for some reason)

## Vector

    Constructor

        Pass a list or generator

        Example
            ```python
            v1 = Vector([0, 1, 2, 3])
            v2 = Vector(range(4))
            ```

    Operations

        ** All Vectoresque objects must support indexing, length, and iteration | such as list **
        ** Numerics are either 'int' or 'float' **

        Vector + Vectoresque                -> add elements of each vector
        Vector - Vectoresque                -> subtract elements of each vector
        Vector * {Vectoresque | Numeric}    -> multiply elements of each vector, or multiply each element by numeric
        Vector / {Vectoresque | Numeric}    -> divide elements of each vector, or divide each element by numeric

        All operators also support 'op=', with the same behavior

        Indexing works normally (as would be expected)

        len()               returns length of vector
        iter()              returns iterator over vector elements
        str() and repr()    return string representation of vector
