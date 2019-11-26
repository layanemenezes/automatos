import sys
import os
from afn import AFN
from afd import AFD
from afntoafd import AFNtoAFD
from afd_minimizer import AFDMinimizer

def read_AFN():
	alfabet = input("Informe o alfabeto (∑): ").split()
	states = input("Informe o conjunto de estados (Q): ").split()
	initial_state = input("Informe o estado inicial: ")
	final_states = input("Informe o conjunto de estados finais (F): ").split()

	afn = AFN(alfabet, states, initial_state, final_states)

	print("\nINFORME AS TRANSIÇÕES [LINHA VAZIA PARA TERMINAR]: \n")

	count_t = 0

	while True:
		try:
			origin, dest, symbol = input("Transição Nº {0}: ".format(count_t+1)).split()
		except:
			break	
			
		afn.insert_transition(origin, dest, symbol)
		count_t += 1


	return afn

def main(args):
	afn = read_AFN()

	print("------------------- AFN: \n")
	afn.show()

	print("------------------- AFN -> AFD: \n")
	new_afd = AFNtoAFD.run(afn)
	new_afd.show()

	print("------------------- AFD MINIMIZADO: \n")
	reduzed_afd = AFDMinimizer.run(new_afd)
	reduzed_afd.show()

	print("TESTAR PALAVRAS ACEITAS: \n")

	while True:
		word = input("Informe a palavra: ")

		print("\n")

		try:
			result = afn.read_word(word)
		except:
			result = False

		if result is True:
			print("AFN -> ACEITA!")
		else:
			print("AFN -> REJEITA!")

		try:	
			result = new_afd.read_word(word)
		except:
			result = False

		if result is True:
			print("AFD -> ACEITA!")
		else:
			print("AFD -> REJEITA!")

		try:
			result = reduzed_afd.read_word(word)
		except:
			result = False

		if result is True:
			print("AFD MINIMIZADO -> ACEITA!")
		else:
			print("AFD MINIMIZADO -> REJEITA!")

		print("\n")

if __name__ == '__main__':
	main(sys.argv)