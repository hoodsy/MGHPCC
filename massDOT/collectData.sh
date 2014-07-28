#!/bin/sh

while true; do
    python -c 'import store; store.feed("http://www.massdot.state.ma.us/feeds/traveltimes/RTTM_feed.aspx", "travelTimes")'
    sleep 45
done