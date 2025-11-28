# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import numpy as np


# ---------------------------------------------------------------------
# Defined prompts at the beginning of the program
#  -> make the code flexible if prompts or values changed changed
# ---------------------------------------------------------------------

prompts_enter_date= "Insert a date (YYYY-MM-DD):"
error_message = "Incorrect format. Insert a date in format YYYY-MM-DD"
# ---------------------------------------------------------------------
# FUNCTION: Read CSV data into Dataframe
# ---------------------------------------------------------------------


def date_time_calc():
    """
    Function which returns today - date_time_calc
    """
    today = np.datetime64('today')
   
    #only asks is no date inputted -> necessary for unit tests
    while True:
        user_input = input(prompts_enter_date)
        try:
            date_inputted = np.datetime64(user_input)
        except ValueError:
            raise ValueError(error_message)                   
        if date_inputted > today:
            raise ValueError(error_message)
        
        num_days = today - date_inputted
    
        return num_days



    # while True:
    #     try:
    #         first_day  = int(input(prompt_first_day))
    #     except ValueError: # Users can't input non-integers
    #         raise ValueError(f"{prompt_error_handling_week}")

    #     # Users can't input values that dont fall betwwen min_number and max number  
    #     if first_day < min_number_week_days or first_day > max_number_week_days:      
    #         raise ValueError(f"{prompt_error_handling_week}") 
        
    #     # Returned to be passed into calender_printer()  
    #     return first_day


#using xfill{2} using it so that users input values seperately maybe

if __name__ == "__main__":
    date_time_result= date_time_calc()  # calls function and asks for input
    print(f"Number of days: {date_time_result}")



