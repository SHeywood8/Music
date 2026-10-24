import sys
import pickle_interactions as pkl
import info_inputs as inp

from add_entry import add_entry
from delete_artist import delete_artist
from print_mdb import print_mdb

def main(filepath):
    while True:
        content = input("What would you like to do?\n")
        match content.lower():
            case "help" | "?":
                print("""===Command List===
ad, add - Add an entry to the Database.
rm, remove - Remove an entry from the Database.
pr, print - Print the full Database. Use `query` for more precision.

end, '' - Exit this program.
Help, ? - Show this list.
===Command List===""")
            case "ad" | "add":
                add_entry(filepath)
            case "rm" | "remove":
                return NotImplementedError
            case "pr" | "print":
                print_mdb(filepath)
            case "end" | '':
                return
            case _:
                print(f"Command {content} not found. Type 'Help' or '?' for list of commands.")

if __name__ == "__main__":
    args = sys.argv
    try:
        filepath = args[1]
    except:
        filepath = ''
        print("File path not found or not included. Using default file path.")
    main(filepath)