#!/usr/bin/python3

"""
The "101-lazy_matrix_mul" module
"""

import numpy as ny


def lazy_matrix_mul(m_a, m_b):
    """
    Return the Multiplication of two matrices.

    Args:
        m_a: The first matrix.
        m_b: the second matrix.
    """

    return (ny.matmul(m_a, m_b))
