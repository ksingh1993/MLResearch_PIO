# MLResearch_PIO

Once you ssh into vagrant@10.******

to export path:
export PATH=$PATH:$HOME/predictionio/apache-predictionio-0.10.0-incubating/PredictionIO-0.10.0-incubating/bin/

to access engines (say MyClassification1):
cd predictionio/apache-predictionio-0.10.0-incubating/MyClassification1

pio app data-delete <app name>
one of the app names is acceptancePrediction 

use pacora:8000 to access dashboard