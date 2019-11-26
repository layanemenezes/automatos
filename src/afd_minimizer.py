from afd import AFD
import itertools

class AFDMinimizer:
	@staticmethod
	def run(afd):
		afd_states = AFDMinimizer.remove_inacessible(afd) + ['temp']
		afd_final_states = list(afd.final_states)
		afd_alfabet = afd.alfabet
		afd_transitions = dict(afd.transitions)
		afd_initial_state = afd.initial_state

		st_pairs = list(itertools.combinations(afd_states, 2))

		st_lists = dict()
		st_mark = dict()

		st_pairs = [tuple(sorted(list(p))) for p in st_pairs]

		for st_pair in st_pairs:
			st_lists[st_pair] = []
			st_mark[st_pair] = ''

		for st_pair in st_pairs:
			count_finals = 0

			if st_pair[0] in afd_final_states:
				count_finals += 1

			if st_pair[1] in afd_final_states:
				count_finals += 1

			if count_finals == 1:
				st_mark[st_pair] = 'X'

			for symbol in afd_alfabet:
				afd.actual_state = st_pair[0]

				try:
					afd.make_transition(symbol)
					st1_r = afd.actual_state
				except:
					st1_r = 'temp'

				afd.actual_state = st_pair[1]

				try:
					afd.make_transition(symbol)
					st2_r = afd.actual_state
				except:
					st2_r = 'temp'

				if st1_r != st2_r:
					key = tuple(sorted([st1_r, st2_r]))

					if st_mark[key] == 'X':
						st_mark[st_pair] = 'X'

						AFDMinimizer.recursive_mark(st_lists, st_pair, st_mark)
					else:
						st_lists[key].append(st_pair)

		states_to_remove = set(['temp'])

		for key in st_mark.keys():
			if st_mark[key] == '':
				if key[1] != 'temp':
					states_to_remove.add(key[1])

				aux_tt = afd_transitions[key[0]]
				new_tts = []

				for tt in aux_tt:
					if tt[1] == key[1]:
						new_tts.append((tt[0], key[0]))
					else:
						new_tts.append(tt)

				afd_transitions[key[0]] = new_tts

		afd_states = list(set(afd_states) - states_to_remove)
		afd_final_states = list(set(afd_final_states) - states_to_remove)

		for st in states_to_remove:
			afd_transitions.pop(st, None)

		keys = list(afd_transitions.keys())

		for key in keys:
			if key not in afd_states:
				afd_transitions.pop(key, None)

		afd_final_states = list(set(afd_states) & set(afd_final_states))

		afd_states = sorted(afd_states)
		afd_final_states = sorted(afd_final_states)

		new_afd = AFD(afd_alfabet, afd_states, afd_initial_state, afd_final_states)

		for origin in afd_states:
			for symbol, dest in afd_transitions[origin]:
				try:
					new_afd.insert_transition(origin, dest, symbol)
				except:

					aux_keys = st_mark.keys()

					for kk in aux_keys:
						if st_mark[kk] == '' and kk[1] == dest:
							new_afd.insert_transition(origin, kk[0], symbol)

		return new_afd

	@staticmethod
	def recursive_mark(st_lists, st_pair, st_mark):
		while len(st_lists[st_pair]) > 0:
			aux_pair = st_lists[st_pair].pop()
			st_mark[aux_pair] = 'X'
			AFDMinimizer.recursive_mark(st_lists, aux_pair, st_mark)

	@staticmethod
	def remove_inacessible(afd):
		st_visited = set()
		stack = [afd.initial_state]

		while len(stack) > 0:
			state = stack.pop()

			st_visited.add(state)
			for transition in afd.transitions[state]:
				if transition[1] not in st_visited:
					stack.append(transition[1])


		return list(st_visited)

