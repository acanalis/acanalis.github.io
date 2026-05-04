def get_list_of_tools():
    return []  # empty — simulates a failed lookup

# Safe: iterating an empty list is fine
def safe():
    L = get_list_of_tools()
    for tool in L:
        print(f"we have a {tool}")
    print("(done, no crash)")

# Risky: indexing assumes at least one element
def risky():
    L = get_list_of_tools()
    first_tool = L[1]  # IndexError if list is empty
    print(f"The first tool is {first_tool}")

safe()
risky()

# Output:
# (done, no crash)
# Traceback (most recent call last):
#   ...
# IndexError: list index out of range
# (exit 1)
