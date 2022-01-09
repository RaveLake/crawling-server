import inspect
from typing import List


def get_or_create(session, _instance, **kwargs):
    instance = session.query(_instance.__class__).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        session.add(_instance)
        return _instance, True


def fetch_entities(entities: List[object]):
    return [fetch_entity(entity) for entity in entities]


def fetch_entity(entity: object):
    expected = set(inspect.getfullargspec(entity.__class__.__init__).args)
    fields = entity.__dict__.copy()
    for k in entity.__dict__:
        if k not in expected:
            del fields[k]
    return entity.__class__(**fields)
