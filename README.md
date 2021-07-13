# I3 Essential Open Patent Datasets Tracker

This repository is set up to track and version updates to the [I3 Essential Open Patent Datasets Index](https://docs.google.com/spreadsheets/d/1bdyhGrj0oNz-_qW3Rv2GNGqhZZ73rgj-DYWePLA_1Ms/edit#gid=1389884911), which includes the index itself, and a catalog comparing repositories used by members of the community. It looks for changes at 00:00 UTC daily, and pushes an update if any are discovered.

The versioned sheets may be accessed in the folder `index_archive`. If you'd like to browse and query either sheet, you can do so using Github's Flat Data tool [here](https://flatgithub.com/Innovation-Information-Initiative/Dataset-Index-Sheet-Tracker?filename=index_archive%2FOpen_Patent_Datsets.csv&filters=&sha=50624ec98ff61d670b75aa9f9206650395bc624b&sort=Title%2Casc&stickyColumnName=Title).

The Github Action that pulls the sheet is based on Dolthub's [Gsheets-to-csv](https://github.com/dolthub/gsheets-to-csv) action.