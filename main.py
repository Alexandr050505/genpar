import argparse
from passgen.commands import handle_generate, handle_save, handle_find


def main():
    parser = argparse.ArgumentParser(description='Password Generator')

    parser.add_argument('--generate', '-g', action='store_true')
    parser.add_argument('--length', '-l', type=int, default=12)
    parser.add_argument('--uppercase', '-u', action='store_true')
    parser.add_argument('--digits', '-d', action='store_true')
    parser.add_argument('--special', '-s', action='store_true')

    parser.add_argument('--save', action='store_true')
    parser.add_argument('--service')
    parser.add_argument('--login')

    parser.add_argument('--find')

    args = parser.parse_args()

    if args.generate:
        password = handle_generate(args)
        print(f"Password: {password}")

        if args.save and args.service:
            handle_save(args.service, args.login, password)
            print("Password saved!")

    if args.find:
        result = handle_find(args.find)
        if result:
            print(f"Service: {result['service']}")
            print(f"Login: {result['login']}")


if __name__ == "__main__":
    main()