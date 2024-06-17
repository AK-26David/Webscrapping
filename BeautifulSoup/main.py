from bs4 import BeautifulSoup  # Import BeautifulSoup class from bs4 module

# Open the HTML file named 'home.html' in read mode
with open('home.html', 'r') as html_file:
    content = html_file.read()  # Read the entire content of the file into 'content'

# Create a BeautifulSoup object from the HTML content using the built-in HTML parser
soup = BeautifulSoup(content, 'html.parser')

# Now you can use the 'soup' object to interact with the parsed HTML