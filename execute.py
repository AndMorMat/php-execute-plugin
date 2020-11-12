import sublime
import sublime_plugin

import subprocess

class ExecuteCommand(sublime_plugin.TextCommand): 
	
	file_dir = '/tmp/execute.php';
	php_path = '/usr/bin/php';

	def run(self, edit):
		stri = '';
		for sel in self.view.sel():
			line = self.view.line(sel) 
			stri += str(self.view.substr(line).strip())

		arquivo = open(self.file_dir, 'w')
		inicio = stri[:5]
		if inicio != "<?php":
			stri = "<?php "+stri

		arquivo.write(stri)
		arquivo.close();

		cmd = [self.php_path] + [self.file_dir]

		p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()

		self.view.insert(edit, line.end(), '\n/* {0} */'.format((out if not err else err).decode().strip()))