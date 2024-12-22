import streamlit as st
import heapq
from collections import defaultdict, namedtuple

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def encode(text, codebook):
    return ''.join(codebook[char] for char in text)

def decode(binary_string, root):
    decoded_output = []
    current_node = root
    for bit in binary_string:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = root
    return ''.join(decoded_output)

st.title("Huffman Coding")

frequencies = {
    'A': 0.5,
    'B': 0.35,
    'C': 0.5,
    'D': 0.1,
    'E': 0.4,
    '-': 0.2
}

huffman_tree = build_huffman_tree(frequencies)
codebook = generate_codes(huffman_tree)


text_to_encode = "CAD-BE"
encoded_text = encode(text_to_encode, codebook)


binary_string_to_decode = "0011011100011100"  
decoded_text = decode(binary_string_to_decode, huffman_tree)


st.write(f"Encoded text for '{text_to_encode}': {encoded_text}")
st.write(f"Decoded text for binary '{binary_string_to_decode}': {decoded_text}")