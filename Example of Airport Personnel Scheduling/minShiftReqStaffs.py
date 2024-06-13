# Copyright (C)  2024 WeiRan Hi-Tech

# using CP-SAT solver
from ortools.sat.python import cp_model


def findMinCostShiftReqStaffs():
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    num_shifts = 5
    s = {}
    for j in range(num_shifts):
        s[j] = model.new_int_var(0, 99999, f"s[{j}]")

    slots = {
        0: [s[0], 48],
        1: [s[0] + s[1], 79],
        2: [s[0] + s[1], 65],
        3: [s[0] + s[1] + s[2], 87],
        4: [s[1] + s[2], 64],
        5: [s[2] + s[3], 73],
        6: [s[2] + s[3], 82],
        7: [s[3], 43],
        8: [s[3] + s[4], 52],
        9: [s[4], 15]
    }

    # Creates the constraints.
    for i in range(10):
        model.add(slots[i][0] >= slots[i][1])

    model.minimize(170 * s[0] + 160 * s[1] + 175 * s[2] + 180 * s[3] + 195 * s[4])

    # solves the model.
    status = solver.solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Minimum of objective function: {solver.objective_value}\n")
        for j in range(num_shifts):
            s[j] = solver.value(s[j])
            print(f"s[{j}] = {solver.value(s[j])}")
    else:
        print("No solution found.")
  
    print(f"  status   : {solver.status_name(status)}")
