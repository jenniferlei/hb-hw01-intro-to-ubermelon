# open text file and assign to log_file variable
log_file = open("um-server-01.txt")


# define sales reports function with log_file parameter
def sales_reports(log_file):
    # for each line in log_file
    for line in log_file:
        # update line variable to the right stripped version of line
        line = line.rstrip()
        # assign new variable day to the first three digits of line (first three characters of day)
        day = line[0:3]
        # if the day is Tuesday or "Tue", print the line
        if day == "Tue":
            print(line)


sales_reports(log_file)