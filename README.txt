####################################################################################

Cryptography and Compression
    Shows how to hide a secret message inside an image file, aka "Steganography".
    The altered image does not appear any different from the original.
    The message can be stored in cleartext, or encoded with a Caesar Cipher,
    or compressed with a Huffman Code before it's hidden inside the image.

    codec.py:
        implements regular Steganography, Caesar Cyper, and Huffman Data Compression
    cryptography.py:
        the driver code that implements the interface of the program
    steganography.py:
        encodes an encoded binary message into an image

####################################################################################

Expression Tree
    Shows how to parse a mathematical expression into an Expression Tree and
    evaluate the expression by recursively walking the Expression Tree.

    calculator.py:
        converts an inputed expression to postfix notation and evaluates interface
    stack.py:
        implmenetation of stack that expression evaluation relies on
    tree.py:
        contains classes Tree and (child class) ExpTree which create an expression tree
        which when traversed properly will return the evaluated expression

####################################################################################

Recursion and Fractals
    Shows how to draw the Koch Star and Dragon fractals using recursion.

    The N-Queens algorithm uses recursion to generate layouts for each Queen on
    an N x N board, and then validates if the permutation is "safe" i.e. none of
    the Queens lies on the path of the other Queens.

    dragon.py:
        recursively draws the Dragon Fractal using Turtle
    snowflake.py:
        recursively draws the Koch Snowflake Fractal using Turtle
    queens.py:
        takes input n which represents an n x n chess board and returns solutions to
        the Queens Problem

####################################################################################

Search Algorithms
    Shows how to efficiently search an input interval to identify all the roots of a
    polynomial equation i.e. X coordinates where the equation touches or crosses the
    X-axis.

    roots.py:
        given the coefficients to a polynomial (up to the 6th degree), returns the roots
        of the function

####################################################################################

User Interfaces
    Play the Game of Fifteen puzzle or ask the computer to solve a shuffled board
    using a simple BFS strategy.

    Interact with a simple Calculator.

    fifteen.py:
        implements an ASCII interface of the Fifteen Puzzle
    game.py:
        a GUI interface implementation of the Fifteen Puzzle
    guicalc.py:
        a GUI interface for a calculator

####################################################################################