# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Letters/starting_letter.txt") as let:
    letter = let.read()
    with open("Input/Names/invited_names.txt") as nam:
        names = nam.readlines()
        for n in names:
            # Deleting the break space
            n = n.strip()
            with open(f"Output/ReadyToSend/letter_{n}.txt", "w") as written:
                written.write(letter.replace("[name]", n))


