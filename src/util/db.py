
def get_or_create(session, _instance, **kwargs):
    instance = session.query(_instance.__class__).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        session.add(_instance)
        return _instance, True
