#!/bin/zsh

cp publication/MoravianCalc.css output/web # copy my css file to output
scripts/addCSS.sh output/web  MoravianCalc.css # make all pages use my css file

#chmod -R go+rX output/web/*  # set permissions so they are correct when I publish to the site


read "REPLY?Ready to upload. Press enter to continue, ^C to stop."
## this was too slow: scp -r output/html/* wwadmin@webwork.moravian.edu:/var/www/apexcalc/
tar czf - -C  output/web . | ssh frabonim@webwork.moravian.edu "cd /var/www/html/apexcalc && tar xzf -"
