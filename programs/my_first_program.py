from nada_dsl import *


def nada_main():
    # Define the party involved in the computation
    party1 = Party(name="Party1")
    
    # Define secret integer inputs for the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform the computation - adding two secret integers
    result = my_int1 + my_int2

    # Define the output of the computation
    return [Output(result, "result", party1)]

# Run the nada_main function
nada_main()
