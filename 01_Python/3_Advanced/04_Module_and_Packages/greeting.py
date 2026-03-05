def greeting(name):
    print(f"hello {name}!!")



# We only want this test to run if we execute greetings.py directly.
# We DO NOT want this to print if another file imports say_hello.
if __name__ == "__main__":
    print("Run Only if the greetin.py is directly run using python greeeting.py")
    greeting("Manas")



# If we import greetings in another file, the say_hello("Manas") test won't run because __name__ will not equal "__main__".