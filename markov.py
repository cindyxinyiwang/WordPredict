import random
import string

class markov:
	def __init__(self, filepath):
		self.model = None
		self.text = self.read_file(filepath)

	def build_model(self, tokens, n):
		model = dict()
		if len(tokens) < n:
			return model
		for i in range(len(tokens) - n):
			gram = tuple(tokens[i:i+n])
			next_token = tokens[i+n]
			if gram in model:
				model[gram].append(next_token)
			else:
				model[gram] = [next_token]
		final_gram = tuple(tokens[len(tokens)-n:])
		if final_gram in model:
			model[final_gram].append(None)
		else:
			model[final_gram] = [None]
		return model

	def build_model_word(self, n):
		model = dict()
		tokens = self.text.strip().split(" ")
		if len(tokens) < n:
			return model
		for i in range(len(tokens) - n):
			gram = tuple(tokens[i:i+n])
			next_token = tokens[i+n]
			if gram in model:
				model[gram].append(next_token)
			else:
				model[gram] = [next_token]
		final_gram = tuple(tokens[len(tokens)-n:])
		if final_gram in model:
			model[final_gram].append(None)
		else:
			model[final_gram] = [None]
		self.model = model

	def next_word(self, myStr):
		""" generate the next word based on input myStr """
		prevTokens = tuple(myStr.strip().split(" "))
		n = len(prevTokens)
		if n < 1:
			return None
		self.build_model_word(n)
		next_token = prevTokens[0]
		if prevTokens in self.model:
			return random.choice(self.model[prevTokens])
		else:
			return None

	def next_words(self, myStr, genLen):
		""" generate a string with length genLen based on the input myStr """
		prevTokens = tuple(myStr.strip().split(" "))
		n = len(prevTokens)
		if n < 1:
			return None
		self.build_model_word(n)
		next_token = prevTokens[0]
		output = self.generate(self.model, n, prevTokens, genLen)
		return ' '.join(output)

	def build_model_char(self, n):
		model = dict()
		tokens = self.text
		if len(tokens) < n:
			return model
		for i in range(len(tokens) - n):
			gram = tuple(tokens[i:i+n])
			next_token = tokens[i+n]
			if gram in model:
				model[gram].append(next_token)
			else:
				model[gram] = [next_token]
		final_gram = tuple(tokens[len(tokens)-n:])
		if final_gram in model:
			model[final_gram].append(None)
		else:
			model[final_gram] = [None]
		self.model = model

	def generate(self, model, n, seed=None, max_iterations=100):
		if seed is None:
			seed = random.choice(model.keys())
		output = list(seed)
		current = tuple(seed)
		for i in range(max_iterations):
			if current in model:
				possible_next_tokens = model[current]
				next_token = random.choice(possible_next_tokens)
				if next_token is None: break
				output.append(next_token)
				current = tuple(output[-n:])
			else:
				break
		return output

	def read_file(self, filepath):
		with open(filepath, "r") as file:
			return file.read()

	def word_level_gen(self, n):
		tokens = self.text.strip().split(" ")
		self.model = self.build_model(tokens, n)
		result = self.generate(self.model, n)
		out = ' '.join(result)
		return out

	def char_level_gen(self, n):
		tokens = self.text
		self.model = self.build_model(tokens, n)
		result = self.generate(self.model, n)
		out = ''.join(result)
		return out

if __name__ == '__main__':
	import sys
	n = int(sys.argv[1])
	filepath = sys.argv[2]
	mk = markov(filepath)
	"""print mk.word_level_gen(n)"""
	print mk.next_words("Sometimes", 20)