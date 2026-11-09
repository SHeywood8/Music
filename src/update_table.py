from mdb_classes import MusicDatabase
import pickle_interactions as pkl

def update_table(filepath = ''):
    mdb:MusicDatabase = pkl.load_mdb(filepath)
    if mdb == None:
        return

    with open('data/album_table.md', 'w') as f:
        f.write(mdb.to_md_table())
        f.close()
    print("Table successfully updated.")
    return