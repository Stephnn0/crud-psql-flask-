from flask import Blueprint, jsonify, request
from services.ServiceRepository import get_all_notes_service, create_note_service, get_note_by_id_service, update_note_service, delete_note_service


notes_bp = Blueprint('notes', __name__)


@notes_bp.route('/api/v1/notes', methods=['GET'])
def get_notes():
    notes = get_all_notes_service()
    notes_list = [{'id': note.id, 'name': note.name, 'description': note.description} for note in notes]
    return jsonify({'notes': notes_list})



@notes_bp.route('/api/v1/notes', methods=['POST'])
def create_note_route():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({'error': 'Name and description are required'}), 400

    new_note_id = create_note_service(name, description)
    return jsonify({'message': 'Note created successfully', 'note_id': new_note_id})


@notes_bp.route('/api/v1/notes/<int:note_id>', methods=['GET'])
def get_note_by_id(note_id):
    note = get_note_by_id_service(note_id)
    if note:
        return jsonify({'note': {'id': note.id, 'name': note.name, 'description': note.description}})
    else:
        return jsonify({'error': 'Note not found'}), 404


@notes_bp.route('/api/v1/notes/<int:note_id>', methods=['PUT'])
def update_note_route(note_id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({'error': 'Name and description are required'}), 400

    existing_note = get_note_by_id_service(note_id)
    if existing_note:
        update_note_service(note_id, name, description)
        return jsonify({'message': 'Note updated successfully', 'note_id': note_id})
    else:
        return jsonify({'error': 'Note not found'}), 404


@notes_bp.route('/api/v1/notes/<int:note_id>', methods=['DELETE'])
def delete_note_route(note_id):
    existing_note = get_note_by_id_service(note_id)
    if existing_note:
        delete_note_service(note_id)
        return jsonify({'message': 'Note deleted successfully'})
    else:
        return jsonify({'error': 'Note not found'}), 404