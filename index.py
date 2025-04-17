def sort(width, height, length, mass):
    is_bulky = any(i >= 150 for i in [width, height, length]) or (width * height * length) >= 1000000
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"

    if is_bulky or is_heavy:
        return "SPECIAL"

    return "STANDARD"

assert sort(20, 50, 100, 15) == "STANDARD"
assert sort(100, 100, 100, 10) == "SPECIAL"
assert sort(200, 20, 20, 10) == "SPECIAL"
assert sort(50, 50, 50, 25) == "SPECIAL"
assert sort(200, 200, 200, 25) == "REJECTED"

print("All tests passed!")