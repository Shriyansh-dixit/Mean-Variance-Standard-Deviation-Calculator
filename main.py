from mean_var_std import calculate

if __name__ == "__main__":
    try:
        # Prompt the user for input
        user_input = input("Enter 9 numbers separated by spaces: ")
        # Convert the input string into a list of integers
        input_list = list(map(int, user_input.split()))
        # Call the calculate function with the input list
        result = calculate(input_list)
        print(result)
    except ValueError as e:
        print(e)

