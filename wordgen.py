import sys
import markov

text = sys.stdin.read()
model = markov.build_model(text.split(), 3)
generated = markov.generate(model, 3)
print ' '.join(generated)