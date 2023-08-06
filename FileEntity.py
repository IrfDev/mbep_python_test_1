import os

import file_manager


class Entity:
    def __init__(self, name):
        current_path = os.path.dirname(__file__)
        file_name = f"{name}.json"
        self.file_path = current_path + f"/{file_name}"

    def get_all(self):
        return file_manager.read_json_file(self.file_path)

    def save(self):
        dict_log = self.__dict__

        try:
            file_manager.get_is_file_exist(self.file_path)
            file_manager.update_json_file(self.file_path, dict_log, True)
        except FileNotFoundError:
            file_manager.create_json_file(self.file_path, [dict_log])

    def search_entities(self, key, value):
        all_entites: list = self.get_all()

        filtered_entities = [
            element
            for element in all_entites
            if element[key] == value or element[key].find(value) >= 0
        ]

        return filtered_entities

    def get_entity(self, key, value):
        filtered_contacts = self.search_entities(key, value)
        return filtered_contacts[0]

    def get_entities_count(self):
        all_entites: list = self.get_all()
        return all_entites.count()

    def update_entities(self, value):
        file_manager.update_json_file(value)

    def delete_entity_by_key(self, key, value):
        all_entites: list = self.get_all()

        filtered_entities = [
            element
            for element in all_entites
            if element[key] != value or element[key].find(value) == -1
        ]

        try:
            file_manager.update_json_file(self.file_path, filtered_entities)
        except:
            print("Something goes wrong deleting the contact")

    def get_entities_with_limit(self, limit=int):
        all_entities = self.get_all()

        return all_entities[0:limit]
