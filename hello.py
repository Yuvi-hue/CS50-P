def main():
    name=str(input("Whats your name? "))
    hello(name)

def hello(to="world"):
    print(f"Hello {to}")

main()