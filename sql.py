database = sqlite3.connect("database.sqlite")

def sql(c, d, r):
	if not isinstance(d, tuple) or not isinstance(c, str):
		return False
	try:
		cursor = database.cursor()
		cursor.execute(c, d)
		if r:
			return cursor.fetchall()
		database.commit()
		return True
	except Error as e:
		print(f'⚠️ "{e}" {c}: {d}.')
		return False