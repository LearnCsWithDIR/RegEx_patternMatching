# Regular Expressions

# **Pattern Matching Algorithm**
This Python script implements various pattern matching algorithms to search for patterns in a given text file. It supports different pattern matching techniques such as Knuth-Morris-Pratt (KMP), dot (.) matching, question mark (?) matching, start (^) matching, and end ($) matching.

## Table of Contents
* *Introduction*  
* *Usage*  
* *Supported Pattern Matching Techniques*  
* *Input and Output*  
* *Examples*  

## Introduction
This script provides a versatile tool for searching patterns in a text file using various pattern matching algorithms. It's suitable for tasks where you need to locate specific patterns within a larger text document efficiently.

## Usage
Ensure you have Python installed on your system.
Place the text you want to search in the input.txt file.

Run the script using the following command:   
**python pattern_matching.py**

Follow the on-screen instructions to enter the pattern you want to search for.
The script will display the search results on the console and save them in the Output.txt file.

## Supported Pattern Matching Techniques
The script supports the following pattern matching techniques:

`Knuth-Morris-Pratt`: (KMP) algorithm. Normal string pattern matching algorithm.         
`Dot (.) matching`: Treats the dot as a wildcard character to match any character.        
`Question mark (?) matching`: Treats the question mark as an optional character.       
`Start (^) matching`: Searches for patterns at the start of a line or after a space character.  
`End ($) matching`: Searches for patterns at the end of a line or before the end of the file.
## Input and Output
The input text to be searched should be placed in the input.txt file.
The script will save the search results, including line numbers, indices search pattern and total match found strings, in the Output.txt file.

## Examples
Examples are included in code explanation report file.
