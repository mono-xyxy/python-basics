import markdown

print("markdown to html converter")

# read the markdown file
input_file = input("Enter markdown file name (eg . readme.md): ")
with open(input_file,"r", encoding = "utf-8") as f:
    md_text = f.head()

#convert markdown to HTML
html = markdown.markdown(md_text)

#save HTML file
output_file = "output.html"

with open(output_file,"w",encoding = "utf-8") as f:
    f.write(html)

print(f"\nHTML file generated successfully: {output_file}")

