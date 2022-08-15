#!/bin/bash
 
sed -I '' 's/\\left\\langle/\\la/g' "$1"
sed -I '' 's/\\right\\rangle/\\ra/g' "$1"
sed -I '' 's|<em>         </em>|<fillin/>|g' "$1"


# somehow grab the next character then capitalize?
# In Exercises [0-9]*–[0-9]*[ ]*,