from itertools import product


def and_operator(val1: bool, val2: bool) -> bool:
    return val1 and val2


def or_operator(val1: bool, val2: bool) -> bool:
    return val1 or val2


def not_operator(val: bool) -> bool:
    return not val


def eval_statement(statement: str, A: bool, B: bool, C: bool = None, D: bool = None) -> bool:
    local_vars = {'A': A, 'B': B, 'C': C, 'D': D}
    try:
        result = eval(statement, {"__builtins__": None}, local_vars)
        return result
    except:
        raise ValueError(f"Error evaluating the statement: {statement}")


def generate_truth_table(statement: str, variables: list):
    num_vars = len(variables)
    truth_combinations = list(product([False, True], repeat=num_vars))

    # Print header
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))

    # Eval
    for combination in truth_combinations:
        truth_values = dict(zip(variables, combination))
        result = eval_statement(statement, **truth_values)
        truth_row = " | ".join(str(val) for val in combination) + f" | {result}"
        print(truth_row)


if __name__ == "__main__":
    # Define the logical expression (Example: "A and (B or not C)")
    logical_statement = input("Enter your logical statement: ")

    variables = []
    if 'A' in logical_statement: variables.append('A')
    if 'B' in logical_statement: variables.append('B')
    if 'C' in logical_statement: variables.append('C')
    if 'D' in logical_statement: variables.append('D')

    if len(variables) == 0:
        print("No variables found in the statement.")
    else:
        generate_truth_table(logical_statement, variables)
