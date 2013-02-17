#!/usr/bin/python

import nltk
import string
						
def chunk(str):
	tl2 = [];
	str = str.replace("'","");
	sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle');
	sentences = sent_tokenizer.tokenize(str);		#Sentence Tokenization
	for i in range(len(sentences)):
		tokens = nltk.word_tokenize(sentences[i]);		#Word Tokenization		
		tagged = nltk.pos_tag(tokens);
		patterns = """NP:{<NN>+}
						 {<NNP>+}
		""";
		NPChunker = nltk.RegexpParser(patterns);
		result = NPChunker.parse(tagged);
		tl1 = result.pos();								#Parse Tree Traversal
		#Forming the vocab
		t = '';
		for j in range(len(tl1)):
			if tl1[j][1] == 'NP':
				t = t + tl1[j][0][0] + ' ';
			else:
				if t == '':
					t = t + tl1[j][0][0];
					tl2.append(t);
				else:
					t = t[0:len(t)-1];
					tl2.append(t);
					tl2.append(tl1[j][0][0]);
				t = '';
		if t != '':
			t = t[0:len(t)-1];
			tl2.append(t);
	tl2 = [''.join(c for c in s if c not in string.punctuation) for s in tl2];		#Stripping special characters
	tl2 = [s for s in tl2 if s];
	return tl2;