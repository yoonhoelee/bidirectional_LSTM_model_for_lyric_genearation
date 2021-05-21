# Bidirectional_LSTM_model_for_lyric_generation

[Tensorflow LSTM](https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM)


## Project Overview

Based on my experience working in the music industry, one of the most serious problems that artists face is not be stuck in a stalemate where they cannot come up with new content, which is more commonly known as "writer's block".
I realized that this issue could be alleviated with the help of LSTM models that are trained based on their past lyrics.


## Packages and Frameworks that were used

*   Keras (2.4.3)
*   Tensorflow (2.3.0)
*   Django (3.1.7)
*   Python (3.8.5)


## Reasons for using Bidirectional LSTM

There is no doubt that the field of NLP studies has improved dramatically after the introduction of BERT.
However, the downside of BERT when generating lyrics of poetry is that it is attention based and does not learn all aspects of a sentence equally.
Since there are many cases in song lyrics where words or grammar is butchered intentionally for poetic purposes, I believed that the implementation of a LSTM model which learns all aspects of a given sentence equally would be more effective.


## Artists

The lyrics of the songs that are used to train the models are based on the following artists

*   Drake
*   BTS
*   Cardi B
*   Bad Bunny
*   Eminem


Due to memory constraints the model webapp I deployed on Heroku consists of models trained with the lyrics of the following artists

*   BTS
*   Bad Bunny

*   [Web-app deployed on Heroku](https://lyric-generation.herokuapp.com/)


## Limitations

The models were trained on a single GPU environments.
Consequently, the models are trained on a limited amount of data and epochs.
The accuracy of the BTS model is especially low as BTS tends to mix Korean and English in their songs.


## References

*   [Tensorflow-Irish songs generator Colab](https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/TensorFlow%20In%20Practice/Course%203%20-%20NLP/Course%203%20-%20Week%204%20-%20Lesson%202%20-%20Notebook.ipynb)
*   [ Harrison Gill, Daniel (Taesoo) Lee, Nick Marwell; Deep Learnining in Musical Lyric Generation: An LSTM_Based Approach(Sept.2020) ](https://yurj.yale.edu/sites/default/files/deep_learning_in_musical_lyric_generation_an_ltsm_based_approach.pdf)
*   [Cheng-Zhi, Anna Huang; Deep Learning for Music Composition: Generation, Recommendation and Control (April. 2019) ](https://dash.harvard.edu/bitstream/handle/1/42029468/HUANG-DISSERTATION-2019.pdf?sequence=1&isAllowed=y)
*   [Deborah Liske; Lyric Generation with Deep Learning (August. 2019) ](https://www.youtube.com/watch?v=T7NEwx_dLRU&ab_channel=DebbieLiske)



## Authors

*   Adam Lee, ubrain0624@gmail.com, [github](https://github.com/yoonhoelee)
