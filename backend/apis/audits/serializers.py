from rest_framework import serializers

from auditlog.models import LogEntry

class AuditSerializer(serializers.ModelSerializer):
    action = serializers.CharField(source='get_action_display')

    class Meta:
        model = LogEntry
        fields = ('id', 'object_pk', 'action', 'changes', 'remote_addr', 'timestamp', 'actor')
