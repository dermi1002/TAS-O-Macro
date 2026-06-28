import argparse
import frameadvance
import keyboardaction


def add_commands():
    parser = argparse.ArgumentParser(
        prog='Frame Advance CLI Test',
        description='Uses xspeedhack to advance one frame.',
    )

    parser.add_argument(
        'framerate',
        type=int,
        help='How many pictures go by in a second, usually 30 or 60'
    )
    parser.add_argument(
        'process',
        type=str,
        help='Name of Application running'
    )
    parser.add_argument(
        'arch',
        type=str,
        help='CPU architecture the Application is built for'
    )
    parser.add_argument(
        '-u',
        '--userkey',
        type=str,
        default='v',
        help='User-defined alphaneumeric key to call advance one frame; special keys cannot be used.'
    )

    args = parser.parse_args()

    print(
        "Framerate:", args.framerate,
        "Process:", args.process,
        "Process' Arch:", args.arch,
        "User-defined Key", args.userkey
    )

    # frameadvance.placeholder_define_process(args.process, args.arch)
    frameadvance.define_process(args.process, args.arch)
    keyboardaction.keyboard_listener(args.userkey, args.framerate)

def main():
    add_commands()

if __name__ == '__main__':
    main()