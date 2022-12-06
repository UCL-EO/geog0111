# 005 Packages : Answers to exercises

#### Exercise 1

Make and run a Python cell that imports the class `Loader` from the package `yaml` and show the help text for this.


```python
# ANSWER
# 
from yaml import Loader
help(Loader)

# This above is a correct answer 
# you could have done as below
# but that doesnt quite answer the question correctly
# as it specificaly asks you to import Loader
#
#import yaml
#help(yaml.Loader)

```

    Help on class Loader in module yaml.loader:
    
    class Loader(yaml.reader.Reader, yaml.scanner.Scanner, yaml.parser.Parser, yaml.composer.Composer, yaml.constructor.Constructor, yaml.resolver.Resolver)
     |  Loader(stream)
     |  
     |  Method resolution order:
     |      Loader
     |      yaml.reader.Reader
     |      yaml.scanner.Scanner
     |      yaml.parser.Parser
     |      yaml.composer.Composer
     |      yaml.constructor.Constructor
     |      yaml.constructor.UnsafeConstructor
     |      yaml.constructor.FullConstructor
     |      yaml.constructor.SafeConstructor
     |      yaml.constructor.BaseConstructor
     |      yaml.resolver.Resolver
     |      yaml.resolver.BaseResolver
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, stream)
     |      Initialize the scanner.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.reader.Reader:
     |  
     |  check_printable(self, data)
     |  
     |  determine_encoding(self)
     |  
     |  forward(self, length=1)
     |  
     |  get_mark(self)
     |  
     |  peek(self, index=0)
     |  
     |  prefix(self, length=1)
     |  
     |  update(self, length)
     |  
     |  update_raw(self, size=4096)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from yaml.reader.Reader:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.reader.Reader:
     |  
     |  NON_PRINTABLE = re.compile('[^\t\n\r -~\x85\xa0-\ud7ff\ue000-�𐀀-\U0010...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.scanner.Scanner:
     |  
     |  add_indent(self, column)
     |  
     |  check_block_entry(self)
     |  
     |  check_directive(self)
     |  
     |  check_document_end(self)
     |  
     |  check_document_start(self)
     |  
     |  check_key(self)
     |  
     |  check_plain(self)
     |  
     |  check_token(self, *choices)
     |  
     |  check_value(self)
     |  
     |  fetch_alias(self)
     |  
     |  fetch_anchor(self)
     |  
     |  fetch_block_entry(self)
     |  
     |  fetch_block_scalar(self, style)
     |  
     |  fetch_directive(self)
     |  
     |  fetch_document_end(self)
     |  
     |  fetch_document_indicator(self, TokenClass)
     |  
     |  fetch_document_start(self)
     |  
     |  fetch_double(self)
     |  
     |  fetch_flow_collection_end(self, TokenClass)
     |  
     |  fetch_flow_collection_start(self, TokenClass)
     |  
     |  fetch_flow_entry(self)
     |  
     |  fetch_flow_mapping_end(self)
     |  
     |  fetch_flow_mapping_start(self)
     |  
     |  fetch_flow_scalar(self, style)
     |  
     |  fetch_flow_sequence_end(self)
     |  
     |  fetch_flow_sequence_start(self)
     |  
     |  fetch_folded(self)
     |  
     |  fetch_key(self)
     |  
     |  fetch_literal(self)
     |  
     |  fetch_more_tokens(self)
     |  
     |  fetch_plain(self)
     |  
     |  fetch_single(self)
     |  
     |  fetch_stream_end(self)
     |  
     |  fetch_stream_start(self)
     |  
     |  fetch_tag(self)
     |  
     |  fetch_value(self)
     |  
     |  get_token(self)
     |  
     |  need_more_tokens(self)
     |  
     |  next_possible_simple_key(self)
     |  
     |  peek_token(self)
     |  
     |  remove_possible_simple_key(self)
     |  
     |  save_possible_simple_key(self)
     |  
     |  scan_anchor(self, TokenClass)
     |  
     |  scan_block_scalar(self, style)
     |  
     |  scan_block_scalar_breaks(self, indent)
     |  
     |  scan_block_scalar_ignored_line(self, start_mark)
     |  
     |  scan_block_scalar_indentation(self)
     |  
     |  scan_block_scalar_indicators(self, start_mark)
     |  
     |  scan_directive(self)
     |  
     |  scan_directive_ignored_line(self, start_mark)
     |  
     |  scan_directive_name(self, start_mark)
     |  
     |  scan_flow_scalar(self, style)
     |  
     |  scan_flow_scalar_breaks(self, double, start_mark)
     |  
     |  scan_flow_scalar_non_spaces(self, double, start_mark)
     |  
     |  scan_flow_scalar_spaces(self, double, start_mark)
     |  
     |  scan_line_break(self)
     |  
     |  scan_plain(self)
     |  
     |  scan_plain_spaces(self, indent, start_mark)
     |  
     |  scan_tag(self)
     |  
     |  scan_tag_directive_handle(self, start_mark)
     |  
     |  scan_tag_directive_prefix(self, start_mark)
     |  
     |  scan_tag_directive_value(self, start_mark)
     |  
     |  scan_tag_handle(self, name, start_mark)
     |  
     |  scan_tag_uri(self, name, start_mark)
     |  
     |  scan_to_next_token(self)
     |  
     |  scan_uri_escapes(self, name, start_mark)
     |  
     |  scan_yaml_directive_number(self, start_mark)
     |  
     |  scan_yaml_directive_value(self, start_mark)
     |  
     |  stale_possible_simple_keys(self)
     |  
     |  unwind_indent(self, column)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.scanner.Scanner:
     |  
     |  ESCAPE_CODES = {'U': 8, 'u': 4, 'x': 2}
     |  
     |  ESCAPE_REPLACEMENTS = {'\t': '\t', ' ': ' ', '"': '"', '/': '/', '0': ...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.parser.Parser:
     |  
     |  check_event(self, *choices)
     |  
     |  dispose(self)
     |  
     |  get_event(self)
     |  
     |  parse_block_mapping_first_key(self)
     |  
     |  parse_block_mapping_key(self)
     |  
     |  parse_block_mapping_value(self)
     |  
     |  parse_block_node(self)
     |  
     |  parse_block_node_or_indentless_sequence(self)
     |  
     |  parse_block_sequence_entry(self)
     |  
     |  parse_block_sequence_first_entry(self)
     |  
     |  parse_document_content(self)
     |  
     |  parse_document_end(self)
     |  
     |  parse_document_start(self)
     |  
     |  parse_flow_mapping_empty_value(self)
     |  
     |  parse_flow_mapping_first_key(self)
     |  
     |  parse_flow_mapping_key(self, first=False)
     |  
     |  parse_flow_mapping_value(self)
     |  
     |  parse_flow_node(self)
     |  
     |  parse_flow_sequence_entry(self, first=False)
     |  
     |  parse_flow_sequence_entry_mapping_end(self)
     |  
     |  parse_flow_sequence_entry_mapping_key(self)
     |  
     |  parse_flow_sequence_entry_mapping_value(self)
     |  
     |  parse_flow_sequence_first_entry(self)
     |  
     |  parse_implicit_document_start(self)
     |  
     |  parse_indentless_sequence_entry(self)
     |  
     |  parse_node(self, block=False, indentless_sequence=False)
     |  
     |  parse_stream_start(self)
     |  
     |  peek_event(self)
     |  
     |  process_directives(self)
     |  
     |  process_empty_scalar(self, mark)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.parser.Parser:
     |  
     |  DEFAULT_TAGS = {'!': '!', '!!': 'tag:yaml.org,2002:'}
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.composer.Composer:
     |  
     |  check_node(self)
     |  
     |  compose_document(self)
     |  
     |  compose_mapping_node(self, anchor)
     |  
     |  compose_node(self, parent, index)
     |  
     |  compose_scalar_node(self, anchor)
     |  
     |  compose_sequence_node(self, anchor)
     |  
     |  get_node(self)
     |  
     |  get_single_node(self)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.constructor.UnsafeConstructor:
     |  
     |  find_python_module(self, name, mark)
     |  
     |  find_python_name(self, name, mark)
     |  
     |  make_python_instance(self, suffix, node, args=None, kwds=None, newobj=False)
     |  
     |  set_python_instance_state(self, instance, state)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.constructor.UnsafeConstructor:
     |  
     |  yaml_multi_constructors = {'tag:yaml.org,2002:python/module:': <functi...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.constructor.FullConstructor:
     |  
     |  construct_python_bytes(self, node)
     |  
     |  construct_python_complex(self, node)
     |  
     |  construct_python_long(self, node)
     |  
     |  construct_python_module(self, suffix, node)
     |  
     |  construct_python_name(self, suffix, node)
     |  
     |  construct_python_object(self, suffix, node)
     |  
     |  construct_python_object_apply(self, suffix, node, newobj=False)
     |  
     |  construct_python_object_new(self, suffix, node)
     |  
     |  construct_python_str(self, node)
     |  
     |  construct_python_tuple(self, node)
     |  
     |  construct_python_unicode(self, node)
     |  
     |  get_state_keys_blacklist(self)
     |      # 'extend' is blacklisted because it is used by
     |      # construct_python_object_apply to add `listitems` to a newly generate
     |      # python instance
     |  
     |  get_state_keys_blacklist_regexp(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.constructor.FullConstructor:
     |  
     |  yaml_constructors = {'tag:yaml.org,2002:null': <function SafeConstruct...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.constructor.SafeConstructor:
     |  
     |  construct_mapping(self, node, deep=False)
     |  
     |  construct_scalar(self, node)
     |  
     |  construct_undefined(self, node)
     |  
     |  construct_yaml_binary(self, node)
     |  
     |  construct_yaml_bool(self, node)
     |  
     |  construct_yaml_float(self, node)
     |  
     |  construct_yaml_int(self, node)
     |  
     |  construct_yaml_map(self, node)
     |  
     |  construct_yaml_null(self, node)
     |  
     |  construct_yaml_object(self, node, cls)
     |  
     |  construct_yaml_omap(self, node)
     |  
     |  construct_yaml_pairs(self, node)
     |  
     |  construct_yaml_seq(self, node)
     |  
     |  construct_yaml_set(self, node)
     |  
     |  construct_yaml_str(self, node)
     |  
     |  construct_yaml_timestamp(self, node)
     |  
     |  flatten_mapping(self, node)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.constructor.SafeConstructor:
     |  
     |  bool_values = {'false': False, 'no': False, 'off': False, 'on': True, ...
     |  
     |  inf_value = inf
     |  
     |  nan_value = nan
     |  
     |  timestamp_regexp = re.compile('^(?P<year>[0-9][0-9][0-9][0-9])\n   ......
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.constructor.BaseConstructor:
     |  
     |  check_data(self)
     |  
     |  check_state_key(self, key)
     |      Block special attributes/methods from being set in a newly created
     |      object, to prevent user-controlled methods from being called during
     |      deserialization
     |  
     |  construct_document(self, node)
     |  
     |  construct_object(self, node, deep=False)
     |  
     |  construct_pairs(self, node, deep=False)
     |  
     |  construct_sequence(self, node, deep=False)
     |  
     |  get_data(self)
     |  
     |  get_single_data(self)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from yaml.constructor.BaseConstructor:
     |  
     |  add_constructor(tag, constructor) from builtins.type
     |  
     |  add_multi_constructor(tag_prefix, multi_constructor) from builtins.type
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.resolver.Resolver:
     |  
     |  yaml_implicit_resolvers = {'': [('tag:yaml.org,2002:null', re.compile(...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from yaml.resolver.BaseResolver:
     |  
     |  ascend_resolver(self)
     |  
     |  check_resolver_prefix(self, depth, path, kind, current_node, current_index)
     |  
     |  descend_resolver(self, current_node, current_index)
     |  
     |  resolve(self, kind, value, implicit)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from yaml.resolver.BaseResolver:
     |  
     |  add_implicit_resolver(tag, regexp, first) from builtins.type
     |  
     |  add_path_resolver(tag, path, kind=None) from builtins.type
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from yaml.resolver.BaseResolver:
     |  
     |  DEFAULT_MAPPING_TAG = 'tag:yaml.org,2002:map'
     |  
     |  DEFAULT_SCALAR_TAG = 'tag:yaml.org,2002:str'
     |  
     |  DEFAULT_SEQUENCE_TAG = 'tag:yaml.org,2002:seq'
     |  
     |  yaml_path_resolvers = {}
    

