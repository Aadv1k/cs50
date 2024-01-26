print("snake_case:",
      "".join(["_" + i.lower() if i.isupper()
               else i for i in str(input("camelCase: "))])
      )
