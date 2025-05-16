from z3 import Int, Solver, sat

x = Int('x')
y = Int('y')

solver = Solver()
solver.add(x + y == 5)
solver.add(x <= 3)
solver.add(y >= 6)

if solver.check() == sat:
    model = solver.model()
    print("Solution:")
    print("x =", model[x])
    print("y =", model[y])
else:
    print("No solution")
