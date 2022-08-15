#!/bin/zsh

cp publication/MoravianCalc.css output/web # copy my css file to output
scripts/addCSS.sh output/web  MoravianCalc.css # make all pages use my css file

#chmod -R go+rX output/web/*  # set permissions so they are correct when I publish to the site


read "REPLY?Ready to upload. Press enter to continue, ^C to stop."
# this is faster when there are lots of little files
tar czf - -C  output/web . | ssh user@host.edu "cd /var/www/html/apexcalc && tar xzf -"
