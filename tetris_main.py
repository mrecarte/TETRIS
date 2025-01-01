import sys
from tetris_methods import UpdateGrid, PieceCharacteristics

def process_input(input_data):
    """
    This function will process the .txt file with all of the Tetris configurations and calculate the maximum grid height
    for each configuration after all pieces are placed and apprpriate rows are deleted (if its needed).
    We then return a list of tuples where each contains the configuration and the max grid height.
    """
    #List to store the results of each configuration.
    results = []
    #Split the input into lines.
    lines = input_data.strip().split('\n')

    for line in lines:
        #Remove any whitespace.
        line = line.strip()
        if not line:
            #skip empty lines.
            continue

        #Initialize a new Tetris grid for the current configuration.
        grid = UpdateGrid(width=10, height=100)

        #Process each piece in the configuration.
        for piece_description in line.split(','):
            #Get information about at the piece type.
            letter = piece_description[0]
            #Extract the starting column of the piece.
            position = int(piece_description[1:])
            #Create a piece with the type and position that we are looking at.
            piece = PieceCharacteristics(letter, position)
            #Put the piece in the grid.
            grid.new_block(piece)

        #Calc the maximum height of the grid after playing the Tetris configuration and store both the confiuration and the results.
        results.append((line, grid.get_maximum_height()))

    return results

def main():
    """
    The main function to read input, process Tetris configurations, and give results.
    """
    #Read the input data from standard input.
    input_data = sys.stdin.read().strip()
    #Process input and calculate results.
    results = process_input(input_data)
    for configuration, result in results:
        print(f"The maximum height for the configuration '{configuration}' is {result}.")

if __name__ == "__main__":
    main()

