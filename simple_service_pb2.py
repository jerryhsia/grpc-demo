# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: simple_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14simple_service.proto\x12\x06simple\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2H\n\rSimpleService\x12\x37\n\x08SayHello\x12\x14.simple.HelloRequest\x1a\x15.simple.HelloResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'simple_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=32
  _HELLOREQUEST._serialized_end=60
  _HELLORESPONSE._serialized_start=62
  _HELLORESPONSE._serialized_end=94
  _SIMPLESERVICE._serialized_start=96
  _SIMPLESERVICE._serialized_end=168
# @@protoc_insertion_point(module_scope)