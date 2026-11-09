from mdb_classes import MusicDatabase
import pickle_interactions as pkl

def update_readme(filepath = ''):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

    with open('README.md', 'w') as f:
        f.write(mdb.to_html())
        f.close()
    print("README.md successfully updated.")
    return

if __name__ == "__main__":
    update_readme()