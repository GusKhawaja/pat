#!/usr/bin/python

import webbrowser
import time
import os
import subprocess
import argparse

class Utilities:
	
	seperator_line = '------------------------------------------------------------'
	
	def __init__(self):
		self.name = 'static class'

	def usage(self):
		print 'Pentester Automation Tool'
		print Utilities.seperator_line
		print 'Arguments:'
		print '-c\t --company\t Your Client Company Domain Name'
		print 
		print 
		print "Example:"
		print "pat.py --company yourclientdomain.com"
		print
		#exit the application
		exit(0)

class Core:
	
	def __init__(self,company_domain_name,utilities):
		self.company_domain_name = company_domain_name
		self.utilities = utilities

	def _open_terminal(self,app_name,cmd):
		output = '[+] Executing ' + str(app_name) + '...\r\n'
		try:
			output += subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
			output += '\r\n'
		except Exception,e:
			output += str(e)
		output +=  self.utilities.seperator_line + '\r\n'
		return output

	def _save_results(self,results,folder_name,file_name):
		try:
			# Create a directory for the category e.g reconnissance or external scanning ...
			if not os.path.isdir(folder_name):
				os.mkdir(folder_name)
			# Save the results to a file
			file_name = folder_name + '/'+ file_name
			file_to_save = open(file_name,'w')
			file_to_save.write(results)
			file_to_save.close()
		except Exception,e:
			print '[!] Error: Cannot save the results to a file!'

	def _execute_commands(self,commands):
		#Execute commands in terminal
		results = ''
		for key,val in commands.items():
			output = self._open_terminal(key,val)
			results += output
		return results
	
	def _open_websites(self,websites):
		# Open websites in browser
		for website in websites:
			webbrowser.open_new_tab(website)
			time.sleep(2)

	def _execute(self,commands,websites,folder_name,file_name):

		if commands == None and websites == None:
			print 'NO commands available'
			return

		if commands != None:
			results = self._execute_commands(commands)
			print results
			self._save_results(results,folder_name,file_name)
		
		if websites != None:
			self._open_websites(websites)

		
	
	def _get_company_domain_name(self):
		return self.company_domain_name

	def start(self):
		print 'Pentesting Client Domain Name: ' + self.company_domain_name
		print self.utilities.seperator_line
		print
	
		# Create a directory by Client Domain Name
		if not os.path.isdir(self.company_domain_name):
			os.mkdir(self.company_domain_name)

	def check(self,action_name,folder_name):
		# Get/Load the terminal commands from if needed
		commands = {}

		commands_file_path = action_name+'_commands.txt'
		
		if os.path.isfile(commands_file_path):
			commands_file = open(commands_file_path,'r')

			for command_line in commands_file.readlines():
				command_line_splitted = command_line.split(':')
				commands[command_line_splitted[0]] = command_line_splitted[1]
		
	
		# Get/Load the websites from file if needed
		websites = []
		websites_file_path = action_name+'_websites.txt'
		
		if os.path.isfile(websites_file_path):
			websites_file = open(websites_file_path,'r')
			for website_line in websites_file.readlines():
				websites.append(website_line.strip('\r').strip('\n'))

		folder_name = self._get_company_domain_name()+'/Reconnaissance'
		file_name = action_name + '.txt'

		self._execute(commands,websites,folder_name,file_name)


def process_arguments(args,core,utilities):
	reconnaissance_category = 'Reconnaissance'

	if args.dns_test:
		core.check('dns',reconnaissance_category)
		

def main():
	# Arguments
	parser = argparse.ArgumentParser('Pentester Automation Tool')
	parser.add_argument("-c","--company",type=str,help="Your Client Company Domain Name")
	parser.add_argument("-dns","--dns_test",help="Check/Test the DNS security",action="store_true")

	# Parse the arguments
	args= parser.parse_args()

	# initialize the Utilities class
	utilities = Utilities()
	
	if args.company == None:
		utilities.usage()

	core = Core(args.company,utilities)
	core.start()
	
	process_arguments(args,core,utilities)


if __name__ == '__main__':
	main()
		



