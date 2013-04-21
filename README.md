# fargparse

Package fargparsw is a wrapper around command line argument parsing package
`argparse`. It helps using `argparse` in more declarative way, specifing
all command line behaviour in python dict.

## Typical usage

Specify command line arguments in python dict:

    ARGS = {
      "arguments": {
          "-d,--debug": {"dest":"debug", "default": False, "action": "store_true"},
      },
      "subparsers": {
            "unlink": {
              "defaults": {"func": "database.unlink_navision_documents"}
            },
            "ensure-indexes": {
              "defaults": {"func": "database.ensure_indexes"}
            },        
      }
    }

Then call `create_parser(ARGS)` to create tree 
structure of `argparse.ArgumentParser` and then call `parse_arguments(parser)`
to get function to run and keyword arguments to run it with:

    function, kwargs = parse_arguments(create_parser(ARGS))
    function(**kwargs)

Function will be xtracted from `func` variable of the returned `Namespace`. If
func is of form `module.submodule.func` all modules will be loaded automatically.

There is also a convinience function `run` which parses command line
arguments and run deduced function in one step.
