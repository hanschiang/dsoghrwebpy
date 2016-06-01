import markdown

text_file = open('mdtest.txt')
markdown_text_file = text_file.read()

html = markdown.markdown(markdown_text_file)

output_file = open("some_file.html", "w") 
output_file.write(html)
