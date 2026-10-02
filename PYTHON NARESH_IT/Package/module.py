module_content = '''
def greet(name):
      f"Hello, {name}! Welcome to my module." '''

with open('my_module.py', 'w') as f:
    f.write(module_content)

print("my_module.py created successfully!")