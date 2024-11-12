class BasicAuth(Auth):
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            print("Authorization header is None")
            return None
        if not isinstance(authorization_header, str):
            print("Authorization header is not a string")
            return None
        if not authorization_header.startswith('Basic '):
            print("Authorization header does not start with 'Basic '")
            return None
        base64_part = authorization_header[len('Basic '):]
        print("Extracted Base64 part:", base64_part)
        return base64_part

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None:
            print("Base64 authorization header is None")
            return None
        if not isinstance(base64_authorization_header, str):
            print("Base64 authorization header is not a string")
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header).decode('utf-8')
            print("Decoded Base64 value:", decoded)
            return decoded
        except Exception as e:
            print("Error decoding Base64 authorization header:", e)
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        if decoded_base64_authorization_header is None:
            print("Decoded Base64 header is None")
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            print("Decoded Base64 header is not a string")
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            print("Decoded Base64 header does not contain ':'")
            return (None, None)
        email, password = decoded_base64_authorization_header.split(":",1) # only split the 1 times 
        print("Extracted email and password:", email, password)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None or not isinstance(user_email, str):
            print("Invalid user email")
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            print("Invalid user password")
            return None
        users = User.search({'email': user_email})
        if not users or len(users) == 0:
            print("No user found with email:", user_email)
            return None
        user = users[0]
        if user.is_valid_password(user_pwd):
            print("User authenticated:", user)
            return user
        else:
            print("Invalid password for user:", user_email)
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        auth_header = self.authorization_header(request)
        if not auth_header:
            print("No Authorization header provided")
            return None
        base64_auth = self.extract_base64_authorization_header(auth_header)
        if not base64_auth:
            print("No Base64 part in Authorization header")
            return None
        decoded = self.decode_base64_authorization_header(base64_auth)
        if not decoded:
            print("Failed to decode Base64 part")
            return None
        email, password = self.extract_user_credentials(decoded)
        if not email or not password:
            print("Invalid credentials extracted")
            return None
        return self.user_object_from_credentials(email, password)