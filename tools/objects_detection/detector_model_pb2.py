# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import detections_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='detector_model.proto',
  package='doppia_protobuf',
  serialized_pb='\n\x14\x64\x65tector_model.proto\x12\x0f\x64oppia_protobuf\x1a\x10\x64\x65tections.proto\"\x85\x01\n\x0eLinearSvmModel\x12\x13\n\x0bsolved_type\x18\x01 \x01(\t\x12\x19\n\x11number_of_classes\x18\x02 \x01(\r\x12\x0e\n\x06labels\x18\x03 \x03(\x05\x12\x1a\n\x12number_of_features\x18\x04 \x01(\r\x12\x0c\n\x04\x62ias\x18\x05 \x02(\x02\x12\t\n\x01w\x18\x06 \x03(\x02\"S\n\x17IntegralChannelsFeature\x12\x15\n\rchannel_index\x18\x01 \x02(\x05\x12!\n\x03\x62ox\x18\x02 \x02(\x0b\x32\x14.doppia_protobuf.Box\"\xcf\x01\n\x1cIntegralChannelDecisionStump\x12\x39\n\x07\x66\x65\x61ture\x18\x01 \x02(\x0b\x32(.doppia_protobuf.IntegralChannelsFeature\x12\x19\n\x11\x66\x65\x61ture_threshold\x18\x02 \x02(\x02\x12$\n\x15larger_than_threshold\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x18\n\x10true_leaf_weight\x18\n \x01(\x02\x12\x19\n\x11\x66\x61lse_leaf_weight\x18\x0b \x01(\x02\"\xa3\x01\n%IntegralChannelBinaryDecisionTreeNode\x12\n\n\x02id\x18\x01 \x02(\r\x12\x11\n\tparent_id\x18\x02 \x02(\r\x12\x14\n\x0cparent_value\x18\x03 \x01(\x08\x12\x45\n\x0e\x64\x65\x63ision_stump\x18\x04 \x01(\x0b\x32-.doppia_protobuf.IntegralChannelDecisionStump\"j\n!IntegralChannelBinaryDecisionTree\x12\x45\n\x05nodes\x18\x01 \x03(\x0b\x32\x36.doppia_protobuf.IntegralChannelBinaryDecisionTreeNode\"\xe2\x03\n$SoftCascadeOverIntegralChannelsStage\x12X\n\x0c\x66\x65\x61ture_type\x18\x01 \x02(\x0e\x32\x42.doppia_protobuf.SoftCascadeOverIntegralChannelsStage.FeatureTypes\x12\x45\n\x0e\x64\x65\x63ision_stump\x18\n \x01(\x0b\x32-.doppia_protobuf.IntegralChannelDecisionStump\x12P\n\x14level2_decision_tree\x18\x0b \x01(\x0b\x32\x32.doppia_protobuf.IntegralChannelBinaryDecisionTree\x12P\n\x14levelN_decision_tree\x18\x0c \x01(\x0b\x32\x32.doppia_protobuf.IntegralChannelBinaryDecisionTree\x12\x0e\n\x06weight\x18\x02 \x02(\x02\x12\x19\n\x11\x63\x61scade_threshold\x18\x03 \x02(\x02\"J\n\x0c\x46\x65\x61tureTypes\x12\n\n\x06Stumps\x10\x00\x12\x16\n\x12Level2DecisionTree\x10\n\x12\x16\n\x12LevelNDecisionTree\x10\x64\"\xb2\x01\n$SoftCascadeOverIntegralChannelsModel\x12\x45\n\x06stages\x18\x01 \x03(\x0b\x32\x35.doppia_protobuf.SoftCascadeOverIntegralChannelsStage\x12&\n\x14\x63hannels_description\x18\x02 \x01(\t:\x08hog6_luv\x12\x1b\n\x10shrinking_factor\x18\x03 \x01(\r:\x01\x34\"\xe3\x03\n\rDetectorModel\x12\x15\n\rdetector_name\x18\x01 \x01(\t\x12\x1d\n\x15training_dataset_name\x18\x02 \x02(\t\x12\x33\n\x11model_window_size\x18\n \x01(\x0b\x32\x18.doppia_protobuf.Point2d\x12+\n\robject_window\x18\x0b \x01(\x0b\x32\x14.doppia_protobuf.Box\x12\x43\n\rdetector_type\x18\x03 \x02(\x0e\x32,.doppia_protobuf.DetectorModel.DetectorTypes\x12\x39\n\x10linear_svm_model\x18\x64 \x01(\x0b\x32\x1f.doppia_protobuf.LinearSvmModel\x12Q\n\x12soft_cascade_model\x18\x66 \x01(\x0b\x32\x35.doppia_protobuf.SoftCascadeOverIntegralChannelsModel\x12\x11\n\x05scale\x18\xc8\x01 \x01(\x02:\x01\x31\"T\n\rDetectorTypes\x12\r\n\tLinearSvm\x10\x00\x12#\n\x1fSoftCascadeOverIntegralChannels\x10\n\x12\x0f\n\x0bHoughForest\x10\x14\"\x83\x01\n\x18MultiScalesDetectorModel\x12\x15\n\rdetector_name\x18\x01 \x01(\t\x12\x1d\n\x15training_dataset_name\x18\x02 \x02(\t\x12\x31\n\tdetectors\x18\x03 \x03(\x0b\x32\x1e.doppia_protobuf.DetectorModel')



_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE_FEATURETYPES = descriptor.EnumDescriptor(
  name='FeatureTypes',
  full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.FeatureTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='Stumps', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Level2DecisionTree', index=1, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='LevelNDecisionTree', index=2, number=100,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1173,
  serialized_end=1247,
)

_DETECTORMODEL_DETECTORTYPES = descriptor.EnumDescriptor(
  name='DetectorTypes',
  full_name='doppia_protobuf.DetectorModel.DetectorTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='LinearSvm', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SoftCascadeOverIntegralChannels', index=1, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='HoughForest', index=2, number=20,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1830,
  serialized_end=1914,
)


_LINEARSVMMODEL = descriptor.Descriptor(
  name='LinearSvmModel',
  full_name='doppia_protobuf.LinearSvmModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='solved_type', full_name='doppia_protobuf.LinearSvmModel.solved_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='number_of_classes', full_name='doppia_protobuf.LinearSvmModel.number_of_classes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='labels', full_name='doppia_protobuf.LinearSvmModel.labels', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='number_of_features', full_name='doppia_protobuf.LinearSvmModel.number_of_features', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bias', full_name='doppia_protobuf.LinearSvmModel.bias', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='w', full_name='doppia_protobuf.LinearSvmModel.w', index=5,
      number=6, type=2, cpp_type=6, label=3,
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
  extension_ranges=[],
  serialized_start=60,
  serialized_end=193,
)


_INTEGRALCHANNELSFEATURE = descriptor.Descriptor(
  name='IntegralChannelsFeature',
  full_name='doppia_protobuf.IntegralChannelsFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='channel_index', full_name='doppia_protobuf.IntegralChannelsFeature.channel_index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='box', full_name='doppia_protobuf.IntegralChannelsFeature.box', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=195,
  serialized_end=278,
)


_INTEGRALCHANNELDECISIONSTUMP = descriptor.Descriptor(
  name='IntegralChannelDecisionStump',
  full_name='doppia_protobuf.IntegralChannelDecisionStump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='feature', full_name='doppia_protobuf.IntegralChannelDecisionStump.feature', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='feature_threshold', full_name='doppia_protobuf.IntegralChannelDecisionStump.feature_threshold', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='larger_than_threshold', full_name='doppia_protobuf.IntegralChannelDecisionStump.larger_than_threshold', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='true_leaf_weight', full_name='doppia_protobuf.IntegralChannelDecisionStump.true_leaf_weight', index=3,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='false_leaf_weight', full_name='doppia_protobuf.IntegralChannelDecisionStump.false_leaf_weight', index=4,
      number=11, type=2, cpp_type=6, label=1,
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
  extension_ranges=[],
  serialized_start=281,
  serialized_end=488,
)


_INTEGRALCHANNELBINARYDECISIONTREENODE = descriptor.Descriptor(
  name='IntegralChannelBinaryDecisionTreeNode',
  full_name='doppia_protobuf.IntegralChannelBinaryDecisionTreeNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='doppia_protobuf.IntegralChannelBinaryDecisionTreeNode.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='parent_id', full_name='doppia_protobuf.IntegralChannelBinaryDecisionTreeNode.parent_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='parent_value', full_name='doppia_protobuf.IntegralChannelBinaryDecisionTreeNode.parent_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='decision_stump', full_name='doppia_protobuf.IntegralChannelBinaryDecisionTreeNode.decision_stump', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  extension_ranges=[],
  serialized_start=491,
  serialized_end=654,
)


_INTEGRALCHANNELBINARYDECISIONTREE = descriptor.Descriptor(
  name='IntegralChannelBinaryDecisionTree',
  full_name='doppia_protobuf.IntegralChannelBinaryDecisionTree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='nodes', full_name='doppia_protobuf.IntegralChannelBinaryDecisionTree.nodes', index=0,
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
  extension_ranges=[],
  serialized_start=656,
  serialized_end=762,
)


_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE = descriptor.Descriptor(
  name='SoftCascadeOverIntegralChannelsStage',
  full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='feature_type', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.feature_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='decision_stump', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.decision_stump', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level2_decision_tree', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.level2_decision_tree', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='levelN_decision_tree', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.levelN_decision_tree', index=3,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='weight', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.weight', index=4,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cascade_threshold', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsStage.cascade_threshold', index=5,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOFTCASCADEOVERINTEGRALCHANNELSSTAGE_FEATURETYPES,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=765,
  serialized_end=1247,
)


_SOFTCASCADEOVERINTEGRALCHANNELSMODEL = descriptor.Descriptor(
  name='SoftCascadeOverIntegralChannelsModel',
  full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stages', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsModel.stages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='channels_description', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsModel.channels_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("hog6_luv", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shrinking_factor', full_name='doppia_protobuf.SoftCascadeOverIntegralChannelsModel.shrinking_factor', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=4,
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
  extension_ranges=[],
  serialized_start=1250,
  serialized_end=1428,
)


_DETECTORMODEL = descriptor.Descriptor(
  name='DetectorModel',
  full_name='doppia_protobuf.DetectorModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='detector_name', full_name='doppia_protobuf.DetectorModel.detector_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='training_dataset_name', full_name='doppia_protobuf.DetectorModel.training_dataset_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='model_window_size', full_name='doppia_protobuf.DetectorModel.model_window_size', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='object_window', full_name='doppia_protobuf.DetectorModel.object_window', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detector_type', full_name='doppia_protobuf.DetectorModel.detector_type', index=4,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='linear_svm_model', full_name='doppia_protobuf.DetectorModel.linear_svm_model', index=5,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='soft_cascade_model', full_name='doppia_protobuf.DetectorModel.soft_cascade_model', index=6,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='scale', full_name='doppia_protobuf.DetectorModel.scale', index=7,
      number=200, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DETECTORMODEL_DETECTORTYPES,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1431,
  serialized_end=1914,
)


_MULTISCALESDETECTORMODEL = descriptor.Descriptor(
  name='MultiScalesDetectorModel',
  full_name='doppia_protobuf.MultiScalesDetectorModel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='detector_name', full_name='doppia_protobuf.MultiScalesDetectorModel.detector_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='training_dataset_name', full_name='doppia_protobuf.MultiScalesDetectorModel.training_dataset_name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detectors', full_name='doppia_protobuf.MultiScalesDetectorModel.detectors', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=1917,
  serialized_end=2048,
)

_INTEGRALCHANNELSFEATURE.fields_by_name['box'].message_type = detections_pb2._BOX
_INTEGRALCHANNELDECISIONSTUMP.fields_by_name['feature'].message_type = _INTEGRALCHANNELSFEATURE
_INTEGRALCHANNELBINARYDECISIONTREENODE.fields_by_name['decision_stump'].message_type = _INTEGRALCHANNELDECISIONSTUMP
_INTEGRALCHANNELBINARYDECISIONTREE.fields_by_name['nodes'].message_type = _INTEGRALCHANNELBINARYDECISIONTREENODE
_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE.fields_by_name['feature_type'].enum_type = _SOFTCASCADEOVERINTEGRALCHANNELSSTAGE_FEATURETYPES
_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE.fields_by_name['decision_stump'].message_type = _INTEGRALCHANNELDECISIONSTUMP
_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE.fields_by_name['level2_decision_tree'].message_type = _INTEGRALCHANNELBINARYDECISIONTREE
_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE.fields_by_name['levelN_decision_tree'].message_type = _INTEGRALCHANNELBINARYDECISIONTREE
_SOFTCASCADEOVERINTEGRALCHANNELSSTAGE_FEATURETYPES.containing_type = _SOFTCASCADEOVERINTEGRALCHANNELSSTAGE;
_SOFTCASCADEOVERINTEGRALCHANNELSMODEL.fields_by_name['stages'].message_type = _SOFTCASCADEOVERINTEGRALCHANNELSSTAGE
_DETECTORMODEL.fields_by_name['model_window_size'].message_type = detections_pb2._POINT2D
_DETECTORMODEL.fields_by_name['object_window'].message_type = detections_pb2._BOX
_DETECTORMODEL.fields_by_name['detector_type'].enum_type = _DETECTORMODEL_DETECTORTYPES
_DETECTORMODEL.fields_by_name['linear_svm_model'].message_type = _LINEARSVMMODEL
_DETECTORMODEL.fields_by_name['soft_cascade_model'].message_type = _SOFTCASCADEOVERINTEGRALCHANNELSMODEL
_DETECTORMODEL_DETECTORTYPES.containing_type = _DETECTORMODEL;
_MULTISCALESDETECTORMODEL.fields_by_name['detectors'].message_type = _DETECTORMODEL
DESCRIPTOR.message_types_by_name['LinearSvmModel'] = _LINEARSVMMODEL
DESCRIPTOR.message_types_by_name['IntegralChannelsFeature'] = _INTEGRALCHANNELSFEATURE
DESCRIPTOR.message_types_by_name['IntegralChannelDecisionStump'] = _INTEGRALCHANNELDECISIONSTUMP
DESCRIPTOR.message_types_by_name['IntegralChannelBinaryDecisionTreeNode'] = _INTEGRALCHANNELBINARYDECISIONTREENODE
DESCRIPTOR.message_types_by_name['IntegralChannelBinaryDecisionTree'] = _INTEGRALCHANNELBINARYDECISIONTREE
DESCRIPTOR.message_types_by_name['SoftCascadeOverIntegralChannelsStage'] = _SOFTCASCADEOVERINTEGRALCHANNELSSTAGE
DESCRIPTOR.message_types_by_name['SoftCascadeOverIntegralChannelsModel'] = _SOFTCASCADEOVERINTEGRALCHANNELSMODEL
DESCRIPTOR.message_types_by_name['DetectorModel'] = _DETECTORMODEL
DESCRIPTOR.message_types_by_name['MultiScalesDetectorModel'] = _MULTISCALESDETECTORMODEL

class LinearSvmModel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LINEARSVMMODEL
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.LinearSvmModel)

class IntegralChannelsFeature(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INTEGRALCHANNELSFEATURE
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.IntegralChannelsFeature)

class IntegralChannelDecisionStump(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INTEGRALCHANNELDECISIONSTUMP
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.IntegralChannelDecisionStump)

class IntegralChannelBinaryDecisionTreeNode(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INTEGRALCHANNELBINARYDECISIONTREENODE
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.IntegralChannelBinaryDecisionTreeNode)

class IntegralChannelBinaryDecisionTree(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INTEGRALCHANNELBINARYDECISIONTREE
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.IntegralChannelBinaryDecisionTree)

class SoftCascadeOverIntegralChannelsStage(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOFTCASCADEOVERINTEGRALCHANNELSSTAGE
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.SoftCascadeOverIntegralChannelsStage)

class SoftCascadeOverIntegralChannelsModel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SOFTCASCADEOVERINTEGRALCHANNELSMODEL
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.SoftCascadeOverIntegralChannelsModel)

class DetectorModel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DETECTORMODEL
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.DetectorModel)

class MultiScalesDetectorModel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MULTISCALESDETECTORMODEL
  
  # @@protoc_insertion_point(class_scope:doppia_protobuf.MultiScalesDetectorModel)

# @@protoc_insertion_point(module_scope)
