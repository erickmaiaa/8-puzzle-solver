from pysat.solvers import Glucose3

g = Glucose3()

# Cláusulas existentes
g.add_clause([-1, 2, 3, 4, 5, 6])
g.add_clause([-2, 3, 5])

# Novas cláusulas
g.add_clause([-1, -2, -3])  # ¬p1 ∨ ¬p2 ∨ ¬p3
g.add_clause([2, -4])       # p2 ∨ ¬p4
g.add_clause([3, -4])       # p3 ∨ ¬p4
g.add_clause([4, -5, -6])   # p4 ∨ ¬p5 ∨ ¬p6
g.add_clause([5, -7])       # p5 ∨ ¬p7
g.add_clause([6, -7])       # p6 ∨ ¬p7
g.add_clause([4, 1])        # p4 ∨ p1

# Resolver e imprimir o resultado
print(g.solve())
print(g.get_model())