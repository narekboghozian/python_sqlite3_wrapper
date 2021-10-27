
import sqlite3
import os
from datetime import datetime

class database:

	def __init__(self, db_name, db_path="./", debug = False):
		self.__fullpath = os.path.join(db_path, db_name)
		self.debug = debug

	def raw_command(self, command):
		try:
			self.__connect()
			self.__conn.execute("command")
			self.__close()
		except Exception:
			return False

	def raw_command_commit(self, command):
		try:
			self.__connect()
			self.__conn.execute("command")
			self.__conn.commit()
			self.__close()
		except Exception:
			return False


	def fullpath(self):
		return self.__fullpath

	def get_tables(self):
		try:
			self.__connect()
			self.__tables = self.__conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
			ret_tables = list(self.__tables)
			self.__disconnect()
			ret = []
			for item in ret_tables:
				ret.append(item[0])
			return ret
		except Exception:
			return False

	def tables(self):
		return self.get_tables()

	def get_fields(self, table_name):
		try:
			if not isinstance(table_name, list):
				table_name = [table_name]
			ret2 = []
			for name in table_name:
				command = "SELECT name FROM PRAGMA_TABLE_INFO('%s');"%(name)
				self.__connect()
				ret_fields = list(self.__conn.execute(command))
				self.__disconnect()
				ret = []
				for item in ret_fields:
					ret.append(item[0])
				ret2.append(ret)
			return ret2
		except Exception:
			return False

	def fields(self, table_name):
		return self.get_fields(table_name)

	def __connect(self):
		self.__conn = sqlite3.connect(self.__fullpath)

	def __disconnect(self):
		self.__conn.close()

	def __process_fields(self, fields):
		ret = ''
		has_primary = False
		try:
			for index, item in enumerate(fields):
				param = ''
				if len(item) == 1:
					field_type = 'INT NOT NULL'
				elif len(item) == 2:
					field_type = item[1]
					if field_type.lower() == 'primary':
						field_type = 'INT PRIMARY KEY NOT NULL'
				else:
					field_type = item[1]
					param = '(%s)'%(str(item[2]))
					if field_type.lower() == 'primary':
						field_type = '%s PRIMARY KEY'%(item[2].upper())
						param = ''
				if index != 0:
					ret += ', '
				ret += '%s %s%s'%(item[0].replace(' ','_'), field_type.upper(), param)

			if self.debug: print(ret)
			return ret
		except Exception:
			return False

	def new_table(self, table_name, fields):
		try:
			processed_fields = self.__process_fields(fields)
			command = 'CREATE TABLE IF NOT EXISTS %s (%s);'%(table_name, processed_fields)
			if self.debug: print(command)
			self.__connect()
			self.__conn.execute(command)
			self.__conn.close()
		except Exceptiwon:
			return False


	def insert_row(self, table_name, values, fields = False):
		field_replace = {'[':'(', ']':')', "'": ''}
		value_replace = {'[':'(', ']':')'}
		try:
			if fields == False:
				fields = str(self.get_fields(table_name)[0])
			else:
				fields = str(fields)
			for i in field_replace:
				fields = fields.replace(i,field_replace[i])
			values = str(values)
			for i in value_replace:
				values = values.replace(i,value_replace[i])
			command = "INSERT INTO %s %s VALUES %s "%(table_name, fields, values)
			if self.debug: print(command)
			self.__connect()
			self.__conn.execute(command)
			self.__conn.commit()
			self.__disconnect()
		except Exception:
			return False

	def insert_rows(self, table_name, values, fields = False):
		field_replace = {'[':'(', ']':')', "'": ''}
		value_replace = {'[':'(', ']':')'}
		try:
			if fields == False:
				fields = str(self.get_fields(table_name)[0])
			else:
				fields = str(fields)
			for i in field_replace:
				fields = fields.replace(i,field_replace[i])
			values = str(values)[1:-1]
			for i in value_replace:
				values = values.replace(i,value_replace[i])
			command = "INSERT INTO %s %s VALUES %s "%(table_name, fields, values)
			if self.debug: print(command)
			self.__connect()
			self.__conn.execute(command)
			self.__conn.commit()
			self.__disconnect()
		except Exception:
			return False


	def drop_table(self, table_name):
		try:
			command = "DROP TABLE IF EXISTS %s;"%(table_name)
			self.__connect()
			self.__conn.execute(command)
			self.__disconnect()
		except Exception:
			return False

	def select(self, table, conditions):
		return False

	def read_table(self, table_name, header=False):
		try:
			command = "SELECT * FROM %s"%(table_name)
			self.__connect()
			cursor = self.__conn.execute(command)
			all_data = cursor.fetchall()
			self.__conn.close()
			if header:
				head = self.get_fields(table_name)
				all_data = head + all_data
			return all_data
		except Exception:
			return False













