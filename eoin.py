from subprocess import check_output


def system_time():
    """Returns the Time of the day"""
    output = check_output(["date"]).decode("utf-8").split()
    time = output[3]
    return time


def system_date():
    """Returns the date"""
    output = check_output(["date"]).decode("utf-8").split()
    date = output[2] + " " + output[1] + " " + output[5]
    return date

# print("The date is", (system_date()))
# print("The time is", system_time())
