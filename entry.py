import os
import subprocess

print("Hello!")
print("Which script do you want to try?")

scripts = [
    {"Always one": "values-that-always-equal-to-one.py"}
]

for number, script in enumerate(scripts, 1):
    for name in script:
        print(f"{number}. {name}")

choice = int(input("Enter the number: "))

if 1 <= choice <= len(scripts):
    script = scripts[choice - 1]

    for name, filename in script.items():
        os.system("clear")
        subprocess.run(["python3", filename])
else:
    print("Invalid choice.")