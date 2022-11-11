import re

# # =============== Metacharacters =================
# # "A RegEx, or Regular Expression"
#
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)
#
# # Find all lower case characters alphabetically between "a" and "m":  [] A set of characters
# x = re.findall("[a-m]", txt)
# print(x)
#
# # Find all digit characters: \ Signals a special sequence
# txt = "Takashi 69's cell number 567"
# x = re.findall("\d", txt)
# print(x)
#
# txt = "hello planet"
# # Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# # . Any character (except newline character)
# x = re.findall("he..o", txt)
# print(x)
#
# txt = "Samir help! hello!! "
# # Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
# # * Zero(0) or more occurrences
# x = re.findall("he.*o", txt)
# print(x)
#
# # Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
# # + One(1) or more occurrences
# x = re.findall("he.+o", txt)
# print(x)
#
# # Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
# # ? Zero(0) or one(1) occurrences
# x = re.findall("he.?o", txt)
# # This time we got no match, because there were not zero, not one, but two characters between "he" and the "o
# print(x)
#
# # Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
# # {} Exactly the specified number of occurrences
# x = re.findall("he.{2}o", txt)
# print(x)
#
# txt = "The rain in Spain falls mainly in the plain!"
#
# # Check if the string contains either "falls" or "stays":
# # | Either or
# x = re.findall("falls|stays", txt)
# print(x)
# if x:
#     print("Yes, there is at least one match!")
# else:
#     print("No match")
#
# # ==================================re Special Sequences =================================
# txt = "The rain in Spain"
# # Check if the string starts with "The": \A
# x = re.findall("\AThe", txt)
# print(x)
# y = re.search("^The", txt)
# print(y)
# if x:
#     print("Yes, there is a match!")
# else:
#     print("No match")
#
# txt = "The rain in Spain"
# # Check if "ain" is present at the beginning of a WORD: \b___
# x = re.findall(r"\bain", txt)
# print(x)
# # Check if "ain" is present at the end of a WORD: ___\b
# x = re.findall(r"ain\b", txt)
# print(x)

# txt = "The rain in Spain"
# # Check if "ain" is present, but NOT at the beginning of a word: \B___
# x = re.findall(r"\Bain", txt)
# print(x)
# txt = "The rain in Spain"
# # Check if "ain" is present, but NOT at the End of a word: \B___
# x = re.findall(r"ain\B", txt)
# print(x)

# txt = "Takashi 69's cell number 567"
# # Check if the string contains any digits (numbers from 0-9): \d
# x = re.findall("\d", txt)
# print(x)
#
# txt = "The rain in Spain page 2"
# # Return a match at every no-digit character:
# x = re.findall("\D", txt)
# print(x)

# txt = "The rain in Spain"
# # Return a match at every white-space character: \s
# x = re.findall("\s", txt)
# print(x)
#
# # Return a match at every NON white-space character: \S
# x = re.findall("\S", txt)
# print(x)

# txt = "The rain in Spain"  # \w
# # Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
# x = re.findall("\w", txt)
# print(x)
#
# txt = "The rain in Spain!"  # \W
# # Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
# x = re.findall("\W", txt)
# print(x)
#
# txt = "The rain in Spain"
# # Check if the string ends with "Spain": \Z
# x = re.findall("Spain\Z", txt)
# print(x)

'''
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string'''

# # ================================== function() ==================================
'''
findall	    Returns a * list * containing all matches
search	    Returns a Match object if there is a match * anywhere * in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
'''

# # ================================== Use ==================================
# # Return a list containing every occurrence of "ai":
# txt = "The rain in Spain"
# x = re.findall(r"ai", txt)
# print(x)

# txt = "There is rain in Spain"
# x = re.search("\s", txt)
# print(x)
# print("The first white-space character is located in position:", x.start())  # Special Use******

# txt = "The rain in Spain"
# # Split at each white-space character:
# x = re.split("\s", txt)
# print(x)

# #Replace all white-space characters with the digit "9":
#
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)
# # Replace the first 2 occurrences:
# x = re.sub("\s", "9", txt, 2)
# print(x)

x="As we all know, a paragraph is a group of sentences that are connected and makes absolute sense. While writing a long essay or letter, we break them into paragraphs for better understanding, and to make a well-structured writing piece. Paragraph writing on any topic is not only about expressing your thoughts on the given topic, but it is also about framing ideas about the topic and making it convenient for the readers to follow it. In English paragraph writing, it is essential to focus on the writing style, i.e., the flow and connection between the sentences.Therefore, a paragraph must be written in simple language in order to avoid any interruption while reading. In order to write a paragraph on any topic, you can refer to the samples given below, and write a paragraph without any hindrance."

value=re.compile(r"l{2}")
matchs=value.finditer(x)  # finditer()************** is the Best all in one
y=value.findall(x)
print(y)
for match in matchs:
    print(match)

