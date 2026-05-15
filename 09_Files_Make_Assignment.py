# filename: 09_Files_Make_Assignment.py
"""
Assignment: Simple Journal

In this assignment, you will create a program that lets a user write journal
entries. Each new entry should be added to the end of a file called `journal.txt`.

Instructions:
1.  Ask the user for their journal entry for the day using `input()`.
2.  Open the file `journal.txt` in **append mode**. This is very important, as
    you don't want to erase previous entries.
3.  Write the user's entry to the file.
4.  Make sure to add a newline character `\n` after the entry so that the next
    entry will start on a new line.
5.  Close the file.
6.  Print a confirmation message to the user, like "Journal entry saved."

Run the program multiple times and enter different entries. Then, open the
`journal.txt` file in a text editor to see if all your entries were saved correctly.
"""

# --- YOUR CODE GOES BELOW ---

# 1. Ask the user for a journal entry
# This prompts the user to type their journal entry for the day and stores it in a variable.
journal_entry = input("What would you like to write in your journal today? ")

# 2. Open journal.txt in append mode
# The 'a' mode opens the file for appending, which adds new content to the end without erasing existing entries.
# We use a context manager (with statement) to automatically close the file when done.
with open("journal.txt", "a") as journal_file:
    
    # 3. Write the entry to the file (don't forget the newline character!)
    # This writes the user's journal entry to the file, followed by a newline character (\n).
    # The newline ensures that the next entry will start on a new line.
    journal_file.write(journal_entry + "\n")

# 4. The file is automatically closed by the 'with' statement (context manager)
# This is safer than manually calling close() as it happens even if an error occurs.

# 5. Print a confirmation message
# This provides feedback to the user confirming that their entry was successfully saved.
print("Journal entry saved.")

# --- END YOUR CODE ---
