
Name: read_to_table
Purpose: reads information from a file to a table
Parameters: filename
Return: main_table
Algorithm
1. set main_table as empty string
2. open filename to read
   1. write information from file to main_table
   2. return main_table


Name: headlines_with_word
Purpose: output headlines which contain a specific user indicated word
Parameters: main_table
Return: N/A
Algorithm:
1. set headline_table to empty
2. ask user to enter the word they would like to use
3. set headline_word to user inputted word
4. for each row in table:
   1. if headline_word in row
      1. append row to headline_table
5. ask user to enter a file name to write to
6. open file
7. for row in write_table
   1. write row to file
8. close file
9. return



Name: long_or_short_headline
Purpose: outputs the longest or shortest headline as indicated by user
Parameters: main_table
Return: N/A
Algorithm:
1. set longest and shortest to empty
2. set long_headline and short_headline to empty
3. for row in table:
   1. concatenate row_length with len(row)
   2. if row_length is less than longest:
      1. equal longest to row_length
      2. equal long_headline to longest
   3. elif check if row_length is less than shortest
      1. equal shortest to row_length
      2. equal short_headline to shortest
4. output shortest and longest headline to user

Name: word_count
Purpose: count the number of titles that a specific user indicated word is in
Parameters: main_table
Return: N/A
Algorithm:
1. set count to 0
2. ask user to enter word they would like to see number of times used
3. for each row in table
   1. if word is in row:
      1. add 1 to count
4. output count to user

Name: avg_headline_characters
Purpose: output the average number of characters in a headline
Parameters: main_table
return: N/A
Algorithm:
1. set both row_length and total_length to 0
2. for each row in table:
   1. set row_length to the number of total characters in every row
   2. concatenate total_length and row_length
3. divide total_length by len(table) and equal the result to average_characters
4. output result to user
5. return

Name: error_check_file_name
Purpose: error check the user inputted file name
Parameters: N/A
Return: file
Algorithm:
1. ask user to input name of file, set as variable file
2. while file does not exist:
   1. ask user to re-enter a valid file name
   2. set as variable file
3. return file

Name: main
Purpose: main function
Parameters: N/A
Return: N/A
Algorithm:
1. set continue to y
2. output program explanation to user
3. call error_check_file_name
4. call read_to_table
5. while continue equals y:
   1. explain program options to user
   2. ask user to input what process they want done
   3. set user input to choice
   4. while choice is not 1-5:
      1. if choice equals 1:
         1. call word_word count with main_table as parameter
      2. if choice equals 2:
         1. call headlines_with_word with main_table as parameter
      3. if choice equals 3:
         1. call avg_headline_characters with main_table as parameter         
      4. if choice equals 4:
         1. call long_or_short_headline with main_table as parameter
      5. if choice equals 5:
         1. call error_check_file_name
         2. set as file_name
         3. call read_file_to_table
         4. set as main_table
      6. ask user if they wish to continue
      7. while continue does not equal y or n 
         1. ask user to input valid answer
6. output program ending 
