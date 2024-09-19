def print_name_in_star(name):
    # Define the star patterns for each letter
    star_patterns = {
        'A': ['  *  ', ' * * ', '*****', '*   *', '*   *'],
        'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'C': [' *** ', '*   *', '*    ', '*    ', ' *** '],
        'D': ['***  ', '*  * ', '*   *', '*  * ', '***  '],
        'E': ['*****', '*    ', '**** ', '*    ', '*****'],
        'F': ['*****', '*    ', '**** ', '*    ', '*    '],
        'G': [' *** ', '*    ', '* ***', '*   *', ' *** '],
        'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
        'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
        'J': ['  ***', '   * ', '   * ', '*  * ', ' **  '],
        'K': ['*  * ', '* *  ', '**   ', '* *  ', '*  * '],
        'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
        'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
        'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
        'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        'P': ['**** ', '*   *', '**** ', '*    ', '*    '],
        'Q': [' *** ', '*   *', '*   *', '*  **', ' *** '],
        'R': ['**** ', '*   *', '**** ', '*  * ', '*   *'],
        'S': [' ****', '*    ', ' *** ', '    *', '**** '],
        'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
        'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
        'V': ['*   *', '*   *', '*   *', ' * * ', '  *  '],
        'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
        'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
        'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
        'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
        ' ': ['     ', '     ', '     ', '     ', '     ']
    }

    # Iterate through each row of the star patterns and print the corresponding rows for each letter
    for row in range(5):  # There are 5 rows in each pattern
        for letter in name.upper():  # Convert the name to uppercase and iterate through each letter
            print(star_patterns[letter][row], end='  ')  # Print the row of the corresponding letter
        print()  # Move to the next line after printing all the rows for each letter

# Call the function with your name
print_name_in_star("Rutuja")
