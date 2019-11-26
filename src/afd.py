class AFD:
	def __init__(self, alfabet, states, initial_state, final_states):
		self.alfabet = alfabet
		self.states = states
		self.initial_state = initial_state
		self.final_states = final_states
		self.actual_state = initial_state

		self.transitions = dict()

		for state in self.states:
			self.transitions[state] = []

	def show(self):
		print('Alfabeto (∑) -> {0}'.format(self.alfabet))
		print('Conjunto de Estados (Q) -> {0}'.format(self.states))
		print('Estado Inicial -> \'{0}\''.format(self.initial_state))
		print("Conjunto de Estados Finais (F) -> {0}".format(self.final_states))

		print("Transições:")
		for state in self.states:
			print("{0} -> {1}".format(state, self.transitions[state]))

		print("\n---------------------\n")


	def check_symbol(self, symbol):
		if symbol not in self.alfabet:
			raise Exception("Função programa não definida para o símbolo -> {0}.".format(symbol))

	def check_state(self, state):
		if state not in self.states:
			raise Exception("Estado não presente no autômato definido -> {0}.".format(state))

	def is_final(self):
		if self.actual_state in self.final_states:
			return True

		return False

	def insert_transition(self, origin, dest, symbol):
		self.check_symbol(symbol)
		self.check_state(origin)
		self.check_state(dest)


		for transition in self.transitions[origin]:
			if symbol == transition[0]:
				raise Exception("Transição inválida, o símbolo {0} já está sendo usado em uma transição".format(symbol))


		self.transitions[origin].append((symbol, dest))

	def make_transition(self, symbol):
		self.check_symbol(symbol)

		new_state = None

		for transition in self.transitions[self.actual_state]:
			if transition[0] == symbol:
				new_state = transition[1]

		if new_state == None:
			raise Exception("Não há transições do estado {0} com o símbolo {1}.".format(self.actual_state, symbol))

		self.actual_state = new_state

	def read_word(self, word):
		self.actual_state = self.initial_state

		for symbol in word:
			self.make_transition(symbol)

		return self.is_final()

