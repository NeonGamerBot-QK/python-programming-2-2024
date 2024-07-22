# Project 3: Implementing wc 

This Python script mimics the functionality of the Unix `wc` command, allowing you to count words, lines, bytes, and regex matches in a file.

## Description

The Unix `wc` (word count) command reads one or more input files and, by default, generates three columns of output for each file: the newline count, the word count, and the byte count. The `wc` command can also accept standard input if no files are provided.

This script provides similar functionality, with additional support for counting occurrences of a regex pattern.

## Features

- **Count Words**: Counts the number of words in the file.
- **Count Bytes**: Counts the number of bytes in the file (requires opening the file in binary mode).
- **Count Lines**: Counts the number of lines in the file.
- **Count Regex Matches**: Counts the number of matches for a given regex pattern in the file.

## Usage

To run the script, use the following command in your terminal:

```sh
python wordcount.py [options] filename
```

### Options

- `-w`, `--words`: Count words in the file.
- `-c`, `--bytes`: Count bytes in the file.
- `-l`, `--lines`: Count lines in the file.
- `-r`, `--regex PATTERN`: Count regex matches for the given pattern in the file.

### Example

```sh
python wordcount.py -w -c -l -r '\bthe\b' meditations.txt
```

### Functions to Implement

Students are required to implement the following functions:

- `get_word_count(file)`: Count the number of words in the file.
- `get_byte_count(file)`: Count the number of bytes in the file. **Note**: Open the file in binary mode to get the byte count.
- `get_line_count(file)`: Count the number of lines in the file.
- `get_regex_count(file, pattern)`: Count the number of matches for the given regex pattern in the file.

### Hints:
- Use `re` function `findall()` to implement `get_regex_count(file, pattern)`. 
