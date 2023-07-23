from rest_framework.fields import ChoiceField as _ChoiceField
from typing import Any, Optional
import json


class ChoiceField(_ChoiceField):
    """A custom 'ChoiceField' that accepts and renders a human-friendly
    label.

    Example:
        Let's say we have the following choices:
        >>> GENDER_CHOICES = ((1, 'Male'), (2, 'Female'))

        In this case your payload should use either 'Male' or 'Female'
        instead of 1 or 2, as shown below:
        >>> {
        >>>     ...
        >>>     'gender': 'Female',
        >>>     ...
        >>> }
    """

    def to_internal_value(self, data: Any) -> Optional[str]:
        result = None

        if data == '' and self.allow_blank:
            result = ''

        for key, label in self.choices.items():
            if str(data) == label:
                result = key
                break

        if result is None:
            self.fail('invalid_choice', input=data)

        return result

    def to_representation(self, value: Any) -> Optional[str]:
        result = None
        if value in ('', None):
            result = value

        if isinstance(value, str):
            result = []
            data_list = json.loads(value)
            for data in data_list:
                for key, label in self.choices.items():
                    if data == key:
                        result.append(label)
                        break
        else:
            for key, label in self.choices.items():
                if key == value:
                    result = label
                    break

        return result
