from subprocess import check_output

def users():
    """Returns the number of system users as an integer."""
    output = check_output(["uptime"]).decode("utf-8").split()
    number = int(output[-7])
    return number

def load():
    """Returns the system load for the last 15 minutes as a float."""
    output = check_output(["uptime"]).decode("utf-8").split()
    number = float(output[-1])
    return number

# Test output
print(users(), "users")
print(load(), "system load")
