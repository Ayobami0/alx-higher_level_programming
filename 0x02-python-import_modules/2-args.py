#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv[1:])

    print("{} {}{}".format(
        argc,
        "argument" if argc == 1 else "arguments",
        "." if argc == 0 else ":"
    ))
    for arg_idx in range(1, argc + 1):
        print("{}: {}".format(arg_idx, argv[arg_idx]))
