A lightly modified version of [APEX calculus](https://www.apexcalculus.com/) for use at Moravian University.  Written in [Pretext XML](https://pretextbook.org/).


To compile:
* instal Pretext command line tool following [instructions on their site](https://pretextbook.org/doc/guide/html/quickstart-getting-pretext.html)

* if you make changes to figures, need to recompile them with `pretext build -g`

* once figures are built, compile the site with `pretext build web`

* If you edit project.ptx you can build just one chapter/section using `pretext build subset`


Finally, I add my css and publish to my server using `scripts/publish_to_webwork.sh`

