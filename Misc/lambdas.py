def check_jwt_creds(jwt_token):
    if jwt_token != "abc":
        print(jwt_token)
        raise TokenMismatchException("Session Expired")
    else:
        print("Authenticated")


class TokenMismatchException(Exception):
    """my custom exception class"""


class UnauthenticatedUser(Exception):
    """custom exception class"""


def some_decorator(f):
    def wraps(args):
        try:
            print(f"Calling function '{f.__name__}'")
            check_jwt_creds(args["jwt_token"])
        except KeyError as ez:
            raise ez
        except TokenMismatchException as e:
            raise UnauthenticatedUser
        return f(args)

    return wraps


@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")


# decorated_function('abcd')

print(some_decorator(lambda x: print("in lambda boiss"))({"jwt_token": "abkc"}))
