from afn import AFN
from afd import AFD
import itertools

class AFNtoAFD:
	@staticmethod
	def run(afn):
		afd_states = []
		afd_transitions = dict()
		afd_alfabet = afn.alfabet
		afd_final_states = []
		afd_initial_state = afn.initial_state

		for i in range(1, len(afn.states)+1):
			states = list(itertools.combinations(afn.states, i))
			
			for st in states:
				afd_states.append(list(st))

		for state in afd_states:
			afd_transitions[''.join(state)] = []

			for symbol in afd_alfabet:
				afn.actual_states = state

				try:
					afn.make_transition(symbol)
					afd_transitions[''.join(state)].append((symbol, ''.join(sorted(afn.actual_states))))
				except:
					pass

		for state in afd_states:
			afn.actual_states = state 

			if afn.is_final():
				afd_final_states.append(''.join(state))

		aux = []

		for state in afd_states:
			aux.append(''.join(state))

		afd_states = aux

		new_afd = AFD(afd_alfabet, afd_states, afd_initial_state, afd_final_states)

		for origin in afd_states:
			for symbol, dest in afd_transitions[origin]:
				new_afd.insert_transition(origin, dest, symbol)

		return new_afd
