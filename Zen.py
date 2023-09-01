def number_to_word(n):
    """that takes an integer between 0 and 20 and returns the English word for that number"""
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
             "twenty"]
    return words[n]


with open("Zen.txt") as file:
    content = file.readlines()

# new_content initialize with first two lines of Zen.txt
new_content = content[:2]
for line_number, line in enumerate(content[2:], start=1):
    new_content.append(line.replace(number_to_word(line_number), str(line_number), 1))

with open("New_Zen.txt", "w") as file:
    file.writelines(new_content)
