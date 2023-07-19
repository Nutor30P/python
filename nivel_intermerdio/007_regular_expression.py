## regular expresion ##

import re

my_string = "Let's write RegEx!"

pattern = r"\w+"

#findall() returns all non-overlapping matches of pattern in string, as a list of strings.

print(re.findall(pattern, my_string))

#match() checks for a match only at the beginning of the string, while search() checks for a match anywhere in the string.

print(re.match("let", my_string, re.IGNORECASE))

#search() checks for a match anywhere in the string.

print(re.search(r"RegEx", my_string))

#sub() returns a new string with all occurrences of the pattern replaced by the replacement string.

print(re.sub(r"RegEx", "regular expression", my_string))

#split() returns a list of substrings separated by the pattern.

print(re.split(r"!", my_string))

print(re.findall(r"\w+", my_string, re.IGNORECASE))

# Write a pattern to match sentence endings: sentence_endings

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


# Write a pattern to match sentence endings: sentence_endings

sentence_endings = r"[.?!]"

# Split my_string on sentence endings and print the result

print(re.split(sentence_endings, my_string))

# Find all capitalized words in my_string and print the result

capitalized_words = r"[A-Z]\w+"

print(re.findall(capitalized_words, my_string))

# Split my_string on spaces and print the result

spaces = r"\s+"

print(re.split(spaces, my_string))


#patrones personalizados

patter = r"[lL]et's|Expresiones"

print(re.findall(patter, my_string))


patter_new = r"[a-zA-Z]+"

print(re.findall(patter_new, my_string))



email = 'tony@tiremove_thisger.net'

m = re.search('remove_this', email)

print(m.start(), m.end())

print(email[:m.start()] + email[m.end():])

# Write a pattern to match sentence endings: sentence_endings