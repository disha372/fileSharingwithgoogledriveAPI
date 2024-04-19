from Google import Create_Service

CLIENT_SECRET_FILE = 'client-secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Update Sharing Setting
file_id = '<file id>'

request_body = {
    'role': 'reader',
    'type': 'anyone'
}

response_permission = service.permissions().create(
    fileId=file_id,
    body=request_body
).execute()

print(response_permission)


# Print Sharing URL
response_share_link = service.files().get(
    fileId=file_id,
    fields='webViewLink'
).execute()
