# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kuscia/proto/api/v1alpha1/appconfig/app_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4kuscia/proto/api/v1alpha1/appconfig/app_config.proto\x12#kuscia.proto.api.v1alpha1.appconfig\"/\n\x07Service\x12\x11\n\tport_name\x18\x01 \x01(\t\x12\x11\n\tendpoints\x18\x02 \x03(\t\"c\n\x05Party\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12>\n\x08services\x18\x03 \x03(\x0b\x32,.kuscia.proto.api.v1alpha1.appconfig.Service\"\x7f\n\rClusterDefine\x12;\n\x07parties\x18\x01 \x03(\x0b\x32*.kuscia.proto.api.v1alpha1.appconfig.Party\x12\x16\n\x0eself_party_idx\x18\x02 \x01(\x05\x12\x19\n\x11self_endpoint_idx\x18\x03 \x01(\x05\"C\n\x04Port\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\r\n\x05scope\x18\x03 \x01(\t\x12\x10\n\x08protocol\x18\x04 \x01(\t\"J\n\x0e\x41llocatedPorts\x12\x38\n\x05ports\x18\x01 \x03(\x0b\x32).kuscia.proto.api.v1alpha1.appconfig.PortB^\n!com.secretflow.v1alpha1.appconfigZ9github.com/secretflow/kuscia/proto/api/v1alpha1/appconfigb\x06proto3')



_SERVICE = DESCRIPTOR.message_types_by_name['Service']
_PARTY = DESCRIPTOR.message_types_by_name['Party']
_CLUSTERDEFINE = DESCRIPTOR.message_types_by_name['ClusterDefine']
_PORT = DESCRIPTOR.message_types_by_name['Port']
_ALLOCATEDPORTS = DESCRIPTOR.message_types_by_name['AllocatedPorts']
Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'kuscia.proto.api.v1alpha1.appconfig.app_config_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.appconfig.Service)
  })
_sym_db.RegisterMessage(Service)

Party = _reflection.GeneratedProtocolMessageType('Party', (_message.Message,), {
  'DESCRIPTOR' : _PARTY,
  '__module__' : 'kuscia.proto.api.v1alpha1.appconfig.app_config_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.appconfig.Party)
  })
_sym_db.RegisterMessage(Party)

ClusterDefine = _reflection.GeneratedProtocolMessageType('ClusterDefine', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERDEFINE,
  '__module__' : 'kuscia.proto.api.v1alpha1.appconfig.app_config_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.appconfig.ClusterDefine)
  })
_sym_db.RegisterMessage(ClusterDefine)

Port = _reflection.GeneratedProtocolMessageType('Port', (_message.Message,), {
  'DESCRIPTOR' : _PORT,
  '__module__' : 'kuscia.proto.api.v1alpha1.appconfig.app_config_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.appconfig.Port)
  })
_sym_db.RegisterMessage(Port)

AllocatedPorts = _reflection.GeneratedProtocolMessageType('AllocatedPorts', (_message.Message,), {
  'DESCRIPTOR' : _ALLOCATEDPORTS,
  '__module__' : 'kuscia.proto.api.v1alpha1.appconfig.app_config_pb2'
  # @@protoc_insertion_point(class_scope:kuscia.proto.api.v1alpha1.appconfig.AllocatedPorts)
  })
_sym_db.RegisterMessage(AllocatedPorts)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.secretflow.v1alpha1.appconfigZ9github.com/secretflow/kuscia/proto/api/v1alpha1/appconfig'
  _SERVICE._serialized_start=93
  _SERVICE._serialized_end=140
  _PARTY._serialized_start=142
  _PARTY._serialized_end=241
  _CLUSTERDEFINE._serialized_start=243
  _CLUSTERDEFINE._serialized_end=370
  _PORT._serialized_start=372
  _PORT._serialized_end=439
  _ALLOCATEDPORTS._serialized_start=441
  _ALLOCATEDPORTS._serialized_end=515
# @@protoc_insertion_point(module_scope)