import os
from os import path as p


def linker(item: str) -> str:

	return p.normpath(p.join(os.getcwd(), "Templates", item))

def saver(item: str) -> str:

	return p.normpath(p.join(os.getcwd(), "Output", item))
