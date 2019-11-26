import sys
from afn import AFN
from afd import AFD
from afntoafd import AFNtoAFD
from afd_minimizer import AFDMinimizer

def main(args):
	#alfabet = ['a', 'b', 'c']
	#states = ['q0', 'q1', 'q2']
	#initial_state = 'q0'
	#final_states = ['q2']

	alfabet = ['a', 'b']
	states = ['q0', 'q1', 'q2', 'q3']
	initial_state = 'q0'
	final_states = ['q3']

	automat = AFN(alfabet, states, initial_state, final_states)

	automat.insert_transition('q0', 'q0', 'a')
	automat.insert_transition('q0', 'q0', 'b')
	automat.insert_transition('q0', 'q1', 'a')
	automat.insert_transition('q0', 'q2', 'b')
	automat.insert_transition('q1', 'q3', 'a')
	automat.insert_transition('q2', 'q3', 'b')
	automat.insert_transition('q3', 'q3', 'a')
	automat.insert_transition('q3', 'q3', 'b')


	#automat.insert_transition('q0', 'q0', 'a')
	#automat.insert_transition('q0', 'q0', 'b')
	#automat.insert_transition('q0', 'q0', 'c')
	#automat.insert_transition('q0', 'q1', 'c')
	#automat.insert_transition('q1', 'q2', 'c')
	#automat.insert_transition('q2', 'q2', 'a')
	#automat.insert_transition('q2', 'q2', 'b')
	#automat.insert_transition('q2', 'q2', 'c')

	new_afd = AFNtoAFD.run(automat)

	reduzed_afd = AFDMinimizer.run(new_afd)

	automat.show()
	new_afd.show()
	reduzed_afd.show()


	print(automat.read_word("bbababababaabb"))
	print(new_afd.read_word("bbabababababb"))
	print(reduzed_afd.read_word("bbababababaa"))

if __name__ == '__main__':
	main(sys.argv)