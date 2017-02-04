import os
import glob

def data_walker (mini_directory_parser = [['/', False]], file_include_regex = '*', ignore_on_no_such_file = False, verbose = False):
	
	""" Data Walker

	Parameters
	----------
	mini_directory_parser : 2D-list, the discovering rule.
	file_include_regex : string, the file varients.
	ignore_on_no_such_file : boolean, optional (default = False), True : continue to scan files while one of the path elements
				in the mini_directory_parser are invalid.
	verbose : boolean, optional (default = False), print the walker footage.
	
	Returns
	-------
	The list of files' absolute path.
	[[The parent directory of first file, The first file name],...]	
	"""
	recursive_mdp = []
	result = []
	not_exist = False
	for x in range(len(mini_directory_parser)):
		if mini_directory_parser[x][1] == False:
			if (not ignore_on_no_such_file) or os.path.isdir(mini_directory_parser[x][0]):
				os.chdir(mini_directory_parser[x][0])
			else:
				not_exist = True
		elif mini_directory_parser[x][1] == True:
			now = sorted(glob.glob(mini_directory_parser[x][0] + '/'))
			for y in range(len(now)):
				recursive_mdp = mini_directory_parser
				recursive_mdp[x] = [now[y][:-1], False]
				result.extend(data_walker(recursive_mdp, file_include_regex, ignore_on_no_such_file, verbose))

	if not_exist == False:
		current = sorted(glob.glob(file_include_regex))
		for x in range(len(current)):
			current[x] = [os.getcwd(),  current[x]]
		result.extend(current)
	if verbose:
		print(now)
	return result
