# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/grpc/logging/v2/logging_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/grpc/logging/v2/logging_config.proto',
  package='google.logging.v2',
  syntax='proto3',
  serialized_pb=_b('\n1google/cloud/grpc/logging/v2/logging_config.proto\x12\x11google.logging.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xbd\x02\n\x07LogSink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\t\x12G\n\x15output_version_format\x18\x06 \x01(\x0e\x32(.google.logging.v2.LogSink.VersionFormat\x12\x17\n\x0fwriter_identity\x18\x08 \x01(\t\x12.\n\nstart_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"?\n\rVersionFormat\x12\x1e\n\x1aVERSION_FORMAT_UNSPECIFIED\x10\x00\x12\x06\n\x02V2\x10\x01\x12\x06\n\x02V1\x10\x02\"I\n\x10ListSinksRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\"W\n\x11ListSinksResponse\x12)\n\x05sinks\x18\x01 \x03(\x0b\x32\x1a.google.logging.v2.LogSink\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"#\n\x0eGetSinkRequest\x12\x11\n\tsink_name\x18\x01 \x01(\t\"m\n\x11\x43reateSinkRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12(\n\x04sink\x18\x02 \x01(\x0b\x32\x1a.google.logging.v2.LogSink\x12\x1e\n\x16unique_writer_identity\x18\x03 \x01(\x08\"p\n\x11UpdateSinkRequest\x12\x11\n\tsink_name\x18\x01 \x01(\t\x12(\n\x04sink\x18\x02 \x01(\x0b\x32\x1a.google.logging.v2.LogSink\x12\x1e\n\x16unique_writer_identity\x18\x03 \x01(\x08\"&\n\x11\x44\x65leteSinkRequest\x12\x11\n\tsink_name\x18\x01 \x01(\t2\xfe\x04\n\x0f\x43onfigServiceV2\x12}\n\tListSinks\x12#.google.logging.v2.ListSinksRequest\x1a$.google.logging.v2.ListSinksResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v2/{parent=projects/*}/sinks\x12t\n\x07GetSink\x12!.google.logging.v2.GetSinkRequest\x1a\x1a.google.logging.v2.LogSink\"*\x82\xd3\xe4\x93\x02$\x12\"/v2/{sink_name=projects/*/sinks/*}\x12{\n\nCreateSink\x12$.google.logging.v2.CreateSinkRequest\x1a\x1a.google.logging.v2.LogSink\"+\x82\xd3\xe4\x93\x02%\"\x1d/v2/{parent=projects/*}/sinks:\x04sink\x12\x80\x01\n\nUpdateSink\x12$.google.logging.v2.UpdateSinkRequest\x1a\x1a.google.logging.v2.LogSink\"0\x82\xd3\xe4\x93\x02*\x1a\"/v2/{sink_name=projects/*/sinks/*}:\x04sink\x12v\n\nDeleteSink\x12$.google.logging.v2.DeleteSinkRequest\x1a\x16.google.protobuf.Empty\"*\x82\xd3\xe4\x93\x02$*\"/v2/{sink_name=projects/*/sinks/*}B(\n\x15\x63om.google.logging.v2B\rLoggingConfigP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_LOGSINK_VERSIONFORMAT = _descriptor.EnumDescriptor(
  name='VersionFormat',
  full_name='google.logging.v2.LogSink.VersionFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERSION_FORMAT_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V2', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='V1', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=419,
  serialized_end=482,
)
_sym_db.RegisterEnumDescriptor(_LOGSINK_VERSIONFORMAT)


_LOGSINK = _descriptor.Descriptor(
  name='LogSink',
  full_name='google.logging.v2.LogSink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.logging.v2.LogSink.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='google.logging.v2.LogSink.destination', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.logging.v2.LogSink.filter', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_version_format', full_name='google.logging.v2.LogSink.output_version_format', index=3,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='writer_identity', full_name='google.logging.v2.LogSink.writer_identity', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.logging.v2.LogSink.start_time', index=5,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.logging.v2.LogSink.end_time', index=6,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LOGSINK_VERSIONFORMAT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=482,
)


_LISTSINKSREQUEST = _descriptor.Descriptor(
  name='ListSinksRequest',
  full_name='google.logging.v2.ListSinksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.logging.v2.ListSinksRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.logging.v2.ListSinksRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.logging.v2.ListSinksRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=484,
  serialized_end=557,
)


_LISTSINKSRESPONSE = _descriptor.Descriptor(
  name='ListSinksResponse',
  full_name='google.logging.v2.ListSinksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sinks', full_name='google.logging.v2.ListSinksResponse.sinks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.logging.v2.ListSinksResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=559,
  serialized_end=646,
)


_GETSINKREQUEST = _descriptor.Descriptor(
  name='GetSinkRequest',
  full_name='google.logging.v2.GetSinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sink_name', full_name='google.logging.v2.GetSinkRequest.sink_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=648,
  serialized_end=683,
)


_CREATESINKREQUEST = _descriptor.Descriptor(
  name='CreateSinkRequest',
  full_name='google.logging.v2.CreateSinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.logging.v2.CreateSinkRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sink', full_name='google.logging.v2.CreateSinkRequest.sink', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_writer_identity', full_name='google.logging.v2.CreateSinkRequest.unique_writer_identity', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=685,
  serialized_end=794,
)


_UPDATESINKREQUEST = _descriptor.Descriptor(
  name='UpdateSinkRequest',
  full_name='google.logging.v2.UpdateSinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sink_name', full_name='google.logging.v2.UpdateSinkRequest.sink_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sink', full_name='google.logging.v2.UpdateSinkRequest.sink', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_writer_identity', full_name='google.logging.v2.UpdateSinkRequest.unique_writer_identity', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=796,
  serialized_end=908,
)


_DELETESINKREQUEST = _descriptor.Descriptor(
  name='DeleteSinkRequest',
  full_name='google.logging.v2.DeleteSinkRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sink_name', full_name='google.logging.v2.DeleteSinkRequest.sink_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=910,
  serialized_end=948,
)

_LOGSINK.fields_by_name['output_version_format'].enum_type = _LOGSINK_VERSIONFORMAT
_LOGSINK.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGSINK.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LOGSINK_VERSIONFORMAT.containing_type = _LOGSINK
_LISTSINKSRESPONSE.fields_by_name['sinks'].message_type = _LOGSINK
_CREATESINKREQUEST.fields_by_name['sink'].message_type = _LOGSINK
_UPDATESINKREQUEST.fields_by_name['sink'].message_type = _LOGSINK
DESCRIPTOR.message_types_by_name['LogSink'] = _LOGSINK
DESCRIPTOR.message_types_by_name['ListSinksRequest'] = _LISTSINKSREQUEST
DESCRIPTOR.message_types_by_name['ListSinksResponse'] = _LISTSINKSRESPONSE
DESCRIPTOR.message_types_by_name['GetSinkRequest'] = _GETSINKREQUEST
DESCRIPTOR.message_types_by_name['CreateSinkRequest'] = _CREATESINKREQUEST
DESCRIPTOR.message_types_by_name['UpdateSinkRequest'] = _UPDATESINKREQUEST
DESCRIPTOR.message_types_by_name['DeleteSinkRequest'] = _DELETESINKREQUEST

LogSink = _reflection.GeneratedProtocolMessageType('LogSink', (_message.Message,), dict(
  DESCRIPTOR = _LOGSINK,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.LogSink)
  ))
_sym_db.RegisterMessage(LogSink)

ListSinksRequest = _reflection.GeneratedProtocolMessageType('ListSinksRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSINKSREQUEST,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListSinksRequest)
  ))
_sym_db.RegisterMessage(ListSinksRequest)

ListSinksResponse = _reflection.GeneratedProtocolMessageType('ListSinksResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSINKSRESPONSE,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.ListSinksResponse)
  ))
_sym_db.RegisterMessage(ListSinksResponse)

GetSinkRequest = _reflection.GeneratedProtocolMessageType('GetSinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSINKREQUEST,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.GetSinkRequest)
  ))
_sym_db.RegisterMessage(GetSinkRequest)

CreateSinkRequest = _reflection.GeneratedProtocolMessageType('CreateSinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESINKREQUEST,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.CreateSinkRequest)
  ))
_sym_db.RegisterMessage(CreateSinkRequest)

UpdateSinkRequest = _reflection.GeneratedProtocolMessageType('UpdateSinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATESINKREQUEST,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.UpdateSinkRequest)
  ))
_sym_db.RegisterMessage(UpdateSinkRequest)

DeleteSinkRequest = _reflection.GeneratedProtocolMessageType('DeleteSinkRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETESINKREQUEST,
  __module__ = 'google.cloud.grpc.logging.v2.logging_config_pb2'
  # @@protoc_insertion_point(class_scope:google.logging.v2.DeleteSinkRequest)
  ))
_sym_db.RegisterMessage(DeleteSinkRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.google.logging.v2B\rLoggingConfigP\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class ConfigServiceV2Stub(object):
  """Service for configuring sinks used to export log entries outside of
  Stackdriver Logging.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListSinks = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/ListSinks',
        request_serializer=ListSinksRequest.SerializeToString,
        response_deserializer=ListSinksResponse.FromString,
        )
    self.GetSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/GetSink',
        request_serializer=GetSinkRequest.SerializeToString,
        response_deserializer=LogSink.FromString,
        )
    self.CreateSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/CreateSink',
        request_serializer=CreateSinkRequest.SerializeToString,
        response_deserializer=LogSink.FromString,
        )
    self.UpdateSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/UpdateSink',
        request_serializer=UpdateSinkRequest.SerializeToString,
        response_deserializer=LogSink.FromString,
        )
    self.DeleteSink = channel.unary_unary(
        '/google.logging.v2.ConfigServiceV2/DeleteSink',
        request_serializer=DeleteSinkRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class ConfigServiceV2Servicer(object):
  """Service for configuring sinks used to export log entries outside of
  Stackdriver Logging.
  """

  def ListSinks(self, request, context):
    """Lists sinks.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSink(self, request, context):
    """Gets a sink.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSink(self, request, context):
    """Creates a sink.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSink(self, request, context):
    """Updates or creates a sink.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteSink(self, request, context):
    """Deletes a sink.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ConfigServiceV2Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListSinks': grpc.unary_unary_rpc_method_handler(
          servicer.ListSinks,
          request_deserializer=ListSinksRequest.FromString,
          response_serializer=ListSinksResponse.SerializeToString,
      ),
      'GetSink': grpc.unary_unary_rpc_method_handler(
          servicer.GetSink,
          request_deserializer=GetSinkRequest.FromString,
          response_serializer=LogSink.SerializeToString,
      ),
      'CreateSink': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSink,
          request_deserializer=CreateSinkRequest.FromString,
          response_serializer=LogSink.SerializeToString,
      ),
      'UpdateSink': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSink,
          request_deserializer=UpdateSinkRequest.FromString,
          response_serializer=LogSink.SerializeToString,
      ),
      'DeleteSink': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteSink,
          request_deserializer=DeleteSinkRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.logging.v2.ConfigServiceV2', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaConfigServiceV2Servicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  """Service for configuring sinks used to export log entries outside of
  Stackdriver Logging.
  """
  def ListSinks(self, request, context):
    """Lists sinks.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetSink(self, request, context):
    """Gets a sink.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def CreateSink(self, request, context):
    """Creates a sink.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def UpdateSink(self, request, context):
    """Updates or creates a sink.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def DeleteSink(self, request, context):
    """Deletes a sink.
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaConfigServiceV2Stub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  """Service for configuring sinks used to export log entries outside of
  Stackdriver Logging.
  """
  def ListSinks(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Lists sinks.
    """
    raise NotImplementedError()
  ListSinks.future = None
  def GetSink(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Gets a sink.
    """
    raise NotImplementedError()
  GetSink.future = None
  def CreateSink(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Creates a sink.
    """
    raise NotImplementedError()
  CreateSink.future = None
  def UpdateSink(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Updates or creates a sink.
    """
    raise NotImplementedError()
  UpdateSink.future = None
  def DeleteSink(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Deletes a sink.
    """
    raise NotImplementedError()
  DeleteSink.future = None


def beta_create_ConfigServiceV2_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('google.logging.v2.ConfigServiceV2', 'CreateSink'): CreateSinkRequest.FromString,
    ('google.logging.v2.ConfigServiceV2', 'DeleteSink'): DeleteSinkRequest.FromString,
    ('google.logging.v2.ConfigServiceV2', 'GetSink'): GetSinkRequest.FromString,
    ('google.logging.v2.ConfigServiceV2', 'ListSinks'): ListSinksRequest.FromString,
    ('google.logging.v2.ConfigServiceV2', 'UpdateSink'): UpdateSinkRequest.FromString,
  }
  response_serializers = {
    ('google.logging.v2.ConfigServiceV2', 'CreateSink'): LogSink.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'DeleteSink'): google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'GetSink'): LogSink.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'ListSinks'): ListSinksResponse.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'UpdateSink'): LogSink.SerializeToString,
  }
  method_implementations = {
    ('google.logging.v2.ConfigServiceV2', 'CreateSink'): face_utilities.unary_unary_inline(servicer.CreateSink),
    ('google.logging.v2.ConfigServiceV2', 'DeleteSink'): face_utilities.unary_unary_inline(servicer.DeleteSink),
    ('google.logging.v2.ConfigServiceV2', 'GetSink'): face_utilities.unary_unary_inline(servicer.GetSink),
    ('google.logging.v2.ConfigServiceV2', 'ListSinks'): face_utilities.unary_unary_inline(servicer.ListSinks),
    ('google.logging.v2.ConfigServiceV2', 'UpdateSink'): face_utilities.unary_unary_inline(servicer.UpdateSink),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_ConfigServiceV2_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('google.logging.v2.ConfigServiceV2', 'CreateSink'): CreateSinkRequest.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'DeleteSink'): DeleteSinkRequest.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'GetSink'): GetSinkRequest.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'ListSinks'): ListSinksRequest.SerializeToString,
    ('google.logging.v2.ConfigServiceV2', 'UpdateSink'): UpdateSinkRequest.SerializeToString,
  }
  response_deserializers = {
    ('google.logging.v2.ConfigServiceV2', 'CreateSink'): LogSink.FromString,
    ('google.logging.v2.ConfigServiceV2', 'DeleteSink'): google_dot_protobuf_dot_empty__pb2.Empty.FromString,
    ('google.logging.v2.ConfigServiceV2', 'GetSink'): LogSink.FromString,
    ('google.logging.v2.ConfigServiceV2', 'ListSinks'): ListSinksResponse.FromString,
    ('google.logging.v2.ConfigServiceV2', 'UpdateSink'): LogSink.FromString,
  }
  cardinalities = {
    'CreateSink': cardinality.Cardinality.UNARY_UNARY,
    'DeleteSink': cardinality.Cardinality.UNARY_UNARY,
    'GetSink': cardinality.Cardinality.UNARY_UNARY,
    'ListSinks': cardinality.Cardinality.UNARY_UNARY,
    'UpdateSink': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'google.logging.v2.ConfigServiceV2', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
