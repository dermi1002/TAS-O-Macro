import argparse
import frameadvance


def add_commands():
    parser = argparse.ArgumentParser(
        prog='Frame Advance CLI Test',
        description='Uses xspeedhack to advance one frame.',
    )

    parser.add_argument('framerate', type=int, help='How many pictures go by in a second, usually 30 or 60')
    parser.add_argument('process', type=str, help='Name of Application running')
    parser.add_argument('arch', type=str, help='CPU architecture the Application is built for')
    parser.add_argument(
        '-u',
        '--userkey',
        type=str,
        default='v',
        help='User-defined key to call advance one frame')

    args = parser.parse_args()

    print(args.framerate, args.process, args.arch, args.userkey)

    # frameadvance.keyboard_action(args.userkey)

def main():
    add_commands()

if __name__ == '__main__':
    main()