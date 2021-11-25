import boto3

def get_secret_value(name, version=None):
    """Gets the value of a secret.

    Version (if defined) is used to retrieve a particular version of
    the secret.

    """
    secrets_client = boto3.client("secretsmanager")
    kwargs = {'SecretId': name}
    if version is not None:
        kwargs['VersionStage'] = version
    response = secrets_client.get_secret_value(**kwargs)
    return response