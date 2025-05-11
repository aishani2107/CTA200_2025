def iterate_complex(x, y, max_iter):
    
    """
    This function determines if the iteration z(i+1) = [z(i)]^2 + c is bounded
    by |z|^2 = <= 2 (maximum value) when performed max_iter number of times.
    
    inputs: x, y ------ int, in [-2, 2], real and imaginary parts of c
            max_iter -- int, maximum number of iterations to perform
            
    output: iter ------ the iteration number when (if ever) |z| diverges to infinity
    """
    # define complex number
    c = x + y*1j
    
    # iterate z
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter