import re

print("Yes" if bool(
    re.match(
        "(fou?rty ?-?two)|42", 
        input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    )) else "No")
