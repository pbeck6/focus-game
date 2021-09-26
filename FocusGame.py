# Author: Philip Beck
# Email: stoneroll6@gmail.com
# Date: 11/24/2020
# Description:
#    Creates a game of Focus, a board game
#    in which two players try to remove six of the
#    opponents' pieces from the 6x6 game board
#    For educational use only,
#    Not for commercial use


class Player:
    """
    Player class handles player name, player color,
    player's reserves, and player's captures.
    Also checks if Player has enough captures to win
    Composite: GameBoard, PieceStack
    """

    def __init__(self, player_tuple):
        """
        Initializes Player,
        sets reserve and captured to 0,
        maintains name capitalization for display
        :param player_tuple: 2 elements ('player_name', 'color of pieces')
        """
        self._display_name = player_tuple[0]
        self._player_name = player_tuple[0].upper()
        self._player_color = player_tuple[1].upper()
        self._reserve = 0
        self._captured = 0

    def get_display_name(self):
        """
        Returns display name
        :return: str of display_name
        """
        return self._display_name

    def get_name(self):
        """
        Returns player name in upper-case
        :return: str of player_name
        """
        return self._player_name

    def get_color(self):
        """
        Returns player color in upper-case
        :return: str of player_color
        """
        return self._player_color

    def get_reserve(self):
        """
        Returns player's reserves
        :return: int of pieces in reserve
        """
        return self._reserve

    def get_captured(self):
        """
        Returns player's captured
        :return: int of enemy pieces captured
        """
        return self._captured

    def set_reserve(self, number):
        """
        Sets player's reserves
        :param number: int of new reserves
        :return: updates player's reserves
        """
        self._reserve = number

    def set_captured(self, number):
        """
        Sets player's captured
        :param number: int of new captured
        :return: updates player's captured
        """
        self._captured = number

    def check_winner(self):
        """
        Checks if player has won by capturing
        enough enemy pieces
        :return: boolean
        """
        # Sets victory condition with winning_count
        winning_count = 6
        if self._captured >= winning_count:
            return True
        else:
            return False

class GameBoard:
    """
    GameBoard class handles location of pieces in play,
    handles the moving of pieces across the board
    Composite: FocusGame
    Component (has-a): PieceStack, Player (aka 2 players)
    """

    def __init__(self):
        """
        Initializes gameboard as list of PieceStack objects,
        which are also lists (list of lists)
        """
        # Sets square grid dimensions as gridsize x gridsize (eg 6x6)
        self._gridsize = 6
        self._gameboard = []
        for row in range(self._gridsize):
            if row % 2 == 0:
                self._gameboard.append \
                ([PieceStack('R'),PieceStack('R'),PieceStack('G'),PieceStack('G'),PieceStack('R'),PieceStack('R')])
            if row % 2 == 1:
                self._gameboard.append \
                ([PieceStack('G'),PieceStack('G'),PieceStack('R'),PieceStack('R'),PieceStack('G'),PieceStack('G')])

    def pieces_at_location(self, location):
        """
        Checks if location is valid, and
        returns location value
        :param location: tuple (x,y)
        :return: boolean or list of pieces
        """
        if location == 'reserve':
            return True
        else:
            if location[0] < self._gridsize and location[1] < self._gridsize:
                piecestack = self._gameboard[location[0]][location[1]]
                return piecestack.get_pieces()
            else:
                return 'Invalid location'

    def board_move(self, player, move_from, move_to, piece_quantity):
        """
        Moves pieces from PieceStack object
        into appropriate positions
        :param player: Player object
        :param move_from: source tuple (x,y)
        :param move_to: destination tuple (x,y)
        :param piece_quantity: int of how many pieces to move
        :return: str message for successful move or winner declared
        """
        destination = self.pieces_at_location(move_to)
        destination_piecestack = self._gameboard[move_to[0]][move_to[1]]
        if move_from == 'reserve':
            color = player.get_color()
            destination.append(color.upper())
            player.set_reserve(player.get_reserve() - 1)
            return destination_piecestack.adjust_piecestack(player)
        else:
            source = self.pieces_at_location(move_from)
            detached_pieces = source[-piece_quantity:]
            del source[-piece_quantity:]
            for piece in detached_pieces:
                destination.append(piece.upper())
            else:
                return destination_piecestack.adjust_piecestack(player)

class PieceStack:
    """
    PieceStack class handles the stack of pieces
    handle the capture and reserve of excess pieces
    Composite: GameBoard
    Component (has-a): Player (aka owner)

    NOTE: game pieces in a stack are referred to as
    'piecestack', to avoid confusion with runtime stack

    """

    def __init__(self, color):
        """
        Initializes the Piecestack at a given location
        on the gameboard
        :param color: str color of initial piece
        """
        # Stack_size limits the number of pieces per stack
        self._piecestack = [color]
        self._stack_size = 5

    def get_pieces(self):
        """
        Returns the pieces in a given piecestack
        :return: list of pieces by color
        """
        return self._piecestack

    def adjust_piecestack(self, player):
        """
        Stacks and adjusts the piecestack as necessary
        following a verified move.
        Sends same-color pieces to reserves and
        different-color pieces to captured
        :param player: Player object
        :return: str message
        """
        # self._piecestack[(len(self._piecestack)) - 1] is top-most piece
        # self._piecestack[0] is bottom-most piece
        if len(self._piecestack) <= self._stack_size:
            return 'Successfully moved'
        else:
            extra_pieces = len(self._piecestack) - self._stack_size
            for piece in range(extra_pieces):
                if self._piecestack[0] == self._piecestack[(len(self._piecestack)) - 1]:
                    player.set_reserve(player.get_reserve() + 1)
                    del self._piecestack[0]
                else:
                    player.set_captured(player.get_captured() + 1)
                    del self._piecestack[0]
            else:
                if player.check_winner() == True:
                    return player.get_display_name() + ' wins'
                else:
                    return 'Successfully moved'

class FocusGame:
    """
    Starts one game of Focus, played by two players.
    Manages the two players and their pieces, along with the
    status of the current game board and allows
    for movement and capture of pieces.
    Component (has-a): GameBoard, Player
    """

    def __init__(self, player1_tuple, player2_tuple):
        """
        Initializes empty GameBoard,
        adds both players to player list,
        sets current_turn so anyone can start game
        """
        self._players = [Player(player1_tuple), Player(player2_tuple)]
        self._board = GameBoard()
        self._current_turn = None

    def get_player(self, player_str):
        """
        Gets Player object primarily for use
        with Player class methods
        Case-insensitive
        :param player_str: str 'player_name'
        :return: Player object
        """
        for player in self._players:
            if player_str.upper() == player.get_name().upper():
                return player
        else:
            return None

    def show_reserve(self, player_str):
        """
        Checks for valid player
        then shows player's reserves
        :param player_str: str 'player_name'
        :return: error str or int of reserves
        """
        if self.get_player(player_str) != None:
            return self.get_player(player_str).get_reserve()
        else:
            return "Player not found"

    def show_captured(self, player_str):
        """
        Checks for valid player
        then shows player's captured
        :param player_str: str 'player_name'
        :return: error str or int of captured
        """
        if self.get_player(player_str) != None:
            return self.get_player(player_str).get_captured()
        else:
            return "Player not found"

    def show_pieces(self, location):
        """
        Retrieves pieces at given location
        passed to GameBoard method
        :param location: tuple (x,y)
        :return: error str or list of pieces by color
        """
        return self._board.pieces_at_location(location)

    def move_piece(self, player_str, move_from, move_to, piece_quantity):
        """
        Move player's pieces from source to destination
        while checking that all parameters are valid
        passes parameters to GameBoard method
        :param player_str: str 'player_name'
        :param move_from: source tuple (x,y)
        :param move_to: destination tuple (x,y)
        :param piece_quantity: int pieces to move
        :return: error str or sucess str
        """
        player = self.get_player(player_str)
        if player == None:
            return 'Player not found'
        else:
            if player.get_reserve() == 0 and move_from == 'reserve':
                return 'No pieces in reserve'
            else:
                if self._current_turn != player_str.upper() and self._current_turn != None:
                    return 'Not your turn'
                else:
                    if self.check_valid_move(player_str, move_from, move_to) != True:
                        return 'Invalid location'
                    else:
                        if move_from == 'reserve':
                            self.change_turns(player)
                            return self._board.board_move(player, move_from, move_to, piece_quantity)
                        else:
                            if piece_quantity > len(self.show_pieces(move_from)) or piece_quantity <= 0:
                                return 'Invalid number of pieces'
                            else:
                                self.change_turns(player)
                                return self._board.board_move(player, move_from, move_to, piece_quantity)

    def change_turns(self, player):
        """
        Activates upon completion of
        valid move, changes turns
        :param player: Player object
        :return: current_turn changed to other player
        """
        for next_player in self._players:
            if player != next_player:
                self._current_turn = next_player.get_name()

    def check_valid_move(self, player_str, move_from, move_to):
        """
        Checks if locations are valid
        and if player has control of piecestack
        at that location
        Passes to direction_restriction method
        to check if move direction is valid
        :param player_str: str 'player_name'
        :param move_from: source tuple (x,y)
        :param move_to: destination tuple (x,y)
        :return: boolean or error str
        """
        if self._board.pieces_at_location(move_from) == 'Invalid location' or \
        self._board.pieces_at_location(move_from) == [] or \
        self._board.pieces_at_location(move_to) == 'Invalid location':
            return 'Source has no pieces to move or does not exist'
        else:
            if move_from == 'reserve':
                return True
            else:
                player_color = self.get_player(player_str).get_color()
                top_piecestack = len(self._board.pieces_at_location(move_from)) - 1
                source_color = self._board.pieces_at_location(move_from)[top_piecestack]
                if player_color != source_color:
                    return 'Piecestack does not belong to player'
                else:
                    return self.direction_restriction(move_from, move_to)

    def direction_restriction(self, move_from, move_to):
        """
        Only allows horizontal/vertical moves
        Does not allow moving in place
        Does not allow moves in spaces
        exceeding the size of piecestack
        :param move_from: source tuple (x,y)
        :param move_to: destination tuple (x,y)
        :return: boolean or error str
        """
        if move_from[0] != move_to[0] and move_from[1] != move_to[1]:
            return 'Move is not horizontal or vertical'
        else:
            horizontal = abs(move_from[0] - move_to[0])
            vertical = abs(move_from[1] - move_to[1])
            if horizontal == 0 and vertical == 0:
                return 'Does not move pieces anywhere'
            else:
                spaces_allowed = len(self._board.pieces_at_location(move_from))
                if horizontal > spaces_allowed or vertical > spaces_allowed:
                    return 'Move exceeds allowed spaces'
                else:
                    return True

    def reserved_move(self, player_str, move_to):
        """
        Makes move starting from player's reserves
        passes to move_pieces method for validation
        GameBoard's method board_move
        will deal with decrementing reserves
        once the move is validated
        :param player_str: str 'player_name'
        :param move_to: destination tuple (x,y)
        :return: error or success str
        """
        move_from = 'reserve'
        piece_quantity = 1
        return self.move_piece(player_str, move_from, move_to, piece_quantity)


def main():
    return

if __name__ == '__main__':
    main()
