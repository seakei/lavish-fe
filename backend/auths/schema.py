from rest_framework import serializers
from rest_framework.parsers import JSONParser
from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema_view, extend_schema, inline_serializer


class FixOpenApi(OpenApiViewExtension):
    target_class = "rest_framework_jwt.views.ObtainJSONWebToken"

    def view_replacement(self):
        @extend_schema_view(
            post=extend_schema(
                responses={
                    200: inline_serializer(
                        name="AuthJSONWebToken",
                        fields={"token": serializers.CharField()},
                    )
                }
            )
        )
        class Fixed(self.target_class):
            pass

        return Fixed
