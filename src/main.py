import sys
import pickle_interactions as pkl
import info_inputs as inp

from add_entry import add_entry
from delete_artist import delete_entry
from print_mdb import print_mdb
from query_mdb import query_mdb
from update_readme import update_readme
from update_table import update_table

def main(filepath):
    while True:
        content = input("What would you like to do?\n")
        match content.lower():
            case "help" | "?":
                print("""===Command List===
ad, add - Add an entry to the Database.
rm, remove - Remove an entry from the Database.
pr, print - Print the full Database. Use `query` for more precision.
qr, query - Find and edit an album entry.
up, update - Update project README.md.
ta, table - Generate album table.

end, '' - Exit this program.
Help, ? - Show this list.
===Command List===""")
            case "ad" | "add":
                add_entry(filepath)
            case "rm" | "remove":
                delete_entry(filepath)
            case "pr" | "print":
                print_mdb(filepath)
            case "qr" | "query":
                query_mdb(filepath)
            case "up" | "update":
                update_readme(filepath)
            case "ta" | "table":
                update_table(filepath)
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