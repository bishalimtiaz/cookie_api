import uuid


def gen_pk_perm():
    return str(uuid.uuid4()).replace('-', '')
