with open("Input/Letters/starting_letter.txt") as let:
    letter = let.read()
    with open("Input/Names/invited_names.txt") as nam:
        names = nam.readlines()
        for n in names:
            # Deleting the break space
            n = n.strip()
            with open(f"Output/ReadyToSend/letter_{n}.txt", "w") as written:
                written.write(letter.replace("[name]", n))


