import os
import json


JSON_CONTENT_VALID = (list, dict)


def get_is_file_exist(file_path):
    is_file_exist = os.path.exists(file_path)

    if is_file_exist:
        return True
    else:
        raise FileNotFoundError


def get_is_json_content_valid(content):
    is_content_valid = isinstance(content, JSON_CONTENT_VALID)

    if is_content_valid:
        return True
    else:
        raise ValueError


def create_json_file(file_name: str, content=None):
    with_content = get_is_json_content_valid(content)

    try:
        new_file = open(file_name, "x")

        if with_content:
            json_formatted_content = json.dumps(content)
            new_file.write(json_formatted_content)

        new_file.close()

    except ValueError as error:
        raise IOError("You can't create an empty contact") from error


def update_json_file(file_name: str, content=None, overwrite: bool = False):
    try:
        get_is_json_content_valid(content)

        file = open(file_name, "r")

        file_content = file.read()

        file_content_json = json.loads(file_content)

        file.close()

        get_is_json_content_valid(file_content_json)

        file_content_json.append(content)

        file_content_string = json.dumps(file_content_json)

        updatable_file = open(file_name, open_mode)

        updatable_file.write(file_content_string)

        updatable_file.close()

    except FileExistsError as error:
        raise IOError(
            f"File {file_name} already exist, please try again with a new name"
        ) from error
    except PermissionError as error:
        raise IOError(
            f"You don't have permissions to update the {file_name} file, please update your permissions and try again"
        ) from error
    except ValueError as error:
        raise IOError(
            f"The content you're tring to write into the file ${file_name} is not of type list or dict"
        ) from error


def read_json_file(file_path):
    try:
        get_is_file_exist(file_path)
        file = open(file_path)
        file_stream = file.read()
        file_content_json = json.loads(file_stream)
        print(file_content_json)

        return file_content_json

    except FileNotFoundError as error:
        raise IOError(f"File with path {file_path} doesn't exist") from error

    except PermissionError as error:
        raise IOError(f"You don't have permissions to read this file") from error
