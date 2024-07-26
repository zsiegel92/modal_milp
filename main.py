import modal
import pyomo.environ as pyo

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("coinor-cbc")
    .pip_install_from_requirements("requirements.txt")
)

app = modal.App(
    "cbc-on-modal",
    image=image,
)


@app.function()
def solve_knapsack(knapsack_size: int):
    """
    Knapsack problem from page 3 of [these intro OR lecture notes](https://www.math.clemson.edu/~mjs/courses/mthsc.440/integer.pdf)
    """
    model = pyo.ConcreteModel()
    indices = list(range(4))
    model.x = pyo.Var(indices, domain=pyo.Binary)
    objective_coefficients = [8, 11, 6, 4]
    model.obj = pyo.Objective(
        expr=sum(coef * model.x[i] for i, coef in zip(indices, objective_coefficients)),  # type: ignore
        sense=pyo.maximize,
    )
    constraint_coefficients = [5, 7, 4, 3]
    model.constraint = pyo.Constraint(
        expr=sum(
            coef * model.x[i] for i, coef in zip(indices, constraint_coefficients)  # type: ignore
        )
        <= knapsack_size
    )
    solver = pyo.SolverFactory("cbc")
    print("Calling numerical solver")
    result = solver.solve(model)
    print("Numerical solver done!")
    x_values: list[float] = [pyo.value(model.x[i]) for i in indices]  # type: ignore
    objective_result = sum(
        coef * x_val for coef, x_val in zip(objective_coefficients, x_values)
    )
    print(
        f"""
With a knapsack size of {knapsack_size}
We achieve an objective value of {objective_result} with values
{", ".join(f"x{i+1}={x_values[i]}" for i in range(len(x_values)))}
Problem description:
{result["Problem"]}
Solution description:
{result["Solver"]}
    """
    )
    return objective_result, result, x_values


# python -m modal run main.py
@app.local_entrypoint()
def main():
    knapsack_size = 14
    objective_result, result, x_values = solve_knapsack.remote(knapsack_size)

    # Solve many knapsack problems concurrently!
    knapsack_sizes = list(range(25))
    solutions = list(solve_knapsack.map(knapsack_sizes))
    for knapsack_size, (objective_result, result, x_values) in zip(
        knapsack_sizes, solutions
    ):
      print(f'With a knapsack size of {knapsack_size} We achieve an objective value of {objective_result}.')  