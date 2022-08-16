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

Deploy to api folder: git subtree push --prefix api heroku master

- [x] Todo: fix logic when runs more time
- [x] Todo: add back the load spin
- [x] Todo: split JScode into modules
- [ ] Todo: add validation and avoid XSS on input
- [x] Todo: Eventlet
    - [x] persist connection
    - [x] reconnect socket on reload
    - [x] Find and solve eventlet errors


- [x] Todo: Deploy
    - [x] set Postgesql Database
    - [x] deploy subfolder
    - [x] use dotenv
    - [x] close driver on disconnect
    - [x] set server on client
    - [x] Deploy Backend/frontend with server, in heroku and netlify


- [ ] Todo: error handling:
    - add telegram error msg and screenshoot check

- [ ] Todo: logging
    - [ ] remove logging error print on screen
    - [ ] None = "Vaga não encontrada"

- [ ] Todo: Seo - add SEO tecnictes on the website
    - [ ] Add custom domain
    - [ ] Add SSL
    - [ ] Add https
    - [ ] set h1 tags
    - [ ] set propagandas

- [ ] Todo: Monetize
    - [ ] add key methdo to expire after some time
    - [ ] add payment method