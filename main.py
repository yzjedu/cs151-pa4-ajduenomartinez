# Programmer: Antonio Dueno
# Course:  CS151, Zelalem Yalew
# Due Date: 11/21/24
# Programming Assignment:  PA 4
# Problem Statement: Create a program to analyze headlines from ABC
# Data In: file name, decision on what function to call
# Data Out: number of times word is in a headline, headlines containing specific word,
#           average characters per headline, longest and shortest headline
# Credits: class discussion of tables and reading and writing to files
# Input Files: 2014.txt, 2015.txt, 2016.txt, 2017.txt, 2018.txt, 2019.txt

import os

# name: read_to_table
# parameters: filename
# return: main_table
def read_to_table(filename):
    main_table = []
    try:
        file = open(filename, "r")
        for line in file:
            row = line.strip().split(",")
            main_table.append(row)
        file.close()
    except FileNotFoundError:
        print(f"The file you entered does not exist")
        main_table = []
    return main_table


# name: headlines_with_word
# parameters: main_table
# return: none
def headlines_with_word(main_table):
    headline_table = []
    headline_word = input("please input a word to find in headlines: ").strip()
    for row in main_table:
        if (headline_word.lower() in str(cell).lower() for cell in row):
            headline_table.append(row)
    output_file_name = input("enter a file to write to: ").strip()
    try:
        file = open(output_file_name, "w")
        for row in headline_table:
            file.write(",".join(str(cell) for cell in row) + "\n")
        file.close()
        print(f"'{headline_word}' have been written to '{output_file_name}'")
    except FileNotFoundError:
        print("The file you entered does not exist")
    return

# name: long_or_short_headline
# parameters: main_table
# return: none
def long_or_short_headline(main_table):
    longest = 0
    shortest = 100000
    long_headline = ""
    short_headline = ""
    for row in main_table:
        for headline in row:
            row_length = len(headline)
            if row_length > longest:
                longest = row_length
                long_headline = headline
            if row_length < shortest:
                shortest = row_length
                short_headline = headline
    print(f"the longest headline is: \"{long_headline}\" (Length: {longest})")
    print(f"the shortest headline is: \"{short_headline}\" (Length: {shortest})")

# name: word_count
# parameters: main_table
# return: none
def word_count (main_table):
    count = 0
    search_word = input("enter a word you would like to search for: ").strip()
    for row in main_table:
        title = row[0]
        if search_word.lower() in title.lower():
            count += 1
    print(f"The word '{search_word}' appears in headlines {count} times.")

# name: avg_headline_characters
# parameters: main_table
# return: none
def avg_headline_characters(main_table):
    total_length = 0
    for row in main_table:
        for headline in row:
            row_length = len(headline)
            total_length += row_length
    average_characters = total_length / sum(len(row) for row in main_table) if len(main_table) > 0 else 0
    print(f"The average number of characters in all the headlines in this file are: {average_characters:.2f}")

# name: error_check_file_name
# parameters: main_function
# return: file
def error_check_file_name():
    file = input("Enter the name of the file: ").strip()
    while not os.path.isfile(file):
        print("The file does not exist. Please enter a valid file name.")
        file = input("Enter the name of the file: ").strip()
    return file

# name: main
# parameters: none
# return: none
def main():
    continue_program = 'y'
    print("Hello! this program will ask you to input the name of one of the files containing headlines provided,\n and will"
          "then allow you to run several analysis on the headlines included in that file.")
    file_name = error_check_file_name()
    main_table = read_to_table(file_name)
    while continue_program == 'y':
        print("For this program, you have five options: 1. Search for the number of times a word appears\n in all the headlines,"
              "2. Display headlines which contain a specified word, 3. Display the average\n length of a headline, 4. display what"
              "the shortest and longest headlines are,\n and 5. Enter a different file to perform different analysis on.")
        choice = input("Enter your choice (1-5): ")
        while choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a number between 1 and 5.")
            choice = input("Enter your choice (1-5): ")
        if choice == '1':
            word_count(main_table)
        elif choice == '2':
            headlines_with_word(main_table)
        elif choice == '3':
            avg_headline_characters(main_table)
        elif choice == '4':
            long_or_short_headline(main_table)
        elif choice == '5':
            file_name = error_check_file_name()
            main_table = read_to_table(file_name)
        continue_program = input("Would you like to continue? (y/n): ").lower()
        while continue_program not in ['y', 'n']:
            continue_program = input("Invalid answer. Please enter 'y' to continue or 'n' to exit: ").lower()
    print("Thank you for using this program. Bye!")
    exit()

main()

