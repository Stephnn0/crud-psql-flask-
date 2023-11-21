import psycopg2

from models.Note import Note



def db_conn():
    return psycopg2.connect(database="postgres", host="localhost", user="stefanovitteri", password="", port="5432")




def get_all_notes():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM notescrud''')
    data = cur.fetchall()
    cur.close()
    conn.close()

    notes = [Note(id=note[0], name=note[1], description=note[2]) for note in data]
    return notes




def create_note(name, description):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO notescrud (name, description) VALUES (%s, %s) RETURNING id;''', (name, description))
    new_note_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return new_note_id


def get_note_by_id(note_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM notescrud WHERE id = %s''', (note_id,))
    note_data = cur.fetchone()
    cur.close()
    conn.close()

    if note_data:
        return Note(id=note_data[0], name=note_data[1], description=note_data[2])
    else:
        return None



def update_note(note_id, name, description):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''UPDATE notescrud SET name=%s, description=%s WHERE id=%s;''', (name, description, note_id))
    conn.commit()
    cur.close()
    conn.close()



def delete_note(note_id):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''DELETE FROM notescrud WHERE id = %s;''', (note_id,))
    conn.commit()
    cur.close()
    conn.close()