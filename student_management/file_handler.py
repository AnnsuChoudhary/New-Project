"""
FileHandler: handles reading/writing student records to a JSON file.
Isolates all file I/O so student_manager.py stays clean (modular design).
"""

import json
import os


class FileHandler:
    def __init__(self, filepath="data/students.json"):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists(self.filepath):
            self.save_data([])

    def load_data(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print(f"[Warning] Data file '{self.filepath}' was corrupted. Starting fresh.")
            return []

    def save_data(self, data):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"[Error] Could not save data: {e}")
