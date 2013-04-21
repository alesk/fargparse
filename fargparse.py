"""
Functional wrapper around argparse which allows constructing
parser in fully declerative manner.
"""
import argparse
import importlib

def create_parser(parser_defs):

    def init_parser(parser, parser_dict):
        parser.set_defaults(**parser_dict.get('defaults', {}))
        [parser.add_argument(*name.split(','), **opts) for name, opts in parser_dict.get('arguments', {}).items()]

        subparsers = parser_dict.get('subparsers', {})
        if len(subparsers.keys()):
            subparsers_ = parser.add_subparsers(help='sub-command help')
            for name, opts in subparsers.items():
                s = subparsers_.add_parser(name)
                init_parser(s, opts)

    parser = argparse.ArgumentParser()
    init_parser(parser, parser_defs)
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

