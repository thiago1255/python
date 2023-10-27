string = " a b c f g "
print(1, string)
string = string.strip()
print(2, string)
if "a" in string:
	print(3, "a")
if string.isdigit():
	integer = int(string)
	print(4, integer)
string = string.replace(" ", "")
print(5, string)
string += "hijk"
print(6, string)
string += "\nlmnop"
print(7, string)
string += "\nqrst"
print(8, string)
string = string.split("\n", 1)
print(9, type(string), string)
print(10, string[1])