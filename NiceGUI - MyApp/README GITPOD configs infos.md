GITPOD configs, infos


https://github.com/aknip/three.js-Experiments/blob/main/.gitpod.yml
tasks:
  - name: Open files
    command: gp open README.md && gp open node-js/app/src/visual01/index.html

  - name: Parcel -g
    init: npm install parcel -g

  - name: Start
    command: cd node-js/app && npm install && npm run start
    openMode: split-right




https://github.com/aknip/hardhat-tests/blob/main/.gitpod.yml
tasks:
  - name: Open the readme, contract and test
    command: gp open contracts/Token.sol && gp open test/Token.js && gp open README.md
  
  - name: Hardhat server
    init: npm install
    command: npx hardhat node

  - name: Frontend server
    command: npx hardhat --network localhost run scripts/deploy.js && cd frontend && npm install && npm run start
    openMode: split-right










https://github.com/aknip/phaser-01/blob/main/.gitpod.yml
image: gitpod/workspace-full
vscode:
  extensions:
    - ritwickdey.liveserver
    - abusaidm.html-snippets
    - Zignd.html-css-class-completion
    - ctf0.save-editors-layout





# phaser-01

Start with: https://gitpod.io/#https://github.com/aknip/phaser-01

More infos about Gitpod and static HTML:
- https://community.gitpod.io/t/open-preview-equivalent-for-a-static-html-file/1320/4
- https://www.gitpod.io/docs/languages/html


# Gitpod tips & tricks

## Shortcuts
CMD SHIFT P : Comman Palette

## Browser preview
- View - Command Palette: Simple Browser
- URL is current gitpod-URL with a prefix "5500-" or "9000-" (the portnumber)
- Option 1: 
    - Open live preview by clicking buttom right: "Go live"
- Option 2: 
    - npm install http-server -g
    - http-server -p 9000


## Notes
Install "Save Editors layout": Download from Github, unzip, create .vsix, upload .vsix to Gitpod, install extension
- https://github.com/ctf0/vscode-save-editor-layout
- https://code.visualstudio.com/api/working-with-extensions/publishing-extension
- https://stackoverflow.com/questions/42017617/how-to-install-vs-code-extension-manually