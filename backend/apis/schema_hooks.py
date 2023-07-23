import os
import logging


logging.basicConfig(level=os.getenv("LOGLEVEL", "WARNING").upper())


def fix_auth_request_body(result, generator, request, public):
    for path, data in result["paths"].items():
        path: str

        if not path.startswith("/api/auth-service/api-token"):
            continue

        for method, methodData in data.items():
            logging.info(f'Fixing method "{method}" for "{path}"')

            methodData["requestBody"]["content"] = {
                "application/json": methodData["requestBody"]["content"][
                    "application/json"
                ]
            }

    return result


def fix_enum_varnames(result, generator, request, public):
    from django.utils.text import slugify

    for schema_name, schema_data in result["components"]["schemas"].items():
        schema_name: str

        if not schema_name.endswith("Enum"):
            continue
        elif schema_name == "NullEnum":
            continue

        desc: str = schema_data.get("description", "")
        enum_varnames = []
        for enum_str in desc.splitlines():
            varname = enum_str.split("` - ").pop()
            varname = slugify('enum_' + varname).upper().replace("-", "_")
            enum_varnames.append(varname)

        logging.info(f"Mapping {len(enum_varnames)} enums for {schema_name}")
        schema_data["x-enum-varnames"] = enum_varnames

    return result
