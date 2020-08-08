#Create an HTML List
#Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:

#<ul>
#<li>first string</li>
#<li>second string</li>
#</ul>
#That is, the string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items: # loops through the list of items
    html_str += "<li>{}</li>\n".format(item) # adds a new line to html_str
                                             # with the item inserted between <li> tags 
                                             # and \n ensure next item is on a new line 
html_str += "</ul>" # adds a closing "</ul>" tag to html_str.

print(html_str)
