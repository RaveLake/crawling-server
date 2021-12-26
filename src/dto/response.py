from flask import Response

from src.util.json_stub import get_json_from_dataclass


def get_200_response(o: object):
    return Response(
        response=get_json_from_dataclass(o),
        status=200,
        headers={'content-type': 'application/json'}
    )
