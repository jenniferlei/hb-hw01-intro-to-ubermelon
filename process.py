# open text file and assign to log_file variable
log_file = open("/home/hackbright/src/homework/hw1-intro-to-ubermelon/um-server-01.txt")


# define sales reports function with log_file parameter
def sales_reports(log_file):
    '''prints sales info for monday'''
    # for each line in log_file
    for line in log_file:
        # update line variable to the right stripped version of line
        line = line.rstrip()
        # assign new variable day to the first three digits of line (first three characters of day)
        day = line[0:3]
        # if the day is Monday or "Mon", print the line
        if day == "Mon":
            print(line)


# call sales_reports function
sales_reports(log_file)