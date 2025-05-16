from pysat.solvers import Minisat22

solver = Minisat22()

# Encoding for the formula: (x1 v x2) ∧ (¬x1 v ¬x3)
solver.add_clause([1, 2]) 
solver.add_clause([-1, -3]) 

is_sat = solver.solve()
print("SAT?" , is_sat)

if is_sat:
    model = solver.get_model()
    print("A satisfying assignment is:")
    print(model)

solver.delete()
