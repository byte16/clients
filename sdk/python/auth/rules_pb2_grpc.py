# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from auth import rules_pb2 as auth_dot_rules__pb2


class RulesStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/go.micro.auth.Rules/Create',
        request_serializer=auth_dot_rules__pb2.CreateRequest.SerializeToString,
        response_deserializer=auth_dot_rules__pb2.CreateResponse.FromString,
        )
    self.Delete = channel.unary_unary(
        '/go.micro.auth.Rules/Delete',
        request_serializer=auth_dot_rules__pb2.DeleteRequest.SerializeToString,
        response_deserializer=auth_dot_rules__pb2.DeleteResponse.FromString,
        )
    self.List = channel.unary_unary(
        '/go.micro.auth.Rules/List',
        request_serializer=auth_dot_rules__pb2.ListRequest.SerializeToString,
        response_deserializer=auth_dot_rules__pb2.ListResponse.FromString,
        )


class RulesServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RulesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=auth_dot_rules__pb2.CreateRequest.FromString,
          response_serializer=auth_dot_rules__pb2.CreateResponse.SerializeToString,
      ),
      'Delete': grpc.unary_unary_rpc_method_handler(
          servicer.Delete,
          request_deserializer=auth_dot_rules__pb2.DeleteRequest.FromString,
          response_serializer=auth_dot_rules__pb2.DeleteResponse.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=auth_dot_rules__pb2.ListRequest.FromString,
          response_serializer=auth_dot_rules__pb2.ListResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'go.micro.auth.Rules', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))