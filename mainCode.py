# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import numpy as np

# ---------------------------------------------------------------------
# Defined prompts at the beginning of the program
#  -> make the code flexible if prompts or values changed changed
# ---------------------------------------------------------------------

prompts_enter_date= "Check how many days it's been since a date. Use the format: YYYY-MM-DD. "
error_message = "Incorrect format. Insert a date in format YYYY-MM-DD"
error_future_date = "Error. Data inputted cannot be a future date. Enter a past date"
# ---------------------------------------------------------------------
# FUNCTION: Read CSV data into Dataframe
# ---------------------------------------------------------------------


def date_time_calc():
    
    """

    Asks user to input a date and takes away from todays date

    Calculations
    ------------

    Calculate difference between user input and todays date
         - num_days = today - date_inputted 


    Returns
    -------

    num_days -> integer, the difference between the two days

    """

    today = np.datetime64('today')
   
    
    while True:

        user_input = input(prompts_enter_date)
        try:
            # Tests if user input can be converted to np.datetime64
            date_inputted = np.datetime64(user_input)
        except ValueError:
            # Users cant input values which aren't in the format YYYY-MM-DD 
            raise ValueError(error_message)                   
        if date_inputted > today:
            # Users can't input a value large than todays date
            raise ValueError(error_future_date)
        
        # Calculation
        num_days = today - date_inputted
    
        # Returns number of days to be printed
        return num_days

# runs 
if __name__ == "__main__":
    date_time_result= date_time_calc()  

    # Example usage
    print(f"Number of days: {date_time_result}")



