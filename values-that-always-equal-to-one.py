import time

while True:
    # Get values
    x1 = float(input("x1, Give me one number. "))
    x2 = float(input("x2, Give me another. "))
    z1 = float(input("z1, One more. "))
    z2 = float(input("z2, One last one. "))

    if 0 in {x1, x2, z1,z2}:
        print("You can't do that. Divide by zero?")
        print("")
        continue

    # Calculate values
    x = x1 + x2
    z = z1 + z2
    xz = x + z
    xxz = x / xz
    zxz = z / xz
    result = zxz + xxz

    # Tell the user about it!
    print(f"If I take x1 and x2 and plus them, I get {x}")
    time.sleep(3)
    print(f"Then, z1 and z2 make {z}")
    time.sleep(3)
    print(f"I plus those. Then I get {xz}")
    time.sleep(3)
    print("Then, weird stuff starts happening.")
    time.sleep(3)
    print(f"If I divide, say x with xz, I get xxz. That's {xxz}")
    time.sleep(3)
    print(f"The same goes for z + xz. zxz = {zxz}")
    time.sleep(3)
    print("At last. You get zxz + xxz. This gives a value close to one.")
    time.sleep(2)
    print("And that is:")
    time.sleep(1)
    print(result)

    break 