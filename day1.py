# A a program that reads a text file, counts the number of lines, words, and characters, and prints the counts.
# Usage: python day1.py <filename>

with open("text.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
print(line_count, word_count, char_count)
