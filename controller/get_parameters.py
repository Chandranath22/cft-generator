import yaml

# Constructor to add support for tags to safe_load constructor


def any_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)


yaml.add_multi_constructor('', any_constructor, Loader=yaml.SafeLoader)


def read_yaml_file():
    with open('s3_bucket.yaml', 'r') as file:
        parameters = yaml.safe_load(file)
        return parameters['Parameters']
