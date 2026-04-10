filename = "numbers.txt"
filepath = "/.../data-heroes/python/wyjatki_obsluga_plikow/numbers.txt"
sum = 0

try:
    with open(filepath, "r", encoding="utf-8") as file:
        print(f"Open file: {filename}")
        lines = file.readlines()
        print(lines)

        for line in lines:
            try:
                value = int(line.strip())
                print(value)
                sum += value
            except ValueError:
                print(f"wrong line {line}")
except FileNotFoundError:
    print("no such file!")
else:
    print(f"Sum of values: {sum}")
finally:
    print("process ended")
