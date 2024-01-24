# task1


# with open("text1.txt", "r") as File1:
#     file1_lines = set(File1.readlines())

# with open("text2.txt", "r") as File2:
#     file2_lines = set(File2.readlines())

# different_lines1 = file1_lines - file2_lines
# different_lines2 = file2_lines - file1_lines

# if file1_lines == file2_lines:
#     print("Files are the same")
# else:
#     print("Files are different")

#     if different_lines1:
#         print("Lines unique to text1.txt:")
#         print("\n".join(different_lines1))

#     if different_lines2:
#         print("Lines unique to text2.txt:")
#         print("\n".join(different_lines2))


# --------------------------------------------------------------


# task2


# def calculate_statistics(input_file_path, output_file_path):
#     with open(input_file_path, "r", encoding="utf-8") as file1:
#         content = file1.read()
#         num_symbols = len(content)
#         num_lines = len(content.splitlines())
#         num_vowels = sum(1 for char in content if char.lower() in "aeiouаеёиоуыэюя")
#         num_consonants = sum(1 for char in content if char.isalpha() and char.lower() not in "aeiouаеёиоуыэюя")
#         num_digits = sum(1 for char in content if char.isdigit())
        
#         with open(output_file_path, 'w', encoding="utf-8") as file2:
#             file2.write(f"Number of characters: {num_symbols}\n")
#             file2.write(f"Number of lines: {num_lines}\n")
#             file2.write(f"Number of vowels: {num_vowels}\n")
#             file2.write(f"Number of consonants: {num_consonants}\n")
#             file2.write(f"Number of digits: {num_digits}\n")

# input_file_path = "text1.txt"
# output_file_path = "text2.txt"
# calculate_statistics(input_file_path, output_file_path)


# task3


# with open("text1.txt","r") as File1:
#     lines = File1.readlines()
#     lines.pop()     
    
    
# with open("text2.txt","w") as File2:
#     File2.writelines(lines)


# task4


# with open("text1.txt","r+") as File1:
#     lines = File1.readlines()
#     print(max(len(line) for line in lines) - 1)


# task5


# import re

# word = input("Enter the word: ")

# with open("text1.txt", "r") as File1:
#     content = File1.read()
#     words = re.findall(r'\b\w+\b', content)
#     print(words.count(word))


# task6


# search_word = input("Enter the word to search: ")
# replace_word = input("Enter the word to replace with: ")

# with open("text1.txt", "r") as file1:
#     content = file1.read()

# new_content = content.replace(search_word, replace_word)

# with open("text1.txt", "w") as file2:
#     file2.write(new_content)