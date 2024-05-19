v7 = [168, 193, 122, 172, 158, 108, 206, 153, 175, 175, 194, 189, 141, 127, 101, 202, 208, 116, 149, 160, 146, 179, 114, 143, 187, 159, 126, 109, 174, 156, 185, 120, 164, 189, 112, 120, 123, 145]
v8 = [53, 87, 22, 73, 48, 1, 91, 53, 58, 62, 89, 74, 35, 28, 1, 92, 99, 17, 41, 45, 29, 79, 10, 44, 68, 58, 11, 12, 72, 38, 83, 2, 67, 74, 12, 5, 23, 45]

#Initialize an empty list for the main part of the key
key_main_part = []

#Generate the 38-character main part of the key
for i in range(38):
    key_main_part.append(chr(v7[i] - v8[i]))

#Convert the list of characters to a string
key_main_part_str = ''.join(key_main_part)

#Form the full key
full_key = "FUSec{" + key_main_part_str + "}"

print("The correct license key is:", full_key)