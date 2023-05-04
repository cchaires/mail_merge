# Letter Creator

This script creates a letter for each name in the "invited_names.txt" file by replacing the placeholder "[name]" with the actual name and saving the resulting letters in the "ReadyToSend" folder.

## How to Use

1. Make sure you have the following files in the correct directories:
   - A starting letter file with the placeholder "[name]" that will be replaced (e.g., "starting_letter.txt") in the "Input/Letters" directory.
   - A file with the list of names (e.g., "invited_names.txt") in the "Input/Names" directory.

2. Run the script.

3. Check the "Output/ReadyToSend" directory for the generated letters, each one named "letter_[name].txt", where [name] is the actual name from the list.

## Dependencies

- None

## Important Notes

- Make sure to replace the placeholder "[name]" in the starting letter file with the exact string you want to replace it with.
