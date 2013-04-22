"""
Functional wrapper around argparse which allows constructing
parser in fully declerative manner.
"""
import argparse
import importlib

def create_parser(defs):
    def init_parser(parser, parser_dict):
        parser.set_defaults(**parser_dict.get('defaults', {}))
        [ parser.add_argument(*name.split(','), **opts) for name, opts in parser_dict.get('arguments', {}).items()]

        subparsers = parser_dict.get('subparsers', {})
        if len(subparsers.keys()):
            subparsers_ = parser.add_subparsers(help='sub-command help')

            for name, opts in subparsers.items():
                parents_ = filter(lambda x:x,
                    [ parents.get(p) for p in opts.get('parents', [])])
                s = subparsers_.add_parser(name, parents=parents_)
                init_parser(s, opts)
        return parser

    parents = dict([ (k, init_parser(argparse.ArgumentParser(add_help=False), v))
                 for k,v in defs.get('parent_parsers', {}).items()])
    parser = argparse.ArgumentParser(
        parents= [ parents[p] for p in defs.get('parents', [])])
    init_parser(parser, defs)
    return parser


def parse_arguments(parser):
    args = parser.parse_args()
    kwargs = dict([ (k,v) for k,v in vars(args).items() if k not in ['func']])

    parts = args.func.split(".")
    module_name, func = (".".join(parts[:-1]), parts[-1]) if len(parts) > 1 else (None, parts[0])
    if module_name:
        module = importlib.import_module(module_name)
        return getattr(module, func), kwargs
    else:
        return func, kwargs


def run(parser):
    func, kwargs = parse_arguments(parser)
    func(**kwargs)

