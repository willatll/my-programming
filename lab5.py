# Lecture 7: Lab 5 â€” Sensor List Builder and Calibrator
# I am using the dummy student ID you specified earlier:
#Student ID = 2585070
#d1 = 0
#d2 = 7
#k = (0 + 7) % 4 + 2 = 5
#shift = 0 - 7 = -7
#rows_keep = (0 % 2) + 2 = 2
#So all personalized outputs below use:
#k = 5
#shift = -7
#rows_keep = 2
#

def main():
    d1 = 0
    d2 = 7
    k = 5
    shift = -7
    rows_keep = 2

    readings = [10.5, 12.0, 9.5, 15.0]

    print("Original readings:", readings)

    if len(readings) > 0:
        print("First reading:", readings[0])
        print("Last reading:", readings[-1])
    else:
        print("The list is empty.")

    if len(readings) >= 4:
        print("Slice from index 1 to index 3:", readings[1:4])
    else:
        print("Not enough values for slice [1:4].")

    total = sum(readings)
    print("Sum of readings:", total)

    shifted = [x + shift for x in readings]
    scaled = [x * k for x in readings]
    zipped_sum = [a + b for a, b in zip(readings, shifted)]

    print("Shifted readings:", shifted)
    print("Scaled readings:", scaled)
    print("Element-wise sum of original and shifted:", zipped_sum)

    print("\nManual check for first 3 elements:")
    for i in range(2):
        print(f"Original={readings[i]}, Shifted={shifted[i]}, Scaled={scaled[i]}, ZipSum={zipped_sum[i]}")


if __name__ == "__main__":
    main()