Once you ssh into vagrant@10.****** :
[command line]

- run the following to make sure pio works:
export PATH=$PATH:$HOME/predictionio/apache-predictionio-0.10.0-incubating/PredictionIO-0.10.0-incubating/bin/

- to access engines (say MyClassification1):
cd predictionio/apache-predictionio-0.10.0-incubating/MyClassification1

- to train
pio train

- to deploy
pio deploy

- to delete the data
pio app data-delete <app name>
one of the app names is acceptancePrediction 

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

use pacora:8000 to access dashboard