
from collections import defaultdict

def waterjug(amt1, amt2, jug1, jug2, aim, visited):
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True
    if visited[(amt1, amt2)]:
        return False
    visited[(amt1, amt2)] = True
    print(amt1, amt2)

    return (waterjug(0, amt2, jug1, jug2, aim, visited) or
            waterjug(amt1, 0, jug1, jug2, aim, visited) or
            waterjug(jug1, amt2, jug1, jug2, aim, visited) or
            waterjug(amt1, jug2, jug1, jug2, aim, visited) or
            waterjug(min(jug1, amt1 + amt2), amt1 + amt2 - min(jug1, amt1 + amt2), jug1, jug2, aim, visited) or
            waterjug(amt1 + amt2 - min(jug2, amt1 + amt2), min(jug2, amt1 + amt2), jug1, jug2, aim, visited))

def main():
    jug1 = int(input("Enter capacity of jug1: "))
    jug2 = int(input("Enter capacity of jug2: "))
    aim = int(input("Enter amount of water to be measured: "))
    visited = defaultdict(lambda: False)
    print("Steps:")
    if not waterjug(0, 0, jug1, jug2, aim, visited):
        print("No solution found")

if __name__ == "__main__":
    main()