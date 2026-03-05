import sys

# sys.argv is a list of arguments passed to the script from the terminal
# e.g., if you run: python script.py data.csv
print(f"Script name: {sys.argv[0]}")

# Exiting a program prematurely
if len(sys.argv) < 2:
    print("Error: Not enough arguments provided.")
    sys.exit(1) # Stops the script immediately with an error code


print(sys.platform)
print(sys.version)



print("Python is currently looking for modules in these folders:")
for folder in sys.path:
    print(folder)
