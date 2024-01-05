# Intro automation on Blender

## TODO test blender python script
- create text
- apply material
### Intro generation
- Triggered by api call
- creation of the scene using a template .blend
- make changes
- render previous to /tmp
## TODO create fastapi app
- define routes to generate an intro preview
- expose API to the internet using ngrok on local machine
- run Blender on headless
- run python script
- return video
- (improvement): upload video to bucket and return link to video
- (improvement): run inside a docker container
## TODO call the api in n8n to generate an intro using text input
- call api
- upload intro to dropbox
- send mail with dropbox link when render is finished

### n8n infrastructure

First I want to deploy the workflow using a click and an input.
I want to call the api. The api will trigger the build and the render of a preview.
I don't want to wait until the render is finished to return a response (too long).

For now I won't handle multiple request at the same time. If we had multiple request we could
implement a queue system.

Once the render is completed the backend will call a webhook on n8n. It will trigger
the process of uploading the intro to dropbox and sending a mail.

