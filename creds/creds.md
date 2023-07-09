Create a `creds.json` file in this directory with the following format:

```json

{
    "client_id": "your client id",
    "client_secret": "your client secret",
    "user_agent": "your user agent",
    "username": "your username",
    "password": "your password"
}

```
How to get the client id and client secret:
1. Go to https://www.reddit.com/prefs/apps
2. Click on "create another app..."
3. Fill in the details and select "script"
4. Copy the client id and client secret

User agent can be anything you want, but it is recommended to use the following format:
`<platform>:<app ID>:<version string> (by /u/<reddit username>)`

Example:
```
User-Agent: android:com.example.myredditapp:v1.2.3 (by /u/kemitche)
```