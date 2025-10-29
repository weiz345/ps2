import random

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

class BoggleBoard:
    def __init__(self, size=4):
        self.size = size
        self.board = self.generate_board()
    
    def generate_board(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return [[random.choice(alphabet) for _ in range(self.size)] for _ in range(self.size)]
    
    def print_board(self):
        for row in self.board:
            print(' '.join(row))

class BoggleSolver:
    def __init__(self, dictionary):
        self.trie = Trie()
        for w in dictionary:
            self.trie.insert(w.upper())
    
    def find_words(self, board):
        found = set()
        for i in range(len(board)):
            for j in range(len(board)):
                self.dfs(board, i, j, "", set(), found)
        return list(found)
    
    def dfs(self, board, i, j, word, visited, found):
        if (i, j) in visited or i < 0 or j < 0 or i >= len(board) or j >= len(board):
            return
        word += board[i][j]
        if not self.trie.starts_with(word):
            return
        if self.trie.search(word):
            found.add(word)
        visited.add((i, j))
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                if x or y:
                    self.dfs(board, i + x, j + y, word, visited, found)
        visited.remove((i, j))
