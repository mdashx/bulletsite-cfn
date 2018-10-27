import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("out")
    parser.parse_args()
    args = parser.parse_args()

    cfn_template = "Build template."

    with open(args.out, "w") as fh:
        fh.write(cfn_template)
