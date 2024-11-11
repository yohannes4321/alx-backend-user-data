import re
from typing import List
# i am using for regular expersion 
def filter_datum(fields:List[str],redaction:str,message:str,separator:str)->str:
    for field in fields:
        message=re.sub(f"{field}=.*?{separator}",f"{field}={redaction}{separator}",message)
    return message
        # this is regex expersion to obscute fields value and replace by the reducation string
        #pattern replaced_value real string
