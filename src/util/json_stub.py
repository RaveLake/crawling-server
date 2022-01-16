import dataclasses
import json


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


def get_json_from_dataclass(o: object):
    return json.dumps(o, cls=EnhancedJSONEncoder)
