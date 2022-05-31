import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys


def setup_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "selector", help="fetch output for matching entities", nargs='?')
    parser.add_argument(
        "--format", help="format of the output", default="json",
        choices=["json", "yaml", "text"])
    parser.add_argument(
        "--kind", help="scope selector to", default="objective",
        choices=["objective", "score", "scorecard"])
    parser.add_argument(
        "--save-as", help="save results to given file path", default="stdout")
    parser.add_argument(
        "--if-no-budget-then",
        help="warn or exit the job if no budget is left for the entities "
             "(requires format to be json)",
        choices=["warn", "fail", "noop"])
    return parser


def run():
    parser = setup_parser()
    args = parser.parse_args()

    c = f'{shutil.which("reliably")} --no-color status'

    if args.format:
        c = f"{c} --format {args.format}"

    if args.kind:
        c = f"{c} --kind {args.kind}"

    if args.selector:
        c = f"{c} --selector {args.selector}"

    c = shlex.split(c)
    p = subprocess.run(
        c, text=True, capture_output=True, encoding="utf-8",
        env=os.environ)
    p.check_returncode()

    result = p.stdout.strip()

    if result is None:
        print("no matching resources found")
        return

    if args.save_as not in [None, "noop", "stdout"]:
        with open(args.save_as, "w") as f:
            f.write(result)
    elif args.save_as == "stdout":
        print(result)
    
    if args.format == "json" and args.if_no_budget_then not in [None, "noop"]:
        lacking_budget = []
        for d in json.loads(result):
            if d["has_budget"] is False:
                if args.if_no_budget_then == "fail":
                    sys.exit(1)
                elif args.if_no_budget_then == "warn":
                    lacking_budget.append(
                        f'{d["name"]} => Current: {d["current"]}% - '
                        f'Target: {d["target"]}%')

        if lacking_budget:
            print("The following objectives have no budget left:")
            print("\n- " + "\n- ".join(lacking_budget))


if __name__ == '__main__':
    run()