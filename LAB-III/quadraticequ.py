import cmath
def solve_quadratic_eqn(a, b, c):
  d = cmath.sqrt(b**2-4*a*c)
  root1 = (-b + d) / (2 * a)
  root2 = (-b - d) / (2 * a)
  return (root1, root2)

print(solve_quadratic_eqn(1, -7, 12))