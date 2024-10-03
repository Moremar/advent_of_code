from part1 import parse
import math

# We get a list of k equations of the form t = ai [ni] with all ni prime with each other.
# This means we can apply the CRT (chinese remainders theorem) saying there is a unique solution for t
# smaller than the product of all ni.
#
# The solution is t = ((a1 * N1 * y1) + (a2 * N2 * y2) + ... + (ak * Nk * yk)) % N
# with :
#  N  = the product of the ni in the k equations
#  ai = the expected remainder in the ith equation
#  Mi = N / ni
#  yi = Mi^-1 the modular inverse or Mi, so that Mi * yi = 1 [ni]
#
# The modular inverse can be calculated from the extended Euclide inverse algorithm.
# it gives GCD(a, b), and a pair of numbers (u, v) so that au + bv = GCD(a, b)
# When a and b are prime with each other, GCD(a, b) = 1, so :
#    au + bv = 1    =>    au = 1 [b]    =>    u is the modular inverse of a modulo b
# With the same logic, v is the modular inverse of b modulo a


def euclide_gcd_algo(a, b):
    """Calculate (r, u, v) so that u * a + v * b = r = GCD(a, b)"""
    (r, u, v, r2, u2, v2) = (a, 1, 0, b, 0, 1)
    while r2 > 0:
        q = r // r2
        (r, u, v, r2, u2, v2) = (r2, u2, v2, r - q * r2, u - q * u2, v - q * v2)
    return r, u, v


def solve(data):
    _, buses = data
    # we have a list of equation of the type t + i = 0 [n]
    # we turn them into equation like t = a [n]
    equations = []
    for (i, bus_id) in buses:
        equations.append(((-i) % bus_id, bus_id))

    # The CRT (Chinese Remainders Theorem) states that there is a unique t satisfying all above equations
    N = math.prod([eq[1] for eq in equations])
    result = 0
    for (a, n) in equations[1:]:
        # N//n and n are prime so their GCD is 1 and the Euclide algorithm gives the modular inverse
        inverse = euclide_gcd_algo(N // n, n)[1]
        result += a * (N // n) * inverse
    return result % N


if __name__ == "__main__":
    print(solve(parse("data.txt")))
