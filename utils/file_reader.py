
def read_sql(path):
    with open(path,"r") as file:
        return file.read()
    
    # with is used becaus python automatically closes the file after reading
    # file.read reads the file and return query in the form of string
    # and after file colon : is present its syntax it used with :- with ,for if class etc
    # file.read() this reads the files and returns sql query in string format  to the function