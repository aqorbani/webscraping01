import re

# string = """amirhossein@gmail.com
# javad330@yahoo.com
# milad@outlook.com"""
#
# string = """web scraping in python"""
#
# result = re.split(r" ", string, 1)
# result = re.sub(r"\w{6}$", "java", string)
# result = re.findall(r"^\w+@(\w+)\.\w{2,3}", string, re.MULTILINE)
# result = re.match(r"^\w{3}\s", string, re.MULTILINE)
#
# print(result)

number = re.compile(r"^(910|918)([0-9]{3})([0-9]{4})$", re.MULTILINE)

number_string = """95165
9105698565
9185698585"""

x = number.findall(number_string)

print(x)
