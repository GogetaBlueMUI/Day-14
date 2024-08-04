def format_string(template, values):
    return template.format(**values)
template = "Hello, {name}! You are {age} years old."
values = {"name": "Alice", "age": "30"}
formatted_string = format_string(template, values)
print(formatted_string) 
