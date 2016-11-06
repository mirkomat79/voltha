# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='schema',
  syntax='proto3',
  serialized_pb=_b('\n\x0cschema.proto\x12\x06schema\x1a\x1bgoogle/protobuf/empty.proto\"A\n\tProtoFile\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\r\n\x05proto\x18\x02 \x01(\t\x12\x12\n\ndescriptor\x18\x03 \x01(\x0c\",\n\x07Schemas\x12!\n\x06protos\x18\x01 \x03(\x0b\x32\x11.schema.ProtoFile2G\n\rSchemaService\x12\x36\n\tGetSchema\x12\x16.google.protobuf.Empty\x1a\x0f.schema.Schemas\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROTOFILE = _descriptor.Descriptor(
  name='ProtoFile',
  full_name='schema.ProtoFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='schema.ProtoFile.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto', full_name='schema.ProtoFile.proto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='schema.ProtoFile.descriptor', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=118,
)


_SCHEMAS = _descriptor.Descriptor(
  name='Schemas',
  full_name='schema.Schemas',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protos', full_name='schema.Schemas.protos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=164,
)

_SCHEMAS.fields_by_name['protos'].message_type = _PROTOFILE
DESCRIPTOR.message_types_by_name['ProtoFile'] = _PROTOFILE
DESCRIPTOR.message_types_by_name['Schemas'] = _SCHEMAS

ProtoFile = _reflection.GeneratedProtocolMessageType('ProtoFile', (_message.Message,), dict(
  DESCRIPTOR = _PROTOFILE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.ProtoFile)
  ))
_sym_db.RegisterMessage(ProtoFile)

Schemas = _reflection.GeneratedProtocolMessageType('Schemas', (_message.Message,), dict(
  DESCRIPTOR = _SCHEMAS,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.Schemas)
  ))
_sym_db.RegisterMessage(Schemas)


import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class SchemaServiceStub(object):
  """Schema services
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSchema = channel.unary_unary(
        '/schema.SchemaService/GetSchema',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=Schemas.FromString,
        )


class SchemaServiceServicer(object):
  """Schema services
  """

  def GetSchema(self, request, context):
    """Return active grpc schemas
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SchemaServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSchema': grpc.unary_unary_rpc_method_handler(
          servicer.GetSchema,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=Schemas.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'schema.SchemaService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaSchemaServiceServicer(object):
  """Schema services
  """
  def GetSchema(self, request, context):
    """Return active grpc schemas
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaSchemaServiceStub(object):
  """Schema services
  """
  def GetSchema(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Return active grpc schemas
    """
    raise NotImplementedError()
  GetSchema.future = None


def beta_create_SchemaService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('schema.SchemaService', 'GetSchema'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
  }
  response_serializers = {
    ('schema.SchemaService', 'GetSchema'): Schemas.SerializeToString,
  }
  method_implementations = {
    ('schema.SchemaService', 'GetSchema'): face_utilities.unary_unary_inline(servicer.GetSchema),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_SchemaService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('schema.SchemaService', 'GetSchema'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
  }
  response_deserializers = {
    ('schema.SchemaService', 'GetSchema'): Schemas.FromString,
  }
  cardinalities = {
    'GetSchema': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'schema.SchemaService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
