class UpdateGrid:
    """
    This class is made for the Tetris grid to manage the placement of pieces,
    removal of complete rows, and then to be able to calculate the maximum height of blocks left.
    """
    def __init__(self, width=10, height=100):
        """
        This functions helps to initialize the grid with the specified dimensions given.
        It is represented as a 2D list of integers (0 for empty, 1 for filled).
        'Width' of the grid is 10 units.
        'Height' of the grid is 100 units.
        """
        self.width = width
        self.height = height
        self.grid = [[0] * self.width for _ in range(self.height)]

    def new_block(self, piece):
        """
        This functions helps to add a new piece to the grid. We are placing the piece in the grid
        and clearing any fully filled rows after its placement.
        """
        #Place the piece in the correct position.
        self._place_block(piece)
        #Remove rows that are completely filled.
        self._remove_full_rows()

    def _place_block(self, piece):
        """
        This function helps to determine the correct position to drop the piece and update the grid.
        We iteratively drop the piece row by row until it has a collision with another block or reaches the bottom of the grid.
        """
        drop_row = 0
        #Determine the row where the piece should stop.
        while True:
            if any(
                drop_row + r >= self.height or self.grid[drop_row + r][piece.position + c]
                for r, c in piece.shape
            ):
                #Stop when a collision happens or grid bottom is reached.
                break
            drop_row += 1
        #Adjust to the last valid row before collision.
        drop_row -= 1
        #Place the piece in the correct position.
        for r, c in piece.shape:
            self.grid[drop_row + r][piece.position + c] = 1

    def _remove_full_rows(self):
        """
        This function helps to remove rows that are filled with blocks.
        Then we shift the remaining rows down and add empty rows at the top to maintain grid height.
        """
        #Identify the full rows.
        rows_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for row in rows_to_clear:
            #Remove the full row.
            del self.grid[row]
            #Add an empty row at the top.
            self.grid.insert(0, [0] * self.width)

    def get_maximum_height(self):
        """
        This functions helps to calculate the max height of the blocks in the grid.
        The maximum height is found from the highest row having a filled space.
        Then we return The height of the highest block or 0 if the grid is empty.
        """
        for row in range(self.height):
            #Check if any space in the row is filled.
            if any(self.grid[row]):
                #Return the height relative to the grid's top.
                return self.height - row
        #If no blocks are there, return 0.    
        return 0


class PieceCharacteristics:
    """
    This class is made to describe a Tetris piece (like its type, position, and shape).
    The shapes are in terms of relative coordinates.
    """
    dict_shape = {
        'Q': [(0, 0), (0, 1), (1, 0), (1, 1)],
        'Z': [(0, 0), (0, 1), (1, 1), (1, 2)],
        'S': [(0, 1), (0, 2), (1, 0), (1, 1)],
        'T': [(1, 1), (0, 1), (0, 0), (0, 2)],
        'I': [(0, 0), (0, 1), (0, 2), (0, 3)],
        'L': [(0, 0), (1, 0), (2, 0), (2, 1)],
        'J': [(0, 1), (1, 1), (2, 1), (2, 0)],
    }

    def __init__(self, letter_type, position):
        """
        This function helps initialize a piece with its type and starting position.
        'letter_type' is the type of the piece such as Q, Z, S, T, I, L, or J.
        'position' is the leftmost column where the piece is placed.
        """
        self.letter_type = letter_type
        #This is a lazy-loaded shape.
        self._shape = None
        self.position = position

    @property
    def shape(self):
        """
        This function helps get the shape of the piece based on its type.
        The shapes are coordinates relative to the top-left of the piece.
        Then we return a list of (row, column) tuples representing the piece's shape.
        """
        if self._shape is None:
            self._shape = self.dict_shape[self.letter_type]
        return self._shape
