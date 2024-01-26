g = input("Greeting: ").strip()

if g.startswith("Hello"):
    print("$0")
else:
    print(f"\$${20 if g[0].lower() == 'h' else 100}")
