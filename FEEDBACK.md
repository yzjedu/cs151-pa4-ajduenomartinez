

- [PA 4 Feedback](#pa-4-feedback)
  - [Comments](#comments)
  - [Format / Design](#format--design)
  - [Correctness / Completeness](#correctness--completeness)
  - [Usability](#usability)
  - [Supporting Documents](#supporting-documents)
  - [Comments on the grading](#comments-on-the-grading)
  - [Grade:](#grade)
  - [Participation Grade:](#participation-grade)


## PA 4 Feedback


### Comments
| Result   | Description                                   |
|----------|-----------------------------------------------|
| **YES-**   | Intro comments complete/clear                 |
| **YES-**   | Function comments complete for each function  |
| **-NO**   | Appropriate in-line commentary                |

### Format / Design
| Result   | Description                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------|
| **YES-NO**   | Proper use of upper/lowercase                                                                          |
| **YES-NO**   | Correct use of whitespace                                                                              |
| **YES-NO**   | Appropriate variable names                                                                             |
| **YES-NO**   | A function for reading in file name until it exists. Uses `os.ispath.file` in Boolean expression       |
| **YES-NO**   | A function for reading file into a list of strings. Returns list.                                      |
| **YES-NO**   | Reading file function uses try/except correctly                                                        |
| **YES-NO**   | A function for user menu and error checking that valid value given                                     |
| **YES-NO**   | A function for each analysis task (4 total functions)                                                  |
| **YES-NO**   | Uses read file function and file name input function that already exist for option to read in new file |
| **YES-NO**   | File is only read at start or when new file is requested; all analysis is on list.                     |
| **YES-NO**   | No spaghetti code (inappropriate use of break, exit, etc)                                              |

### Correctness / Completeness
| Result   | Description                                                                                                |
|----------|------------------------------------------------------------------------------------------------------------|
| **YES-**   | Menu provided to user for choice with 5 expected choices only                                              |
| **YES-**   | Program continues running until user chooses to quit                                                       |
| **YES-**   | User chooses name of input file, which can be any file that exists (not just the ones originally provided) |
| **YES-**   | Reads in input file to create a list of strings                                                            |
| **YES-**   | Input file is closed before file reading function returns                                                  |
| **YES-**   | Correctly determines how many headlines have a particular word in it, and outputs to user                  |
| **YES-**   | Correctly determines headlines with a particular word                                                      |
| **YES-**   | User chooses name of output file for outputting headlines                                                  |
| **YES-**   | Correct headlines written to file, one headline per line                                                   |
| **-NO**   | Output file is closed when writing is complete                                                             |
| **YES-**   | Correctly determines average number of characters per headline and outputs to user                         |
| **YES-**   | Correctly determines either shortest or longest headline, and outputs headline                             |
| **YES-**   | If user chooses to analyze a new file, the list of data is overwritten with the new data                   |
| **YES-**   | Code follows final algorithm                                                                               |
| **YES-**   | No other logic errors                                                                                      |

### Usability
| Result   | Description                                               |
|----------|-----------------------------------------------------------|
| **YES-**   | Outputs purpose of program at start                       |
| **-NO**   | Menu is easy to read                                      |
| **-NO**   | It is clear what to type in when making choice from menu  |
| **YES-**   | Prompts for input are clear                               |
| **YES-**   | Output is well formatted                                  |

### Supporting Documents
| Result   | Description                                               |
|----------|-----------------------------------------------------------|
| **YES-NO**   | Algorithm                                                 |
| **YES-NO**   | Reflection                                                |


### Comments on the grading
- ` if (headline_word.lower() in str(cell).lower() for cell in row):` looks like writen by LLM
- `sum(len(row) for row in main_table) if len(main_table) > 0 else 0` another LLM written code
- `long_or_short_headline`: should return longest or shortest not print both
- If you prove to me that you have written this code, I can upgrade your grade to an E. 

### Grade: R

### Participation Grade: S
 - If participation grade is unsatisfactory check the `NO` in the documents sections