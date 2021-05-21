from django.shortcuts import render
from keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from . import sample_lyric


def home(request):
    return render(request, 'home.html')


def lygen(request):
    seed_text=request.POST.get('lyric')
    next_words=int(request.POST.get('next'))
    nm=request.POST.get('model')
    
    if nm == 'bts':
        tokenizer = Tokenizer() 
        model = load_model('./models/bts_gen.h5')
        max_sequence_len = 10403
        tokenizer.fit_on_texts(sample_lyric.bts10)


    elif nm == 'drake':
        tokenizer = Tokenizer() 
        model = load_model('./models/drake_gen.h5')
        max_sequence_len = 5648
        tokenizer.fit_on_texts(sample_lyric.dr10)


    elif nm == 'cardi_b':
        tokenizer = Tokenizer() 
        model = load_model('./models/cb_gen.h5')
        max_sequence_len = 4385
        tokenizer.fit_on_texts(sample_lyric.cardi10)

    
    elif nm == 'bad_bunny':
        tokenizer = Tokenizer() 
        model = load_model('./models/bb_gen.h5')
        max_sequence_len = 4608
        tokenizer.fit_on_texts(sample_lyric.cardi10)


    elif nm=='eminem':
        tokenizer = Tokenizer() 
        model = load_model('./models/em_gen.h5')
        max_sequence_len = 7193
        tokenizer.fit_on_texts(sample_lyric.em10)

        
    for x in range(next_words):
	    token_list = tokenizer.texts_to_sequences([seed_text])[0]
	    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
	    predicted = model.predict_classes(token_list, verbose=0)
	    output_word = ""
	    for word, index in tokenizer.word_index.items():
		    if index == predicted:
			    output_word = word
			    break
	    seed_text += " " + output_word

    context = {'seed_text':seed_text}

    return render(request, 'home.html', context)