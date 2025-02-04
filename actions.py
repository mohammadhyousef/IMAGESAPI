from flask import Blueprint,redirect, request, url_for, jsonify
from PIL import Image
from helpers import get_secure_filename_filepath

bp = Blueprint('actions', __name__, url_prefix='/actions')

@bp.route('/resize', methods=["POST"])
def resize():
    pass 
filename = request.json['filename']
filename, filepath = get_secure_filename_filepath (filename)

try:
    width, height = int(request.json['width']), int(request.json['height'])
    Image = Image.open(filepath)
    out = Image.resize((width, height))
    out.save(filepath)
    return redirect(url_for('download_file', name=filename))

except FileNotFoundError:
    return jsonify({'message': 'file not found'}), 404

@bp.route('/presets<presets>', methods=["POST"])
def resize_preset(preset):
    pass 

@bp.route('/rotate', methods=["POST"])
def rotate():
    pass 

@bp.route('/flip', methods=["POST"])
def flip():
    pass 

