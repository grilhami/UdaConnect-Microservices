# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='location.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0elocation.proto\"`\n\x0fLocationMessage\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x15\n\rcreation_time\x18\x04 \x01(\t\":\n\x13LocationMessageList\x12#\n\tlocations\x18\x01 \x03(\x0b\x32\x10.LocationMessage\"\x07\n\x05\x45mpty2Z\n\x0fLocationService\x12\"\n\x06\x43reate\x12\x10.LocationMessage\x1a\x06.Empty\x12#\n\x03Get\x12\x06.Empty\x1a\x14.LocationMessageListb\x06proto3'
)




_LOCATIONMESSAGE = _descriptor.Descriptor(
  name='LocationMessage',
  full_name='LocationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='LocationMessage.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='LocationMessage.longitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='LocationMessage.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='LocationMessage.creation_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=114,
)


_LOCATIONMESSAGELIST = _descriptor.Descriptor(
  name='LocationMessageList',
  full_name='LocationMessageList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations', full_name='LocationMessageList.locations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=174,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=176,
  serialized_end=183,
)

_LOCATIONMESSAGELIST.fields_by_name['locations'].message_type = _LOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['LocationMessage'] = _LOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['LocationMessageList'] = _LOCATIONMESSAGELIST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationMessage = _reflection.GeneratedProtocolMessageType('LocationMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONMESSAGE,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:LocationMessage)
  })
_sym_db.RegisterMessage(LocationMessage)

LocationMessageList = _reflection.GeneratedProtocolMessageType('LocationMessageList', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONMESSAGELIST,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:LocationMessageList)
  })
_sym_db.RegisterMessage(LocationMessageList)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'location_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_LOCATIONSERVICE = _descriptor.ServiceDescriptor(
  name='LocationService',
  full_name='LocationService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=185,
  serialized_end=275,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='LocationService.Create',
    index=0,
    containing_service=None,
    input_type=_LOCATIONMESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='LocationService.Get',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_LOCATIONMESSAGELIST,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATIONSERVICE)

DESCRIPTOR.services_by_name['LocationService'] = _LOCATIONSERVICE

# @@protoc_insertion_point(module_scope)
