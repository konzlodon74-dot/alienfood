import os

ENTRY = "One star: your saucer parking is atrocious and locals keep photographing my tentacles, but your tacos alone justify the 400 light-year trip."

assert ENTRY.strip() == ENTRY and ENTRY, "entry must be non-blank with no padding"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY.endswith(".") and ENTRY.count(".") == 1, "entry must be exactly one sentence"
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(ENTRY.encode("utf-8"))
