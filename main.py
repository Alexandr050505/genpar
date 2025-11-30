"""
Главный модуль для генератора паролей.
"""

import argparse
import sys
import os

if sys.platform == "win32":
    os.system('chcp 65001 > nul')
    sys.stdout.reconfigure(encoding='utf-8')

from passgen.commands import handle_generate, handle_save, handle_find, handle_list, handle_delete


def main():
    parser = argparse.ArgumentParser(description='Password Generator with Database Storage')

    parser.add_argument('--generate', '-g', action='store_true')
    parser.add_argument('--length', '-l', type=int, default=12)
    parser.add_argument('--uppercase', '-u', action='store_true')
    parser.add_argument('--digits', '-d', action='store_true')
    parser.add_argument('--special', '-s', action='store_true')

    parser.add_argument('--save', action='store_true')
    parser.add_argument('--service')
    parser.add_argument('--login')

    parser.add_argument('--find')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('--delete')

    args = parser.parse_args()

    if args.generate:
        password = handle_generate(args)
        print(f"Password: {password}")

        if args.save and args.service:
            if not args.login:
                print("Error: --login is required when saving password")
                return
            handle_save(args.service, args.login, password)
            print("Password saved!")

    if args.find:
        result = handle_find(args.find)
        if result:
            print(f"Service: {args.find}")
            print(f"Login: {result['login']}")
            print(f"Password: {result['password']}")
        else:
            print(f"No password found for service: {args.find}")

    if args.list:
        passwords = handle_list()
        if passwords:
            print("\nSaved Passwords:")
            print("-" * 50)
            for pwd in passwords:
                print(f"Service: {pwd['service']}")
                print(f"Login: {pwd['login']}")
                print(f"Created: {pwd['created_at']}")
                print("-" * 30)
        else:
            print("No passwords saved yet.")

    if args.delete:
        if handle_delete(args.delete):
            print(f"Password for service '{args.delete}' deleted successfully")
        else:
            print(f"No password found for service: {args.delete}")


if __name__ == "__main__":
    main()