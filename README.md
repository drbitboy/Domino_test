### Simple Domino printer server emulation

Cf. https://www.plctalk.net/qanda/showthread.php?t=129352

Usage
----

    % ### Start server repeatedly in a loop
    % while sleep 1 ; do python dominoserver.py || break ; end &
    [1] <PID>

    % ### Make a client calll
    % python dominoclient.py 127.0.0.1 3 34 23-Jan-07 0374 11 16.38 605

    % ### Stop server
    % kill %1

TODO
----

Add printer response
