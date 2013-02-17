#!/usr/bin/python

import nltk
import string
import enchant
						
def chunk(str):
	tl2 = [];
	d = enchant.Dict("en_US");
	str = str.replace("'","");
	str = str.replace("- ","");
	str = str.replace("1)","p");
	str = str.replace("l)","p");
	sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle');
	sentences = sent_tokenizer.tokenize(str);		#Sentence Tokenization
	for i in range(len(sentences)):
		tokens1 = [];
		tokens2 = [];
		tokens = nltk.word_tokenize(sentences[i]);			#Word Tokenization	
		tokens = [''.join(c for c in s if c not in string.punctuation) for s in tokens];		#Stripping special characters
		tokens = [s for s in tokens if s];
		for k in range(len(tokens)):
			tokens2.append(filter(lambda s:s in string.printable,tokens[k]));
		tokens2 = filter(None, tokens2);
		for k in range(len(tokens2)):
			if d.check(tokens2[k]) == True:
				tokens1.append(filter(lambda s:s in string.printable,tokens2[k]));
		tokens1 = filter(None, tokens1);
		if len(tokens1) > 0:
			tagged = nltk.pos_tag(tokens1);
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
	return tl2;