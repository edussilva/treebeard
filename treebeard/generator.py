import json

from treebeard.utils import tree_to_dict


def generate_json(root_path):

    with open('{}.json'.format(root_path), 'w') as f:
        json.dump(tree_to_dict(root_path), f)

    return f
