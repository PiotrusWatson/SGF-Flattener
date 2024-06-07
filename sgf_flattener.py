from sgfmill.sgf import Sgf_game, Tree_node
import argparse

def load_file(file_path):
    with open(file_path, "r") as f:
        contents = f.read()
        return contents
    

def load_sgf_from_file(file_path):
    game_string = load_file(file_path)
    return Sgf_game.from_string(game_string)

def write_file(content, output_name="output"):
    with open(output_name + ".sgf", "wb") as f:
        f.write(content)

def flatten_sgf(game):

    to_process = []
    to_process.append(game.get_root())

    while len(to_process) != 0:
        current_node: Tree_node = to_process.pop()
        for child in current_node:
            if child:
                child.reparent(current_node, 0)
                to_process.append(child)


parser = argparse.ArgumentParser(description="Given a path to an SGF file, makes the longest path be placed first")
parser.add_argument("SGF_path", type=str, help="The path to an SGF file on your computer")
parser.add_argument("output_filename", type=str, nargs="?", default="output", help="The name of the output file")
args = parser.parse_args()

game = load_sgf_from_file(args.SGF_path)
flatten_sgf(game)
write_file(game.serialise, args.output_filename)
