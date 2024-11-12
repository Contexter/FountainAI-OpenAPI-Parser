from typing import Dict, Union from pydantic import RootModel

from . import *


def get_models():

return {

'callback': callback,

'link': link,

'requestbody': requestbody,

'server': server,

'encoding': encoding,

'style': style,

'header': header,

'externaldocumentation': externaldocumentation,

'parameterlocation': parameterlocation,

'openapi': openapi,

'xml': xml,

'response': response,

'operation': operation,

'oauthflow': oauthflow,

'oauthflows': oauthflows,

'example': example,

'mediatype': mediatype,

'securityschemetype': securityschemetype,

'reference': reference,

'license': license,

'components': components,

'info': info,

'parameter': parameter,

'securityscheme': securityscheme,

'discriminator': discriminator,

'servervariable': servervariable,

'tag': tag,

'pathitem': pathitem,

'contact': contact,

'schema': schema,

}
