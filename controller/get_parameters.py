import yaml
import boto3

# Constructor to add support for tags to safe_load constructor


def any_constructor(loader, tag_suffix, node):
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_scalar(node)


yaml.add_multi_constructor('', any_constructor, Loader=yaml.SafeLoader)


def read_yaml_file(service_name):
    try:
        session = boto3.Session(profile_name='admin', region_name='us-east-1')

        s3 = session.client("s3")
        s3_object = s3.get_object(
            Bucket="cf-templates-poc-dev", Key=f"{service_name}/s3_bucket.yaml")
        parameters = yaml.safe_load(s3_object["Body"])
        return parameters['Parameters']

    except Exception as e:
        print(e)
        return f"Something went wrong--{e}"
