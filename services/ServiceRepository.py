from repository.NoteRepository import get_all_notes, create_note, get_note_by_id, update_note, delete_note

def get_all_notes_service():
    return get_all_notes()

def get_note_by_id_service(note_id):
    return get_note_by_id(note_id)

def create_note_service(name, description):
    return create_note(name, description)

def update_note_service(note_id, name, description):
    update_note(note_id, name, description)

def delete_note_service(note_id):
    delete_note(note_id)