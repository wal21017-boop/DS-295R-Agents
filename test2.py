from pathlib import Path

base = Path(r"C:\Users\brian\OneDrive\Desktop\Fall 2026")

matches = list(base.rglob("file_storage"))

print("Found folders:")
for match in matches:
    print(match)