from typing import Iterable, Any

from marshmallow import fields, Schema, validates_schema, ValidationError

VALID_CMD_PARAMS: Iterable[str] = (
    'filter',
    'sort',
    'map',
    'unique',
    'limit',
    'regex'
)


class RequestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values: dict[str, str], *args: Any, **kwargs: Any) -> dict[str, str]:
        if values['cmd1'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd1" contains invalid value')
        if values['cmd2'] not in VALID_CMD_PARAMS:
            raise ValidationError('"cmd2" contains invalid value')

        return values
