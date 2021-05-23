from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "angular-test-ad2e1-firebase-adminsdk-3gg7g-73b112bf06.json", scopes=scopes)

# Or, use the token directly, as described in the "Authenticate with an
# access token" section below. (not recommended)
request = Request()
credentials.refresh(request)
access_token = credentials.token

print('Here comes the token')
print(access_token)
