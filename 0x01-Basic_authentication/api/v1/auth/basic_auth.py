from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
from models.user import User
class BasicAuth(Auth):
    def extract_base64_authorization_header(self,authorization_header:str)->str:
      
        if authorization_header is None:
            return None
        if  not isinstance(authorization_header,str):
            return None
        auth=authorization_header
         
         
        if not  auth.startswith('Basic '):
            return None
        
        return authorization_header[len('Basic '):]
        
    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        
        if base64_authorization_header is None:
            return None
        if not  isinstance(base64_authorization_header,str):
            return None
        try:
            decoded=base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except:
            None
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        if decoded_base64_authorization_header is None:
            return (None,None)
        if not isinstance(decoded_base64_authorization_header,str):
            return (None,None)
        if ':' not in decoded_base64_authorization_header:
            return (None,None)
        value1=decoded_base64_authorization_header.split(':')[0]
        value2=decoded_base64_authorization_header.split(':')[1]
        return (value1,value2)
    def user_object_from_credentials(self,user_email:str,user_pwd:str)->TypeVar('user'):
        if user_email is None or  not isinstance(user_email,str):
            return None
        if user_pwd is None or not isinstance(user_pwd,str):
            return None
        
        user=User.search({'email':user_email})
        if not user or len(user)==0:
            return None
        user=user[0] # becuase this is list 
        if user.is_valid_password(user_pwd):
            return user
        else:
            None

        
       