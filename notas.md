open = 0
close = 1

taskkill /F /IM "chrome.exe" /T

- [x] Todo: find a way to avoid refresh when emit job to client/server (File, database, etc)
    - [/] Use File handler
    - [/] Use Database(SQLite)
    - [/] Use async/await
    - [/] Use Different Thread
    - [x] ignore and procced with adapt UI
    - [/] use eventlet
    - [/] remove form tag
    - [/] use innerText instead of innerHTML
    - [x] use cloud database


- [x] Todo: fix logic when runs more time
- [x] Todo: add back the load spin
- [x] Todo: split JScode into modules
- [ ] Todo: add validation and avoid XSS on input
- [ ] Todo: Eventlet
    - [x] persist connection
    - [ ] reconnect socket on reload
    - [ ] Find and solve eventlet errors


- [ ] Todo: Deploy
    - [x] set Postgesql Database
    - [ ] deploy subfolder
    - [ ] use dotenv
    - [ ] set server on client
    - [ ] Deploy Backend/frontend with server, in heroku and netlify
    - [ ] find erros and solve-it 