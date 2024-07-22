import sys
import argparse
import re
import os
def get_word_count(file):
    # YOUR CODE GOES HERE
    content = str(file.read())
    # print(content)
    return len(content.split(' '))
    pass

def get_byte_count(file):
   # YOUR CODE GOES HERE
#    print(type(file.read1()))
   return os.path.getsize(file.name)
   pass

def get_line_count(file):
    # YOUR CODE GOES HERE
    count = 0
    for line in file:
        count+=1
    return count
    pass

def get_regex_count(file, pattern):
    # YOUR CODE GOES HERE
    return len(re.findall(pattern=pattern, string=str(file.read())))
    pass

def main():
    parser = argparse.ArgumentParser(description='Count words, lines, bytes, and regex matches in a file or from standard input.')
    parser.add_argument('-w', '--words', action='store_true', help='Count words')
    parser.add_argument('-c', '--bytes', action='store_true', help='Count bytes')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-r', '--regex', type=str, help='Count regex matches (provide pattern)')
    parser.add_argument('filename', nargs='?', type=str, help='File to process (default: standard input)')
    
    args = parser.parse_args()
    counts = {}
    if args.filename:
        with open(args.filename, 'rb') as file_stream:
            if args.words:
                counts['words'] = get_word_count(file_stream)
                file_stream.seek(0)  
            if args.lines:
                counts['lines'] = get_line_count(file_stream)
                file_stream.seek(0)  
            if args.regex:
                counts['regex'] = get_regex_count(file_stream, args.regex)
                file_stream.seek(0)
        if args.bytes:
            with open(args.filename, 'rb') as file_stream:
                counts['bytes'] = get_byte_count(file_stream)
                file_stream.seek(0)  
                
    filename = args.filename if args.filename else ""

    # Print the counts in the requested order
    if 'lines' in counts:
        print(counts['lines'], end='L ')
    if 'words' in counts:
        print(counts['words'], end='W ')
    if 'bytes' in counts:
        print(counts['bytes'], end='B ')
    if 'regex' in counts:
        print(counts['regex'], end='R ')

    if filename:
        print(filename)

if __name__ == "__main__":
    main()
