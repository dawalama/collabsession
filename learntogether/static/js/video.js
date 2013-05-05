window.addEventListener("load", loaded);
function loaded() {
    var api_key = "1127";
    var session_id = "2_MX4xMTI3fn5TYXQgTWF5IDA0IDIwOjMwOjQwIFBEVCAyMDEzfjAuMDgyMjAyOTF-";
    var token = "T1==cGFydG5lcl9pZD0xMTI3JnNpZz0xODFiNzM2NzcyY2MxYzc4MGY4MGI1M2E1MjZkYjhmYTZhNzQ5ZDlhOnNlc3Npb25faWQ9Ml9NWDR4TVRJM2ZuNVRZWFFnVFdGNUlEQTBJREl3T2pNd09qUXdJRkJFVkNBeU1ERXpmakF1TURneU1qQXlPVEYtJmNyZWF0ZV90aW1lPTEzNjc3MjQ3MTQmbm9uY2U9Njc1MjE0JnJvbGU9cHVibGlzaGVy";

    var session = TB.initSession(session_id);
    var _streams = [];

    var linkUrl;
    if (window.location.search) {
        linkUrl = window.location;
    } else {
        linkUrl = window.location + '?sessionId=' + session_id;
    }
    $('#shareUrlInput').val(linkUrl);
    $('#shareUrlLink').attr("href", linkUrl);

    TB.setLogLevel(TB.DEBUG);

    session.addEventListener("sessionConnected", sessionConnectedHandler);
    session.addEventListener("streamCreated", streamCreatedHandler);
    session.addEventListener("streamDestroyed", streamDestroyedHandler);
    session.connect(api_key, token);

    function sessionConnectedHandler(event) {
        var div = document.createElement("div");
        div.setAttribute("id", "publisher");

        var container = document.getElementById("stream-container-1");
        container.appendChild(div);


        /*
           if (version == "v2") {
           $("#publisher").append("<div id='allowFloater'>Allow access to your camera.</div>");
           function animateFloater() {
           $("#allowFloater").animate({top: "7"}, 500).delay(5).animate({top: "17"}, 500);
           }
           setInterval(animateFloater, 1100);
           }
           */

        var publisher = TB.initPublisher(api_key, "publisher");
        session.publish(publisher);

        subscribeToStreams(event.streams);
    }

    function streamCreatedHandler(event) {
        subscribeToStreams(event.streams);
    }

    function streamDestroyedHandler(event) {
        for (var i = 0; i < event.streams.length; i++) {
            var stream = event.streams[i];
            _streams.splice(_streams.indexOf(stream), 1);
        }
    }

    function subscribeToStreams(streams) {
        for (var i = 0; i < streams.length; i++) {
            if (_streams.length >= 4) {
                return;
            }

            var stream = streams[i];
            _streams.push(stream);

            // Make sure we don't subscribe to ourself
            if (streams[i].connection.connectionId == session.connection.connectionId) {
                //$("#allowFloater").fadeOut('fast');
                return;
            }

            var containerDivId;
            // Get the first strema container without a stream
            $(".stream-container").each(function(index, container) { 
                if (!containerDivId && $(this).children().length == 0) {
                    containerDivId = this.id;
                }
            });

            if (!containerDivId) {
                return;
            }

            // Create the div to put the subscriber element in to
            var div = document.createElement('div');
            div.setAttribute('id', 'stream' + streams[i].streamId);

            var container = document.getElementById(containerDivId);
            container.appendChild(div);

            // Subscribe to the stream
            session.subscribe(streams[i], div.id);
        }
    }
    /*
    // Handle copy to clipboard
    $("input").on("mouseup", function(event) {
        $(this).select();
    });
    */
}

