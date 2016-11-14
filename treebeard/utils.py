import os


DICT = 'directory'
FILE = 'file'


def tree_to_dict(root_path):
    d = {'name': os.path.basename(root_path)}

    if os.path.isdir(root_path):
        d['type'] = DICT
        d['children'] = list()
        for element in os.listdir(root_path):
            d['children'].append(
                tree_to_dict(os.path.join(root_path, element)))
    else:
        d['type'] = FILE

    return d
