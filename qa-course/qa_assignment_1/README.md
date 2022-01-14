# qa_assignment_1

To run a server:

```shell
cd src
sh server.sh <PORT>
```

It will run this server in a docker container.
To browse this' server output us `telnet` utility:

```shell
telnet 127.0.0.1 <PORT>
```

You will see a contents of file and checksum.
To quit from listening press `control + ]`. Then iput `quit` to exit from telnet.