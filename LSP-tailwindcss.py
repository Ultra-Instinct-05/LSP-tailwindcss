import os
from lsp_utils import NpmClientHandler

def plugin_loaded():
	TailwindCSS.setup()

def plugin_unloaded():
	TailwindCSS.cleanup()

class TailwindCSS(NpmClientHandler):
	package_name = __package__
	server_directory = "node_modules"
	server_binary_path = os.path.join(server_directory, "tailwindcss-language-server/dist", "index.js")