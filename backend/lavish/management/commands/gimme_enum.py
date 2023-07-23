from pathlib import Path
from re import sub

from django.core.management.base import BaseCommand
from django.utils.module_loading import import_string
from django.utils.text import slugify
from lavish.settings import BASE_DIR


# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-96.php
def camel_case(s):
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return "".join([s[0].lower(), s[1:]])


class Command(BaseCommand):
    """
    carbon: because i too can get tired of copy pasting variables from the backend
    """
    help = "Create the dumb enums for the dumb frontend"

    def add_arguments(self, parser):
        parser.add_argument(
            "const_name",
            type=str,
        )

        parser.add_argument(
            "--as-int",
            action="store_true",
            dest="as_int",
            default=False,
        )

    def handle(self, *args, **options):
        const_name = options.get("const_name", "")
        as_int = options.get("as_int", False)

        import_enum = None
        paths = Path(BASE_DIR).glob("**/const.py")

        for p in paths:
            p = p.relative_to(BASE_DIR).as_posix()
            p = p.replace("/", ".").replace(".py", "")

            try:
                import_enum = import_string(f"{p}.{const_name}")
                break
            except Exception:
                pass

        if import_enum is None:
            print("Unable to find the import")
            return

        if not type(import_enum) in [list, tuple]:
            print("Import is incorrect")
            return

        if not type(import_enum[0]) in [list, tuple]:
            print("Import is incorrect")
            return

        # res = self.handle_v1(import_enum, const_name, as_int)
        res = self.handle_v2(import_enum, const_name, as_int)
        print("\n".join(["", *res, ""]))

    def handle_v1(self, import_enum, const_name: str, as_int: bool) -> list[str]:
        camel_const_name = camel_case(const_name)
        pascal_const_name = camel_const_name[0].upper() + camel_const_name[1:]
        enum_str = [
            f"export const {camel_const_name}Enum = {{",
        ]

        for enum_value, enum_text in import_enum:
            enum_text_slug = slugify(enum_text).upper().replace("-", "_")
            enum_combo = f"    {enum_text_slug}: '{enum_text}',"

            if as_int:
                enum_combo = f"    {enum_text_slug}: {enum_value},"

            enum_str.append(enum_combo)

        enum_str.extend(
            [
                "} as const;",
                f"export type I{pascal_const_name}Values = GetObjectValueTypes<typeof {camel_const_name}Enum>;",
            ]
        )

        return enum_str

    def handle_v2(self, import_enum, const_name: str, as_int: bool) -> list[str]:
        camel_const_name = camel_case(const_name)
        pascal_const_name = camel_const_name[0].upper() + camel_const_name[1:]

        enum_str = [
            f"export enum {pascal_const_name}Enum {{",
        ]
        enum_keys = []
        enum_vals = []

        for enum_value, enum_text in import_enum:
            enum_text_slug = slugify(enum_text).upper().replace("-", "_")
            enum_combo = f"    {enum_text_slug}: '{enum_text}'"
            enum_keys.append(f"'{enum_text_slug}'")

            if as_int:
                enum_combo = f"    {enum_text_slug} = {enum_value} as {pascal_const_name}EnumValues,"
                enum_vals.append(f"{enum_value}")
            else:
                enum_combo = f"    {enum_text_slug} = '{enum_text}',"
                enum_vals.append(f"'{enum_text}'")

            enum_str.append(enum_combo)

        enum_str.append("};")

        return [
            f"export type {pascal_const_name}EnumKeys = {' | '.join(enum_keys)};",
            f"export type {pascal_const_name}EnumValues = {' | '.join(enum_vals)};",
            *enum_str,
        ]
