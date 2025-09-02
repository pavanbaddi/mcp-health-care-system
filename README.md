## Manually run 

In Gitbash
```
D:/mcp-servers/health_care_mcp_server/.venv/Scripts/uv.EXE run --with mcp[cli] --with sqlalchemy mcp run D:/mcp-servers/health_care_mcp_server/main.py:mcp_server

clear && mcp dev main.py:server
```

## Installation
In Gitbash
```
D:/mcp-servers/health_care_mcp_server/.venv/Scripts/uv.EXE run mcp install D:/mcp-servers/health_care_mcp_server/main.py:mcp_server

D:/mcp-servers/health_care_mcp_server/.venv/Scripts/uv.EXE run mcp dev D:/mcp-servers/health_care_mcp_server/main.py:mcp_server
```

## PIP Windows configuration
```
C:\Python313\Scripts\
C:\Python313\
```

## activate VENV
```
.venv\Script\activate
source ./.venv/Script/activate
```

## Install in Claude
```
mcp install main.py:server --with-editable .
```

- mcp_app
|- src
    |- doctor
        |- models.py # this will have a doctor model id, name and specialization
        |- tools.py #this will contain tools like get the list of doctors
    |- mcp_server.py #this will contain mcp server instance that will be used by doctors/tools.py
|- main.py #this will contain mcp_server and run it
