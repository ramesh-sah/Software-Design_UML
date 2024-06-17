import os



def main():
    """
    This function is the main entry point of the program.
    It prints a welcome message and the current working directory.

    Parameters:
         None



    Returns:
    """_summary_



    
    """    None
    """ 
   

     


if __name__ == "__main__":
    """
    The __name__ variable is a built-in Python variable.
    It holds the name of the current module.
    When the Python interpreter reads a source file, it executes all of the code found in it.
    Before executing the code, it defines a few special variables.
    For example, if the Python interpreter is running the module (the source file) as the main program,
    it sets the special __name__ variable to have a value "__main__".
    If this file is being imported from another module, __name__ will be set to the module's name.
    """
    print("Welcome to the Sequence Diagram Generator!")
    print(f"The current working directory is: {os.getcwd()}")
    