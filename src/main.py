import argparse

parser = argparse.ArgumentParser(
    prog="ddl_exporter",
    description="This is demo for argparse library.",
    epilog="Powered by Souhei.H"
)

# 位置による引数の取得
parser.add_argument(
    "schema"
)

# 位置による引数の取得（任意）
parser.add_argument(
    "table",
    nargs="?",
)

# 真理値のオプション引数の取得
parser.add_argument(
    "-s",
    "--silent",
    dest="isSilent",
    action="store_true",
    help="show export progress"
)

# リスト形式の引数を取得 #1
# -e hoge fuga
# parser.add_argument(
#     "-e",
#     "--env",
#     dest="envs",
#     nargs="*",
# )

# リスト形式の引数を取得 #2
# -e hoge -e fuga
parser.add_argument(
    "-e",
    "--env",
    dest="envs",
    action="append"
)

args = parser.parse_args()

print(args.schema)
print(args.table)
print(args.isSilent)
print(args.envs)
