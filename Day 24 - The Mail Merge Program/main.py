# file = open("my_file.txt")
# contents = file.read()
# print(contents)
#
# file.close()

# reading
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# # modes: write: w, read: r, append: a
#
# # writing
# with open("my_file.txt", mode="w") as file:
#     file.write("New Text")
#
# # Appending
# with open("my_file.txt", mode="a") as file:
#     file.write("\nI love appending")
#
# # writing to a file that doesn't exist
# with open("my_new_file.txt", mode="w") as file:
#     file.write("New Text")

with open("Input/Names/invited_names.txt", "r") as f:
    for a in f.readlines():
        receiver = a.strip()
        # print(receiver)
        with open('Input/Letters/starting_letter.txt') as h:
            starting_letter = h.read()
            final_letter = starting_letter.replace('[name]', receiver).replace('Angela', 'Chimezie')
            # final_letter = starting_letter
            # print(final_letter)
            final_path = 'Output/ReadyToSend/' + receiver
            with open(final_path, mode='w') as j:
                j.write(final_letter)



