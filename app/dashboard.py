import streamlit as st

from msal_streamlit_authentication import msal_authentication


value = msal_authentication(
    auth={
        "clientId": "aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "authority": "https://login.microsoftonline.com/aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    login_request={
        "scopes": ["aaaaaaa-bbbb-cccc-dddd-eeeeeeeeeee/.default"]
    },
    key=1)
st.write("Received", value)
