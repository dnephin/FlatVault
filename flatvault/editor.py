"""
 Edit a file.
"""
import getpass
import os
import os.path
import subprocess
import sys
import tempfile
from flatvault import crypt


def run_editor(tmp_filename):
    """Run the editor and wait for it to exit. If an exit code is set
    return False.
    """
    editor = os.environ.get('EDITOR')
    if not editor:
        raise SystemExit("$EDITOR must be set in environment.")
    try:
        subprocess.call([editor, tmp_filename])
    except OSError:
        raise SystemExit("Editor not found: %s" % editor)


def get_plaintext(filename, pass_key):
    try:
        with open(filename, 'r') as f:
            return crypt.decrypt(f.read(), pass_key)
    except IOError:
        return ""


def create_temp_file(source):
    tmp_file = tempfile.NamedTemporaryFile()
    print >> sys.stderr, "Using tempfile %s" % tmp_file.name
    tmp_file.write(source)
    tmp_file.flush()
    return tmp_file


def file_modified(tmp_file, prev_modified):
    """Return True if the file has been modified since prev_modified."""
    return os.path.getmtime(tmp_file.name) != prev_modified


def save_ciphertext(tmp_file, filename, pass_key):
    tmp_file.seek(0)
    ciphertext = crypt.encrypt(tmp_file.read(), pass_key)
    with open(filename, 'w') as f:
        f.write(ciphertext)


def edit_file(filename):
    """Decrypt, edit, and encrypt a file."""
    pass_key    = getpass.getpass()
    plaintext   = get_plaintext(filename, pass_key)
    tmp_file    = create_temp_file(plaintext)
    modified    = os.path.getmtime(tmp_file.name)

    run_editor(tmp_file.name)
    if not file_modified(tmp_file, modified):
        raise SystemExit("Cancelled: No changes.")

    new_pass = getpass.getpass("New Password ? ")
    save_key = new_pass or pass_key
    save_ciphertext(tmp_file, filename, save_key)
