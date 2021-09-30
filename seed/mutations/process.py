"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Process
from app.models import User
from seed.schema.types import Process as ProcessType

class SaveProcessMutation(graphene.Mutation):
    
    process = graphene.Field(ProcessType)
    
    class Arguments:
        decimal = graphene.Int(required=True)
        result = graphene.String(required=True)
        userId = graphene.Int(required=True)
        pass
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        process = {}
        if "decimal" in kwargs:
            process["decimal"] = kwargs["decimal"]
        if "result" in kwargs:
            process["result"] = kwargs["result"]
        if "userId" in kwargs:
            user_id = User.filter_permissions(
                User.objects,
                User.permission_filters(user)) \
                .get(pk=kwargs["userId"])
            process["user_id"] = user_id
        process = \
            Process.objects.create(**process)
        process.save()
    
        return SaveProcessMutation(
            process=process)

class SetProcessMutation(graphene.Mutation):
    
    process = graphene.Field(ProcessType)
    
    class Arguments:
        id = graphene.Int(required=True)
        decimal = graphene.Int(required=False)
        result = graphene.String(required=False)
        userId = graphene.Int(required=False)
        
    # pylint: disable=R0912,W0622
    def mutate(self, info, **kwargs):
        user = info.context.user
        process = Process.filter_permissions(
            Process.objects,
            Process.permission_filters(user)) \
            .get(pk=kwargs["id"])
        if "decimal" in kwargs:
            process.decimal = kwargs["decimal"]
        if "result" in kwargs:
            process.result = kwargs["result"]
        if "userId" in kwargs:
            user_id = User.objects \
                .get(pk=kwargs["userId"])
            process.user_id = user_id
        process.save()
    
        return SetProcessMutation(
            process=process)

class DeleteProcessMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        process_id = kwargs["id"]
        process = Process.objects.get(pk=kwargs["id"])
        process.delete()
        return DeleteProcessMutation(
            id=process_id)