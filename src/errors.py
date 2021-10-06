class ServerError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(ServerError, self).__init__(message)


class SignatureVerificationError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(SignatureVerificationError, self).__init__(message)
