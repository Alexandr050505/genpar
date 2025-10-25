from .generator import generate_password
from .storage import save_password, find_password

def handle_generate(args):
    return generate_password(
        length=args.length,
        use_upper=args.uppercase,
        use_digits=args.digits,
        use_special=args.special
    )

def handle_save(service, login, password):
    save_password(service, login, password)

def handle_find(service):
    return find_password(service)